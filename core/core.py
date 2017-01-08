import unittest
import pytest
import allure
from driver_setup import Browsers
from driver_setup import DriverSetUp


class CoreSetUp(unittest.TestCase):

    @classmethod
    def setUpClass(cls, browser, url, *args, **kwargs):
        cls.driver = DriverSetUp.get_driver(browser)
        cls.driver.get(url)

    def setUp(self, *args, **kwargs):
        pass

    def tearDown(self, *args, **kwargs):
        pass

    @classmethod
    def tearDownClass(cls, *args, **kwargs):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
