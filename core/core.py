import os
import unittest

import sys
from abc import abstractmethod

import pytest
import allure
from allure.constants import AttachmentType

from container import AllureWrapper, Context
from inspection import attach_screenshot_to_failed_tc
from driver_setup import Browsers
from driver_setup import DriverSetUp
from utiles.excel_parser import Excel


class CoreSetUp(unittest.TestCase):

    BROWSER = None

    @classmethod
    def setUpClass(cls, browser, url, excel_path=None, *args, **kwargs):
        cls.__set_excel_path(excel_path)

        if browser is None: return cls
        CoreSetUp.BROWSER = browser
        Context.Excel.excel_data = Excel.get_excel_data('dev', 'LOGIN')
        cls.driver = DriverSetUp.get_driver(browser)
        cls.driver.get(url)

    def setUp(self, *args, **kwargs):
        pass

    @attach_screenshot_to_failed_tc
    def tearDown(self, screenshot=True, *args, **kwargs):
        pass

    @classmethod
    def tearDownClass(cls, *args, **kwargs):
        if CoreSetUp.BROWSER is None: return cls
        cls.driver.quit()

    def allure_screenshot(self):
        allure.MASTER_HELPER.attach('Screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)

    @classmethod
    def __set_excel_path(cls, excel_path):
        if excel_path is not None: Context.Excel.excel_path = excel_path
        else: Context.Excel.excel_path = os.path.join(Context.Path.ROOT_DIR, 'files', 'sample_excel_file.xlsx')


if __name__ == '__main__':
    unittest.main()
