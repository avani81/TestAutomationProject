import time

from libs.ui.pageobjects.base_page import BasePage, IncorrectPageException
from libs.ui.locators.locators import LoginPageLocators, ProductPageLocators, ProductDetailsPageLocators


class ProductListPage(BasePage):
    """Login page UI actions."""

    def __init__(self, driver):
        super(ProductListPage, self).__init__(driver)

    def _verify_page(self):
        """Verify login page is loaded.

        Raises:
            Incorrect Page Exception

        """
        try:
            ProductListPage.find_one_element(
                self, ProductPageLocators.PAGETITLE_LABEL)

        except BaseException:
            raise IncorrectPageException

    def click_product_onesie_details(self):
        self.click_button(wait_time=2, locator=ProductPageLocators.PRODUCT_ONE)
        time.sleep(1)

    def click_product_back_light_details(self):
        self.click_button(wait_time=2, locator=ProductPageLocators.PRODUCT_TWO)
        time.sleep(1)

    def add_products_to_cart(self):
        self.click_button(
            wait_time=2,
            locator=ProductPageLocators.PRODUCT_ONE_ADD_CART_BUTTON)
        self.click_button(
            wait_time=2,
            locator=ProductPageLocators.PRODUCT_TWO_ADD_CART_BUTTON)
        time.sleep(1)

    def click_view_cart(self):
        self.click_button(wait_time=2, locator=ProductPageLocators.CART_BUTTON)
        time.sleep(1)

    def get_cart_products(self):
        product_list = []
        self.find_one_element(locator=ProductPageLocators.PRODUCT_ONE)
        self.find_one_element(locator=ProductPageLocators.PRODUCT_TWO)
        product_text = self.get_text(ProductPageLocators.PRODUCT_ONE)
        print(product_text)
        product_list.append(product_text)
        product_text = self.get_text(ProductPageLocators.PRODUCT_TWO)
        print(product_text)
        product_list.append(product_text)
        return product_list

    def click_add_to_cart_product_detail_page(self):
        self.click_button(
            wait_time=1,
            locator=ProductDetailsPageLocators.ADD_TO_CART_BUTTON)
        time.sleep(2)
        self.click_button(
            wait_time=1,
            locator=ProductDetailsPageLocators.BACK_BUTTON)
