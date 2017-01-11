import xlrd as xlrd

from core.container import Context


class Excel(object):
    KEY = 'KEY'
    TAB = '_TAB'

    @staticmethod
    def get_excel_data(key, sheet):
        workbook = xlrd.open_workbook(Context.Excel.excel_path)
        excel = {}
        return Excel.__collect_data(key, sheet, workbook.sheets(), excel)

    @staticmethod
    def __collect_data(key, sheet, sheets, excel):
        for s in sheets:
            for cell_values in s.__dict__['_cell_values']:
                if cell_values[0] == key:
                    excel.update(dict(zip(s.__dict__['_cell_values'][0], cell_values)))
                    temp_excel = dict(zip(s.__dict__['_cell_values'][0], cell_values))
                    for c in temp_excel.keys():
                        if Excel.TAB in c: Excel.__collect_data(c.replace(Excel.TAB, ''), excel[c], sheets, excel)
        return excel
