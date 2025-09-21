import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_button_double_click_with_screenshots(driver):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)

    double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
    actions.double_click(double_click_btn).perform()
    double_click_message = driver.find_element(By.ID, "doubleClickMessage")
    driver.execute_script("arguments[0].scrollIntoView(true);",double_click_message)
    driver.save_screenshot("screenshots/1_after_double_click.png")
    assert "You have done a double click" in double_click_message.text

def test_button_right_click_with_screenshots(driver):

    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)

    right_click_btn = driver.find_element(By.ID, "rightClickBtn")
    actions.context_click(right_click_btn).perform()
    right_click_message = driver.find_element(By.ID, "rightClickMessage")
    driver.execute_script("arguments[0].scrollIntoView(true);",right_click_message)
    driver.save_screenshot("screenshots/1_after_right_click.png")
    assert "You have done a right click" in right_click_message.text

def test_button_dynamic_click_with_screenshots(driver):

    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)
    driver.maximize_window

    #element_abs = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button")
    #element_normalize = driver.find_element(By.XPATH, "//button[normalize-space()='Click Me']")
    dynamic_click_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    dynamic_click_btn.click()
    #actions.dynamic_click(dynamic_click_btn).perform() - Nesse caso não usa actionchains? - AttributeError: 'ActionChains' object has no attribute 'dynamic_click'
    dynamic_click_message = driver.find_element(By.ID, "dynamicClickMessage")
    driver.execute_script("arguments[0].scrollIntoView(true);",dynamic_click_message)
    driver.save_screenshot("screenshots/1_after_click_me.png")
    assert "You have done a dynamic click" in dynamic_click_message.text
    