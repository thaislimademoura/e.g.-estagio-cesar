import pytest
from pages_mobile.home_page import HomePage
from pages_mobile.product_page import ProductPage

# Import other page objects as needed

def test_product_selection(driver):
    # Initialize page objects with the driver provided by the fixture
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    # product_page = ProductPage(driver)

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
    assert product_page.get_qnt_items_txt() == "2"
    product_page.add_to_cart_click()

    # 9 - Validate that a circle has appeared in the cart icon informing you of the exact number
    assert product_page.get_cart_icon() == True
    assert product_page.get_cart_icon_number() == product_page.get_qnt_items_txt()

    ####################################################################

