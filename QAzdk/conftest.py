import os

import pytest as pytest
from selenium import webdriver
from constants import Config
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver(request):
    version = os.environ.get("version_browser")

    options = Options()
    if version == "mobile":
        options.add_experimental_option(
            "mobileEmulation",
            {"deviceMetrics": {"width": 500, "height": 900}}
        )

    driver = webdriver.Chrome(Config.CHROME_PATH, options=options)

    request.addfinalizer(driver.quit)
    request.addfinalizer(driver.close)

    return driver

