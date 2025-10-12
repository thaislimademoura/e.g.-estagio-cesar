from appium.webdriver.common.appiumby import AppiumBy
from pages_mobile.base_page import BasePage

class PaymentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.payment_title_id = "com.saucelabs.mydemoapp.android:id/enterPaymentMethodTV"

    def get_payment_page_title(self):
        self.find_element(AppiumBy.ID, self.payment_title_id)
        return self.get_element_text(AppiumBy.ID, self.payment_title_id)