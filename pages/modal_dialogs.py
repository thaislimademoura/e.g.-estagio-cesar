from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ModalDialogsPage:
    def __init__(self,driver):
        self.driver = driver
        self.url = "https://demoqa.com/modal-dialogs"
        self.wait = WebDriverWait(self.driver, 10)
        #Locators
        self.small_modal_click_btn = (By.ID, "showSmallModal")
        self.small_modal_click_message = (By.CSS_SELECTOR, ".modal-body")
        self.small_close_btn = (By.ID, "closeSmallModal")
        self.large_modal_click_btn = (By.ID, "showLargeModal")
        self.large_modal_click_message = (By.CSS_SELECTOR, ".modal-body")
        self.large_close_btn = (By.ID, "closeLargeModal")

    def navigate(self, url):
        self.driver.get(url)
    
    def small_btn(self):
        #button = self.driver.find_element(*self.small_modal_click_btn).click()
        self.driver.find_element(*self.small_modal_click_btn).click()

    def get_small_message(self):
        small_message = self.wait.until(EC.visibility_of_element_located(self.small_modal_click_message))
        return small_message.text

    # def small_modal_click_message(self):
    #     self.driver.find_element(*self.small_modal_click_message).click()

    def close_btn(self):
        self.driver.find_element(*self.small_close_btn).click()

    def large_btn(self):
        self.driver.find_element(*self.large_modal_click_btn).click()

    def get_large_message(self):
        large_message = self.wait.until(EC.visibility_of_element_located(self.large_modal_click_message))
        return large_message.text

    def close_btn(self):
        self.driver.find_element(*self.large_close_btn).click()
    
