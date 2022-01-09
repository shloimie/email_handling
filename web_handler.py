from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import re


class WebHandleing():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.set_window_size(900, 650)


    def check_url(self, in_url):
        in_url = in_url
        if in_url[:4] != "http":
            in_url= "https://www.google.com/search?q=" + re.sub("\s", "+", in_url) + "&hl=en"
        return in_url
    def get(self,inp):
        self.driver.get(inp)

    def send_tabs(self,amount):
        actions = ActionChains(self.driver)
        for _ in range(amount+17):
            actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()
    def screen(self, name = "screenshot"):
        self.driver.save_screenshot(name + ".png")

