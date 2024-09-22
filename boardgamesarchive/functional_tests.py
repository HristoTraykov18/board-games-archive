"""Functional tests"""

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.xfail
def test_main_page(chrome_browser):
    """Check the elements of the main page"""

    chrome_browser.get("http://localhost:8000")
    option_buttons = chrome_browser.find_element(
        By.CLASS_NAME, "option-button")
    assert "Board games archive" in chrome_browser.title
    assert len(option_buttons) == 5
    print("OK")
