import time

from libs.ui.pageobjects.base_page import BasePage, IncorrectPageException
from libs.ui.locators.locators import LoginPageLocators, ProductPageLocators


class LoginPage(BasePage):
    """Login page UI actions."""

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def _verify_page(self):
        """Verify login page is loaded.

        Raises:
            Incorrect Page Exception

        """
        try:
            LoginPage.find_one_element(self, LoginPageLocators.LOGIN_BUTTON)

        except BaseException:
            raise IncorrectPageException

    def enter_username(self, username):
        """Enter username for login

        Args:
            username: The username of the account.

        """
        self.enter_text(LoginPageLocators.USERNAME_TEXTBOX, username)

    def enter_password(self, password):
        self.enter_text(LoginPageLocators.PASSWORD_TEXTBOX, password)

    def login_user(self, username, password):
        """Login with username and password.

        Args:
            username: The username of account.
            password: The password of the account.

        Returns:
            The browser driver instance currently using.

        """
        self.enter_text(LoginPageLocators.USERNAME_TEXTBOX, username)
        self.enter_text(LoginPageLocators.PASSWORD_TEXTBOX, password)
        self.click_login()
        return self.driver

    def click_login(self):
        self.wait_for_element_visibility(5, LoginPageLocators.LOGIN_BUTTON)
        self.click_button(3, LoginPageLocators.LOGIN_BUTTON)
        time.sleep(2)
        return self.driver

    def click_product_one(self):
        # ProductListPage.move_to_element(self,locator=ProductPageLocators.PRODUCT_ONE)
        print("in here")
        #self.click_on_text("Sauce Labs Onesie")
        # ProductListPage.wait_for_element_visibility(self,locator=ProductPageLocators.PRODUCT_ONE)

        self.click_button(wait_time=2, locator=ProductPageLocators.MENU_BUTTON)
        time.sleep(6)
        print("in here 1")
