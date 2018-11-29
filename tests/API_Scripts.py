import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class API_Scripts(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome("C://python/gameboyz/myvenv/scripts/chromedriver.exe")

   def test_API_Scripts(self):
       driver = self.driver
       driver.maximize_window()
       # select and purchase game

       driver.get("http://ebrousseau.pythonanywhere.com/Games")
       time.sleep(5)
       driver.get("http://ebrousseau.pythonanywhere.com/1/witcher3/")
       time.sleep(5)
       elem = driver.find_element_by_xpath("//input[@value='Add to cart']")
       elem.click()
       time.sleep(3)

       # select & checkout

       driver.get("http://ebrousseau.pythonanywhere.com/cart/")
       time.sleep(3)
       elem = driver.find_element_by_link_text("Checkout")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_id("id_first_name")
       elem.clear()
       elem.send_keys("Jonathan")
       time.sleep(2)
       elem = driver.find_element_by_id("id_last_name")
       elem.clear()
       elem.send_keys("Gombas")
       time.sleep(2)
       elem = driver.find_element_by_id("id_email")
       elem.clear()
       elem.send_keys("jgombas@unomaha.edu")
       time.sleep(2)
       elem = driver.find_element_by_id("id_phone_number")
       elem.clear()
       elem.send_keys("4026571789")
       time.sleep(2)
       elem = driver.find_element_by_id("id_address")
       elem.clear()
       elem.send_keys("5024 Maple Street")
       time.sleep(2)
       elem = driver.find_element_by_id("id_postal_code")
       elem.clear()
       elem.send_keys("68104")
       time.sleep(2)
       elem = driver.find_element_by_id("id_city")
       elem.clear()
       elem.send_keys("Omaha")
       time.sleep(5)
       elem = driver.find_element_by_xpath("//input[@value='Place order']")
       elem.click()
       time.sleep(3)
       driver.switch_to.frame(0)
       elem = driver.find_element_by_xpath("//input[@id='credit-card-number']")
       elem.clear()
       elem.send_keys("4111 1111 1111 1111")
       driver.switch_to.default_content()
       driver.switch_to.frame(1)
       elem = driver.find_element_by_id("cvv")
       elem.clear()
       elem.send_keys("123")
       driver.switch_to.default_content()
       driver.switch_to.frame(2)
       elem = driver.find_element_by_id("expiration")
       elem.clear()
       elem.send_keys("1220")
       driver.switch_to.default_content()
       time.sleep(4)
       elem = driver.find_element_by_xpath("//input[@value='Pay']")
       elem.click()
       time.sleep(5)

   def tearDown(self):
        self.driver.close()