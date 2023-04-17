from selenium.webdriver.common.by import By

from PageObject.Locators import Locators

class RegisterAccountPage(object):
    def __init__(self, driver):
        self.driver = driver

        self.first_name_label = driver.find_element(By.XPATH, Locators.first_name_label).text
        self.last_name_label = driver.find_element(By.XPATH, Locators.last_name_label).text
        self.email_label = driver.find_element(By.XPATH, Locators.email_label).text
        self.telephone_label = driver.find_element(By.XPATH, Locators.telephone_label).text
        self.password_label = driver.find_element(By.XPATH, Locators.password_label).text
        self.confirm_password_label = driver.find_element(By.XPATH, Locators.confirm_password_label).text
        self.subscribe_label = driver.find_element(By.XPATH, Locators.subscribe_label).text

        self.first_name = driver.find_element(By.ID, Locators.first_name)
        self.last_name = driver.find_element(By.ID, Locators.last_name)
        self.email = driver.find_element(By.ID, Locators.email)
        self.telephone = driver.find_element(By.ID, Locators.telephone)
        self.terms = driver.find_element(By.XPATH, Locators.terms)
        self.password = driver.find_element(By.ID, Locators.password)
        self.confirm_password = driver.find_element(By.ID, Locators.confirm_password)     
        self.continue_button = driver.find_element(By.XPATH, Locators.continue_button)
        self.new_page_title = driver.title
            
    def getFirstNameLabel(self):
        return self.first_name_label

    def getLastNameLabel(self):
        return self.last_name_label
    
    def getEmaileLabel(self):
        return self.email_label
    
    def getTelephoneLabel(self):
        return self.telephone_label
    
    def getPasswordLabel(self):
        return self.password_label
    
    def getConfirmPasswordLabel(self):
        return self.confirm_password_label
    
    def getSubscribeLabel(self):
        return self.subscribe_label
    
    def getFirstName(self):
        return self.first_name
    
    def getLastName(self):
        return self.last_name
    
    def getEmail(self):
        return self.email
    
    def getTelephone(self):
        return self.telephone
    
    def getTerms(self):
        return self.terms
    
    def getPassword(self):
        return self.password
    
    def getConfirmPassword(self):
        return self.confirm_password
    
    def getContinueButton(self):
        return self.continue_button
    
    def getNewPageTitle(self):
        return self.new_page_title