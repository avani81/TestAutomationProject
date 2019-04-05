

from libs.ui.pageobjects.home_page import HomePage
from tests.ui.base_ui_test import BaseUITestCase

class MoviedbTests(BaseUITestCase):

    def setUp(self):
        print("Test Setup")
        # Setup- Load Test_site in browser
        super(MoviedbTests, self).setUp()
        self.url_site = self.automationConfig.parser.get('UI', 'test_site')
        self.browser.get(self.url_site)



    def test_main_page_load(self):
        """
        Test case  - Validate main page for themoviedb site is loaded and page title and url
        Steps
        1. Load test_site from configurations
        2. Validate page title with expected title and home page object with discover element on page
        3. Validate page url
        """
        home_page = HomePage(self.browser) # This will validate one menubar link element in __init()
        page_title = HomePage.get_page_title(home_page)
        expected_title = 'The Movie Database (TMDb)'
        self.assertEqual(page_title,expected_title,msg="Page title not matched")
        self.assertEqual(home_page.get_page_url(),"https://www.themoviedb.org/",msg="current url doesn't match")
        print("Test {} completed".format(self.__str__()))

    def test_main_page_discover_menu(self):
        """
        Test case  - Validate Discover menu link is click able and loads discover page
        Steps
        1. Load test_site from configurations
        2. Click on DISCOVER link
        2. Validate page title with expected title
        3. Validate page url
        """
        home_page = HomePage(self.browser)
        home_page.click_menu_discover()
        self.assertIn("Discover New Movies",home_page.get_page_title(),msg="Page title not matched")
        self.assertIn("Discover New Movies & TV Shows",home_page.get_menu_subtitle_text(),
                         msg="Discover page subtitle does not match")
        self.assertEqual(home_page.get_page_url(), "https://www.themoviedb.org/discover/movie")
        # Note - This test can be enhanced by adding new Page object of Discover page and sub items validation

    def test_main_page_movies_menu(self):
        """
        Test case  - Validate MOVIES menu link is click able and loads Popular movies page
        Steps
        1. Load test_site from configurations
        2. Click on MOVIES link
        2. Validate page title with expected title
        3. Validate page sub-title and  page url
        """
        home_page = HomePage(self.browser)
        home_page.click_menu_movies()
        self.assertIn("Popular Movies",home_page.get_page_title(),msg="Page title not matched")
        self.assertEqual(home_page.get_menu_subtitle_text(),"Popular Movies",
                         msg="Discover page subtitle does not match")
        self.assertEqual(home_page.get_page_url(),"https://www.themoviedb.org/movie")
        # Note - This test can be enhanced by adding new Page object of Movies page and sub-items validation

    def test_main_page_people_menu(self):
        "TODO - Add test to validate people menu"
        pass

    def test_main_page_tvshows_menu(self):
        "TODO - Add test to validate tv Show menu"
        pass

    def test_main_page_people_signup(self):
        "TODO - Add test to validate people menu"
        pass



    def tearDown(self):
        # Test Teardown
        super(MoviedbTests, self).tearDown()
        self.browser.quit()






