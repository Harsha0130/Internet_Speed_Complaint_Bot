# Internet Speed Complaint Bot

- This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp for 2023" course by Dr. Angela Yu.

### Project Overview

- **Purpose:**
  - Developed a Python script to monitor internet speeds using a speed test service and automatically tweet a complaint if the speeds fall below predefined thresholds.
  - This project is part of a Python automation series focusing on internet speed monitoring and automated complaint handling.

- **Functionality:**
  - **Speed Check:**
    - Uses Selenium to interact with a speed test website (`https://speed.is/`) to measure download and upload speeds.
    - Compares the measured speeds against predefined thresholds (`S_DOWNLOAD` and `S_UPLOAD`).
    - Updates the internal speed values if the measured speeds are stable and non-zero.

  - **Twitter Integration:**
    - Automates the Twitter login process and posting functionality using Selenium WebDriver.
    - Posts a complaint tweet if the measured speeds are below the specified thresholds.

- **Technology Stack:**
  - **Selenium:** For automating browser interactions.
  - **Python:** Programming language used for scripting.

- **Prerequisites:**
  - Python 3.x installed.
  - Required Python library: `selenium` (install via `pip install selenium`).
  - ChromeDriver installed and configured (download from [ChromeDriver](https://sites.google.com/chromium.org/driver/)).
  - Environment variables set for Twitter credentials (`TWITTER_EMAIL`, `TWITTER_USERNAME`, `TWITTER_PASSWORD`).

### Script Details

- **`get_internet_speed()` Method:**
  - Navigates to the speed test website.
  - Initiates the speed test and retrieves download and upload speeds.
  - Waits until the speeds stabilize before updating the internal values.

- **`tweet_at_provider()` Method:**
  - Logs into Twitter using Selenium WebDriver.
  - Posts a complaint tweet if the download and upload speeds are below the specified thresholds.
  - Provides feedback if the internet speeds are acceptable.

### Replace placeholders in the script:

- Replace `TWITTER_EMAIL` with your Twitter email.
- Replace `TWITTER_USERNAME` with your Twitter username.
- Replace `TWITTER_PASSWORD` with your Twitter password.
- Adjust `S_DOWNLOAD` to your acceptable minimum download speed (in Mbps).
- Adjust `S_UPLOAD` to your acceptable minimum upload speed (in Mbps).

### Screenrecord: 

https://github.com/user-attachments/assets/119d14bd-9699-4a3b-8948-39cbdfd4afb2




