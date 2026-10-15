import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from scr.config import URL

@pytest.fixture(scope="function")
def driver():
    
    driver = webdriver.Firefox()
    driver.get(URL)
    yield driver
    driver.quit()


    