from selenium.webdriver.common.by import By
from selenium import webdriver

class Login_page:

    text_username_path =(By.XPATH,"//input[@id='Email']")
    text_password_path =(By.XPATH,"//input[@id='Password']")
    click_login_path =(By.XPATH,"//button[@type='submit']")
    click_logout_path = (By.XPATH,"//button[@type='submit']")

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(*Login_page.text_username_path).clear()
        self.driver.find_element(*Login_page.text_username_path).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*Login_page.text_password_path).clear()
        self.driver.find_element(*Login_page.text_password_path).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*Login_page.click_login_path).click()

    def click_logout_button(self):
        self.driver.find_element(*Login_page.click_logout_path).click()
