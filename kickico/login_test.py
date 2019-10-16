# -*- coding: utf-8 -*-


import unittest
from selenium.webdriver.firefox.webdriver import WebDriver
import re


class UpdateRes(unittest.TestCase):

    def setUp(self):
        self.wd = WebDriver()
        self.url = "https://www.kickico.com/signin"
        self.login = "XXXXXX@gmail.com"
        self.passw = "XXXXXX"
        self.wd.implicitly_wait(15)

    def perform_login(self,  login="", password=""):
        driver = self.wd
        driver.get(self.url)
        login_input = driver.find_element_by_id("UserLogin_username")
        login_input.clear()
        login_input.send_keys(login)
        passwd_input = driver.find_element_by_id("UserLogin_password")
        passwd_input.clear()
        passwd_input.send_keys(password)
        driver.find_element_by_css_selector("input.btn").click()
        return driver

    def test_good_credentials(self):
        driver = self.perform_login(login=self.login, password=self.passw)
        is_profile_button = driver.find_element_by_class_name("profile-nav-avatar").is_enabled()
        assert is_profile_button
        driver.close()

    def test_email_to_uppercase(self):
        upper_login = self.login.upper()
        print('Email to upper case is %s' % upper_login)
        driver = self.perform_login(login=upper_login, password=self.passw)
        is_profile_button = driver.find_element_by_class_name("profile-nav-avatar").is_enabled()
        assert is_profile_button
        driver.close()

    def test_empty_credentials(self):
        driver = self.perform_login()
        login_input = driver.find_element_by_id("UserLogin_username")
        passwd_input = driver.find_element_by_id("UserLogin_password")
        assert login_input.is_displayed()
        assert passwd_input.is_displayed()
        assert not login_input.get_attribute("value")
        assert not passwd_input.get_attribute("value")
        driver.close()

    def test_empty_password(self):
        driver = self.perform_login(login=self.login, password="")
        passwd_input = driver.find_element_by_id("UserLogin_password")
        assert passwd_input.is_displayed()
        assert not passwd_input.get_attribute("value")
        driver.close()

    def test_empty_login(self):
        driver = self.perform_login(login="", password=self.passw)
        login_input = driver.find_element_by_id("UserLogin_username")
        assert login_input.is_displayed()
        assert not login_input.get_attribute("value")
        driver.close()

    def test_swapped_login_and_password(self):
        driver = self.perform_login(login=self.passw, password=self.login)
        login_input = driver.find_element_by_id("UserLogin_username")
        passwd_input = driver.find_element_by_id("UserLogin_password")
        assert login_input.is_displayed()
        assert passwd_input.is_displayed()
        assert login_input.get_attribute("value") == self.passw
        assert passwd_input.get_attribute("value") == self.login
        driver.close()

    def test_script_injection(self):
        raw_string = r"<script>alert(123)</script>"
        driver = self.perform_login(login=raw_string, password=self.passw)
        html = driver.page_source
        security_error = re.search("Please complete the security check to access", html)
        assert security_error
        driver.close()
        
    def minimal_username_and_password(self):
        """
        Username should be at least 3 simbols
        Password should be at least 4 simbols
        according to Registration form
        """
        login = "vlad_goreletsky@lexpr.ru"
        password = "Kpv1"
        driver = self.perform_login(login=login, password=password)
        is_profile_button = driver.find_element_by_class_name("profile-nav-avatar").is_enabled()
        assert is_profile_button
        driver.close()

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
