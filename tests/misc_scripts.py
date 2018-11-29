import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class misc_scripts(unittest.TestCase):
    # this sets up the location of the chrome driver
    def setUp(self):
        self.driver = webdriver.Chrome("C://python/gameboyz/myvenv/scripts/chromedriver.exe")

    def test_misc_scripts(self):

        driver = self.driver
        driver.maximize_window()
        # homepage

        driver.get("http://ebrousseau.pythonanywhere.com")
        time.sleep(15)

        # About

        driver.get("http://ebrousseau.pythonanywhere.com/About")
        time.sleep(8)

        # contact

        driver.get("http://ebrousseau.pythonanywhere.com/Contact")
        time.sleep(8)

    def tearDown(self):
        self.driver.close()