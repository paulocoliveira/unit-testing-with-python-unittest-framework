import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

#This class will check the correct text to each label of the page
class TestLambdaTestPlaygroundRegisterFormLabels(unittest.TestCase):
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
        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
    
    def tearDown(self):
        self.driver.quit()
    
    def test_first_name_label(self):
        first_name_label = self.driver.find_element(By.XPATH, "//label[@for='input-firstname']").text
        self.assertEqual(first_name_label, "First Name")
    
    def test_last_name_label(self):
        last_name_label = self.driver.find_element(By.XPATH, "//label[@for='input-lastname']").text
        self.assertEqual(last_name_label, "Last Name")
    
    def test_email_label(self):
        email_name_label = self.driver.find_element(By.XPATH, "//label[@for='input-email']").text
        self.assertEqual(email_name_label, "E-Mail")
    
    def test_telephone_label(self):
        telephone_label = self.driver.find_element(By.XPATH, "//label[@for='input-telephone']").text
        self.assertEqual(telephone_label, "Telephone")
    
    def test_password_label(self):
        password_label = self.driver.find_element(By.XPATH, "//label[@for='input-password']").text
        self.assertEqual(password_label, "Password")
    
    def test_confirm_password_label(self):
        confirm_password_label = self.driver.find_element(By.XPATH, "//label[@for='input-confirm']").text
        self.assertEqual(confirm_password_label, "Password Confirm")
    
    def test_subscribe_label(self):
        subscribe_label = self.driver.find_element(By.XPATH, "//div[@class='form-group row']//label[@class='col-sm-2 col-form-label']").text
        self.assertEqual(subscribe_label, "Subscribe")

if __name__ == '__main__':
    unittest.main()