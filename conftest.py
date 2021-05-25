import pytest
import json
from selenium import webdriver

TEST_DATA_PATH = 'test_data.json'


@pytest.fixture(scope='session')
def test_data():
    test_data_file = open(TEST_DATA_PATH)
    return json.load(test_data_file)


def pytest_addoption(parser):
    parser.addoption(
        "--book_title", action="store", default="default book title")


def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.book_title
    if 'book_title' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("book_title", [option_value])


@pytest.fixture()
def get_link_locator(book_title):
    with open('books.json') as f:
        data = json.load(f)
        if book_title in data:
            return data[book_title]
        else:
            pytest.exit('Wrong title. Enter a correct title.')


@pytest.fixture
def chrome_driver_init():
    driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
    yield driver
    driver.quit()


@pytest.fixture
def ff_driver_init():
    driver = webdriver.Firefox(executable_path='./drivers/geckodriver')
    yield driver
    driver.quit()
