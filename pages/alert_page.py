from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertPage:
    def __init__(self,driver):
        self.driver = driver
        self.url = "https://demoqa.com/"
        self.wait = WebDriverWait(self.driver, 10)
        #Locators
        self.alerts_frame_window_button = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[3]')
        self.alerts_button = (By.XPATH, "//span[text()='Alerts']")
        self.first_click_me_button = (By.ID, "alertButton")
        self.second_click_me_button = (By.ID, "timerAlertButton")
        self.third_click_me_button = (By.ID, "confirmButton")
        self.confirm_box_message = (By. ID, "confirmResult")

    def navigate(self):
        self.driver.get(self.url)

    def click_alerts_frame_window_button(self):
        self.driver.find_element(*self.alerts_frame_window_button).click()

    def click_alerts_button(self):
        self.driver.find_element(*self.alerts_button).click()

    def click_first_click_me_button(self):
        self.driver.find_element(*self.first_click_me_button).click()
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
        
    def click_second_click_me_button(self):
        self.driver.find_element(*self.second_click_me_button).click()
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def click_third_click_me_button(self):
        third_click_me_button = self.wait.until(EC.visibility_of_element_located(self.third_click_me_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", third_click_me_button)
        self.driver.find_element(*self.third_click_me_button).click()
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()
        confirm_box_message = self.wait.until(EC.visibility_of_element_located(self.confirm_box_message))
        #third_button = self.driver.find_element(*self.third_click_me_button)
        #confirm_box_message = self.wait.until(EC.alert_is_present())
        self.driver.execute_script("arguments[0].scrollIntoView(true);", confirm_box_message)
        #third_click_me_button = self.driver.find_element(*self.confirm_box_message)
        #confirm_box_message = self.driver.find_element(*self.confirm_box_message)
        return confirm_box_message.text


    # def accept_alert(self):
    #     simple_alert = self.wait.until(EC.alert_is_present())
    #     return simple_alert.accept()

    # def check_see_alert_text(self):
    #     see_alert = self.wait.until(EC.alert_is_present())
    #     return see_alert.text

    def click_time_alert_button(self):
        self.driver.find_element(*self.time_alert_button).click()

    


    # def get_small_message(self):
    #     small_message = self.wait.until(EC.visibility_of_element_located(self.small_modal_click_message))
    #     return small_message.text