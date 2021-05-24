from pages.base_page import BasePage
from locators.ebook import Ebook


class KnowlegdeCenterPage(BasePage):

    def get_book_link(self):
        link = self.driver.find_element(*Ebook.link_locator)
        return link.get_attribute('href')
