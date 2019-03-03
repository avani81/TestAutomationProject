import unittest

from libs.ui.locators.locators import TestSite, LoginPageLocators, ProductPageLocators
from libs.ui.pageobjects.login_page import LoginPage
from libs.ui.pageobjects.product_list_page import ProductListPage

from tests.ui.base_ui_test import BaseUITestCase


class SiteMainTests(BaseUITestCase):

    def setUp(self):

        super(SiteMainTests, self).setUp()
        self.browser.get(TestSite.URL)
        self.log.printStep("site loaded")

    def test_verify_page_load_01(self):
        """
        Test Description - Load Site and verify UI elements found and displayed
        Test Steps - 1. Load Test Site in setup
        Test Verification -Verify Page title , username , password text boxes and login button on main page displayed
        """
        login_page = LoginPage(self.browser)
        page_title = LoginPage.get_page_title(login_page)
        self.assertEqual(
            "Swag Labs",
            page_title,
            msg="Page title does not match")
        login_page.find_one_element(locator=LoginPageLocators.USERNAME_TEXTBOX)
        login_page.find_one_element(locator=LoginPageLocators.PASSWORD_TEXTBOX)
        login_page.find_one_element(locator=LoginPageLocators.LOGIN_BUTTON)
        self.log.printStep("Elements Verified on Page load")

    def test_login_standard_user(self):
        """
            Test Description - Test to validate login with standard_user
            Test Steps -
            1. Load the site
            2. Enter Username and Password in text boxes
            3. Click on Login button and control goes to product_list(inventory) page
            Test Verification
            On successful login control goes to Product page with _init and _verify_page of Product List

        """
        login_page = LoginPage(self.browser)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        ProductListPage(login_page.click_login())

    # MORE TESTS CAN BE ADDED IF TIME PERMITS
    def test_login_locked_out_user(self):
        # TODO
        pass

    def test_login_locked_problem_user(self):
        # TODO
        pass

    def test_login_locked_performance_glitch_user(self):
        # TODO
        pass

    def test_logout(self):
        # TODO
        pass

    def test_invalid_login_input_scenarios(self):
        # TODO
        pass

    def tearDown(self):
        super(SiteMainTests, self).tearDown()
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
