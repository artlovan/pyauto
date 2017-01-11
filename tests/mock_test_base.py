import unittest

from core.container import MockContext


class MockTestBase(unittest.TestCase):

    def setUp(self, *args, **kwargs): pass

    @classmethod
    def tearDownClass(cls, *args, **kwargs): pass

    @classmethod
    def setUpClass(cls, *args, **kwargs):
        MockContext.MOCK_ACTIVATE = True

    def tearDown(self, screenshot=True, *args, **kwargs): pass


if __name__ == '__main__':
    unittest.main()
