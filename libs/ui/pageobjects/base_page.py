import time
from abc import abstractmethod

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Base page object for common UI actions and element access."""

    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    @abstractmethod
    def _verify_page(self):
        """  This method verifies that we are on the correct page. """
        return

    def click_button(self, wait_time, locator):
        """ allows to click any element - button or links """
        self.wait_until_element_clickable(
            wait_time,
            locator.__getitem__(0),
            locator.__getitem__(1)).click()

    def click_button_with_sleep(self, wait_time, locator):
        """ allows to click any element - button or links """
        time.sleep(wait_time)
        self.wait_until_element_clickable(
            wait_time,
            locator.__getitem__(0),
            locator.__getitem__(1)).click()

    def click_on_text(self, text):
        self.driver.find_element_by_link_text(text).click()

    def enter_text(self, locator, text):
        """ general method to enter text by locator (from locators.py) - no need to specify locator type
            locator.__getitem__(0) - is locator type i.e. xpath , name , id
            locator.__getitem__(1) - is locator value based on locator type
        """
        try:
            self.driver.find_element(
                locator.__getitem__(0),
                locator.__getitem__(1)).clear()
            self.driver.find_element(
                locator.__getitem__(0),
                locator.__getitem__(1)).send_keys(text)
        except NoSuchElementException as e:
            raise e

    def find_one_element(self, locator):
        return self.driver.find_element(
            locator.__getitem__(0), locator.__getitem__(1))

    def find_all_elements(self, locator):
        return self.driver.find_elements(
            locator.__getitem__(0), locator.__getitem__(1))

    def get_page_title(self):
        return self.driver.title

    def get_text(self, locator):
        value = self.wait_for_element_visibility(2, locator).text
        return value

    def move_to_element(self, locator):
        try:
            el = self.find_one_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", el)
            time.sleep(2)
        except NoSuchElementException as e:
            self.log.printDebug("ERROR " + e.msg)  # Log
            raise

    def wait_until_element_clickable(self, wait_time, locator_type, locator):
        """ Explicit wait for element with defined wait time """
        try:
            element = WebDriverWait(self.driver, wait_time). \
                until(EC.element_to_be_clickable((locator_type, locator)))
            return element
        except (NoSuchElementException, TimeoutException) as e:
            self.log.printDebug("ERROR " + e.msg)
            raise

    def wait_for_element_visibility(self, wait_time, locator):
        """ Explicit wait for element till visible with defined wait time """
        while True:
            try:
                element = WebDriverWait(
                    self.driver, wait_time). until(
                    EC.visibility_of_element_located(
                        (locator.__getitem__(0), locator.__getitem__(1))))
                return element
            except(TimeoutError, NoSuchElementException) as e:
                print("ERROR " + e.msg)
                raise
            except StaleElementReferenceException:
                time.sleep(0.1)


class IncorrectPageException(Exception):
    """This exception is raised when we try to instantiate the wrong page."""
    pass
