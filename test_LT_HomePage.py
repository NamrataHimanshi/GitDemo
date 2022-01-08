# import time
# import pytest
# #import self as self
# from self import self
#
# from Homepage import LT_Homepage
#
#
# class test_Home_page(self):
#
#     def test_home_page(self):
#         driver = self.driver
#         self.driver.get("https://www.lambdatest.com/")
#         time.sleep(5)
#
#         web_page_title = "Free Cross Browser Testing Tool | Selenium Automation Testing Online"
#
#         try:
#             if driver.title == web_page_title:
#                 print("Web page loaded successfully")
#                 self.assertEqual(driver.title, web_page_title)
#
#         except Exception as error:
#             print(error+"Web page not loaded")
#
#         # Create an instance of the class so that you we can make use of the methods
#         # in the class
#         lt_home_page = LT_Homepage(driver)
#         if lt_home_page.get_lt_logo().is_displayed():
#             print (lt_home_page.get_lt_logo().get_attribute('alt')+" logo is successfully displayed")
#         else:
#             print("Lambdatest logo is not displayed")
#
#
