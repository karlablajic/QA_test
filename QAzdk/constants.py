class Config:
    HOME_PAGE = "https://finansavisen.no/"
    NYHETER_BUTTONS_NUMBER = 12
    CHROME_PATH = "C:/Users/Korisnik/Desktop/chromedriver_win32/chromedriver"


class Locators:
    HEADER_DROPDOWN_BUTTON = "//span[contains(@class,'item__text') and text()='{text}']"
    HEADER_DROPDOWN_OPEN_CHECKER = "//div[span[contains(@class,'item__text') and text()='{text}']]//following-sibling::div"
    NYHETER_BUTTON_LI_ELEMENTS = "//li[descendant::span[contains(@class,'item__text') and text()='Nyheter']]//li"
    LOGO = "//a[@class='c-header-bar__logo']"
    TOGGLE_MENU = "//div[contains(@class,'c-header-bar__toggle-menu')]"
    TOGGLE_MENU_OPEN_CHECKER = "//div[contains(@class,'c-header-bar__toggle-menu')]//div[contains(@class,'js-header-menu')]"
    SPAN_TEXT = "//li[contains(@class,'header-bar')]//span[text()='{text}']"
    A_ELEMENT = "//a[text()='{text}']"

    MOBILE_HEADER_DROPDOWN_BUTTON = "//span[contains(@class,'frontpagemobilenav') and text()='{text}']"
    MOBILE_HEADER_DROPDOWN_OPEN_CHECKER = "//div[span[contains(@class,'pagemobile') and text()='Nyheter']]"
    MOBILE_SPAN_TEXT = "//li[contains(@class,'frontpagemobilenav')]//span[text()='{text}']"
    MOBILE_TOGGLE_MENU = "//div[contains(@class,'toggle-btn--mobile')]"
