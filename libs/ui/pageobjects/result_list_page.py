import time

from libs.ui.pageobjects.base_page import BasePage, IncorrectPageException
from libs.ui.locators.locators import LoginPageLocators,ResultsPageLocators


class ResultListPage(BasePage):
    """Result page UI actions. TODO - implementation as time permits"""

    def __init__(self, driver):
        super(ResultListPage, self).__init__(driver)

    def _verify_page(self):
        """Verify result page is loaded.

        Raises:
            Incorrect Page Exception

        """
        try:
            ResultListPage.find_one_element(
                self, ResultsPageLocators.RESULT_TITLE)

        except BaseException:
            raise IncorrectPageException


