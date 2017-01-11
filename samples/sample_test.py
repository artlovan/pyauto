from core.core import *


@pytest.mark.sampletest
class SampleTests(CoreSetUp):

    URL = 'https://www.python.org/'

    @classmethod
    def setUpClass(cls, browser=Browsers.CHROME, url=URL, *args, **kwargs):
        super(SampleTests, cls).setUpClass(browser, url, *args, **kwargs)

    def setUp(self, *args, **kwargs):
        super(SampleTests, self).setUp(*args, **kwargs)

    @classmethod
    def tearDownClass(cls, *args, **kwargs):
        super(SampleTests, cls).tearDownClass(*args, **kwargs)

    def tearDown(self, screenshot=True, *args, **kwargs):
        super(SampleTests, self).tearDown(screenshot, *args, **kwargs)

    def test_my_first_test(self):
        pass

