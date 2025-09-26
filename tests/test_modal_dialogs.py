from selenium.webdriver.common.by import By
import time
from pages.modal_dialogs import ModalDialogsPage
import pytest
from utils.data_loader import load_json_data

test_data = load_json_data("data/test_data.json")

@pytest.mark.widgets
def test_modal_dialogs(driver):
    modal_dialogs_page = ModalDialogsPage(driver)
    modal_dialogs_page.navigate(test_data["modal_dialogs_url"])

    modal_dialogs_page.small_btn()

    small_message = modal_dialogs_page.get_small_message()
    assert small_message == test_data["modal_dialogs_small_message"]

    
# def small_modal_click_message(self):
#         self.driver.find_element(*self.small_modal_click_message).click()

#     def small_close_btn(self):
#         self.driver.find_element(*self.small_close_btn).click()

#     def large_modal_click_btn(self):
#         self.driver.find_element(*self.large_modal_click_btn).click()

#     def large_modal_click_message(self):
#         self.driver.find_element(*self.large_modal_click_message).click()

#     def large_close_btn(self):
#         self.driver.find_element(*self.large_close_btn).click()