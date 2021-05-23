from pages.base_page import BasePage
from locators.dropdown_menu import DropdownMenu


class IndexPage(BasePage):

    url = 'https://www.salesmanago.com/'

    def get_resources(self):
        dropdown = self.driver.find_element(*DropdownMenu.dropdown_locator)
        self.driver.execute_script('arguments[0].click()', dropdown)
        self.driver.find_element(*DropdownMenu.ebooks_locator).click()
