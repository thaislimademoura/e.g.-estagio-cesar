from appium.webdriver.common.appiumby import AppiumBy
from pages_mobile.base_page import BasePage


class AddressPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.address_title_id = "com.saucelabs.mydemoapp.android:id/enterShippingAddressTV"
        self.full_name_input_id = "com.saucelabs.mydemoapp.android:id/fullNameET"
        self.address_line_1_input_id = "com.saucelabs.mydemoapp.android:id/address1ET"
        self.address_line_2_input_id = "com.saucelabs.mydemoapp.android:id/address2ET"
        self.city_input_id = "com.saucelabs.mydemoapp.android:id/cityET"
        self.state_input_id = "com.saucelabs.mydemoapp.android:id/stateET"
        self.zip_code_input_id = "com.saucelabs.mydemoapp.android:id/zipET"
        self.country_input_id = "com.saucelabs.mydemoapp.android:id/countryET"
        self.to_payment_button_id = "com.saucelabs.mydemoapp.android:id/paymentBtn"

    def get_address_page_title(self):
        self.find_element(AppiumBy.ID, self.address_title_id)
        return self.get_element_text(AppiumBy.ID, self.address_title_id)
    

    def fill_the_form_address(self, data):
        user_data = data["valid_user"]
        self.send_keys_to_element(AppiumBy.ID, self.full_name_input_id, user_data["full_name"])
        self.send_keys_to_element(AppiumBy.ID, self.address_line_1_input_id, user_data["address_line_1"])
        self.send_keys_to_element(AppiumBy.ID, self.address_line_2_input_id, user_data["address_line_2"])
        self.send_keys_to_element(AppiumBy.ID, self.city_input_id, user_data["city"])
        self.send_keys_to_element(AppiumBy.ID, self.state_input_id, user_data["state"])
        self.send_keys_to_element(AppiumBy.ID, self.zip_code_input_id, user_data["zip_code"])
        self.send_keys_to_element(AppiumBy.ID, self.country_input_id, user_data["country"])

        assert self.find_element(AppiumBy.ID, self.full_name_input_id).text == user_data["full_name"]
        assert self.find_element(AppiumBy.ID, self.address_line_1_input_id).text == user_data["address_line_1"]
        assert self.find_element(AppiumBy.ID, self.address_line_2_input_id).text == user_data["address_line_2"]
        assert self.find_element(AppiumBy.ID, self.city_input_id).text == user_data["city"]
        assert self.find_element(AppiumBy.ID, self.state_input_id).text == user_data["state"]
        assert self.find_element(AppiumBy.ID, self.zip_code_input_id).text == user_data["zip_code"]
        assert self.find_element(AppiumBy.ID, self.country_input_id).text == user_data["country"]

    def to_payment_button_click(self):
        self.click_element(AppiumBy.ID, self.to_payment_button_id)