import time
import  pytest
from logging import exception
from selenium import webdriver
from Homepage import LT_Homepage
from loginpage import Lt_Loginpage

username = "Nam018kari@gmail.com"
password = "Abcxyz"

class test_Login_page():
    def test_login_page(self):
        driver = webdriver.Chrome(executable_path="C:\Selenium_path\chromedriver")
        driver = self.driver
        self.driver.get("https://lambdatest.com/")
        self.driveer.maximize()
        time.sleep(5)

        # Create an instance of the class so that you we can make use of the methods
        # in the class
        lt_home_page = LT_Homepage(driver)

        # Click the login button to go to the next page https://accounts.lambdatest.com/login

        lt_home_page.lt_login.click()

        # Re-verify whether the page is loaded successfully

        web_page_title = "Login - LambdaTest"
        try:

            if driver.title == web_page_title:
                print("page loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except exception as error:
            print(error+"page not loaded")

        # Create an object of the Login Class

        lt_login_obj = Lt_Loginpage(driver)

        time.sleep(5)

        lt_login_obj.lt_username.send_keys(username)
        lt_login_obj.lt_password.send_keys(password)

    # Click the login button to go to the dashboard
        lt_login_obj.lt_login.click()

        time.sleep(5)
        #
        # # See if the login is successful by checking the title, if successful than exit
        # # else report an Error
        # web_page_title = "Welcome - LambdaTest"
        #
        # try:
        #     if driver.title == web_page_title:
        #         print("User Logged in successfully")
        #         self.assertEqual(driver.title, web_page_title)
        # except Exception as error:
        #     print(error + "WebPage Failed to load")
        #
        # sleep(10)
        #
        # # Click on the automation tab and than exit
        # automation_element = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//a[.='Automation']
        #     '))
        #                                 )
        # automation_element.click()
        #
        # sleep(5)
        #
        # print("Login test completed successfully")
        #
