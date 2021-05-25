from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class KnowlegdeCenterPage(BasePage):

    def get_book_link(self, link_locator):
        link = self.driver.find_element(
            By.XPATH, '// *[contains(@href, "' + link_locator + '")]')
        return link.get_attribute('href')
