from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Locators for LOGIN PAGE"""
    LOGIN_BUTTON = (By.XPATH, "//input[@class='k-button k-primary']")
    PASSWORD_TEXTBOX = (By.XPATH, "//input[@id='password']")
    USERNAME_TEXTBOX = (By.XPATH, "//input[@id='username']")


class HomePageLocators:
    """ HomePage Locators - Main top user_menu links """

    DISCOVER_LINK = (By.XPATH,"//a[@href='/discover' and text()='Discover']")
    LOGIN_LINK = (By.XPATH, "//li//a[@href='/login' and text()='Login']")
    MOVIES_LINK =(By.XPATH,"//a[@href='/movie' and text()='Movies']")
    PEOPLE_LINK = (By.XPATH, "//a[@href='/person' and text()='People']")
    SEARCH_BAR_TEXTBOX = (By.XPATH,"//input[@id='search_v4']")
    SIGNUP_LINK = (By.XPATH, "//li//a[@href='/account/signup' and text()='Sign Up']")
    TV_SHOWS_LINK = (By.XPATH, "//a[@href='/tv' and text()='TV Shows']")
    PAGE_SUBTITLE_H2 = (By.XPATH,"//h2")


class ResultsPageLocators:
    RESULT_GRID = (By.XPATH, "//div[@class='flex']//a")
    RESULT_TITLE = (By.ID,"movie_results") # //h2[@id='movie_results']

