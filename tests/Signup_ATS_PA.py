import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SignUp_ATS_PA(unittest.TestCase):
#this sets up the location of the chrome driver
   def setUp(self):
       self.driver = webdriver.Chrome("C://python/gameboyz/myvenv/scripts/chromedriver.exe")
#Method is used to test login
   def test_SignUp_PA(self):
       #initializes variables for logging in.
       user = "instructor"
       firstname = "George"
       email = "groyce@unomaha.edu"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window() #Maximizes the window
       driver.get("http://ebrousseau.pythonanywhere.com/") #Starts at the home page
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/header/div/nav/ul/span/div/li[1]/a").click() #Clicks the Signup button
       time.sleep(3)
       driver.get("http://ebrousseau.pythonanywhere.com/register/") #After signup button is clicked taken to the register screen
       time.sleep(3)
       elem = driver.find_element_by_id("id_username") #Find the username by ID
       time.sleep(3)
       elem.send_keys(user) #use the user variable to populate the username
       time.sleep(3)
       elem = driver.find_element_by_id("id_first_name") #Finds the firstname by ID
       time.sleep(3)
       elem.send_keys(firstname) #populates the email with the firstname variable
       time.sleep(3)
       elem = driver.find_element_by_id("id_email") #Finds the email by ID
       time.sleep(3)
       elem.send_keys(email) #populates the email with the email variable
       time.sleep(3)
       elem = driver.find_element_by_id("id_password") #FInd the password by ID
       time.sleep(3)
       elem.send_keys(pwd) #use the pwd variable to populate the password
       time.sleep(3)
       elem = driver.find_element_by_id("id_password2") #Finds the password by ID
       time.sleep(3)
       elem.send_keys(pwd) #populates this field with the pwd variable
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div/form/p[6]/input").click() #Clicks on the create an account button
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div/p/a").click()  # Clicks on the login again hyperlink
       time.sleep(3)
       driver.get("http://ebrousseau.pythonanywhere.com/login/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(5)
       elem.send_keys(Keys.RETURN)
       driver.get("http://ebrousseau.pythonanywhere.com/")
       time.sleep(5)







       def tearDown(self):
           self.driver.close()


if __name__ == "__main__":
    unittest.main()

