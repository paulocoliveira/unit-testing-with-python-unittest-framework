class Locators(object):
    #Register Account Page
    
    #Labels
    first_name_label = "//label[@for='input-firstname']"
    last_name_label = "//label[@for='input-lastname']"
    email_label = "//label[@for='input-email']"
    telephone_label = "//label[@for='input-telephone']"
    password_label = "//label[@for='input-password']"
    confirm_password_label = "//label[@for='input-confirm']"
    subscribe_label = "//div[@class='form-group row']//label[@class='col-sm-2 col-form-label']"

    #Form Fields
    first_name = "input-firstname"
    last_name = "input-lastname"
    email = "input-email"
    telephone = "input-telephone"
    terms = "//label[@for='input-agree']"
    password = "input-password"
    confirm_password = "input-confirm"
    continue_button = "//input[@value='Continue']"

    #Error Messages
    password_error_message = "//input[@id='input-password']/following-sibling::div"
    password_confirm_error_message = "//input[@id='input-confirm']/following-sibling::div"
