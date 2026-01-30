from appium.webdriver.common.appiumby import AppiumBy
from pages_mobile.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_complete_title_id = "com.saucelabs.mydemoapp.android:id/completeTV"
        self.continue_shopping_button_id = "com.saucelabs.mydemoapp.android:id/shoopingBt"


    def get_checkout_complete_page_title(self):
        self.find_element(AppiumBy.ID, self.checkout_complete_title_id)
        return self.get_element_text(AppiumBy.ID, self.checkout_complete_title_id)
    
    def continue_shopping_button_click(self):
        self.click_element(AppiumBy.ID, self.continue_shopping_button_id)