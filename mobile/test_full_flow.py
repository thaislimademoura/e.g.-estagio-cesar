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

username_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
username_input.click()
username = "UserTest"
username_input.send_keys(username)

password_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
password_input.click()
password = "PasswordTest"
password_input.send_keys(password)

login_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn")
login_btn.click()
time.sleep(3)

# Checkout Address Form

full_name_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameET")
full_name_input.click()
full_name = "abcd"
full_name_input.send_keys(full_name)

address_line_1_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address1ET")
address_line_1_input.click()
address_1 = "aaaa"
address_line_1_input.send_keys(address_1)

address_line_2_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address2ET")
address_line_2_input.click()
address_2 = "bbbb"
address_line_2_input.send_keys(address_2)

city_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityET")
city_input.click()
city = "Recife"
city_input.send_keys(city)

state_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/stateET")
state_input.click()
state = "PE"
state_input.send_keys(state)

zip_code_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/zipET")
zip_code_input.click()
zip_code = "00000000"
zip_code_input.send_keys(zip_code)

country_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryET")
country_input.click()
country = "Brasil"
country_input.send_keys(country)

to_payment_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn")
to_payment_btn.click()

# Checkout Payment Form
full_name_payment_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
full_name_payment_input.click()
full_name_payment_input.send_keys(full_name)

card_number_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardNumberET")
card_number_input.click()
card_number = "0000000000000000"
card_number_input.send_keys(card_number)

expiration_date_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/expirationDateET")
expiration_date_input.click()
expiration_date = "1111"
expiration_date_input.send_keys(expiration_date)

security_code_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/securityCodeET")
security_code_input.click()
security_code = "000"
security_code_input.send_keys(security_code)

review_order_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn")
review_order_btn.click()

# Final Steps

place_order_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Completes the process of checkout")
place_order_btn.click()

checkout_complete_message = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/completeTV")
checkout_complete_message.is_displayed()
assert "Checkout Complete" in checkout_complete_message.text

driver.quit()