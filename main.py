from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

chrome_driver_path = "D:\chromedriver.exe"
net_link = "https://www.speedtest.net/"
twitter_link = "https://twitter.com/"
twitter_mailid = "k.balaganesh26@gmail.com"
twitter_password = os.environ.get("password")
twitter_username = "@Balaganesh__"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.download_speed = 0
        self.upload_speed = 0
        self.get_internet_speed()

    def get_internet_speed(self):
        self.driver.get(net_link)
        time.sleep(3)

        start_button = self.driver.find_element_by_css_selector(".start-button a")
        start_button.click()

        time.sleep(60)
        download = int(float(self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '2]/div/div[2]/span').text))

        upload = int(float(self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '3]/div/div[2]/span').text))
        self.upload_speed = upload
        self.download_speed = download

    def tweet_at_provider(self, mail_id, secrect_password, username, complain_statement):
        self.driver.get(twitter_link)
        time.sleep(10)
        sign_in = self.driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/div['
                                                    '4]/span/span')
        sign_in.click()

        sighin_with_mail = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a')
        sighin_with_mail.click()
        time.sleep(10)
        user_name = self.driver.find_element_by_css_selector(
            'div input')
        user_name.send_keys(mail_id)
        user_name.send_keys(Keys.ENTER)
        time.sleep(10)
        try:
            u = self.driver.find_element_by_css_selector("div input")
            u.send_keys(username)
            u.send_keys(Keys.ENTER)
            time.sleep(5)
        finally:
            time.sleep(5)
            password = self.driver.find_element_by_css_selector("div input")
            password.send_keys(secrect_password)
            password.send_keys(Keys.ENTER)
        time.sleep(10)
        self.driver.get("https://twitter.com/home")
        time.sleep(10)
        tweet = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet.click()
        time.sleep(5)

        text_box = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div['
            '1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div['
            '2]/div')
        text_box.send_keys(complain_statement)

        tweet_button = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div['
            '1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweet_button.click()


bot = InternetSpeedTwitterBot()
statement = f"Hey internet provider ,why is my internet speed {bot.download_speed}down/{bot.upload_speed}Up when i " \
            f"pay for 100down/10up "


if bot.upload_speed < 10 or bot.download_speed < 50:
    bot.tweet_at_provider(
        username=twitter_username, secrect_password=twitter_password, mail_id=twitter_mailid,
        complain_statement=statement
    )
time.sleep(5)
bot.driver.quit()    
    
