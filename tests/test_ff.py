import pytest
from pages.index_page import IndexPage
from pages.knowledgecenter_page import KnowlegdeCenterPage
from pages.login_page import LoginPage


def test_ff(ff_driver_init, get_link_locator, test_data):
    index = IndexPage(ff_driver_init)
    index.navigate(IndexPage.url)
    index.get_resources()
    ebook = KnowlegdeCenterPage(ff_driver_init)
    url = ebook.get_book_link(get_link_locator)
    ebook.navigate(url)
    login = LoginPage(ff_driver_init)
    login.set_user_input(
        test_data["name"], test_data["email"],
        test_data["company"], test_data["website"], test_data["phone"])
    assert login.get_message()
