import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

expected_title = "Sauce Labs Backpack (orange)"
actual_qnt_item = 2


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

before_minus = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)

decrease_item_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/minusIV")
decrease_item_btn.click()
time.sleep(2)

after_minus = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)

assert before_minus - after_minus == 1

# -

add_to_cart_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
assert not add_to_cart_btn.is_enabled()

# assert plus

before_minus = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)

add_more_item_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/plusIV")
add_more_item_btn.click()
time.sleep(2)

after_minus = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)

assert before_minus + after_minus == 1

add_to_cart_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
assert add_to_cart_btn.is_enabled()

# add another unit
add_more_item_btn.click()
actual_qnt_item_box = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV")
assert actual_qnt_item == 2
time.sleep(2)












