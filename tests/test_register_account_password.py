import unittest
from TestBase.WebDriverSetup import WebDriverSetup
from selenium.webdriver.common.by import By
from PageObject.Locators import Locators

#This class will check specifically the behaviour of the password and confirm password fields
class TestLambdaTestPlaygroundRegisterFormPassword(WebDriverSetup):

    def test_password_correct_confirmation(self):
        first_name = self.register_account_page.getFirstName()
        first_name.send_keys("FirstName")

        last_name = self.register_account_page.getLastName()
        last_name.send_keys("LastName")

        email = self.register_account_page.getEmail()
        email.send_keys("email13117@email.com")

        telephone = self.register_account_page.getTelephone()
        telephone.send_keys("+351999888777")
        
        password = self.register_account_page.getPassword()
        password.send_keys("123456")

        password_confirm = self.register_account_page.getConfirmPassword()
        password_confirm.send_keys("123456")

        terms = self.register_account_page.getTerms()
        terms.click()

        continue_button = self.register_account_page.getContinueButton()
        continue_button.click()

        new_page_title = self.driver.title
        self.assertEqual(new_page_title, "Your Account Has Been Created!")
    
    def test_password_not_filled(self):  
        continue_button = self.register_account_page.getContinueButton()
        continue_button.click()

        self.password_error_message = self.driver.find_element(By.XPATH, Locators.password_error_message).text

        self.assertEqual(self.password_error_message, "Password must be between 4 and 20 characters!")
    
    def test_password_less_than_minimum(self):
        password = self.register_account_page.getPassword()
        password.send_keys("123")
        
        continue_button = self.register_account_page.getContinueButton()
        continue_button.click()

        self.password_error_message = self.driver.find_element(By.XPATH, Locators.password_error_message).text
        self.assertEqual(self.password_error_message, "Password must be between 4 and 20 characters!")
       
    def test_password_without_confirmation(self):
        password = self.register_account_page.getPassword()
        password.send_keys("123456")
        
        continue_button = self.register_account_page.getContinueButton()
        continue_button.click()

        self.password_confirm_error_message = self.driver.find_element(By.XPATH, Locators.password_confirm_error_message).text
        self.assertEqual(self.password_confirm_error_message, "Password confirmation does not match password!")
    
    def test_password_wrong_confirmation(self):
        password = self.register_account_page.getPassword()
        password.send_keys("123456")

        password_confirm = self.register_account_page.getConfirmPassword()
        password_confirm.send_keys("12345")
        
        continue_button = self.register_account_page.getContinueButton()
        continue_button.click()

        self.password_confirm_error_message = self.driver.find_element(By.XPATH, Locators.password_confirm_error_message).text
        self.assertEqual(self.password_confirm_error_message, "Password confirmation does not match password!")

if __name__ == '__main__':
    unittest.main()