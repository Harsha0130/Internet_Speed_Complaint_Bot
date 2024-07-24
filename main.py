from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import os
import time

S_DOWNLOAD = 100
S_UPLOAD = 120
TWITTER_EMAIL = os.environ["Email"]
TWITTER_USERNAME = os.environ["Username"]
TWITTER_PASSWORD = os.environ["Password"]


class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.upload = 0
        self.download = 0

    def get_internet_speed(self):
        self.driver.get("https://speed.is/")
        go_button = self.driver.find_element(By.CLASS_NAME, value="text-primary")
        go_button.click()

        previous_download = None
        previous_upload = None

        while True:
            current_download = self.driver.find_element(By.ID, "result_download_val").text
            current_upload = self.driver.find_element(By.ID, "result_upload_val").text

            if previous_download and previous_upload:
                # Break if the speeds have stabilized and are non-zero
                if current_download == previous_download and current_upload == previous_upload:
                    if float(current_download) > 0 and float(current_upload) > 0:
                        self.download = current_download
                        self.upload = current_upload
                        break

            previous_download = current_download
            previous_upload = current_upload
            time.sleep(2)  # Check every second

    def tweet_at_provider(self):
        if float(self.download) < S_DOWNLOAD and float(self.upload) < S_UPLOAD:
            # wait = WebDriverWait(self.driver, 10)
            self.driver.get("https://x.com/i/flow/login")
            time.sleep(5)
            email = self.driver.find_element(By.NAME, value="text")
            email.send_keys(TWITTER_EMAIL, Keys.ENTER)
            # For reverification with username
            time.sleep(2)
            email = self.driver.find_element(By.NAME, value="text")
            email.send_keys(TWITTER_USERNAME, Keys.ENTER)
            time.sleep(1)
            email = self.driver.find_element(By.NAME, value="password")
            email.send_keys(TWITTER_PASSWORD, Keys.ENTER)

            time.sleep(5)
            tweet_box = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0"]')
            tweet_box.send_keys(f"Hey @SallSatinder, why is my internet speed is Download_speed = {self.download}Mbps"
                                f"| Upload_speed = {self.upload}Mbps, when i pay for {S_DOWNLOAD}Mbps|{S_UPLOAD}Mbps")
            time.sleep(2)
            post = self.driver.find_element(By.CSS_SELECTOR, value='button[data-testid="tweetButtonInline"]')
            post.click()

        else:
            print("Your internet speed good")
            print(f"Download speed: {self.download} Mbps")
            print(f"Upload speed: {self.upload} Mbps")


# Create an instance of the bot and run the speed test
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
