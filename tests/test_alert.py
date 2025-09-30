import pytest
from selenium.webdriver.common.by import By
import time
from pages.alert_page import AlertPage


def test_navigate_to_home_page(driver):
    alert_page = AlertPage(driver)
    alert_page.navigate()
    assert "demoqa.com" in driver.current_url

    alert_page.click_alerts_frame_window_button()
    assert "alertsWindows" in driver.current_url
    
    alert_page.click_alerts_button()
    assert "alerts" in driver.current_url

    alert_page.click_first_click_me_button()

    alert_page.click_second_click_me_button()

    text = alert_page.click_third_click_me_button()
    assert text == "You selected Cancel"




    



# def test_fill_text_box_form_and_validate(driver):
#     text_box_page = TextBoxPage(driver)
    
#     text_box_page.navigate()
    

# def test_navigate_to_alerts_page(driver):
#     alerts_frame_window = HomePage(driver)
#     alerts_frame_window.navigate()
#     assert "https://demoqa.com/" in driver.current_url

# def test_locate_by_id(driver):
#     elements_page = ElementsPage(driver)
#     elements_page.navigate()

#     #element = driver.find_element(By.ID, "item-0")
#     time.sleep(1)
#     assert elements_page.is_check_box_id_visible()
#     assert elements_page.get_menu_check_box_id_text() == "Text Box"