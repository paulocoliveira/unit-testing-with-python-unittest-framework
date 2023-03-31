import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLambdaTestPlaygroundEcommerce(unittest.TestCase):
    def setUp(self):       
        #lambdatest setup and opening the desired website
        username = "Your LambdaTest Username"
        accessToken = "Your LambdaTest Access Token"
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
        
        self.driver.maximize_window()
        self.driver.get("https://ecommerce-playground.lambdatest.io/")
    
    def tearDown(self):
        self.driver.quit()
    
    def test_page_title(self):
        title = self.driver.title
        self.assertEqual(title, "Your Store")

if __name__ == '__main__':
    unittest.main()