import unittest
from selenium import webdriver
from PageObject.RegisterAccountPage import RegisterAccountPage

class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        #lambdatest setup and opening the desired website
        username = "paulocol"
        accessToken = "8Yl2j4huUuLPcQIkt54LrxujI0Of43g1vZaSAbBiCi8FRMdi7Y"
        gridUrl = "hub.lambdatest.com/wd/hub"
        
        capabilities = {
            'LT:Options' : {
                "user" : "Your LambdaTest Username",
                "accessKey" : "Your LambdaTest Access Key",
                "build" : "your build name",
                "name" : "your test name",
                "platformName" : "Windows 11",
            },
            "browserName" : "Chrome",
            "browserVersion" : "103.0",
        }
        
        url = "https://"+username+":"+accessToken+"@"+gridUrl
        
        self.driver = webdriver.Remote(
            command_executor=url,
            desired_capabilities=capabilities
        )

        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
        self.driver.maximize_window()

        self.register_account_page = RegisterAccountPage(self.driver)
    
    def tearDown(self):
        self.driver.quit()