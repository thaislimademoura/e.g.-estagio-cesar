import pytest
from pages_mobile.home_page import HomePage
from pages_mobile.product_page import ProductPage
from pages_mobile.my_cart_page import MyCartPage
from pages_mobile.login_page import LoginPage
from pages_mobile.address_page import AddressPage
from pages_mobile.payment_page import PaymentPage
from pages_mobile.review_page import ReviewPage
from pages_mobile.checkout_complete import CheckoutPage

# Import other page objects as needed

def test_product_selection(driver, load_data_capabilities):
    # Initialize page objects with the driver provided by the fixture
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    my_cart_page = MyCartPage(driver)
    login_page = LoginPage(driver)
    address_page = AddressPage(driver)
    payment_page = PaymentPage(driver)
    review_page = ReviewPage(driver)
    checkout_page = CheckoutPage(driver)

    #form_data = load... ["valid_user"]["backpack"]

    # Perform actions using page object methods
    assert home_page.get_home_page_title() == "Products"
    home_page.select_orange_backpack()

    # Continue with product page interactions
    assert product_page.get_product_page_title() == "Sauce Labs Backpack (orange)"
    
    # 4 - Decrease and validate decreased by 1 unit
    items_before = product_page.get_qnt_items()
    product_page.select_decrease_items()
    items_after = product_page.get_qnt_items()
    assert items_after == items_before -1

    # 5 - When you reach zero quantity, button will become inactive.
    assert product_page.add_to_cart_enabled() == False

    # 6 - Increase and check increased by 1 unit
    items_before = product_page.get_qnt_items()
    product_page.select_increase_items()
    items_after = product_page.get_qnt_items()
    assert items_after == items_before +1
   
    # 7 - When you reach 1 quantity, button will become active.
    assert product_page.add_to_cart_enabled() == True
    
    # 8 - Add another unit, make sure you have 2 units and click on the Add to cart button.
    product_page.select_increase_items()
    assert product_page.get_qnt_items() == 2
    product_page.add_to_cart_click()

    # 9 - Validate that a circle has appeared in the cart icon informing you of the exact number
    assert product_page.get_cart_icon() == True
    assert product_page.get_cart_icon_number() == product_page.get_qnt_items()

    # 10 - Open the cart page by clicking on the cart icon
    product_page.cart_click()

    # 11 - Validate that the My Cart screen has been opened
    assert my_cart_page.get_product_page_title() == "My Cart"

    # 12 - Validate that your product is correct
    assert my_cart_page.get_unit_product_title() == "Sauce Labs Backpack (orange)"

    # 13 - Validate that the unit price is as expected
    assert my_cart_page.get_unit_price() == "$ 29.99"

    # 14 - Validate that the quantity is correct in the field below the product photo 
    assert my_cart_page.get_qnt_items() == 2

    # 15 - Validate that the quantity is correct in the Total: x Items field

    assert my_cart_page.get_total_items() == "2 Items"

    # 16 - Validate that the total value of the purchase is as expected for 2 units of the product
    assert my_cart_page.get_total_price_calculated() == True

    # 17 - Click on the Proceed To Checkout button
    my_cart_page.proceed_checkout_button_click()

    # 18 - Validate that the Login screen has been displayed
    assert login_page.get_login_page_title() == "Login"

    # 19 - Try to log in without entering Username and Password and validate the error in the Username field
    assert login_page.error_username_message()
    
    # 20 - Try to log in without entering Password and validate the error in the Password field
    assert login_page.error_password_message()

    # 21 - Capture the first Username from the Usernames list at the bottom of the screen and enter this value in the Username field
    assert login_page.username_input()
   
    # 22 - Capture the Password from the Password list at the bottom of the screen and enter this value in the Password field
    assert login_page.password_input()
    
    # 23 - Click on the Login button
    login_page.login_complete_click()

    # 24 - Validate that the Checkout, Shipment Address screen has been displayed
    assert address_page.get_address_page_title() == "Enter a shipping address"

    # 25 - Enter information in all the form fields and proceed to payment.
    address_page.fill_the_form_address(load_data_capabilities)

    address_page.to_payment_button_click()

    # 27 - Validate that the Checkout, Payment screen has been displayed
    assert payment_page.get_payment_page_title() == "Enter a payment method"

    # 28 - Enter the values in the corresponding fields and keep the check-box selected
    payment_page.fill_the_form_payment(load_data_capabilities)

    # 31 - Proceed to the review by clicking on the Review Order button
    payment_page.to_payment_button_click()

    # 32 - Validate that the Checkout, Review your order screen has been displayed.
    assert review_page.get_review_page_title() == "Review your order"

    # 33 - Validate that the Deliver Address and Payment Method information is correct
    review_page.validade_name_output(load_data_capabilities)
    review_page.validate_address_output(load_data_capabilities)
    review_page.validade_city_output(load_data_capabilities)
    review_page.validade_state_output(load_data_capabilities)
    review_page.validade_country_output(load_data_capabilities)
    review_page.validade_zipcode_output(load_data_capabilities)

    review_page.validate_card_name_output(load_data_capabilities)
    review_page.validate_card_number_output(load_data_capabilities)

    # 34 - Validate the product's unit information such as Name and Value
    review_page.validate_product_title(load_data_capabilities)
    review_page.validate_product_price(load_data_capabilities)

    review_page.validate_exp_date(load_data_capabilities)

    # 35 - Validate that the total value of the items plus the Freight value is correct.
    review_page.calculated_total_price(load_data_capabilities)

    # 36 - Click on the Place Order button
    review_page.place_order_button_click()

    # 37 - Validate that the Checkout Complete screen has been displayed
    checkout_page.get_checkout_complete_page_title()

    # 38 - Click on the Continue Shopping button
    checkout_page.continue_shopping_button_click()

    # 39 - Validate that the Products screen has been displayed and that the cart is empty.
    product_page.get_product_page_title()
    product_page.assert_cart_is_empty()