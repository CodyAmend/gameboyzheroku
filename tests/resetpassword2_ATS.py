import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class resetpassword2 (unittest.TestCase):
#This function sets up the chrome driver.
   def setUp(self):
       self.driver = webdriver.Chrome("C://python/gameboyz/myvenv/scripts/chromedriver.exe")
#This is the method used to test the reset password fucntion on the website
   def test_resetpassword2(self):
       #Set up Variables
       user = "admin"
       pwd = "eb708199"
       driver = self.driver
       driver.maximize_window() #Maximizes the window
       # will need to change this to the valid password reset link (Can get this from Reset_Password_ATS
       driver.get("http://127.0.0.1:8000/reset/MQ/511-59c0d511f1947c2fee4c/")
       time.sleep(3)
       elem = driver.find_element_by_id("id_new_password1") #Finds the first new password field by ID
       elem.send_keys(pwd) #using the pwd variable to populate the first new password field
       time.sleep(3)
       elem = driver.find_element_by_id("id_new_password2") #Finds the second new password field by ID
       elem.send_keys(pwd) #using the pwd variable to populate the second new password field
       time.sleep(5)
       elem.send_keys(Keys.RETURN) #sneds the enter key to prograss to the next screen
       time.sleep(5)
       driver.get("http://127.0.0.1:8000/reset/done/") #This page tells you that the reset password has been complete
       elem = driver.find_element_by_xpath("/html/body/div[3]/p/a") #Clicks on the login again hyperlink
       driver.get("http://127.0.0.1:8000/login/") #Takes you to the login screen
       time.sleep(3)
       elem = driver.find_element_by_id("id_username") #Find the username by ID
       elem.send_keys(user) #use the user variable to populate the username field
       time.sleep(3)
       elem = driver.find_element_by_id("id_password") #Find the password by ID
       elem.send_keys(pwd) #use the pwd variable to populate the password field
       time.sleep(3)
       elem.send_keys(Keys.RETURN) #Enter key to login
       time.sleep(5)
       driver.get("http://127.0.0.1:8000/") #Go back to the home page





