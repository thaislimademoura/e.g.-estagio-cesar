import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

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


first_backpack = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/productIV").instance(0)')
first_backpack.click()

select_green_color = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Green color"]')
select_green_color.click()

add_more_item = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Increase item quantity")
add_more_item.click()

add_to_cart = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Tap to add product to cart")
add_to_cart.click()
time.sleep(3)

open_cart = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartIV")
open_cart.click()
time.sleep(3)

decrease_item = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/minusIV")
decrease_item.click()
time.sleep(5)

proceed_to_checkout = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
proceed_to_checkout.click()
time.sleep(3)

# Login

alice_locked_out = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/username2TV")
alice_locked_out.click()

login_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn")
login_btn.click()
time.sleep(3)

locked_out_message = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordErrorTV")
locked_out_message.is_displayed()
assert "Sorry this user has been locked out." in locked_out_message.text
time.sleep(3)

driver.quit()