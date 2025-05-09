from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrderConfirmationLocators(BasePage):
        """
        Order Confirmation Locators
        """

        CONFIRMATION_INFO = (By.XPATH, '//*[@id="post-7"]/header/h1')

class OrderConfirmationPage(BasePage):
    """
    Page Object Model class for the Order Page
    Provides methods to interact with order form fields and actions
    """
    def __init__(self, driver):
        """
        Initializes the class with a given WebDriver instance and sets up an explicit wait.
        :param driver: Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_confirmation_message(self):
        """
        Waits maximum 5s for Confirmation text in Confirmation page
        :return: Confirmation text
        """
        self.wait.until(EC.text_to_be_present_in_element(OrderConfirmationLocators.CONFIRMATION_INFO, "Zamówienie otrzymane"))
        return self.driver.find_element(*OrderConfirmationLocators.CONFIRMATION_INFO).text