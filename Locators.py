# We have a look at another example where the web page under test is LambdaTest. Below are the broad test requirements:
#
# Setup Selenium WebDriver for the Chrome web browser.
# Open the web page under test https://www.lambdatest.com.
# Locate the Login Button on the page and log in using the registered credentials.
# Check whether the login operation is successful and the LambdaTest Automation Dashboard is available.
# Perform a clean-up operation before exiting the test.



class LT_Locator(object):


#locators for lamdatest Home page
    lt_logo = "//img[@alt='LambdaTest']"
    lt_signup = "//a[.='Start Free Testing']"
    lt_login = "//a[.='Log in']"
    lt_automation = "//ul[@class='navbar-nav']//a[.='Automation']"

#Locators for Lamdatest login page --  https://accounts.lambdatest.com/login
    lt_username= "//input[@id='email']"
    lt_password= "//input[@id='password']"
    lt_Login_button= "//button[@id='login-button']"





