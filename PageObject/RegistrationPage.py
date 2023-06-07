import selenium
from selenium.webdriver.common.by import By


class RegisterPage:
    First_name_xpath = "//input[@id='first_name']"
    Last_name_xpath = "//input[@id='last_name']"
    Email_xpath = "//input[@id='email']"
    Mobile_no_xpath = "//input[@id='phone']"
    Organization_Name = "//input[@id='organization_name']"
    Set_password_xpath = "//input[@id='password']"
    confirm_password_xpath = "//input[@id='password_confirmation']"
    Register_btn_xpath = "//button[@type='submit']"
    resend_email_xpath = '//button[@type="submit"]'

    def __init__(self, driver):
        self.driver = driver

    def setfirstname(self, first_name):
        self.driver.find_element(By.XPATH, self.First_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.First_name_xpath).send_keys(first_name)

    def setlastname(self, last_name):
        self.driver.find_element(By.XPATH, self.Last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.Last_name_xpath).send_keys(last_name)

    def setemail(self, email_id):
        self.driver.find_element(By.XPATH, self.Email_xpath).clear()
        self.driver.find_element(By.XPATH, self.Email_xpath).send_keys(email_id)

    def setmobileno(self, mob_no):
        self.driver.find_element(By.XPATH, self.Mobile_no_xpath).clear()
        self.driver.find_element(By.XPATH, self.Mobile_no_xpath).send_keys(mob_no)

    def setorganisation(self, org_name):
        self.driver.find_element(By.XPATH, self.Organization_Name).clear()
        self.driver.find_element(By.XPATH, self.Organization_Name).send_keys(org_name)

    def setPassword(self, passowrd):
        self.driver.find_element(By.XPATH, self.Set_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.Set_password_xpath).send_keys(passowrd)

    def confirmpassword(self, password):
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(password)

    def clickregister(self):
        self.driver.find_element(By.XPATH, self.Register_btn_xpath).click()

    def resdenemail(self):
        self.driver.find_element(By.XPATH, self.resend_email_xpath).isDisplayed()