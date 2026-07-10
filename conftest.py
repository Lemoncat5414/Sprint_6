import pytest
from selenium import webdriver
from data import Urls

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.PAGE_MAIN)
    driver.maximize_window()
    yield driver
    driver.quit()