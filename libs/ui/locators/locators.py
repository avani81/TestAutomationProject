from selenium.webdriver.common.by import By


class TestSite:
    URL = "https://www.saucedemo.com/"


class LoginPageLocators:
    """Locators for LOGIN PAGE"""
    USERNAME_TEXTBOX = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_TEXTBOX = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "#login_button_container > div > form > input.login-button")
    LOGIN_ERROR_TEXT = (By.CLASS_NAME, 'error-button')


class ProductPageLocators:
    """ Product list page locators """
    CART_BUTTON = (By.ID, 'shopping_cart_container')
    MENU_BUTTON = (
        By.CSS_SELECTOR,
        "#menu_button_container > div > div:nth-child(3) > div > button")

    PRODUCT_LABEL = (By.CSS_SELECTOR, "#inventory_filter_container > div")
    PAGETITLE_LABEL = (By.CSS_SELECTOR, "#header_container > div.header_label")

    PRODUCT_ONE = (
        By.XPATH,
        "//div[contains(., 'Sauce Labs Onesie') and @class='inventory_item_name']")
    PRODUCT_TWO = (
        By.XPATH,
        "//div[contains(., 'Sauce Labs Bike Light') and @class='inventory_item_name']")
    PRODUCT_ONE_ADD_CART_BUTTON = (
        By.CSS_SELECTOR,
        "#inventory_container > div > div:nth-child(5) > div.pricebar > button")
    PRODUCT_TWO_ADD_CART_BUTTON = (
        By.CSS_SELECTOR,
        "#inventory_container > div > div:nth-child(2) > div.pricebar > button")


class ProductDetailsPageLocators:
    """ Product details Page locators"""
    ADD_TO_CART_BUTTON = (
        By.CSS_SELECTOR,
        "#inventory_item_container > div > div > div > button")
    BACK_BUTTON = (By.CSS_SELECTOR, '#inventory_item_container > div > button')
