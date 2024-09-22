"""Tests fixtures"""

import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="module")
def chrome_browser(request):
    """Webdriver fixture"""

    os.chdir(request.fspath.dirname)
    _driver = webdriver.Chrome(service=Service("chromedriver"))
    _driver.set_page_load_timeout(15)
    yield _driver

    _driver.quit()
    os.chdir(request.config.invocation_params.dir)
