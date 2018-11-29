import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class login_scripts(unittest.TestCase):
    # this sets up the location of the chrome driver
    def setUp(self):
        self.driver = webdriver.Chrome("C://python/gameboyz/myvenv/scripts/chromedriver.exe")
        # Method is used to test login

    def test_Login_PA(self):
        # initializes variables for logging in.
        user = "admin"
        pwd = "eb708199"
        driver = self.driver
        driver.maximize_window()  # Maximizes the window
        driver.get("http://ebrousseau.pythonanywhere.com/")  # Starts at the home page
        time.sleep(3)
        elem = driver.find_element_by_xpath(
            "/html/body/header/div/nav/ul/span/div/li[2]/a").click()  # Clicks the login button
        time.sleep(3)
        driver.get(
            "http://ebrousseau.pythonanywhere.com/login/")  # After login button is clicked taken to the login screen
        elem = driver.find_element_by_id("id_username")  # Find the username by ID
        elem.send_keys(user)  # use the user variable to populate the username
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")  # FInd the password by ID
        elem.send_keys(pwd)  # use the pwd variable to populate the password
        time.sleep(2)
        elem.send_keys(Keys.RETURN)  # Simulates the enter key
        driver.get("http://ebrousseau.pythonanywhere.com/")  # Goes back to the login screen
        time.sleep(5)
        assert "logged in"
        elem = driver.find_element_by_xpath(
            "/html/body/header/div[1]/nav/ul/span/div/li[1]/a").click()  # Click on the logout button
        driver.get("http://ebrousseau.pythonanywhere.com/")  # take us back to the home page
        time.sleep(3)

        # Method to test the login with email authentication

    def test_Loginwithemailauth_PA(self):
        # Sets the variables needed for this
        user = "pythonrocks225@gmail.com"
        pwd = "eb708199"
        driver = self.driver
        driver.maximize_window()  # Maximizes the size of the window
        driver.get("http://ebrousseau.pythonanywhere.com/")  # Starts at the home page
        elem = driver.find_element_by_xpath(
            "/html/body/header/div/nav/ul/span/div/li[2]/a").click()  # Click the login button
        time.sleep(3)
        driver.get(
            "http://ebrousseau.pythonanywhere.com/login/")  # Once the login button is pushed it loads the login screen
        elem = driver.find_element_by_id("id_username")  # Finds the username by ID
        elem.send_keys(user)  # sends the user variable above and populates the username field
        elem = driver.find_element_by_id("id_password")  # Finds the password field by ID
        elem.send_keys(pwd)  # sends the password variable above and populates the password field
        time.sleep(3)
        elem.send_keys(Keys.RETURN)  # acts as the enter key and submits the login
        driver.get("http://ebrousseau.pythonanywhere.com/")  # Takes you back to the home page
        time.sleep(5)
        assert "logged in"
        elem = driver.find_element_by_xpath(
            "/html/body/header/div[1]/nav/ul/span/div/li[1]/a").click()  # Click on the logout button
        driver.get("http://ebrousseau.pythonanywhere.com/")  # Take you back to the home page
        time.sleep(3)
        # Method is used to test login

    def test_SignUp_PA(self):
        # initializes variables for logging in.
        user = "instructor"
        firstname = "George"
        lastname = "Royce"
        email = "groyce@unomaha.edu"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()  # Maximizes the window
        driver.get("http://ebrousseau.pythonanywhere.com/")  # Starts at the home page
        time.sleep(3)
        elem = driver.find_element_by_xpath(
            "/html/body/header/div/nav/ul/span/div/li[1]/a").click()  # Clicks the Signup button
        time.sleep(3)
        driver.get(
            "http://ebrousseau.pythonanywhere.com/register/")  # After signup button is clicked taken to the register screen
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")  # Find the username by ID
        time.sleep(2)
        elem.send_keys(user)  # use the user variable to populate the username
        time.sleep(2)
        elem = driver.find_element_by_id("id_first_name")  # Finds the firstname by ID
        time.sleep(2)
        elem.send_keys(firstname)  # populates the email with the firstname variable
        time.sleep(2)
        elem = driver.find_element_by_id("id_last_name") #Finds the lastname by ID
        elem.send_keys(lastname) #populates the lastname variable
        time.sleep(2)
        elem = driver.find_element_by_id("id_email")  # Finds the email by ID
        time.sleep(2)
        elem.send_keys(email)  # populates the email with the email variable
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")  # FInd the password by ID
        time.sleep(2)
        elem.send_keys(pwd)  # use the pwd variable to populate the password
        time.sleep(2)
        elem = driver.find_element_by_id("id_password2")  # Finds the password by ID
        time.sleep(2)
        elem.send_keys(pwd)  # populates this field with the pwd variable
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/form/p[7]/input").click()  # Clicks on the create an account button
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

        # edit profile

        driver.get("http://ebrousseau.pythonanywhere.com")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Edit Profile")
        elem.click()
        elem = driver.find_element_by_id("id_last_name")
        elem.clear()
        elem.send_keys("Dude")
        elem = driver.find_element_by_id("id_date_of_birth")
        elem.clear()
        elem.send_keys("1987-05-18")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/form/p[7]/input")
        elem.click()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()