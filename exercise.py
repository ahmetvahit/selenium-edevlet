from edevletUserInfo import username, password, kurum
from selenium import webdriver
import time

class E_devlet:
    def __init__(self, username, password, kurum):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.kurum = kurum

    def signIn(self):
        self.browser.get("https://giris.turkiye.gov.tr/Giris/")
        time.sleep(2)
        
        self.browser.find_element_by_xpath("//*[@id='tridField']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='egpField']").send_keys(self.password)
        
        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='loginForm']/div[2]/input[4]").click()

        self.browser.find_element_by_xpath("//*[@id='searchField']").send_keys(self.kurum)
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='searchField']").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='a_0']/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='resultTable']/tbody/tr/td[3]/a").click()
        time.sleep(6)
        self.browser.find_element_by_xpath("//*[@id='contentStart']/ul/li[2]/a").click()

edevlet = E_devlet(username, password, kurum)
edevlet.signIn()