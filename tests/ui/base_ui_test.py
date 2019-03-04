import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from libs.utils.config_management import AutomationConfig
from libs.utils.custom_logger import CustomLogger


class BaseUITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        CustomLogger.printStep("Class Setup")
        cls.log = CustomLogger()
        cls.automationConfig = AutomationConfig()
        cls.browser = cls.automationConfig.parser.get('Browser', 'browser')

    def setUp(self):
        CustomLogger.printStep("Test Setup Started - Launching browser ")
        test_browser = self.browser
        if test_browser == "firefox":
            firefox_capabilities = DesiredCapabilities.FIREFOX
            firefox_capabilities['marionette'] = True
            self.browser = webdriver.Firefox(
                capabilities=firefox_capabilities,
                executable_path="/usr/local/bin/geckodriver")
        elif test_browser == "chrome":
            self.browser = webdriver.Chrome()
        else:
            raise Exception(
                "Invalid browser selected - Supported browsers: Firefox, Chrome")
        self.browser.fullscreen_window()
        self.browser.implicitly_wait(4)

    def tearDown(self):
        CustomLogger.printStep("In Test Teardown method")
        self.browser.quit()

    @classmethod
    def tearDownClass(cls):
        CustomLogger.printStep("In Class Teardown")


# if __name__ == '__main__':
#     unittest.main()
