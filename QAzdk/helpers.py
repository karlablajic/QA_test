import time

from constants import Config, Locators

from webdriver_hlp import click_element
from selenium.webdriver.common.action_chains import ActionChains


def go_to_page(driver, page=Config.HOME_PAGE):
    driver.maximize_window()
    driver.get(page)


def hover_in_header(driver, locator):
    element = driver.find_element_by_xpath(locator)
    hover = ActionChains(driver).move_to_element(element)
    hover.perform()


def get_number_of_nyheter_buttons(driver):
    click_element(driver, xpath=Locators.HEADER_DROPDOWN_BUTTON.format(text='Nyheter'))
    li_elements = driver.find_elements_by_xpath(Locators.NYHETER_BUTTON_LI_ELEMENTS)
    return li_elements


def get_number_of_nyheter_buttons_mobile(driver):
    click_element(driver, xpath=Locators.MOBILE_HEADER_DROPDOWN_BUTTON.format(text='Nyheter'))
    li_elements = driver.find_elements_by_xpath(Locators.NYHETER_BUTTON_LI_ELEMENTS)
    return li_elements


def send_to_search(driver, text_sent):
    search_box_element = driver.find_element_by_xpath("//form[@class='c-frontpagemobilenav__search u-desktop-nav-only']/input")
    search_box_element.click()
    search_box_element.send_keys(text_sent)
    time.sleep(10)