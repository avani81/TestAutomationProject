import time


from libs.ui.pageobjects.base_page import BasePage, IncorrectPageException
from libs.ui.locators.locators import LoginPageLocators, HomePageLocators , ResultsPageLocators

from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    """ MovieDB Home/Main page UI actions."""

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def _verify_page(self):
        """Verify main page is loaded.

        Raises:
            Incorrect Page Exception

        """
        try:
            HomePage.find_one_element(self, HomePageLocators.DISCOVER_LINK)

        except BaseException:
            raise IncorrectPageException

    def enter_text_search_box(self,search_query):
        # library method to enter search query for movie titles , show titles and people
        self.enter_text(HomePageLocators.SEARCH_BAR_TEXTBOX, search_query + Keys.RETURN)
        time.sleep(3)  # adding temporarily


    def click_menu_discover(self):
        self.click_button(2, HomePageLocators.DISCOVER_LINK)

    def click_menu_movies(self):
        self.click_button(2, HomePageLocators.MOVIES_LINK)

    def click_menu_tv_shows(self):
        self.click_button(2, HomePageLocators.TV_SHOWS_LINK)

    def click_menu_people(self):
        self.click_button(2,HomePageLocators.PEOPLE_LINK)

    def click_login_menu(self):
        self.click_button(2, HomePageLocators.LOGIN_LINK)
        return self.driver

    def click_signup_menu(self):
        self.click_button(2, HomePageLocators.SIGNUP_LINK)

    def get_menu_subtitle_text(self):
        return self.get_text(HomePageLocators.PAGE_SUBTITLE_H2)

    def get_search_result_titles(self):
        # Method to get search result for titles
        result_list = self.find_all_elements(ResultsPageLocators.RESULT_GRID)
        title_list =[]
        for item in result_list:
            # print(item.get_property('title'))
            title_list.append(item.get_property('title').lower())
        return title_list




