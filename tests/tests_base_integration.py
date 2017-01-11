import unittest

from core.core import CoreSetUp


class TestBase(CoreSetUp):

    def setUp(self, *args, **kwargs):
        super(TestBase, self).setUp(*args, **kwargs)

    @classmethod
    def tearDownClass(cls, *args, **kwargs):
        super(TestBase, cls).tearDownClass(*args, **kwargs)

    @classmethod
    def setUpClass(cls, browser=None, url=None, excel_path=None, *args, **kwargs):
        super(TestBase, cls).setUpClass(browser, url, excel_path, *args, **kwargs)

    def tearDown(self, screenshot=True, *args, **kwargs):
        super(TestBase, self).tearDown(screenshot, *args, **kwargs)


if __name__ == '__main__':
    unittest.main()
