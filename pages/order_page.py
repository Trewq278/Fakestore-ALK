from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.order_confirmation_page import OrderConfirmationPage

class OrderPageLocators(BasePage):
    """
    Order Page Locators
    """
    ORDER_HEADER = (By.XPATH, '//*[@id="post-7"]/header/h1')
    NAME_INPUT = (By.ID, 'billing_first_name')
    LASTNAME_INPUT = (By.ID, 'billing_last_name')
    ADDRESS_INPUT = (By.ID, 'billing_address_1')
    POSTCODE_INPUT = (By.ID, 'billing_postcode')
    CITY_INPUT = (By.ID, 'billing_city')
    PHONE_INPUT = (By.ID, 'billing_phone')
    EMAIL_INPUT = (By.ID, 'billing_email')

    TERMS_CHECKBOX = (By.ID, 'terms')

    PAY_BUTTON = (By.XPATH, '//*[@id="place_order"]')


class OrderPage(BasePage):
    """
    Page Object Model class for the Order Page
    Provides methods to interact with order form fields and actions
    """

    def enter_name(self):
        """
        Enters a predefined first name into the name input field.
        """
        self.driver.find_element(*OrderPageLocators.NAME_INPUT).send_keys("Janusz")

    def enter_lastname(self):
        """
        Enters a predefined last name into the last name input field
        """
        self.driver.find_element(*OrderPageLocators.LASTNAME_INPUT).send_keys("Kwiatkowski")

    def enter_address(self):
        """
        Enters a predefined address into the address input field
        """
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys("Testowa 2")

    def enter_postcode(self):
        """
        Enters a predefined postcode into the postcode input field
        """
        self.driver.find_element(*OrderPageLocators.POSTCODE_INPUT).send_keys("11-111")

    def enter_city(self):
        """
        Enters a predefined city name into the city name input field
        """
        self.driver.find_element(*OrderPageLocators.CITY_INPUT).send_keys("Testowisko")

    def enter_phone(self):
        """
        Enters a predefined phone number into the phone number input field
        """
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys("111-111-111")

    def enter_email(self):
        """
        Enters a predefined email address into the email input field
        """
        self.driver.find_element(*OrderPageLocators.EMAIL_INPUT).send_keys("test_alk@test.pl")

    def click_terms(self):
        """
        Clicks terms and conditions checkbox
        """
        self.driver.find_element(*OrderPageLocators.TERMS_CHECKBOX).click()

    def click_pay_button(self):
        """
        Clicks Pay button and returns Order Confirmation instance
        :return: Order Confirmation instance
        """
        self.driver.find_element(*OrderPageLocators.PAY_BUTTON).click()
        return OrderConfirmationPage(self.driver)