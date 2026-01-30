from appium.webdriver.common.appiumby import AppiumBy
from pages_mobile.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_title_id = "com.saucelabs.mydemoapp.android:id/productTV"
        self.qnt_items_id = "com.saucelabs.mydemoapp.android:id/noTV"
        self.decrease_button_id = "com.saucelabs.mydemoapp.android:id/minusIV"
        self.increase_button_id = "com.saucelabs.mydemoapp.android:id/plusIV"
        self.add_to_cart_button_id = "com.saucelabs.mydemoapp.android:id/cartBt"
        self.cart_icon_id = "com.saucelabs.mydemoapp.android:id/cartIV"
        self.cart_icon_number_id = "com.saucelabs.mydemoapp.android:id/cartTV"
        self.cart_empty_id = "com.saucelabs.mydemoapp.android:id/cartIV"
        self.cart_full_id = 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/cartTV")'

    def get_product_page_title(self):
        self.find_element(AppiumBy.ID, self.product_title_id)
        return self.get_element_text(AppiumBy.ID, self.product_title_id)
    
    def get_qnt_items(self):
        self.find_element(AppiumBy.ID, self.qnt_items_id)
        return int(self.get_element_text(AppiumBy.ID, self.qnt_items_id))

    def select_decrease_items(self):
        self.find_element(AppiumBy.ID, self.decrease_button_id)
        self.click_element(AppiumBy.ID, self.decrease_button_id)

    def select_increase_items(self):
        self.find_element(AppiumBy.ID, self.increase_button_id)
        self.click_element(AppiumBy.ID, self.increase_button_id)

    def add_to_cart_enabled(self):
        return self.is_element_enabled(AppiumBy.ID, self.add_to_cart_button_id)
    
    def add_to_cart_click(self):
        self.find_element(AppiumBy.ID, self.add_to_cart_button_id)
        self.click_element(AppiumBy.ID, self.add_to_cart_button_id)

    def get_cart_icon(self):
        return self.find_element(AppiumBy.ID, self.cart_icon_id).is_displayed()
    
    def get_cart_icon_number(self):
        self.find_element(AppiumBy.ID, self.cart_icon_number_id)
        return int(self.get_element_text(AppiumBy.ID, self.cart_icon_number_id))
    
    def cart_click(self):
        self.click_element(AppiumBy.ID, self.cart_icon_id)


    def assert_cart_is_empty(self):
        cart_empty = self.find_element(AppiumBy.ID, self.cart_empty_id)
        cart_full_present = self.is_element_present(AppiumBy.ANDROID_UIAUTOMATOR, self.cart_full_id)
        assert cart_empty.is_displayed() and not cart_full_present
       

      
