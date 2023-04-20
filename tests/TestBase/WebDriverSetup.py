import unittest
import os
from selenium import webdriver
from PageObject.RegisterAccountPage import RegisterAccountPage

class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        username = os.getenv("LT_USERNAME")
        accessToken = os.getenv("LT_ACCESS_KEY")
        gridUrl = "hub.lambdatest.com/wd/hub"

        options = webdriver.ChromeOptions()
        options.browser_version = "latest"
        options.platform_name = "Windows 11"
        lt_options = {}
        lt_options["username"] = username
        lt_options["accessKey"] = accessToken
        lt_options["build"] = "your build name"
        lt_options["project"] = "your project name"
        lt_options["name"] = "your test name"
        options.set_capability('LT:Options', lt_options)
        
        url = "https://"+username+":"+accessToken+"@"+gridUrl
        
        self.driver = webdriver.Remote(
            command_executor=url,
            options=options
        )

        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
        self.driver.maximize_window()

        self.register_account_page = RegisterAccountPage(self.driver)
    
    def tearDown(self):
        self.driver.quit()