from selenium import webdriver
from paths import *


class Browsers:

    CHROME = 'chrome'
    FIREFOX = 'ff'
    IE = 'ie'
    SAFARI = 'safari'


class DriverPath:
    CHROME = os.path.join(ROOT_DIR, 'selenium_driver', 'chromedriver')
    FIREFOX = os.path.join(ROOT_DIR, 'selenium_driver', 'geckodriver')


class DriverSetUp(object):

    @staticmethod
    def get_driver(browser):
        if browser == 'chrome': driver = webdriver.Chrome(executable_path=DriverPath.CHROME)
        elif browser in ['ff', 'firefox']: driver = webdriver.Firefox(executable_path=DriverPath.FIREFOX)
        elif browser == 'ie': driver = webdriver.Ie()
        elif browser == 'safari': driver = webdriver.Safari()
        else: driver = webdriver.Firefox()

        return driver






