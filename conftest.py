import pytest
from selenium import webdriver


@pytest.fixture
def setup() -> None:
    driver = webdriver.Firefox(executable_path='./geckodriver')

    yield driver

    driver.quit()
