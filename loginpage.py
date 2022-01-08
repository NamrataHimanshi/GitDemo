
from selenium.webdriver.common.by import By

from Locators import LT_Locator


class Lt_Loginpage():
    def __init__(self, driver):
        self.driver = driver

        self.lt_username= driver.find_element(By.XPATH, LT_Locator.lt_username)
        self.lt_password = driver.find_element(By.XPATH, LT_Locator.lt_password)
        self.lt_login = driver.find_element(By.XPATH, LT_Locator.lt_login)

    def get_LT_username(self):
        return self.lt_username

    def get_LT_password(self):
        return self.lt_password

    def get_LT_Login(self):
        return self.lt_login

