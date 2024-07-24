from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

S_DOWNLOAD = 100
S_UPLOAD = 120
TWITTER_EMAIL = os.environ["Email"]
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
            time.sleep(1)  # Check every second

        print(f"Download speed: {self.download} Mbps")
        print(f"Upload speed: {self.upload} Mbps")

    def tweet_at_provider(self):
        pass


# Create an instance of the bot and run the speed test
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
