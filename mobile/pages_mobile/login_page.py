from appium.webdriver.common.appiumby import AppiumBy
from pages_mobile.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_title_id = "com.saucelabs.mydemoapp.android:id/loginTV"

    def get_login_page_title(self):
        self.find_element(AppiumBy.ID, self.product_title_id)
        return self.get_element_text(AppiumBy.ID, self.product_title_id)