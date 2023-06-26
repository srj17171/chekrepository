from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from pageobjects.loginpage import Login_page
from utilities.readproperties import Readconfig
from utilities.logger import LogGen

class Test_login:
    url = Readconfig.get_url()
    username = Readconfig.get_username()
    password = Readconfig.get_password()
    log = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_001(self,setup):
         self.log.info("test_login_001 is started")
         self.driver = setup
         self.log.info("browser started")
         self.driver.get(self.url)
         self.log.info("Going to Url -->" + self.url)
         self.lp = Login_page(self.driver)
         self.lp.enter_username(self.username)
         self.lp.enter_password(self.password)
         self.lp.click_login_button()
         if self.driver.title == "Dashboard / nopCommerce administration":
             self.driver.save_screenshot("C:\\Users\\HOME\\PycharmProjects\\pythonProject4\\screenshot\\test001.png")

             assert True
             self.log.info("test_page_title_001 is Passed")

         else:
             self.driver.save_screenshot("C:\\Users\\HOME\\PycharmProjects\\pythonProject4\\screenshot\\test001.png")
             assert False

         self.log.info("test_page_title_001 is Completed")
    @pytest.mark.regression
    def test_login_tittle_002(self,setup):
        self.log.info("test_login_001 is started")
        self.driver = setup
        self.log.info("browser started")
        self.driver.get(self.url)
        self.log.info("Going to Url -->" + self.url)

        if self.driver.title == "Dashboard / nopCommerce administration":
            self.driver.save_screenshot("C:\\Users\\HOME\\PycharmProjects\\pythonProject4\\screenshot\\test001.png")

            assert True
            self.log.info("test_page_title_001 is Passed")

        else:
            self.driver.save_screenshot("C:\\Users\\HOME\\PycharmProjects\\pythonProject4\\screenshot\\test001.png")
            assert False

        self.log.info("test_page_title_001 is Completed")







