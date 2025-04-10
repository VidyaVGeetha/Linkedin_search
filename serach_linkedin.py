from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === CONFIGURATION ===
LINKEDIN_USERNAME = 'xxxxxxxx'
LINKEDIN_PASSWORD = 'yyyyy'

JOB_TITLE = 'Embedded Engineer OR Embedded Systems OR Firmware Engineer'
LOCATION = 'Scotland'

# === SETUP CHROME DRIVER ===
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# === 1. LOGIN TO LINKEDIN ===
driver.get("https://www.linkedin.com/login")
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "username")))

driver.find_element(By.ID, "username").send_keys(LINKEDIN_USERNAME)
driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# === 2. NAVIGATE TO JOBS PAGE ===
driver.get("https://www.linkedin.com/jobs/")
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search by title, skill, or company']"))
)

# === 3. ENTER JOB TITLE ===
job_input = driver.find_element(By.XPATH, "//input[@aria-label='Search by title, skill, or company']")
job_input.clear()
job_input.send_keys(JOB_TITLE)

# === 4. ENTER LOCATION AND SELECT FIRST DROPDOWN OPTION ===
location_input = driver.find_element(By.XPATH, "//input[@aria-label='City, state, or zip code']")
location_input.clear()
location_input.send_keys(LOCATION)
time.sleep(2)  # Wait for dropdown to appear
location_input.send_keys(Keys.ARROW_DOWN)  # Select first option
location_input.send_keys(Keys.RETURN)


time.sleep(4)  # Wait for dropdown to appear
easy_apply_button = driver.find_element(By.XPATH, "//button[.//span[text()='Easy Apply']]")

easy_apply_button.click()
time.sleep(40)  # Wait for dropdown to appear
# === 9. CLOSE BROWSER ===
driver.quit()
