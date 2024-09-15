from selenium import webdriver
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service("chromedriver"))
driver.set_page_load_timeout(15)
driver.get("http://localhost:8000")

assert "Congratulations!" in driver.title
print("OK")
