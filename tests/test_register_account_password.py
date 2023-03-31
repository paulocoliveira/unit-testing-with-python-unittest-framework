import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

#This class will check specifically the behaviour of the password and confirm password fields
class TestLambdaTestPlaygroundRegisterFormPassword(unittest.TestCase):
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

        first_name = self.driver.find_element(By.ID, "input-firstname")
        first_name.send_keys("FirstName")

        last_name = self.driver.find_element(By.ID, "input-lastname")
        last_name.send_keys("LastName")

        email = self.driver.find_element(By.ID, "input-email")
        email.send_keys("email13100@email.com")

        telephone = self.driver.find_element(By.ID, "input-telephone")
        telephone.send_keys("+351999888777")

        terms = self.driver.find_element(By.XPATH, "//label[@for='input-agree']")
        terms.click()
    
    def tearDown(self):
        self.driver.quit()
    
    def test_password_not_filled(self):
        continue_button = self.driver.find_element(By.XPATH, "//input[@value='Continue']")
        continue_button.click()

        password_error_message = self.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text
        self.assertEqual(password_error_message, "Password must be between 4 and 20 characters!")
    
    def test_password_less_than_minimum(self):
        password = self.driver.find_element(By.ID, "input-password")
        password.send_keys("123")
        
        continue_button = self.driver.find_element(By.XPATH, "//input[@value='Continue']")
        continue_button.click()

        password_error_message = self.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text
        self.assertEqual(password_error_message, "Password must be between 4 and 20 characters!")
    
    #this test will fail, message shows that 20 is the maximum size, but this is not working properly
    def test_password_greater_than_maximum(self):
        password = self.driver.find_element(By.ID, "input-password")
        password.send_keys("123456789012345678901")
        
        continue_button = self.driver.find_element(By.XPATH, "//input[@value='Continue']")
        continue_button.click()

        password_error_message = self.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text
        self.assertEqual(password_error_message, "Password must be between 4 and 20 characters!")
    
    def test_password_without_confirmation(self):
        password = self.driver.find_element(By.ID, "input-password")
        password.send_keys("123456")
        
        continue_button = self.driver.find_element(By.XPATH, "//input[@value='Continue']")
        continue_button.click()

        password_confirm_error_message = self.driver.find_element(By.XPATH, "//input[@id='input-confirm']/following-sibling::div").text
        self.assertEqual(password_confirm_error_message, "Password confirmation does not match password!")
    
    def test_password_wrong_confirmation(self):
        password = self.driver.find_element(By.ID, "input-password")
        password.send_keys("123456")

        password_confirm = self.driver.find_element(By.ID, "input-confirm")
        password_confirm.send_keys("12345")
        
        continue_button = self.driver.find_element(By.XPATH, "//input[@value='Continue']")
        continue_button.click()

        password_confirm_error_message = self.driver.find_element(By.XPATH, "//input[@id='input-confirm']/following-sibling::div").text
        self.assertEqual(password_confirm_error_message, "Password confirmation does not match password!")
    
    def test_password_correct_confirmation(self):
        password = self.driver.find_element(By.ID, "input-password")
        password.send_keys("123456")

        password_confirm = self.driver.find_element(By.ID, "input-confirm")
        password_confirm.send_keys("123456")
        
        continue_button = self.driver.find_element(By.XPATH, "//input[@value='Continue']")
        continue_button.click()

        new_page_title = self.driver.title
        self.assertEqual(new_page_title, "Your Account Has Been Created!")

if __name__ == '__main__':
    unittest.main()