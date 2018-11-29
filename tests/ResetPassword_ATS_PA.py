import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class resetpassword_PA(unittest.TestCase):
#set up to use the chrome driver
   def setUp(self):
       self.driver = webdriver.Chrome("C://python/gameboyz/myvenv/scripts/chromedriver.exe")
#Function used to test the reset password function
   def testresetpassword_PA(self):
       #Set up variables
       user = "admin"
       pwd = "eb708199"
       email = "pythonrocks225@gmail.com"
       driver = self.driver
       driver.maximize_window() #Maximize the window
       driver.get("http://ebrousseau.pythonanywhere.com/") #Start off on the home page
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/header/div/nav/ul/span/div/li[2]/a").click() #Click on the login button
       time.sleep(3)
       driver.get("http://ebrousseau.pythonanywhere.com/login/") #login button takes you to the login screen
       elem = driver.find_element_by_xpath("/html/body/div/main/p[3]/a").click() #Click on the forgot password link
       time.sleep(3)
       driver.get("http://ebrousseau.pythonanywhere.com/password_reset/") #takes us to the page where we can put in our email for password reset link
       elem = driver.find_element_by_id("id_email") #finds the email by ID
       time.sleep(3)
       elem.send_keys(email) #uses the email variable to populate the email field
       elem.send_keys(Keys.RETURN) #Submit and send the email
       time.sleep(3)
       driver.get("http://ebrousseau.pythonanywhere.com/password_reset/done/") #Provide a page that tells you to check your email.
       time.sleep(3)




       def tearDown(self):
           self.driver.close()

   if __name__ == "__main__":
       unittest.main()