import pytest
from selenium import webdriver


@pytest.fixture
def setup() -> None:
    driver = webdriver.Firefox(executable_path='./drivers/geckodriver')

    yield driver

    driver.quit()
