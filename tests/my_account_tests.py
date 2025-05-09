from tests.base_test import BaseTest

class MyAccountTest(BaseTest):
    """
    Test class for verifying user login functionality on the My Account page
    """
    def setUp(self):
        """
        Sets up the test environment before each test by navigating to the My Account page
        """
        super().setUp()
        self.my_account_page = self.home_page.click_my_account()


    def testEmptyPassword(self):
        """
        Tests submitting the login form without entering a password
        Verifies that an appropriate empty password alert is displayed
        """
        self.my_account_page.enter_username_login()
        self.my_account_page.click_login()
        self.assertEqual("Błąd: pole hasła jest puste.", self.my_account_page.get_alert_empty_password())

    def testEmptyUsername(self):
        """
        Tests submitting the login form without entering a username
        Verifies that an appropriate empty username alert is displayed
        """
        self.my_account_page.enter_password_login()
        self.my_account_page.click_login()
        self.assertEqual("Błąd: Nazwa użytkownika jest wymagana.", self.my_account_page.get_alert_empty_username())

    def testInvalidPassword(self):
        """
        Tests submitting the login form with an invalid password
        Verifies that an appropriate invalid password alert is displayed
        """
        self.my_account_page.enter_username_login()
        self.my_account_page.enter_invalid_password()
        self.my_account_page.click_login()
        self.assertEqual("Błąd: dla adresu e-mail test_alk@test.pl podano nieprawidłowe hasło. Nie pamiętasz hasła?", self.my_account_page.get_alert_invalid_password())

    def testInvalidUsername(self):
        """
        Tests submitting the login form with an invalid username
        Verifies that an appropriate invalid username alert is displayed
        """
        self.my_account_page.enter_invalid_username()
        self.my_account_page.enter_password_login()
        self.my_account_page.click_login()
        self.assertEqual("Nieznany adres e-mail. Proszę sprawdzić ponownie lub wypróbować swoją nazwę użytkownika.", self.my_account_page.get_alert_invalid_username())

    def testValidLogin(self):
        """
        Tests logging in with valid credentials
        Verifies that the welcome text is displayed
        """
        self.my_account_page.enter_username_login()
        self.my_account_page.enter_password_login()
        self.my_account_page.click_login()
        # Check if welcome text is presented
        self.assertEqual("Witaj test_alk (nie jesteś test_alk? Wyloguj się)", self.my_account_page.welcome_text())

    def testLogOut(self):
        """
        Tests logging out after a successful login
        Verifies that the 'Log in' button text is displayed
        """
        self.my_account_page.enter_username_login()
        self.my_account_page.enter_password_login()
        self.my_account_page.click_login()
        self.my_account_page.click_log_out()
        #Check if Log in button is presented
        self.assertEqual("Zaloguj się", self.my_account_page.login_button_text())


