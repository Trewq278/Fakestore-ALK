from tests.base_test import BaseTest
from pages.windsurfing_store_page import WindsurfingStoreLocators

class WindsurfingStoreTest(BaseTest):
    """
    Test class for verifying the functionality of adding windsurfing products to the shopping cart
    """

    def setUp(self):
        """
        Sets up the test environment before each test.
        Navigates from the home page to the windsurfing store page.
        """
        super().setUp()
        self.store_page = self.home_page.click_store_page()
        self.windsurfing_store_page = self.store_page.click_windsurfing()

    def testAddGrecja(self):
        """
        Tests adding the Grecja Limnos product to the shopping cart.
        Verifies that the View Cart button is visible after adding the product.
        """
        element = self.driver.find_element(*WindsurfingStoreLocators.GRECJA_LIMNOS_ADD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.windsurfing_store_page.add_grecja()
        element = self.driver.find_element(*WindsurfingStoreLocators.GRECJA_CART_BUTTON)
        self.assertTrue(element.is_displayed(), "Element: Zobacz koszyk, dla Produktu: Grecja Limnos, nie jest widoczny po dodaniu produktu do koszyka")

    def testAddFuerteventrua(self):
        """
        Tests adding the Fuerteventura product to the shopping cart.
        Verifies that the View Cart button is visible after adding the product.
        """
        element = self.driver.find_element(*WindsurfingStoreLocators.FUERTEVENTURA_SOTAVENTO_ADD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.windsurfing_store_page.add_fuerteventura()
        element = self.driver.find_element(*WindsurfingStoreLocators.FUERTEVENTURA_CART_BUTTON)
        self.assertTrue(element.is_displayed(), "Element: Zobacz koszyk, dla Produktu: Fuerteventura Sotavento, nie jest widoczny po dodaniu produktu do koszyka")

    def testAddSal(self):
        """
        Tests adding the Cape Verde Islands - Sal product to the shopping cart.
        Verifies that the View Cart button is visible after adding the product.
        """
        element = self.driver.find_element(*WindsurfingStoreLocators.SAL_ADD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.windsurfing_store_page.add_sal()
        element = self.driver.find_element(*WindsurfingStoreLocators.SAL_ADD)
        self.assertTrue(element.is_displayed(),"Element: Zobacz koszyk, dla Produktu: Wyspy Zielonego Przylądka Sal, nie jest widoczny po dodaniu produktu do koszyka")


