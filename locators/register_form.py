from selenium.webdriver.common.by import By


class RegisterForm:

    name_locator = (By.XPATH, '//input[@name="name"]')
    email_locator = (By.XPATH, '//input[@id="email"]')
    company_locator = (By.XPATH, '//input[@name="company"]')
    website_locator = (By.XPATH, '//input[@name="url"]')
    phone_locator = (By.XPATH, '//input[@id="phoneNumber"]')
    submit_button_locator = (
        By.XPATH, '//button[@class="btn center-block form-btn form-btn"]')
