from appium.webdriver.common.appiumby import AppiumBy
from pages_mobile.base_page import BasePage

class ReviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.review_title_id = "com.saucelabs.mydemoapp.android:id/enterShippingAddressTV"
        self.output_full_name_id = "com.saucelabs.mydemoapp.android:id/fullNameTV"
        self.output_address_line_1_id = "com.saucelabs.mydemoapp.android:id/addressTV"
        self.output_city_state_id = "com.saucelabs.mydemoapp.android:id/cityTV"
        self.output_country_zipcode_id = "com.saucelabs.mydemoapp.android:id/countryTV"
        self.output_card_name_id = "com.saucelabs.mydemoapp.android:id/cardHolderTV"
        self.output_card_number_id = "com.saucelabs.mydemoapp.android:id/cardNumberTV"
        self.product_title_id = "com.saucelabs.mydemoapp.android:id/titleTV"
        self.product_price_id = "com.saucelabs.mydemoapp.android:id/priceTV"
        self.exp_id = "com.saucelabs.mydemoapp.android:id/expirationDateTV"
        self.final_value_id = "com.saucelabs.mydemoapp.android:id/totalAmountTV"
        self.delivery_value_id = "com.saucelabs.mydemoapp.android:id/amountTV"
        self.qnt_items_id = "com.saucelabs.mydemoapp.android:id/itemNumberTV"
        self.unit_price_id = "com.saucelabs.mydemoapp.android:id/priceTV"



    def get_review_page_title(self):
        self.find_element(AppiumBy.ID, self.review_title_id)
        return self.get_element_text(AppiumBy.ID, self.review_title_id)
    
    def validade_name_output(self, data):
        user_data = data["valid_user"]
        assert self.find_element(AppiumBy.ID, self.output_full_name_id).text == user_data["full_name"]
        
    def validate_address_output(self, data):
        user_data = data["valid_user"]
        assert self.find_element(AppiumBy.ID, self.output_address_line_1_id).text == user_data["address_line_1"]
    
#>>>>>>>>

    def validade_city_output(self, data):
        user_data = data["valid_user"]
        element_text = self.get_element_text(AppiumBy.ID, self.output_city_state_id)
        element = element_text.split(",")[0]
        assert element == user_data["city"]

    def validade_state_output(self, data):
        user_data = data["valid_user"]
        element_text = self.get_element_text(AppiumBy.ID, self.output_city_state_id)
        element = element_text.split(",")[1].strip()
        assert element == user_data["state"]
        
    def validade_country_output(self, data):
        user_data = data["valid_user"]
        element_text = self.get_element_text(AppiumBy.ID, self.output_country_zipcode_id)
        element = element_text.split(",")[0]
        assert element == user_data["country"]

    def validade_zipcode_output(self, data):
        user_data = data["valid_user"]
        element_text = self.get_element_text(AppiumBy.ID, self.output_country_zipcode_id)
        element = element_text.split(",")[1].strip()
        assert element == user_data["zip_code"]

    def validate_card_name_output(self, data):
        user_data = data["valid_user"]
        assert self.find_element(AppiumBy.ID, self.output_card_name_id).text == user_data["full_name_payment"]
  
    def validate_card_number_output(self, data):
        user_data = data["valid_user"]
        assert self.find_element(AppiumBy.ID, self.output_card_number_id).text == user_data["card_number"]

    
    
    
    
    
    def validate_product_title(self, data):
        user_data = data["products"]
        assert self.find_element(AppiumBy.ID, self.product_title_id).text == user_data["name"]

    def validate_product_price(self, data):
        user_data = data["products"]
        assert self.find_element(AppiumBy.ID, self.product_price_id).text == user_data["price"]

    

    def validate_exp_date(self, data):
        user_data = data["valid_user"]
        self.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("{self.exp_id}"));')
        element_text = self.get_element_text(AppiumBy.ID, self.exp_id)
        assert element_text == user_data["final_exp_date"]

    

        
    def calculated_total_price(self, data):
        unit_price = data["products"]["unit_price_float"]
        qnt_items = int(self.get_element_text(AppiumBy.ID, self.qnt_items_id).split()[0])
        delivery = float(self.get_element_text(AppiumBy.ID, self.delivery_value_id).replace("$","").strip())
        final_value = float(self.get_element_text(AppiumBy.ID, self.final_value_id).replace("$","").strip())
        assert final_value == delivery + (qnt_items * unit_price)

        
    