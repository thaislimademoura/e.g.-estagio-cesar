import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

expected_title = "Sauce Labs Backpack (orange)"
expected_my_cart_title = "My Cart"
expected_product_name = "Sauce Labs Backpack (orange)"

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:deviceName": "emulator-5554",
	"appium:automationName": "UiAutomator2",
	"appium:appPackage": "com.saucelabs.mydemoapp.android",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True,
    "appium:appWaitActivity": "com.saucelabs.mydemoapp.android.view.activities.MainActivity",
    "appium:appWaitDuration": 30000,  # opcional, tempo de espera em ms (30s)
    "uiautomator2ServerLaunchTimeout": 30000,
    "uiautomator2ServerInstallTimeout": 30000
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
time.sleep(4)

orange_backpack = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/productIV").instance(2)')
orange_backpack.click()
time.sleep(2)

# assert backpack orange opened

actual_title = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV").text
assert actual_title == expected_title, f"Expected title to be '{expected_title}', but found '{actual_title}'"

# assert minus

qnt_box_before = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)

decrease_item_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/minusIV")
decrease_item_btn.click()
time.sleep(2)

qnt_box_after_minus = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)

assert qnt_box_after_minus == qnt_box_before -1

# assert cart is not enabled

add_to_cart_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
assert not add_to_cart_btn.is_enabled()

# assert plus

qnt_box_before_plus = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)

plus_item_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/plusIV")
plus_item_btn.click()
time.sleep(2)

qnt_box_after_plus = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)

assert qnt_box_after_plus == qnt_box_before_plus +1, f"Expected title to be '{qnt_box_before_plus + 1}', but found '{qnt_box_after_plus}'"

#add_to_cart_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
assert add_to_cart_btn.is_enabled()

# add another unit
plus_item_btn.click()
qnt_item_box_actual = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)
assert qnt_item_box_actual == qnt_box_after_plus +1, f"Expected title to be '{qnt_box_after_plus + 1}', but found '{qnt_box_before_plus}'"
add_to_cart_btn.click()
number_cart_circle = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartTV").text)
assert number_cart_circle == qnt_item_box_actual

# open my cart screen
cart_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartIV")
cart_btn.click()

actual_my_cart_title = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/productTV")').text
assert actual_my_cart_title == expected_my_cart_title, f"Expected title to be '{expected_my_cart_title}', but found '{actual_my_cart_title}'"
time.sleep(2)

actual_product_name = driver.find_element(AppiumBy. ID, "com.saucelabs.mydemoapp.android:id/titleTV").text
assert actual_product_name == expected_product_name, f"Expected title to be '{expected_product_name}', but found '{actual_product_name}'"

# validate value
#final_unit_price = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceTV").text)
# valor Unit 
# qnt item 
# total 
# converter valores float 
# total esperado = unit * qnt item 
# assert total = total esperado 

# validate quantity
qnt_final_cart = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)
assert qnt_final_cart == qnt_item_box_actual

time.sleep(2)













