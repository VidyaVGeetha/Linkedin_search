import time
import csv
import schedule
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === CONFIGURATION ===
LINKEDIN_USERNAME = 'effffff'
LINKEDIN_PASSWORD = 'ggggg'
JOB_TITLE = 'Firmware Engineer OR Embedded Engineer OR Embedded Systems'
LOCATION = 'Scotland'
LOG_FILE = 'application_log.csv'

# === CHROME SETUP ===
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

def apply_to_job():
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)

    # === 1. LOGIN TO LINKEDIN ===
    driver.get("https://www.linkedin.com/login")
    wait.until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(LINKEDIN_USERNAME)
    driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # === 2. SEARCH FOR JOB ===
    driver.get("https://www.linkedin.com/jobs/")
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search by title, skill, or company']")))
    
    job_input = driver.find_element(By.XPATH, "//input[@aria-label='Search by title, skill, or company']")
    job_input.clear()
    job_input.send_keys(JOB_TITLE)

    location_input = driver.find_element(By.XPATH, "//input[@aria-label='City, state, or zip code']")
    location_input.clear()
    location_input.send_keys(LOCATION)
    time.sleep(2)
    location_input.send_keys(Keys.ARROW_DOWN)
    location_input.send_keys(Keys.RETURN)

    # === 3. FILTER EASY APPLY AND CLICK FIRST JOB ===
    time.sleep(4)
    try:
        easy_apply_button = driver.find_element(By.XPATH, "//button[.//span[text()='Easy Apply']]")
        easy_apply_button.click()
        time.sleep(2)
    except Exception as e:
        print("No Easy Apply filter available.")
        driver.quit()
        return

    try:
        jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
        if jobs:
            jobs[0].click()
            time.sleep(3)

            apply_button = driver.find_element(By.XPATH, "//button[contains(@class, 'jobs-apply-button')]")
            apply_button.click()
            time.sleep(2)

            # Optional: Auto-submit if possible
            submit = driver.find_element(By.XPATH, "//button/span[text()='Submit application']")
            submit.click()
            print("Application submitted.")
            save_log(datetime.now(), JOB_TITLE, LOCATION, 'Success')
        else:
            print("No jobs found.")
            save_log(datetime.now(), JOB_TITLE, LOCATION, 'No jobs found')
    except Exception as e:
        print("Error applying:", e)
        save_log(datetime.now(), JOB_TITLE, LOCATION, f'Error: {e}')

    driver.quit()

def save_log(timestamp, job_title, location, status):
    data = {
        'Timestamp': [timestamp],
        'Job Title': [job_title],
        'Location': [location],
        'Status': [status]
    }
    df = pd.DataFrame(data)
    try:
        with open(LOG_FILE, 'a', newline='') as f:
            df.to_csv(f, header=f.tell()==0, index=False)
    except Exception as e:
        print("Error saving log:", e)

# === SCHEDULE TO RUN HOURLY ===
schedule.every(1).hours.do(apply_to_job)

print("LinkedIn job bot running. Press Ctrl+C to stop.")
apply_to_job()  # First run immediately

while True:
    schedule.run_pending()
    time.sleep(10)
