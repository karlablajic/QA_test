from constants import Config, Locators
from helpers import go_to_page, get_number_of_nyheter_buttons_mobile

from validations import validate_number_of_nyheter_buttons, validate_dropdown_open, validate_menu_open, \
    validate_menu_closed, validate_dropdown_closed
from webdriver_hlp import click_element

#
 def test_dropdowns_in_header(driver):
#     go_to_page(driver)
#     click_element(driver, Locators.MOBILE_HEADER_DROPDOWN_BUTTON.format(text='Nyheter'))
#     validate_dropdown_open(driver, "Nyheter", "Siste 24 timer", mobile=True)
#     click_element(driver, Locators.LOGO)
#     validate_dropdown_closed(driver, "Nyheter", "Siste 24 timer", mobile=True)
#
#     click_element(driver, Locators.MOBILE_TOGGLE_MENU)
#     validate_menu_open(driver, mobile=True)
#     click_element(driver, Locators.LOGO)
#     validate_menu_closed(driver, mobile=True)


def test_nyheter_dropdown(driver):
    go_to_page(driver)
    li_elements = get_number_of_nyheter_buttons_mobile(driver)
    validate_number_of_nyheter_buttons(Config.NYHETER_BUTTONS_NUMBER, li_elements)
