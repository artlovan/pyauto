import unittest

import sys
from abc import abstractmethod

import pytest
import allure
from allure.constants import AttachmentType

from container import AllureWrapper
from inspection import attach_screenshot_to_failed_tc
from driver_setup import Browsers
from driver_setup import DriverSetUp


class CoreSetUp(unittest.TestCase):

    @classmethod
    def setUpClass(cls, browser, url, *args, **kwargs):
        cls.driver = DriverSetUp.get_driver(browser)
        cls.driver.get(url)

    def setUp(self, *args, **kwargs):
        pass

    @attach_screenshot_to_failed_tc
    def tearDown(self, screenshot=True, *args, **kwargs):
        pass

    @classmethod
    def tearDownClass(cls, *args, **kwargs):
        cls.driver.quit()

    def allure_screenshot(self):
        allure.MASTER_HELPER.attach('Screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)


if __name__ == '__main__':
    unittest.main()
