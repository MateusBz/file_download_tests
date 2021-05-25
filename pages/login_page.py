from pages.base_page import BasePage
from locators.register_form import RegisterForm
from locators.message import Message


class LoginPage(BasePage):

    def set_user_input(self, name, email, company, website, phone):
        self.driver.find_element(*RegisterForm.name_locator).click()
        self.driver.find_element(*RegisterForm.name_locator).send_keys(name)
        self.driver.find_element(*RegisterForm.email_locator).click()
        self.driver.find_element(*RegisterForm.email_locator).send_keys(email)
        self.driver.find_element(*RegisterForm.company_locator).click()
        self.driver.find_element(
            *RegisterForm.company_locator).send_keys(company)
        self.driver.find_element(*RegisterForm.website_locator).click()
        self.driver.find_element(
            *RegisterForm.website_locator).send_keys(website)
        self.driver.find_element(*RegisterForm.phone_locator).click()
        self.driver.find_element(
            *RegisterForm.phone_locator).send_keys(phone)
        self.driver.find_element(*RegisterForm.submit_button_locator).click()

    def get_message(self):
        return self.driver.find_element(*Message.message_locator)
