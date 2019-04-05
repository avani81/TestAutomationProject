import unittest


from libs.ui.pageobjects.home_page import HomePage
from tests.ui.base_ui_test import BaseUITestCase


class MovieDBSiteTests(BaseUITestCase):

    def setUp(self):
        super(MovieDBSiteTests, self).setUp()
        self.url_site = self.automationConfig.parser.get('UI', 'test_site')
        self.browser.get(self.url_site)

    def test_search_movie_title(self):
        """
        Test Case - Test Search functionality for movies by title and validate results
        """
        home_page = HomePage(self.browser)
        # Note - This following data(movie_title,partial_title can be read from
        # dataprovider or file to provide more movie range so
        # that same test method can be used for multiple titles
        movie_title = "The Matrix"
        partial_title  = "matrix"
        home_page.enter_text_search_box(search_query=movie_title)
        text = self.browser.find_element_by_id("movie_results").text # TODO - can be added to page method
        self.assertIn("Movie Results",text,msg="result doesn't match")
        # Validate 1 st place result for actual movie
        titles = home_page.get_search_result_titles()
        self.assertEqual(titles[0],movie_title.lower(),msg="Incorrect movie result found in first place")
        # Validate other titles include matrix in title
        for name in titles:
            if partial_title in name:
                print("partial text {} found in title {}".format(partial_title,name))
            else:
                print("partial text {} not found in title {}".format(partial_title,name))

    def test_search_tv_show_title(self):
        """
        Test Case - Test Search functionality for TV shows by title and validate results
        """
        home_page = HomePage(self.browser)
        # Note - This following data(movie_title,partial_title can be read from
        # data provider or file to provide more movie range so
        # that same test method can be used for multiple titles
        tv_title = "The Office"
        partial_title = "office"
        home_page.enter_text_search_box(search_query=tv_title)
        text = self.browser.find_element_by_id("tv_results").text  # TODO - can be added to page method
        self.assertIn("TV Show Results", text, msg="result doesn't match")
        # Validate 1 st place result for actual movie
        titles = home_page.get_search_result_titles()
        self.assertEqual(titles[0], tv_title.lower(), msg="Incorrect movie result found in first place")
        # Validate other titles include matrix in title
        for name in titles:
            if partial_title in name:
                print("partial text {} found in title {}".format(partial_title, name))
            else:
                print("partial text {} not found in title {}".format(partial_title, name))


    def test_search_people_title(self):
        pass



    def tearDown(self):
        super(MovieDBSiteTests,self).tearDown()

