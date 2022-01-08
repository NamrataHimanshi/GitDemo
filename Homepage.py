from selenium.webdriver.common.by import By

from Locators import LT_Locator


class LT_Homepage(object):
    def __init__(self, driver):
        self.driver = driver

        self.lt_logo= driver.find_element(By.XPATH, LT_Locator.lt_logo)
        self.lt_signup= driver.find_element(By.XPATH, LT_Locator.lt_signup)
        self.lt_login = driver.find_element(By.XPATH, LT_Locator.lt_login)
        self.lt_automation = driver.find_element(By.XPATH, LT_Locator.lt_automation)

    def get_LT_Logo(self):
        return self.lt_logo

    def get_LT_signup(self):
        return self.lt_signup

    def get_LT_login(self):
        return self.lt_login

    def get_LT_automation(self):
        return self.lt_automation
