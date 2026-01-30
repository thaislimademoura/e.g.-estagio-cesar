from appium.webdriver.common.appiumby import AppiumBy
from pages_mobile.base_page import BasePage

class MyCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_title_id = "com.saucelabs.mydemoapp.android:id/productTV"
        self.unit_product_title_id = "com.saucelabs.mydemoapp.android:id/titleTV"
        self.unit_price_id = "com.saucelabs.mydemoapp.android:id/priceTV"
        self.qnt_items_id = "com.saucelabs.mydemoapp.android:id/noTV"
        self.total_items_id = "com.saucelabs.mydemoapp.android:id/itemsTV"
        self.total_price_id = "com.saucelabs.mydemoapp.android:id/totalPriceTV"
        self.proceed_checkout_button_id = "com.saucelabs.mydemoapp.android:id/cartBt"
    
    def get_product_page_title(self):
        self.find_element(AppiumBy.ID, self.product_title_id)
        return self.get_element_text(AppiumBy.ID, self.product_title_id)
    
    def get_unit_product_title(self):
        self.find_element(AppiumBy.ID, self.unit_product_title_id)
        return self.get_element_text(AppiumBy.ID, self.unit_product_title_id)
    
    def get_unit_price(self):
        self.find_element(AppiumBy.ID, self.unit_price_id)
        return self.get_element_text(AppiumBy.ID, self.unit_price_id)
    
    def get_qnt_items(self):
        self.find_element(AppiumBy.ID, self.qnt_items_id)
        return int(self.get_element_text(AppiumBy.ID, self.qnt_items_id))
    
    def get_total_items(self):
        total_items = self.get_element_text(AppiumBy.ID, self.total_items_id)
        total_items_int = int(total_items.split()[0])
        return total_items_int == int(self.qnt_items_id)
    
    def get_total_items(self):
        return self.get_element_text(AppiumBy.ID, self.total_items_id)
    
    def get_total_price_calculated(self):
        total_items = int(self.get_element_text(AppiumBy.ID, self.total_items_id).split()[0])
        unit_price = float(self.get_element_text(AppiumBy.ID, self.unit_price_id).replace("$","").strip())
        calculated_total = total_items * unit_price
        
        total_price = float(self.get_element_text(AppiumBy.ID, self.total_price_id).replace("$","").strip())
        return calculated_total == total_price
    
    def proceed_checkout_button_click(self):
        self.find_element(AppiumBy.ID, self.proceed_checkout_button_id)
        self.click_element(AppiumBy.ID, self.proceed_checkout_button_id)
    
    
        
