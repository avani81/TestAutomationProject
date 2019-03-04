

import os
import os.path

from configparser import ConfigParser

class AutomationConfig:
    """
        Class used to configure Automation properties
        Note  - This class can be enhance to read different environments i.e. Staging , QA , development etc
    """

    def __init__(self):
        self.parser = ConfigParser()
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        self.config_dir = BASE_DIR + '/../tests/config'
        self.config_file = 'automation_configs.ini'
        self.config_file_path = self.config_dir + '/' + self.config_file
        self.parser.read(self.config_file_path)

    def get_config_test(self):
        print(self.parser.get('Keys','api_key'))


# if __name__ == '__main__':
#     AutomationConfig().get_config_test()
#     print(AutomationConfig().parser.get('System','base_url'))