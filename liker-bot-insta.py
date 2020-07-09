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
        time.sleep(5)
        bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
        time.sleep(4)
        bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(4)
        bot.find_element_by_xpath(' /html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(4)

    
    def like_photo(self):
        bot = self.bot
        bot.get("https://www.instagram.com/explore/tags/bitcoin/")#change the word bitcoin here , to whatever hashtag you want
        time.sleep(5)
        bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        bot.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]').click()
        time.sleep(5)
        bot.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
        time.sleep(4)
        bot.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
        time.sleep(3) 
        for i in range(100):
            bot.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
            time.sleep(4)
            bot.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
            time.sleep(3)
            
     
go = InstaBot('username','password') #change the username and password here 
go.Login()
go.like_photo()