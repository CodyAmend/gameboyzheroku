import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Login_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome("C://python/gameboyz/myvenv/scripts/chromedriver.exe")

   def test_Login(self):
       user = "admin"
       pwd = "eb708199"
       firstname = "test"
       lastname = "user"
       email = "pythonrocks225@gmail.com"
       phonenumber = "4026571789"
       address = "9810 V Plaza Apt 2a"
       postalcode = "68005"
       city = "Omaha"
       creditcardnumber = "4111111111111111"
       cvv = "123"
       expiredate = "12/20"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/")
       elem = driver.find_element_by_xpath("/html/body/div[1]/nav/ul/div/span/li/a").click()
       time.sleep(3)
       driver.get("http://127.0.0.1:8000/login/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("http://127.0.0.1:8000")
       time.sleep(5)
       assert "logged in"
       elem = driver.find_element_by_xpath("/html/body/div[1]/nav/ul/li[2]/a").click()
       driver.get("http://127.0.0.1:8000/games/")
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[2]/a").click()
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/a[2]").click()
       time.sleep(3)
       driver.get("http://127.0.0.1:8000/1/game-1/")
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()
       time.sleep(3)
       driver.get("http://127.0.0.1:8000/cart/")
       time.sleep(3)
       elem = driver.find_element_by_xpath("//a[contains(text(),'Checkout')]").click()
       driver.get("http://127.0.0.1:8000/orders/create/")
       time.sleep(3)
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys(firstname)
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys(lastname)
       elem = driver.find_element_by_id("id_email")
       elem.send_keys(email)
       elem = driver.find_element_by_id("id_phone_number")
       elem.send_keys(phonenumber)
       elem = driver.find_element_by_id("id_address")
       elem.send_keys(address)
       elem = driver.find_element_by_id("id_postal_code")
       elem.send_keys(postalcode)
       elem = driver.find_element_by_id("id_city")
       elem.send_keys(city)
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div[3]/form/p[8]/input").click()
       driver.get("http://127.0.0.1:8000/payment/process/")
       elem = driver.find_element_by_css_selector("#credit-card-number")
       elem.send_keys(creditcardnumber)
       elem = driver.find_element_by_id("cvv")
       elem.send_keys(cvv)
       elem = driver.find_element_by_id("expiration")
       elem.send_keys(expiredate)
       elem = driver.find_element_by_xpath("/html/body/div[3]/form/input[3]")
       driver.get("http://127.0.0.1:8000/payment/done/")

       def tearDown(self):
           self.driver.close()


if __name__ == "__main__":
    unittest.main()

