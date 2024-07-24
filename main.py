from selenium import webdriver
from selenium.webdriver.common.by import By
import os

S_DOWNLOAD = 100
S_UPLOAD = 120
TWITTER_EMAIL = os.environ["Email"]
TWITTER_PASSWORD = os.environ["Password"]


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
