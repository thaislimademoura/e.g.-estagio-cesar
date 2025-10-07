import time

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

expected_title = "Sauce Labs Backpack (orange)"
#expected_my_cart_title = "My Cart"
expected_product_name = "Sauce Labs Backpack (orange)"
product_unit_price = "$ 29.99"
qnt_final_product = 2
unit_price = 29.99
username_without_password = "thais"
full_name = "algum nome"
address_line_1 = "abcd"
address_line_2 = "abcdefg"
city = "Recife"
state = "PE"
zip_code = "11111111"
country = "Brasil"
card_number = "1111111111111111"
expiration_date = "11/11"
security_code = "111"
cart_items = 0

# 1
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

# 2
orange_backpack = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/productIV").instance(2)')
orange_backpack.click()
time.sleep(2)

# 3 - assert backpack orange opened

actual_title = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV").text
assert actual_title == expected_title, f"Expected title to be '{expected_title}', but found '{actual_title}'"

# 4 - assert minus

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
time.sleep(2)
my_cart_screen = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/scrollView")

assert my_cart_screen.is_displayed
time.sleep(2)

actual_product_name = driver.find_element(AppiumBy. ID, "com.saucelabs.mydemoapp.android:id/titleTV").text
assert actual_product_name == expected_product_name, f"Expected title to be '{expected_product_name}', but found '{actual_product_name}'"

# validate value
my_cart_unit_price = (driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceTV").text)
assert my_cart_unit_price == product_unit_price

# validate quantity
qnt_final_cart = int(driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/noTV").text)
assert qnt_final_cart == qnt_final_product

# validate total quantity
total_item = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/itemsTV").text
total_item_final = int(total_item.split()[0])

assert total_item_final == qnt_final_product

# validate total price 
total_price = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/totalPriceTV").text
total_price_float = float(total_price.replace("$","").strip())
assert total_price_float == unit_price * 2
time.sleep(2)

proceed_checkout_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
proceed_checkout_btn.click()
time.sleep(2)
login_screen = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(2)')
assert login_screen.is_displayed()
time.sleep(2)

# validate without username
login_button = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn")
login_button.click()
time.sleep(2)
error_username_message = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameErrorTV")
assert error_username_message.is_displayed()

# validate without password
username_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
username_input.send_keys(username_without_password)
login_button.click()
error_password_message = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordErrorTV")
assert error_password_message.is_displayed()
username_input.click()
username_input.clear()

# test first username and password
first_username_list = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/username1TV").text
username_input.send_keys(first_username_list)
password = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/password1TV").text
password_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
password_input.send_keys(password)
login_button.click()
time.sleep(2)

# validate checkout screen
checkout_screen = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.LinearLayout").instance(2)')
assert checkout_screen.is_displayed()

# fill the form
full_name_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameET")
full_name_input.send_keys(full_name)

address_line_1_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address1ET")
address_line_1_input.send_keys(address_line_1)

address_line_2_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address2ET")
address_line_2_input.send_keys(address_line_2)

city_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityET")
city_input.send_keys(city)

state_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/stateET")
state_input.send_keys(state)

zip_code_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/zipET")
zip_code_input.send_keys(zip_code)

country_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryET")
country_input.send_keys(country)

to_payment_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn")
to_payment_btn.click()

# validate payment screen
payment_screen = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/checkoutSV")
assert payment_screen.is_displayed()
time.sleep(2)

full_name_payment_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
full_name_payment_input.send_keys(full_name)

card_number_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardNumberET")
card_number_input.send_keys(card_number)

expiration_date_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/expirationDateET")
expiration_date_input.send_keys(expiration_date)

security_code_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/securityCodeET")
security_code_input.send_keys(security_code)

checkbox = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/billingAddressCB")
assert checkbox.is_selected

# proceed to review
to_payment_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn")
to_payment_btn.click()

review_screen = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(3)')
assert review_screen.is_displayed()
time.sleep(2)

# validate address and payment 
output_full_name = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameTV")
assert full_name in output_full_name.text

output_address_line_1 = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/addressTV")
assert address_line_1 in output_address_line_1.text

output_city_state = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityTV")
assert city in output_city_state.text
assert state in output_city_state.text

output_zip_code_country = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryTV")
assert zip_code in output_zip_code_country.text
assert country in output_zip_code_country.text

output_card_name = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardHolderTV")
assert full_name in output_card_name.text

output_card_number = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardNumberTV")
assert card_number in output_card_number.text


exp_id = "com.saucelabs.mydemoapp.android:id/expirationDateTV"
scrolling = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("{exp_id}"));')


output_expiration_date = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/expirationDateTV")
assert expiration_date in output_expiration_date.text
time.sleep(2)

product_title_id = "com.saucelabs.mydemoapp.android:id/titleTV"
scrolling = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("{product_title_id}"));')

# 34 - validate products unit information
product_title = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/titleTV").text
assert product_title == expected_title, f"Expected title to be '{expected_title}', but found '{actual_title}'"

product_price = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceTV").text
assert product_price == product_unit_price, f"Expected price to be '{product_unit_price}', but found '{product_price}'"

# 35 - validate total value
final_value = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/totalAmountTV").text
final_value_float = float(final_value.replace("$","").strip())

delivery_id = "com.saucelabs.mydemoapp.android:id/amountTV"
scrolling = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("{delivery_id}"));')

delivery = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/amountTV").text
delivery_float = float(delivery.replace("$","").strip())
assert final_value_float == delivery_float + (unit_price * 2)

# 36 - place order button
place_order_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn").click()
time.sleep(2)

# 37 - validate checkout complete screen
checkout_complete_screen = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(2)')
assert checkout_complete_screen.is_displayed

# 38 - continue shopping button
continue_shopping_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/shoopingBt").click()
time.sleep(2)
products_screen = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(2)')
assert products_screen.is_displayed()

cart_empty = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartIV")
cart_full = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/cartTV")')

#assert cart_empty.is_displayed() and not cart_full.is_displayed()
assert cart_empty.is_displayed() and not cart_full

driver.quit()









