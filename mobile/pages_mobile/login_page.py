from appium.webdriver.common.appiumby import AppiumBy
from pages_mobile.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_title_id = "com.saucelabs.mydemoapp.android:id/loginTV"
        self.loggin_button_id = "com.saucelabs.mydemoapp.android:id/loginBtn"
        self.error_username_id = "com.saucelabs.mydemoapp.android:id/nameErrorTV"
        self.first_username_list_id = "com.saucelabs.mydemoapp.android:id/username1TV"
        self.username_input_id = "com.saucelabs.mydemoapp.android:id/nameET"
        self.error_password_id = "com.saucelabs.mydemoapp.android:id/passwordErrorTV"
        self.password_id = "com.saucelabs.mydemoapp.android:id/password1TV"
        self.password_input_id = "com.saucelabs.mydemoapp.android:id/passwordET"

    def get_login_page_title(self):
        self.find_element(AppiumBy.ID, self.login_title_id)
        return self.get_element_text(AppiumBy.ID, self.login_title_id)
    
    def error_username_message(self):
        self.find_element(AppiumBy.ID, self.login_title_id)
        self.click_element(AppiumBy.ID, self.loggin_button_id)
        self.find_element(AppiumBy.ID, self.error_username_id)
        return self.is_element_displayed(AppiumBy.ID, self.error_username_id)

    def error_password_message(self):
        self.click_element(AppiumBy.ID, self.username_input_id)
        first_username = self.get_element_text(AppiumBy.ID, self.first_username_list_id)
        self.send_keys_to_element(AppiumBy.ID, self.username_input_id, first_username)
        self.click_element(AppiumBy.ID, self.loggin_button_id)
        return self.is_element_displayed(AppiumBy.ID, self.error_password_id)
    
    def username_input(self):
        self.clear_field(AppiumBy.ID, self.username_input_id)
        first_username = self.get_element_text(AppiumBy.ID, self.first_username_list_id)
        self.send_keys_to_element(AppiumBy.ID, self.username_input_id, first_username)
        return first_username
    
    def password_input(self):
        password = self.get_element_text(AppiumBy.ID, self.password_id)
        self.send_keys_to_element(AppiumBy.ID, self.password_input_id, password)
        return password
    
    def login_complete_click(self):
        self.click_element(AppiumBy.ID, self.loggin_button_id)
    
