from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class WindsurfingStoreLocators(BasePage):
    """
    Windsurfing Store Page Locators
    """
    CATEGORY_HEADER = (By.XPATH, '//*[@id="main"]/header/h1')
    FUERTEVENTURA_SOTAVENTO_ADD = (By.XPATH, '//*[@id="main"]/ul/li[2]/a[2]')
    GRECJA_LIMNOS_ADD = (By.XPATH, '//*[@id="main"]/ul/li[3]/a[2]')
    SAL_ADD = (By.XPATH, '//*[@id="main"]/ul/li[6]/a[2]')

    FUERTEVENTURA_CART_BUTTON = (By.ID, 'woocommerce_loop_add_to_cart_link_describedby_393')
    GRECJA_CART_BUTTON = (By.ID, 'woocommerce_loop_add_to_cart_link_describedby_391')
    SAL_CART_BUTTON = (By.ID, 'woocommerce_loop_add_to_cart_link_describedby_389')

    INFO_CONTENT_CLOSE = (By.XPATH, '/html/body/p/a')

class WindSurfingStore(BasePage):
    """
    Page Object Model class for the Order Page
    Provides methods to interact with order form fields and actions
    """
    def category_header_text(self):
        """
        Find category header
        :return: text of the header
        """
        return self.driver.find_element(WindsurfingStoreLocators.CATEGORY_HEADER).text

    def add_fuerteventura(self):
        """
        Clicks add Windsurfing in Fuerteventura button
        """
        self.driver.find_element(*WindsurfingStoreLocators.FUERTEVENTURA_SOTAVENTO_ADD).click()

    def add_grecja(self):
        """
        Clicks add Windsurfing in Grecja button
        """
        self.driver.find_element(*WindsurfingStoreLocators.GRECJA_LIMNOS_ADD).click()

    def add_sal(self):
        """
        Clicks add Windsurfing in Sal button
        """
        self.driver.find_element(*WindsurfingStoreLocators.SAL_ADD).click()

    def close_info_content(self):
        """
        Closing info content line at the bottom of the screen
        """
        self.driver.find_element(*WindsurfingStoreLocators.INFO_CONTENT_CLOSE).click()
