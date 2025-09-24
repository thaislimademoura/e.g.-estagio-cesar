from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
import time

def test_modal_dialogs(driver):
    driver.get("https://demoqa.com/modal-dialogs")

    small_modal_click_btn = driver.find_element(By.ID, "showSmallModal")
    small_modal_click_btn.click()
    small_modal_click_message = driver.find_element(By.CSS_SELECTOR, ".modal-body")
    assert "This is a small modal. It has very less content" in small_modal_click_message.text

    time.sleep(3)

    small_close_btn = driver.find_element(By.ID, "closeSmallModal")
    small_close_btn.click()

    large_modal_click_btn = driver.find_element(By.ID, "showLargeModal")
    large_modal_click_btn.click()
    large_modal_click_message = driver.find_element(By.CSS_SELECTOR, ".modal-body")
    assert "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum." in large_modal_click_message.text

    time.sleep(3)
    
    large_close_btn = driver.find_element(By.ID, "closeLargeModal")
    large_close_btn.click()