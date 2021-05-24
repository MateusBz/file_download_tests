from selenium.webdriver.common.by import By


class Ebook:

    link_locator = (
        By.XPATH, '//*[contains(@href, "data-ethics-preference-management")]')
