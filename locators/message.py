from selenium.webdriver.common.by import By


class Message:

    message_locator = (
        By.XPATH, '//*[contains(text(), "ebook has been sent")]')
