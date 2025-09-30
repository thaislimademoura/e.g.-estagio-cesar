from pages.widgets_menu_page import WidgetsMenuPage


def test_navigate_to_widgets_menu_page(driver):
    widgets_menu_page = WidgetsMenuPage(driver)
    widgets_menu_page.navigate()

    widgets_menu_page.hover_over_item_2_button()
   
    widgets_menu_page.hover_over_SUB_SUB_LIST_button()
   
    widgets_menu_page.hover_over_sub_sub_item_1_button()

    assert driver.find_element(*widgets_menu_page.sub_sub_item_1).is_displayed()