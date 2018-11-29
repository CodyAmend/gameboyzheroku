import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class admin_scripts(unittest.TestCase):
    # this sets up the location of the chrome driver
    def setUp(self):
        self.driver = webdriver.Chrome("C://python/gameboyz/myvenv/scripts/chromedriver.exe")

    def test_Admin(self):
        # admin login
        driver = self.driver
        driver.maximize_window()
        driver.get("http://ebrousseau.pythonanywhere.com/admin")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        time.sleep(2)
        elem.send_keys("admin")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("eb708199")
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(3)
        driver.get("http://ebrousseau.pythonanywhere.com/admin")

        # add group
        driver.get("http://ebrousseau.pythonanywhere.com/admin/auth/group")
        time.sleep(2)
        driver.get("http://ebrousseau.pythonanywhere.com/admin/auth/group/add/")
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("Test_Group_Sel")
        time.sleep(2)
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(2)

        # update group

        driver.get("http://ebrousseau.pythonanywhere.com/admin/auth/group/")
        time.sleep(4)
        elem = driver.find_element_by_link_text("Test_Group_Sel")
        elem.click()
        elem = driver.find_element_by_id("id_name")
        elem.clear()
        time.sleep(2)
        elem.send_keys("Test_Group_Sel_update")
        time.sleep(4)
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(2)

        # delete group

        driver.get("http://ebrousseau.pythonanywhere.com/admin/auth/group/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Test_Group_Sel_update")
        elem.click()
        elem = driver.find_element_by_link_text("Delete")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//input[2]")
        elem.click()
        time.sleep(2)

        # add user
        driver.get("http://ebrousseau.pythonanywhere.com/admin")
        time.sleep(2)
        driver.get("http://ebrousseau.pythonanywhere.com/admin/auth/user/")
        time.sleep(2)
        driver.get("http://ebrousseau.pythonanywhere.com/admin/auth/user/add/")
        elem = driver.find_element_by_id("id_username")
        elem.clear()
        elem.send_keys("Test_User_Sel")
        elem = driver.find_element_by_id("id_password1")
        elem.clear()
        time.sleep(2)
        elem.send_keys("instructor1a")
        elem = driver.find_element_by_id("id_password2")
        elem.clear()
        elem.send_keys("instructor1a")
        time.sleep(2)
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(2)

        # update user

        driver.get("http://ebrousseau.pythonanywhere.com/admin/auth/user/")
        time.sleep(2)
        elem = driver.find_element_by_link_text("Test_User_Sel")
        elem.click()
        elem = driver.find_element_by_id("id_username")
        elem.clear()
        elem.send_keys("Test_User_Sel_Update")
        elem = driver.find_element_by_id("id_first_name")
        elem.clear()
        time.sleep(2)
        elem.send_keys("Test")
        elem = driver.find_element_by_id("id_last_name")
        elem.clear()
        elem.send_keys("User")
        time.sleep(2)
        elem = driver.find_element_by_id("id_email")
        elem.clear()
        elem.send_keys("jgombas@unomaha.edu")
        time.sleep(4)
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(2)

        # delete user

        driver.get("http://ebrousseau.pythonanywhere.com/admin/auth/user/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Test_User_Sel_Update")
        elem.click()
        elem = driver.find_element_by_link_text("Delete")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//input[2]")
        elem.click()
        time.sleep(3)

        # create category
        driver.get("http://ebrousseau.pythonanywhere.com/admin/shop/category")
        time.sleep(2)
        driver.get("http://ebrousseau.pythonanywhere.com/admin/shop/category/add/")
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("Games_Sel")
        time.sleep(3)
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(3)

        # update category

        driver.get("http://ebrousseau.pythonanywhere.com/admin/shop/category/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Games_Sel")
        elem.click()
        elem = driver.find_element_by_id("id_name")
        elem.clear()
        elem.send_keys("Games_Sel_update")
        time.sleep(4)
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(3)

        # delete category

        driver.get("http://ebrousseau.pythonanywhere.com/admin/shop/category/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Games_Sel_update")
        elem.click()
        elem = driver.find_element_by_link_text("Delete")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//input[2]")
        elem.click()
        time.sleep(3)

        # create game

        driver.get("http://ebrousseau.pythonanywhere.com/admin/shop/product/")
        time.sleep(2)
        driver.get("http://ebrousseau.pythonanywhere.com/admin/shop/product/add/")
        elem = driver.find_element_by_xpath("//select[@id='id_category']/option[2]")
        elem.click()
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("Game_Sel")
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("Test Game")
        elem = driver.find_element_by_id("id_price")
        elem.send_keys("60.00")
        time.sleep(4)
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(3)

    
        # update game

        driver.get("http://ebrousseau.pythonanywhere.com/admin/shop/product/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Game_Sel")
        elem.click()
        elem = driver.find_element_by_id("id_name")
        elem.clear()
        elem.send_keys("Game_Sel_update")
        time.sleep(2)
        elem = driver.find_element_by_id("id_description")
        elem.clear()
        elem.send_keys("Test Game Update")
        elem = driver.find_element_by_id("id_price")
        elem.clear()
        elem.send_keys("30.00")
        time.sleep(2)
        elem = driver.find_element_by_id("id_slug")
        elem.clear()
        elem.send_keys("game_sel_update")
        time.sleep(4)
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(3)

        # delete game

        driver.get("http://ebrousseau.pythonanywhere.com/admin/shop/product/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Game_Sel_update")
        elem.click()
        elem = driver.find_element_by_link_text("Delete")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//input[2]")
        elem.click()
        time.sleep(3)



        # get orders

        driver.get("http://ebrousseau.pythonanywhere.com/admin")
        time.sleep(2)
        driver.get("http://ebrousseau.pythonanywhere.com/admin/orders/order/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("38")
        elem.click()
        time.sleep(10)

        # get social auth

        driver.get("http://ebrousseau.pythonanywhere.com/admin")
        time.sleep(2)
        driver.get("http://ebrousseau.pythonanywhere.com/admin/social_django/usersocialauth/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("jgombas")
        elem.click()
        time.sleep(3)
        driver.get("http://ebrousseau.pythonanywhere.com/admin/social_django/usersocialauth/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("ErikBrousseau")
        elem.click()
        time.sleep(10)

        #get streaming information

        driver.get("http://ebrousseau.pythonanywhere.com/admin/")
        time.sleep(2)
        driver.get("http://ebrousseau.pythonanywhere.com/admin/streaming/stream/")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Fortnite")
        elem.click()
        time.sleep(5)



    def tearDown(self):
        self.driver.close()
