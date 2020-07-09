from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome('/Users/harsh/Downloads/chromedriver')

    def Login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(3)
        bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
        time.sleep(4)
        bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(4)
        bot.find_element_by_xpath(' /html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(4)


    def openStories(self):
        bot = self.bot
        bot.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[1]/div/div/div/div/ul/li[3]/div/button/div[1]/span/img').click()
        time.sleep(2)
        bot.find_element_by_xpath('/div/div/div/div/div/div[1]').click()
        

go = InstaBot('username','password')
go.Login()
go.openStories()