import time

from libs.ui.pageobjects.home_page import HomePage
from libs.ui.pageobjects.login_page import LoginPage
from tests.ui.base_ui_test import BaseUITestCase


class UserLoginTests(BaseUITestCase):

    def setUp(self):
        print("Test Setup")
        # Setup- Load Test_site in browser
        super(UserLoginTests, self).setUp()
        self.url_site = self.automationConfig.parser.get('UI', 'test_site')
        self.username = self.automationConfig.parser.get('UI','username')
        self.password = self.automationConfig.parser.get('UI','password')
        self.browser.get(self.url_site)



    def test_login_valid_username(self):
        """
        Test case  - Validate registered user can login successfully for moviedb site
        Steps
        1. Load test_site from configurations
        2. Click on login link
        3. Add valid username
        4. Add valid password
        5. Click on Login button
        6. Validate Successful login and control goes to user profile page - verify URL
        Note - more validation for user profile page can be added and control as enhancement
        """
        home_page = HomePage(self.browser) # This will validate one menubar link element in __init()
        login_page = LoginPage(home_page.click_login_menu())
        login_page.login_user(self.username,self.password)
        page_url = login_page.get_page_url()
        self.assertIn(self.username,page_url,msg="invalid user profile page")


    ## Note -  More tests can be added for this test suite - Following are test defination
    # def test_login_with_invalid_username(self):
    #     pass
    #
    # def test_login_with_invalid_password(self):
    #     pass
    #
    # def test_login_with_invalid_username_password(self):
    #     pass
    #
    # def test_login_with_blank_fields(self):
    #     pass
    #
    # def test_login_with_inactive_user_account(self):
    #     pass

    def tearDown(self):
        super(UserLoginTests,self).tearDown()