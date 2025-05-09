from ddt import ddt, data, unpack
from tests.base_test import BaseTest
from test_data.test_data import DataReader
from pages.order_confirmation_page import OrderConfirmationPage
from pages.card_page import CardPage
from time import sleep

@ddt
class OrderPageTests(BaseTest):
    """
    Test class for verifying the order page functionalities, focusing on card payment validations.
    """
    def setUp(self):
        """
        Sets up the test environment before each test
        Adds a product to the cart and navigates to the order page
        """
        super().setUp()
        self.store_page = self.home_page.click_store_page()
        self.windsurfing_store_page = self.store_page.click_windsurfing()
        self.windsurfing_store_page.close_info_content()
        self.windsurfing_store_page.add_fuerteventura()
        sleep(1)
        self.order_page = self.home_page.click_order_page()
        self.card_page = CardPage(self.driver)

    @data(*DataReader.get_csv_data('/home/student/Desktop/FakeStore/test_data/card_types.csv'))
    @unpack
    def testCardValid(self, description, number, cvc, date):
        """
        Tests completing an order using valid card data from card_types.csv file
        Verifies that the order confirmation message is displayed
        """
        print(f"Running test for: {description}")
        self.driver.refresh()
        self.order_page.enter_name()
        self.order_page.enter_lastname()
        self.order_page.enter_address()
        self.order_page.enter_postcode()
        self.order_page.enter_city()
        self.order_page.enter_phone()
        self.order_page.enter_email()
        self.card_page.enter_card_number(number)
        self.card_page.enter_card_date(date)
        self.card_page.enter_card_cvc(cvc)
        self.order_page.click_terms()
        self.order_page.click_pay_button()
        self.order_confirmation_page = OrderConfirmationPage(self.driver)
        message = self.order_confirmation_page.get_confirmation_message()
        self.assertEqual("Zamówienie otrzymane", message)

    @data(*DataReader.get_csv_data('/home/student/Desktop/FakeStore/test_data/rejected_cards.csv'))
    @unpack
    def testCardRejected(self, description, number, cvc, date):
        """
        Tests completing an order using rejected card data from a rejected_cards.csv file
        Verifies that a 'card rejected' alert message is displayed
        """
        print(f"Running test for: {description}")
        self.order_page.enter_name()
        self.order_page.enter_lastname()
        self.order_page.enter_address()
        self.order_page.enter_postcode()
        self.order_page.enter_city()
        self.order_page.enter_phone()
        self.order_page.enter_email()
        self.card_page.enter_card_number(number)
        self.card_page.enter_card_date(date)
        self.card_page.enter_card_cvc(cvc)
        self.order_page.click_terms()
        self.order_page.click_pay_button()
        self.assertEqual("Karta została odrzucona.", self.card_page.get_card_reject_alert())

    def testEmptyCVC(self):
        """
        Tests submitting an order with empty Cvc code input
        Verifies that an appropriate alert is displayed
        """
        print(f"Running test for: Empty CVC")
        self.order_page.enter_name()
        self.order_page.enter_lastname()
        self.order_page.enter_address()
        self.order_page.enter_postcode()
        self.order_page.enter_city()
        self.order_page.enter_phone()
        self.order_page.enter_email()
        self.card_page.enter_card_number("4242424242424242")
        self.card_page.enter_card_date("12/26")
        self.order_page.click_terms()
        self.order_page.click_pay_button()
        self.assertEqual("Kod bezpieczeństwa karty jest niekompletny.", self.card_page.get_empty_cvc_alert())

    def testEmptyDate(self):
        """
        Tests submitting an order with empty card expiry date input
        Verifies that an appropriate alert is displayed
        """
        print(f"Running test for: Empty Expiry Date")
        self.order_page.enter_name()
        self.order_page.enter_lastname()
        self.order_page.enter_address()
        self.order_page.enter_postcode()
        self.order_page.enter_city()
        self.order_page.enter_phone()
        self.order_page.enter_email()
        self.card_page.enter_card_number("4242424242424242")
        self.card_page.enter_card_cvc("111")
        self.order_page.click_terms()
        self.order_page.click_pay_button()
        self.assertEqual("Data ważności karty jest niekompletna.", self.card_page.get_empty_card_date_alert())

    def testEmptyCardNumber(self):
        """
        Tests submitting an order with empty card number input
        Verifies that an appropriate alert is displayed
        """
        print(f"Running test for: Empty Card Number")
        self.order_page.enter_name()
        self.order_page.enter_lastname()
        self.order_page.enter_address()
        self.order_page.enter_postcode()
        self.order_page.enter_city()
        self.order_page.enter_phone()
        self.order_page.enter_email()
        self.card_page.enter_card_date("12/26")
        self.card_page.enter_card_cvc("111")
        self.order_page.click_terms()
        self.order_page.click_pay_button()
        self.assertEqual("Numer karty jest niekompletny.", self.card_page.get_empty_card_number_alert())

    @data(*DataReader.get_csv_data('/home/student/Desktop/FakeStore/test_data/invalid_card_number.csv'))
    @unpack
    def testInvalidCardNumber(self, description, number, cvc, date):
        """
        Tests submitting an order with an invalid card number from an invalid_card_number.csv file
        Verifies that an appropriate invalid card number alert is displayed.
        """
        print(f"Running test for: {description}")
        self.order_page.enter_name()
        self.order_page.enter_lastname()
        self.order_page.enter_address()
        self.order_page.enter_postcode()
        self.order_page.enter_city()
        self.order_page.enter_phone()
        self.order_page.enter_email()
        self.card_page.enter_card_number(number)
        self.card_page.enter_card_date(date)
        self.card_page.enter_card_cvc(cvc)
        self.order_page.click_terms()
        self.order_page.click_pay_button()
        self.assertEqual("Numer karty nie jest prawidłowym numerem karty kredytowej.", self.card_page.get_invalid_card_number_alert())

    @data(*DataReader.get_csv_data('/home/student/Desktop/FakeStore/test_data/invalid_card_cvc.csv'))
    @unpack
    def testInvalidCardCVC(self, description, number, cvc, date):
        """
        Tests submitting an order with an invalid CVC code from an invalid_card_cvc.csv file
        Verifies that an appropriate invalid CVC alert is displayed
        """
        print(f"Running test for: {description}")
        self.order_page.enter_name()
        self.order_page.enter_lastname()
        self.order_page.enter_address()
        self.order_page.enter_postcode()
        self.order_page.enter_city()
        self.order_page.enter_phone()
        self.order_page.enter_email()
        self.card_page.enter_card_number(number)
        self.card_page.enter_card_date(date)
        self.card_page.enter_card_cvc(cvc)
        self.order_page.click_terms()
        self.order_page.click_pay_button()
        self.assertEqual("Kod bezpieczeństwa karty jest niekompletny.", self.card_page.get_invalid_cvc_alert())

    @data(*DataReader.get_csv_data('/home/student/Desktop/FakeStore/test_data/invalid_card_exp_date.csv'))
    @unpack
    def testInvalidCardDate(self, description, number, cvc, date):
        """
        Tests submitting an order with an invalid card expiration date from and invalid_card_exp_date.csv file
        Verifies that an appropriate invalid expiration year alert is displayed
        """
        print(f"Running test for: {description}")
        self.order_page.enter_name()
        self.order_page.enter_lastname()
        self.order_page.enter_address()
        self.order_page.enter_postcode()
        self.order_page.enter_city()
        self.order_page.enter_phone()
        self.order_page.enter_email()
        self.card_page.enter_card_number(number)
        self.card_page.enter_card_date(date)
        self.card_page.enter_card_cvc(cvc)
        self.order_page.click_terms()
        self.order_page.click_pay_button()
        self.assertEqual("Rok ważności karty jest nieprawidłowy.", self.card_page.get_invalid_exp_date_alert())

    @data(*DataReader.get_csv_data('/home/student/Desktop/FakeStore/test_data/expired_card.csv'))
    @unpack
    def testExpiredCard(self, description, number, cvc, date):
        """
        Tests submitting an order with an expired card from an expired_card.csv file
        Verifies that an appropriate expired card alert is displayed
        """
        print(f"Running test for: {description}")
        self.order_page.enter_name()
        self.order_page.enter_lastname()
        self.order_page.enter_address()
        self.order_page.enter_postcode()
        self.order_page.enter_city()
        self.order_page.enter_phone()
        self.order_page.enter_email()
        self.card_page.enter_card_number(number)
        self.card_page.enter_card_date(date)
        self.card_page.enter_card_cvc(cvc)
        self.order_page.click_terms()
        self.order_page.click_pay_button()
        self.assertEqual("Rok ważności karty upłynął w przeszłości", self.card_page.get_card_expired_alert())
