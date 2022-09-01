import time
import pytest
from selenium.common.exceptions import NoSuchElementException

from constants import Config, Locators
from helpers import go_to_page, get_number_of_nyheter_buttons, hover_in_header, send_to_search

from validations import validate_search_results, validate_number_of_nyheter_buttons, validate_dropdown_open, validate_menu_open, validate_dropdown_closed


def test_dropdowns_in_header(driver):
    go_to_page(driver)
    hover_in_header(driver, Locators.HEADER_DROPDOWN_BUTTON.format(text='Nyheter'))
    validate_dropdown_open(driver, "Nyheter", "Siste 24 timer")
    hover_in_header(driver, Locators.LOGO)
    validate_dropdown_closed(driver, "Nyheter")

    hover_in_header(driver, Locators.HEADER_DROPDOWN_BUTTON.format(text='Podcast'))
    validate_dropdown_open(driver, "Podcast", "Alle podcast")
    hover_in_header(driver, Locators.LOGO)
    validate_dropdown_closed(driver, "Podcast")

    hover_in_header(driver, Locators.TOGGLE_MENU)
    validate_menu_open(driver)
    hover_in_header(driver, Locators.LOGO)
    validate_dropdown_closed(driver)


 def test_nyheter_dropdown(driver):
    go_to_page(driver)
    li_elements = get_number_of_nyheter_buttons(driver)
    validate_number_of_nyheter_buttons(Config.NYHETER_BUTTONS_NUMBER, li_elements)

 def test_search_results(driver):
    go_to_page(driver)
    send_to_search(driver, "AASB")
    validate_search_results(driver,  "AASB")
    go_to_page(driver)
    send_to_search(driver, "ABG")
    validate_search_results(driver, "ABG")

from webdriver_hlp import is_element_visible_in_viewpoint


def test_search_subheader(driver):
    go_to_page(driver)
    driver.execute_script("window.scrollTo(0,2000);")
    time.sleep(5)
    subheader = driver.find_element_by_xpath("//nav[@class='c-oms']")

    if is_element_visible_in_viewpoint(driver, subheader):
         pytest.fail('should not be displayed')

def test_header(driver):
    go_to_page(driver)
    try:
        driver.find_element_by_xpath("//a[@href='/minside' and @data-ga-category]")
        pytest.fail('minside should not be displayed')
    except NoSuchElementException:
        pass
    login = driver.find_element_by_xpath("//a[@href='/login' and @data-ga-category and contains(@class,'desktop')]")
    kjop = driver.find_element_by_xpath("//a[@href='/abonnement' and @data-ga-category]")
    if not login or not login.is_displayed():
         pytest.fail('login shoiuld be displayed')
    if not kjop or not kjop.is_displayed():
         pytest.fail('kjop should be displayed')

    login.click()
    username = driver.find_element_by_xpath("//input[@id='j_username']")
    username.send_keys("hupsuciknu@vusra.com")

    password = driver.find_element_by_xpath("//input[@id='j_password']")
    password.send_keys("LongEnoughPasswordToCheckEnoughBoxes")
    driver.find_element_by_xpath( "//input[@id='loginButton']").click()
    time.sleep(5)
    try:
        driver.find_element_by_xpath("//a[@href='/login' and @data-ga-category and contains(@class,'desktop')]")
        pytest.fail('login should not be displayed')
    except NoSuchElementException:
        pass
    login = driver.find_element_by_xpath("//a[@href='/minside' and @data-ga-category]")
    kjop = driver.find_element_by_xpath("//a[@href='/abonnement' and @data-ga-category]")
    if not login or not login.is_displayed():
         pytest.fail('minside shoiuld be displayed')
    if not kjop or not kjop.is_displayed():
         pytest.fail('kjop should be displayed')

def test_footer(driver):
    go_to_page(driver)
    try:
        driver.find_element_by_xpath("//a[@href='/minside' and @data-ga-category]")
        pytest.fail('minside should not be displayed')
    except NoSuchElementException:
        pass
    login = driver.find_element_by_xpath("//a[@href='/login' and @data-ga-category and contains(@class,'desktop')]")
    kjop = driver.find_element_by_xpath("//a[@href='/abonnement' and @data-ga-category]")
    if not login or not login.is_displayed():
         pytest.fail('login shoiuld be displayed')
    if not kjop or not kjop.is_displayed():
         pytest.fail('kjop should be displayed')

    login.click()
    username = driver.find_element_by_xpath("//input[@id='j_username']")
    username.send_keys("hupsuciknu@vusra.com")

    password = driver.find_element_by_xpath("//input[@id='j_password']")
    password.send_keys("LongEnoughPasswordToCheckEnoughBoxes")
    driver.find_element_by_xpath( "//input[@id='loginButton']").click()
    time.sleep(5)

    try:
        driver.find_element_by_xpath("//a[@href='/login' and @data-ga-category and contains(@class,'desktop')]")
        pytest.fail('login should not be displayed')
    except NoSuchElementException:
        pass
    login = driver.find_element_by_xpath("//a[@href='/minside' and @data-ga-category]")
    kjop = driver.find_element_by_xpath("//a[@href='/abonnement' and @data-ga-category]")
    if not login or not login.is_displayed():
         pytest.fail('minside shoiuld be displayed')
    if not kjop or not kjop.is_displayed():
         pytest.fail('kjop should be displayed')





