import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginwithemailAuth_ATS_PA(unittest.TestCase):
#Sets up the location of the chrome driver
   def setUp(self):
       self.driver = webdriver.Chrome("C://python/gameboyz/myvenv/scripts/chromedriver.exe")
#Method to test the login with email authentication
   def test_Loginwithemailauth_PA(self):
       #Sets the variables needed for this
       user = "pythonrocks225@gmail.com"
       pwd = "eb708199"
       driver = self.driver
       driver.maximize_window() #Maximizes the size of the window
       driver.get("http://ebrousseau.pythonanywhere.com/") #Starts at the home page
       elem = driver.find_element_by_xpath("/html/body/header/div/nav/ul/span/div/li[2]/a").click() #Click the login button
       time.sleep(3)
       driver.get("http://ebrousseau.pythonanywhere.com/login/") #Once the login button is pushed it loads the login screen
       elem = driver.find_element_by_id("id_username") #Finds the username by ID
       elem.send_keys(user) #sends the user variable above and populates the username field
       elem = driver.find_element_by_id("id_password") #Finds the password field by ID
       elem.send_keys(pwd) #sends the password variable above and populates the password field
       time.sleep(3)
       elem.send_keys(Keys.RETURN) #acts as the enter key and submits the login
       driver.get("http://ebrousseau.pythonanywhere.com/") #Takes you back to the home page
       time.sleep(5)
       assert "logged in"
       elem = driver.find_element_by_xpath("/html/body/header/div[1]/nav/ul/span/div/li[1]/a").click() #Click on the logout button
       driver.get("http://ebrousseau.pythonanywhere.com/") #Take you back to the home page
       time.sleep(3)

       def tearDown(self):
           self.driver.close()


if __name__ == "__main__":
    unittest.main()

