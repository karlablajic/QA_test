from selenium.common.exceptions import NoSuchElementException
import pytest


def click_element(driver, xpath=None):
    try:
        driver.find_element_by_xpath(xpath).click()
    except NoSuchElementException:
        pytest.fail(f"Could not locate {xpath}")
    except Exception as e:
        pytest.fail(f"Reason: {e}")


# # https://stackoverflow.com/a/63656230
def is_element_visible_in_viewpoint(driver, element) -> bool:
    return driver.execute_script("var elem = arguments[0],                 " 
                                 "  box = elem.getBoundingClientRect(),    " 
                                 "  cx = box.left + box.width / 2,         " 
                                 "  cy = box.top + box.height / 2,         " 
                                 "  e = document.elementFromPoint(cx, cy); " 
                                 "for (; e; e = e.parentElement) {         " 
                                 "  if (e === elem)                        " 
                                 "    return true;                         " 
                                 "}                                        " 
                                 "return false;                            "
                                 , element)
