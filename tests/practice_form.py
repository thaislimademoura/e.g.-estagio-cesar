from pages.practice_form_page import PracticeFormPage
from utils.data_loader import load_json_data
import pytest

@pytest.mark.parametrize("data", load_json_data("data/practice_form_data.json"))
def test_fill_practice_form(driver, data):
    form_page = PracticeFormPage(driver)
    form_page.navigate()