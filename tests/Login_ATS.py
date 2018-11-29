import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Login_ATS(unittest.TestCase):
#this sets up the location of the chrome driver
   def setUp(self):
       self.driver = webdriver.Chrome("C://python/gameboyz/myvenv/scripts/chromedriver.exe")
#Method is used to test login
   def test_Login(self):
       #initializes variables for logging in.
       user = "admin"
       pwd = "eb708199"
       driver = self.driver
       driver.maximize_window() #Maximizes the window
       driver.get("http://127.0.0.1:8000/") #Starts at the home page
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div[1]/nav/ul/div/span/li/a").click() #Clicks the login button
       time.sleep(3)
       driver.get("http://127.0.0.1:8000/login/") #After login button is clicked taken to the login screen
       elem = driver.find_element_by_id("id_username") #Find the username by ID
       elem.send_keys(user) #use the user variable to populate the username
       elem = driver.find_element_by_id("id_password") #FInd the password by ID
       elem.send_keys(pwd) #use the pwd variable to populate the password
       elem.send_keys(Keys.RETURN) #Simulates the enter key
       driver.get("http://127.0.0.1:8000") #Goes back to the login screen
       time.sleep(5)
       assert "logged in"
       elem = driver.find_element_by_xpath("/html/body/div[1]/nav/ul/div/span/li[1]/a").click() #Click on the logout button
       driver.get("http://127.0.0.1:8000") #take us back to the home page
       time.sleep(3)

       def tearDown(self):
           self.driver.close()


if __name__ == "__main__":
    unittest.main()

