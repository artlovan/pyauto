from core.core import *


@pytest.mark.sampletest
class SampleTests(CoreSetUp):

    url = 'https://www.amazon.com/'

    @classmethod
    def setUpClass(cls, browser=Browsers.CHROME, url=url, *args, **kwargs):
        super(SampleTests, cls).setUpClass(browser, url, *args, **kwargs)

    def setUp(self, *args, **kwargs):
        super(SampleTests, self).setUp(*args, **kwargs)

    @classmethod
    def tearDownClass(cls, *args, **kwargs):
        super(SampleTests, cls).tearDownClass(*args, **kwargs)

    def tearDown(self, *args, **kwargs):
        super(SampleTests, self).tearDown(*args, **kwargs)

    def test_my_first_test(self):
        pass

