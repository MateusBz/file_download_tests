import pytest
from pages.index_page import IndexPage


def test_01(setup):
    index = IndexPage(setup)
    index.navigate(IndexPage.url)
    menu = index.get_resources()

