import unittest
from TestBase.WebDriverSetup import WebDriverSetup

#This class will check the correct text to each label of the page
class TestFormLabels(WebDriverSetup):
  
    def test_first_name_label(self):
        self.assertEqual(self.register_account_page.getFirstNameLabel(), "First Name")
    
    def test_last_name_label(self):
        self.assertEqual(self.register_account_page.getLastNameLabel(), "Last Name")
    
    def test_email_label(self):
         self.assertEqual(self.register_account_page.getEmaileLabel(), "E-Mail")
    
    def test_telephone_label(self):
        self.assertEqual(self.register_account_page.getTelephoneLabel(), "Telephone")
    
    def test_password_label(self):
        self.assertEqual(self.register_account_page.getPasswordLabel(), "Password")
    
    def test_confirm_password_label(self):
        self.assertEqual(self.register_account_page.getConfirmPasswordLabel(), "Password Confirm")
    
    def test_subscribe_label(self):
        self.assertEqual(self.register_account_page.getSubscribeLabel(), "Subscribe")

if __name__ == '__main__':
    unittest.main()