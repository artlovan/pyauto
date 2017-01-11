from pprint import pprint

import os
import unittest
import pytest

from core.container import Context
from paths import ROOT_DIR
from tests.mock_test_base import MockTestBase
from utiles.excel_parser import Excel


@pytest.mark.unittest
@pytest.mark.excel_parser
class ExcelParser(MockTestBase):

    @classmethod
    def setUpClass(cls, *args, **kwargs):
        super(ExcelParser, cls).setUpClass(*args, **kwargs)
        Context.Excel.excel_path = os.path.join(ROOT_DIR, 'files', 'sample_excel_file.xlsx')
        cls.excel = Excel.get_excel_data('dev', 'LOGIN')

    def test_something(self):
        expected_excel = {
            u'first_name': u'Dan',
            u'last_name': u'Phil',
            u'price': 12.0,
            u'product': u'kindle',
            u'pop': 222.0,
            u'run_TAB': u'',
            u'KEY': u'run',
            u'date': u'tomorrow',
            u'data_TAB': u'new_tab',
            u'wow': 111.0,
            u'initials': u'DP'
        }
        self.assertEqual(self.excel, expected_excel)


if __name__ == '__main__':
    unittest.main()
