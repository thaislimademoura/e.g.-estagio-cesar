from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class WidgetsMenuPage:
    def __init__(self,driver):
        self.driver = driver
        self.url = "https://demoqa.com/menu"
        self.wait = WebDriverWait(self.driver, 10)
        #Locators
        self.main_item_2 = (By.XPATH, '//*[@id="nav"]/li[2]/a')
        self.SUB_SUB_LIST = (By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')
        self.sub_sub_item_1 = (By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[1]/a')

    def navigate(self):
        self.driver.get(self.url)

    def hover_over_item_2_button(self):
        item_2_button = self.wait.until(EC.visibility_of_element_located(self.main_item_2))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", item_2_button)
        ActionChains(self.driver).move_to_element(item_2_button).perform()

    def hover_over_SUB_SUB_LIST_button(self):
        SUB_SUB_LIST_button = self.wait.until(EC.visibility_of_element_located(self.SUB_SUB_LIST))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", SUB_SUB_LIST_button)
        ActionChains(self.driver).move_to_element(SUB_SUB_LIST_button).perform()

    def hover_over_sub_sub_item_1_button(self):
        sub_sub_item_1_button = self.wait.until(EC.visibility_of_element_located(self.sub_sub_item_1))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", sub_sub_item_1_button)
        ActionChains(self.driver).move_to_element(sub_sub_item_1_button).perform()