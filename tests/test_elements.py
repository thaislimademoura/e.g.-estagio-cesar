from selenium.webdriver.common.by import By
import time
from pages.elements_page import ElementsPage
import pytest

@pytest.mark.smoke
def test_navigate_to_elements_page(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()
    assert "elements" in driver.current_url

def test_locate_by_id(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()

    #element = driver.find_element(By.ID, "item-0")
    time.sleep(1)
    assert elements_page.is_check_box_id_visible()
    assert elements_page.get_menu_check_box_id_text() == "Text Box"

def test_locate_by_css_selector(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()
    assert elements_page.is_check_box_css_visible()

#     element = driver.find_element(By.CSS_SELECTOR, "#item-0")
#     time.sleep(1)
#     assert element.is_displayed()

def test_locate_by_xpath(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()
    assert elements_page.is_check_box_xpath_visible()
#     element = driver.find_element(By.XPATH, "//span[text()='Text Box']")
#     time.sleep(1)
#     assert element.is_displayed()