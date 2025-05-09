from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.order_page import OrderPage

class CardPageLocators(BasePage):
    """
    Card Page Locators
    """
    CARD_IFRAME = (By.CSS_SELECTOR, "#stripe-card-element iframe")
    CARD_NUMBER_INPUT = (By.CSS_SELECTOR, ".InputElement[name='cardnumber']")

    CARD_DATE_IFRAME = (By.CSS_SELECTOR, "#stripe-exp-element iframe")
    CARD_DATE_INPUT = (By.CSS_SELECTOR, "[name='exp-date']")

    CARD_CVC_IFRAME = (By.CSS_SELECTOR, "#stripe-cvc-element iframe")
    CARD_CVC_INPUT = (By.CSS_SELECTOR, "[name='cvc']")

    EMPTY_CVC_ALERT = (By.XPATH, '//*[@id="wc-stripe-cc-form"]/div[5]/ul/li')
    EMPTY_CARD_DATE_ALERT = (By.XPATH, '//*[@id="wc-stripe-cc-form"]/div[5]/ul/li')
    EMPTY_CARD_NUMBER_ALERT = (By.XPATH, '//*[@id="wc-stripe-cc-form"]/div[5]/ul/li')

    INVALID_EXP_YEAR_ALERT = (By.XPATH, '//*[@id="wc-stripe-cc-form"]/div[5]/ul/li')
    INVALID_CVC_ALERT = (By.XPATH, '//*[@id="wc-stripe-cc-form"]/div[5]/ul/li')
    INVALID_CARD_NUMBER_ALERT = (By.XPATH, '//*[@id="wc-stripe-cc-form"]/div[5]/ul/li')

    CARD_REJECT_ALERT = (By.XPATH, '//*[@id="post-7"]/div/div/form[3]/div[1]/div/ul/li')

    CARD_EXPIRED_ALERT = (By.XPATH, '//*[@id="wc-stripe-cc-form"]/div[5]/ul/li')

class CardPage(BasePage):
    """
    Page Object Model class for the Card Page
    Provides methods to interact with order form fields and actions
    """

    def __init__(self, driver):
        """
        Initializes the class with a given WebDriver instance and sets up an explicit wait
        :param driver: Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_card_number(self, number):
        """
        Enters the card number into the card number input field inside an iframe
        :param number: Card number to enter
        :return: OrderPage object
        """
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(CardPageLocators.CARD_IFRAME))
        self.wait.until(EC.visibility_of_element_located(CardPageLocators.CARD_NUMBER_INPUT)).send_keys(number)
        self.driver.switch_to.default_content()
        return OrderPage(self.driver)

    def enter_card_date(self, date):
        """
        Enters the card expiration date into the card date input field inside an iframe
        :param date: Expiration date to enter
        :return: OrderPage object
        """
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(CardPageLocators.CARD_DATE_IFRAME))
        self.wait.until(EC.visibility_of_element_located(CardPageLocators.CARD_DATE_INPUT)).send_keys(date)
        self.driver.switch_to.default_content()
        return OrderPage(self.driver)

    def enter_card_cvc(self, cvc):
        """
        Enters the card CVC code into the CVC input field inside an iframe
        :param cvc: CVC code to enter
        :return: OrderPage object
        """
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(CardPageLocators.CARD_CVC_IFRAME))
        self.wait.until(EC.visibility_of_element_located(CardPageLocators.CARD_CVC_INPUT)).send_keys(cvc)
        self.driver.switch_to.default_content()
        return OrderPage(self.driver)

    def get_empty_cvc_alert(self):
        """
        Waits 10s for the Empty cvc alert text in Card Page object
        :return: Alert text
        """
        self.wait.until(EC.text_to_be_present_in_element(CardPageLocators.EMPTY_CVC_ALERT, "Kod bezpieczeństwa karty jest niekompletny."))
        return self.driver.find_element(*CardPageLocators.EMPTY_CVC_ALERT).text

    def get_empty_card_date_alert(self):
        """
        Waits 10s for the Empty expiration date in Card Page object
        :return: Alert text
        """
        self.wait.until(EC.text_to_be_present_in_element(CardPageLocators.EMPTY_CARD_DATE_ALERT, "Data ważności karty jest niekompletna."))
        return self.driver.find_element(*CardPageLocators.EMPTY_CARD_DATE_ALERT).text

    def get_empty_card_number_alert(self):
        """
        Waits 10s for the Empty card number alert text in Card Page object
        :return: Alert text
        """
        self.wait.until(EC.text_to_be_present_in_element(CardPageLocators.EMPTY_CARD_NUMBER_ALERT, "Numer karty jest niekompletny."))
        return self.driver.find_element(*CardPageLocators.EMPTY_CARD_NUMBER_ALERT).text

    def get_invalid_exp_date_alert(self):
        """
        Waits 10s for the Invalid Expiration date alert text in Card Page object
        :return: Alert text
        """
        self.wait.until(EC.text_to_be_present_in_element(CardPageLocators.INVALID_EXP_YEAR_ALERT,"Rok ważności karty jest nieprawidłowy."))
        return self.driver.find_element(*CardPageLocators.INVALID_EXP_YEAR_ALERT).text

    def get_invalid_cvc_alert(self):
        """
        Waits 10s for the Invalid CVC alert text in Card Page object
        :return: Alert text
        """
        self.wait.until(EC.text_to_be_present_in_element(CardPageLocators.INVALID_CVC_ALERT, "Kod bezpieczeństwa karty jest niekompletny."))
        return self.driver.find_element(*CardPageLocators.INVALID_CVC_ALERT).text

    def get_invalid_card_number_alert(self):
        """
        Waits 10s for the Invalid card number alert text in Card Page object
        :return: Alert text
        """
        self.wait.until(EC.text_to_be_present_in_element(CardPageLocators.INVALID_CARD_NUMBER_ALERT, "Numer karty nie jest prawidłowym numerem karty kredytowej."))
        return self.driver.find_element(*CardPageLocators.INVALID_CARD_NUMBER_ALERT).text

    def get_card_reject_alert(self):
        """
        Waits 10s for the Rejected card alert text in Card Page object
        :return: Alert text
        """
        self.wait.until(EC.text_to_be_present_in_element(CardPageLocators.CARD_REJECT_ALERT, "Karta została odrzucona."))
        return self.driver.find_element(*CardPageLocators.CARD_REJECT_ALERT).text

    def get_card_expired_alert(self):
        """
        Waits 10s for the Expired card alert text in Card Page object
        :return: Alert text
        """
        self.wait.until(EC.text_to_be_present_in_element(CardPageLocators.CARD_EXPIRED_ALERT, "Rok ważności karty upłynął w przeszłości"))
        return self.driver.find_element(*CardPageLocators.CARD_EXPIRED_ALERT).text