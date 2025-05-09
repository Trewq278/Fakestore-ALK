from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class MyAccountPageLocators:
    """
    My account page locators
    """
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOG_IN_BUTTON = (By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/button')
    MY_ACCOUNT_TEXT = (By.XPATH, '//*[@id="post-8"]/div/div/div/p[1]')
    LOG_OUT_LINK = (By.XPATH, '//*[@id="post-8"]/div/div/div/p[1]/a')

    EMPTY_PASSWORD_ALERT = (By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')
    INVALID_PASSWORD_ALERT = (By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')
    EMPTY_LOGIN_ALERT = (By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')
    INVALID_LOGIN_ALERT = (By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')


class MyAccountPage(BasePage):
    """
    Page Object Model class for the Order Page
    Provides methods to interact with order form fields and actions
    """

    def enter_username_login(self):
        """
        Enters username in username input
        """
        self.driver.find_element(*MyAccountPageLocators.USERNAME_INPUT).send_keys("test_alk@test.pl")

    def enter_password_login(self):
        """
        Enters password in password input
        """
        self.driver.find_element(*MyAccountPageLocators.PASSWORD).send_keys("haselko123")

    def enter_invalid_password(self):
        """
        Enters invalid password
        """
        self.driver.find_element(*MyAccountPageLocators.PASSWORD).send_keys("haselko")

    def enter_invalid_username(self):
        """
        Enters invalid username
        """
        self.driver.find_element(*MyAccountPageLocators.USERNAME_INPUT).send_keys("test@test.pl")

    def click_login(self):
        """
        CLicks log in button
        """
        self.driver.find_element(*MyAccountPageLocators.LOG_IN_BUTTON).click()

    def login_button_text(self):
        """
        Checks if login button is presented
        :return: Login button text
        """
        self.wait_5s.until(EC.text_to_be_present_in_element(MyAccountPageLocators.LOG_IN_BUTTON, "Zaloguj się"))
        return self.driver.find_element(*MyAccountPageLocators.LOG_IN_BUTTON).text

    def get_alert_empty_password(self):
        """
        Waits maximum 5s for alert message and returns its text
        :return: password alert text
        """
        self.wait_5s.until(EC.text_to_be_present_in_element(MyAccountPageLocators.EMPTY_PASSWORD_ALERT, "Błąd: pole hasła jest puste."))
        return self.driver.find_element(*MyAccountPageLocators.EMPTY_PASSWORD_ALERT).text

    def get_alert_invalid_password(self):
        """
        Waits maximum 5s for alert message and return its text
        :return: password alert text
        """
        self.wait_5s.until(EC.text_to_be_present_in_element(MyAccountPageLocators.INVALID_PASSWORD_ALERT, "Błąd: dla adresu e-mail test_alk@test.pl podano nieprawidłowe hasło. Nie pamiętasz hasła?"))
        return self.driver.find_element(*MyAccountPageLocators.INVALID_PASSWORD_ALERT).text

    def get_alert_invalid_username(self):
        """
        Waits maximum 5s for alert message and returns its text
        :return: username alert text
        """
        self. wait_5s.until(EC.text_to_be_present_in_element(MyAccountPageLocators.INVALID_LOGIN_ALERT, "Nieznany adres e-mail. Proszę sprawdzić ponownie lub wypróbować swoją nazwę użytkownika."))
        return self.driver.find_element(*MyAccountPageLocators.INVALID_LOGIN_ALERT).text

    def get_alert_empty_username(self):
        """
        Waits maximum 5s for alert message and returns its text
        :return: username alert text
        """
        self.wait_5s.until(EC.text_to_be_present_in_element(MyAccountPageLocators.EMPTY_LOGIN_ALERT, "Błąd: Nazwa użytkownika jest wymagana."))
        return self.driver.find_element(*MyAccountPageLocators.EMPTY_LOGIN_ALERT).text

    def click_log_out(self):
        """
        Waits maximum 5s for log out button to be appeared and clicks it
        """
        self.wait_5s.until(EC.element_to_be_clickable(MyAccountPageLocators.LOG_OUT_LINK))
        self.driver.find_element(*MyAccountPageLocators.LOG_OUT_LINK).click()

    def welcome_text(self):
        """
        Waits maximum 5s for welcome text and returns its text
        :return: Welcome text
        """
        self.wait_5s.until(EC.text_to_be_present_in_element(MyAccountPageLocators.MY_ACCOUNT_TEXT, f"Witaj test_alk (nie jesteś test_alk? Wyloguj się)"))
        return self.driver.find_element(*MyAccountPageLocators.MY_ACCOUNT_TEXT).text