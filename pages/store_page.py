from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.windsurfing_store_page import WindSurfingStore

class StorePageLocators(BasePage):
    STORE_HEADER = (By.XPATH, '//*[@id="main"]/header/h1')
    WINDSURFING_CATEGORY = (By.CSS_SELECTOR, '#main > ul > li:nth-child(1) > a > img')
    HIKING_CATEGORY = (By.XPATH, '//*[@id="main"]/ul/li[2]/a/img')
    YOGA_CATEGORY = (By.XPATH, '//*[@id="main"]/ul/li[3]/a/img')
    SAILING_CATEGORY = (By.XPATH, '//*[@id="main"]/ul/li[4]/a/img')

class StorePage(BasePage):
    """
    Page Object Model class for the Order Page
    Provides methods to interact with order form fields and actions
    """

    def click_windsurfing(self):
        """
        Clicks Windsurfing category and returns Windsurfing Store Page instance
        :return: Windsurfing Store Page
        """
        self.driver.find_element(*StorePageLocators.WINDSURFING_CATEGORY).click()
        return WindSurfingStore(self.driver)

    def click_hiking(self):
        """
        Clicks Hiking category
        """
        self.driver.find_element(*StorePageLocators.HIKING_CATEGORY).click()

    def click_yoga(self):
        """
        CLicks Yoga category
        """
        self.driver.find_element(*StorePageLocators.YOGA_CATEGORY).click()

    def click_sailing(self):
        """
        Clicks Sailing category
        """
        self.driver.find_element(*StorePageLocators.SAILING_CATEGORY).click()