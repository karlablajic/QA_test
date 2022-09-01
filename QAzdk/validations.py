import pytest

from constants import Locators


def validate_number_of_nyheter_buttons(expected_num, li_elements):
    if len(li_elements) != expected_num:
        pytest.fail(f"Should have {expected_num} element but has {len(li_elements)}")
    # for element in li_elements:
    #     if not element.is_displayed():
    #         pytest.fail(f"Element in nyheter dropdown not displayed")
    #


def validate_dropdown_open(driver, button, span_element, mobile=False):
    if mobile:
        locator = Locators.MOBILE_HEADER_DROPDOWN_OPEN_CHECKER
        checker = "toggled"
        span_locator = Locators.MOBILE_SPAN_TEXT
    else:
        locator = Locators.HEADER_DROPDOWN_OPEN_CHECKER
        checker = "open"
        span_locator = Locators.SPAN_TEXT

    element = driver.find_element_by_xpath(locator.format(text=button))
    class_atr = element.get_attribute("class")
    if checker not in class_atr:
        pytest.fail(f"Dropdown for {button} should be opened")
    element = driver.find_element_by_xpath(span_locator.format(text=span_element))
    if not element.is_displayed():
        pytest.fail(f"Dropdown for {button} should be opened. Expected item {span_element} not displayed")


def validate_dropdown_closed(driver, button, span_element, mobile=False):
    if mobile:
        locator = Locators.MOBILE_HEADER_DROPDOWN_OPEN_CHECKER
        checker = "toggled"
        span_locator = Locators.MOBILE_SPAN_TEXT
    else:
        locator = Locators.HEADER_DROPDOWN_OPEN_CHECKER
        checker = "open"
        span_locator = Locators.SPAN_TEXT

    element = driver.find_element_by_xpath(locator.format(text=button))
    class_atr = element.get_attribute("class")
    if checker in class_atr:
        pytest.fail(f"Dropdown for {button} should be closed")
    element = driver.find_element_by_xpath(span_locator.format(text=span_element))
    if element.is_displayed():
        pytest.fail(f"Dropdown for {button} should be closed. Expected item {span_element} displayed")


def validate_menu_open(driver, mobile=False):
    if mobile:
        locator = Locators.MOBILE_TOGGLE_MENU
        checker = "is-open"
    else:
        locator = Locators.TOGGLE_MENU_OPEN_CHECKER
        checker = "open"

    element = driver.find_element_by_xpath(locator)
    class_atr = element.get_attribute("class")
    if checker not in class_atr:
        pytest.fail(f"Menu should be opened")
    if not mobile:
        element = driver.find_element_by_xpath(Locators.A_ELEMENT.format(text="Merkevareskolen"))
        if not element.is_displayed():
            pytest.fail(f"Menu should be opened. Expected element not found - Merkevareskolen")


def validate_menu_closed(driver, mobile=False):
    if mobile:
        locator = Locators.MOBILE_TOGGLE_MENU
        checker = "is-open"
    else:
        locator = Locators.TOGGLE_MENU_OPEN_CHECKER
        checker = "open"

    element = driver.find_element_by_xpath(locator)
    class_atr = element.get_attribute("class")
    if checker in class_atr:
        pytest.fail(f"Menu should be closed")
    if not mobile:
        element = driver.find_element_by_xpath(Locators.A_ELEMENT.format(text="Merkevareskolen"))
        if element.is_displayed():
            pytest.fail(f"Menu should be closed. Expected element found - Merkevareskolen")


def validate_search_results(driver, text_sent):
    search_display = driver.find_element_by_xpath(f"//span[@data-inner and text()='{text_sent}']")
    if not search_display.is_displayed():
        pytest.fail(f"Expected element failed {text_sent}")