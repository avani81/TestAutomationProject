import unittest

from libs.ui.locators.locators import TestSite, ProductPageLocators
from libs.ui.pageobjects.login_page import LoginPage
from libs.ui.pageobjects.product_list_page import ProductListPage

from tests.ui.base_ui_test import BaseUITestCase


class ProductCartTests(BaseUITestCase):

    def setUp(self):
        super(ProductCartTests, self).setUp()
        self.browser.get(TestSite.URL)
        self.log.printStep("site loaded")
        self.login_page = LoginPage(self.browser)
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.product_list = ProductListPage(self.login_page.click_login())

    def test_add_to_cart_from_product_list(self):
        """
            Test 1 - Test to validate add to cart from Product list view
            Setup - Login with standard_user
            Test Steps -
            1. Add 2 products(Sauce Labs Onesie, Sauce Labs Bike Light) to cart from product list
            2. Click and go to Cart
            Test Verification - Verify added products found in cart list
        """
        self.product_list.add_products_to_cart()
        self.product_list.click_view_cart()
        self.product_list.find_one_element(
            locator=ProductPageLocators.PRODUCT_ONE)
        self.product_list.find_one_element(
            locator=ProductPageLocators.PRODUCT_TWO)
        product_text = self.product_list.get_text(
            ProductPageLocators.PRODUCT_ONE)
        expected_products = ['Sauce Labs Onesie', 'Sauce Labs Bike Light']
        self.assertIn(product_text, expected_products, msg="Product not found")
        product_text = self.product_list.get_text(
            ProductPageLocators.PRODUCT_TWO)
        self.assertIn(product_text, expected_products, msg="Product not found")

    def test_add_to_cart_from_product_details(self):
        """
            Test 2 - Test to validate products can be added to cart form product detail page
            Setup - Login with standard_user
            Test Steps -
            1. Click on product "Sauce Labs Onesie" and go to detail page
            2. Click on Add to cart button and go back to product list
            3. Click on product "Sauce Labs Bike Light' and go to detail page
            4. Click on Add to cart button and go back to product list
            5. Go to Cart view
            Test Verification - Verify above added products found in cart list
            (Note and Enhancement - More assert and detail verifcation can be added with step 2 and step 4 to
            check correct product detail is viewed on click)
        """
        self.product_list.click_product_onesie_details()
        self.product_list.click_add_to_cart_product_detail_page()
        self.product_list.click_product_back_light_details()
        self.product_list.click_add_to_cart_product_detail_page()
        self.product_list.click_view_cart()
        product_text = self.product_list.get_text(
            ProductPageLocators.PRODUCT_ONE)
        expected_products = ['Sauce Labs Onesie', 'Sauce Labs Bike Light']
        self.assertIn(product_text, expected_products, msg="Product not found")
        product_text = self.product_list.get_text(
            ProductPageLocators.PRODUCT_TWO)
        self.assertIn(product_text, expected_products, msg="Product not found")

    # MORE TESTS CAN BE ADDED IF TIME PERMITS
    def test_remove_product_from_cart(self):
        # TODO
        pass

    def test_remove_product_from_cart_in_product_page(self):
        # TODO
        pass

    def test_update_product_qty_cart(self):
        # TODO
        pass

    def test_add_all_products_to_cart(self):
        # TODO
        pass

    def tearDown(self):
        super(ProductCartTests, self).tearDown()
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
