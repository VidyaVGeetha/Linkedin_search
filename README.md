# 🤖 LinkedIn Job Auto-Apply Bot (Firmware/Embedded Engineer)

This project automates the process of logging into LinkedIn and applying to the first "Easy Apply" job that matches the keyword **Firmware Engineer**, **Embedded Engineer**, or **Embedded Systems Engineer** in a specified location using **Selenium WebDriver**.

> 🔐 Credentials are stored directly in the script (not recommended for production use – see Security section).

## 🚀 Features Implemented

- ✅ Logs into LinkedIn using Selenium.
- ✅ Searches for job listings by keywords and location.
- ✅ Filters for jobs using **Easy Apply**.
- ✅ Clicks and opens the first job from the filtered list.
- ✅ Ideal for **automated job hunting** in fields like **firmware** and **embedded systems**.

## 🛠 Technologies Used

- `Python` (can be extended to Java)
- `Selenium WebDriver`
- `ChromeDriver`
- `LinkedIn Job Search`

## 🧪 How It Works

1. Open Chrome browser and log in to LinkedIn.
2. Navigate to LinkedIn Jobs page.
3. Search for jobs using pre-defined keywords and location (e.g., *Scotland*).
4. Filters job results using the **Easy Apply** feature.
5. Opens the first job in the list and simulates a click on "Easy Apply".
6. Waits before closing the session.

## 🔄 Planned Features

- ⏰ **Timed Automation**:
  - Apply for jobs every **hour**, increasing visibility and frequency.
  - Schedule runs within a **24-hour window** using task schedulers (like `cron` or Windows Task Scheduler).
- 📄 **Auto-Fill Resume and Details** in Easy Apply forms (WIP).
- 📈 **Log Applications** to a CSV/Excel sheet for tracking.
- 🧠 **Keyword Variation & ML Matching** based on resume profile (future release).
- 💬 **Telegram/Email Notifications** for applied jobs.

## ⚠️ Disclaimer

This bot is for educational/research use only. Automated actions on LinkedIn can violate their [Terms of Service](https://www.linkedin.com/legal/user-agreement), which may result in your account being restricted or banned.

## 🔐 Security Notice

⚠️ Do not store your real LinkedIn username and password in plain text. Instead, consider using:
- Environment variables (`os.environ`)
- `.env` files with `python-dotenv`
- Encrypted credential vaults

---

## 📸 Screenshots (Coming Soon)

## 🧩 How to Run

```bash
# Install dependencies
pip install selenium

# Run the bot
python linkedin_apply_bot.py
