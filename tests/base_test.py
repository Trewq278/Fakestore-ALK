import unittest
from selenium import webdriver
from pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        """
        Sets up the test environment before each test by initializing the Chrome WebDriver, maximizing the window,
        navigating to the test website, and creating a HomePage instance.
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://fakestore.testelka.pl/")
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        """
        Quits the WebDriver after each test, closing the browser window.
        """
        self.driver.quit()
