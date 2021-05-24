from pages.base_page import BasePage
from locators.register_form import RegisterForm
from locators.message import Message


class LoginPage(BasePage):

    def set_user_input(self):
        self.driver.find_element(*RegisterForm.name_locator).click()
        self.driver.find_element(*RegisterForm.name_locator).send_keys(
            'mateusz bzdzion')
        self.driver.find_element(*RegisterForm.email_locator).click()
        self.driver.find_element(*RegisterForm.email_locator).send_keys(
            'mateusz.bzdzion.benhauer+testrekrutacja@salesmanago.com')
        self.driver.find_element(*RegisterForm.company_locator).click()
        self.driver.find_element(
            *RegisterForm.company_locator).send_keys('salesmango')
        self.driver.find_element(*RegisterForm.website_locator).click()
        self.driver.find_element(
            *RegisterForm.website_locator).send_keys(
                'https://www.salesmanago.com/')
        self.driver.find_element(*RegisterForm.phone_locator).click()
        self.driver.find_element(
            *RegisterForm.phone_locator).send_keys(783318951)
        self.driver.find_element(*RegisterForm.submit_button_locator).click()

    def get_message(self):
        return self.driver.find_element(*Message.message_locator)
