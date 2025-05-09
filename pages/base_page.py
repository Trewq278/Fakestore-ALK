from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert


class BasePage:
    """
    Base class for each page
    """

    def __init__(self, driver):
        """
        Initializes the page with a WebDriver instance, default wait, and alert object
        Args: driver (WebDriver): Selenium WebDriver instance.
        """
        self.driver = driver
        self.wait_5s = WebDriverWait(self.driver, 5)
        self.alert = Alert(self.driver)
        self._verify_page()

    def _verify_page(self):
        """
        Hook method for verifying that the correct page is loaded
        Should be overridden by child classes if specific page checks are needed
        """
        return
