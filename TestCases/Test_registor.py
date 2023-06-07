import time

from win32com.server import exception

from PageObject.RegistrationPage import *
from utilties.Readconfig import Redconfig


class Test_Registor:
    name = Redconfig.First_name()
    lastname = Redconfig.lastname()
    email = Redconfig.email()
    mobno = Redconfig.mobno()
    org = Redconfig.org()
    password = Redconfig.password()

    def test_case001(self, setup):
        self.driver = setup
        self.driver.get("https://account.devnagri.com/register")
        # print(self.driver.title)
        if self.driver.title == "Register - Devnagri":
            assert True
        else:
            assert False
        self.driver.close()

    def test_case002(self, setup):
        self.driver = setup
        self.driver.get("https://account.devnagri.com/register")
        reg = RegisterPage(self.driver)
        reg.setfirstname(self.name)
        reg.setlastname(self.lastname)
        reg.setemail(self.email)
        reg.setmobileno(self.mobno)
        reg.setorganisation(self.org)
        reg.setPassword(self.password)
        reg.confirmpassword(self.password)
        reg.clickregister()
        time.sleep(5)
        self.driver.implicitly_wait(5)
        print(self.driver.title)
        if self.driver.title == "Email Verification - Devnagri":
            assert True
        else:
            assert False
