from appium.webdriver.common.appiumby import AppiumBy
from pages_mobile.base_page import BasePage

class PaymentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.payment_title_id = "com.saucelabs.mydemoapp.android:id/enterPaymentMethodTV"
        self.full_name_payment_id = "com.saucelabs.mydemoapp.android:id/nameET"
        self.card_number_id = "com.saucelabs.mydemoapp.android:id/cardNumberET"
        self.expiration_date_id = "com.saucelabs.mydemoapp.android:id/expirationDateET"
        self.security_code_id = "com.saucelabs.mydemoapp.android:id/securityCodeET"
        self.checkbox_id = "com.saucelabs.mydemoapp.android:id/billingAddressCB"
        self.to_payment_button_id = "com.saucelabs.mydemoapp.android:id/paymentBtn"

    def get_payment_page_title(self):
        self.find_element(AppiumBy.ID, self.payment_title_id)
        return self.get_element_text(AppiumBy.ID, self.payment_title_id)
    
    def fill_the_form_payment(self, data):
        user_data = data["valid_user"]
        self.send_keys_to_element(AppiumBy.ID, self.full_name_payment_id, user_data["full_name_payment"])
        self.send_keys_to_element(AppiumBy.ID, self.card_number_id, user_data["card_number"])
        self.send_keys_to_element(AppiumBy.ID, self.expiration_date_id, user_data["exp_date"])
        self.send_keys_to_element(AppiumBy.ID, self.security_code_id, user_data["secure_code"])

        assert self.find_element(AppiumBy.ID, self.full_name_payment_id).text == user_data["full_name_payment"]
        assert self.find_element(AppiumBy.ID, self.card_number_id).text == user_data["card_number"]
        assert self.find_element(AppiumBy.ID, self.expiration_date_id).text == user_data["exp_date"]
        assert self.find_element(AppiumBy.ID, self.security_code_id).text == user_data["secure_code"]

    # def checkbox_checked(self):

    def to_payment_button_click(self):
        self.click_element(AppiumBy.ID, self.to_payment_button_id)