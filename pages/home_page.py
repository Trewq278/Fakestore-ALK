from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.my_account_page import MyAccountPageLocators
from pages.my_account_page import MyAccountPage
from pages.store_page import StorePageLocators
from pages.store_page import StorePage
from pages.order_page import OrderPageLocators
from pages.order_page import OrderPage



class HomePageLocators:
    """
    Home Page locators
    """
    MY_ACCOUNT = (By.CSS_SELECTOR, '#menu-item-201 > a')
    STORE = (By.CSS_SELECTOR, '#menu-item-198 > a')
    CART = (By.XPATH, '//*[@id="site-header-cart"]/li[1]/a/span[1]')
    ORDER = (By.XPATH, '//*[@id="menu-item-199"]/a')

class HomePage(BasePage):
    """
    Page Object Model class for the Order Page
    Provides methods to interact with order form fields and actions
    """

    def click_my_account(self):
        """
        Clicks my account link
        :return: My account instance
        """
        #1. Find My account button
        #2. Click it
        self.driver.find_element(*HomePageLocators.MY_ACCOUNT).click()
        self.wait_5s.until(EC.element_to_be_clickable(MyAccountPageLocators.LOG_IN_BUTTON))
        return MyAccountPage(self.driver)

    def click_store_page(self):
        """
        Clicks store link
        :return: Store instance
        """
        self.driver.find_element(*HomePageLocators.STORE).click()
        self.wait_5s.until(EC.text_to_be_present_in_element(StorePageLocators.STORE_HEADER, "Sklep"))
        return StorePage(self.driver)

    def click_order_page(self):
        """
        Clicks order link
        :return: Order instance
        """
        self.driver.find_element(*HomePageLocators.ORDER).click()
        self.wait_5s.until(EC.text_to_be_present_in_element(OrderPageLocators.ORDER_HEADER, "Zamówienie"))
        return OrderPage(self.driver)



