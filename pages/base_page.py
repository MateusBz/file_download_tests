class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.driver.implicitly_wait(3)

    def navigate(self, url):
        self.driver.get(url)
