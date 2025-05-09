from tests.base_test import BaseTest
from pages.store_page import StorePage

class StorePageTest(BaseTest):
    """
    Test class for verifying navigation from the store page to specific categories.
    """

    def setUp(self):
        """
        Sets up the test environment before each test
        Navigates from the home page to the store page
        """
        super().setUp()
        self.store_page = self.home_page.click_store_page()

    def testClickWindsurfing(self):
        """
        Tests clicking on the Windsurfing category from the store page.
        """
        self.store_page = StorePage(self.driver)
        self.store_page.click_windsurfing()
