#coding:utf-8
import xlrd
from xlutils.copy import copy

# data = xlrd.open_workbook('../cases/case.xls')
# tables = data.sheets()[0]
#
# print(tables.nrows)# 打印行数
# print(tables.cell_value(2,3))# 第二行第三列的数据


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../cases/case.xls'
            self.sheet_id = 0
        self.SheetValue = self.getSheetValue()

    # 获取sheets的内容
    def getSheetValue(self):
        data = xlrd.open_workbook(self.file_name)
        SheetValue = data.sheets()[self.sheet_id]
        return SheetValue

    # 获取单元格的行数
    def getLines(self):
        lines = self.SheetValue
        return lines.nrows

    # 获取某一个单元格的内容
    def getCellValue(self, row, col):
        return self.SheetValue.cell_value(row, col)

    # 获取实际结果单元格的数据,并写进去
    def geteCellValue(self, row, col, value):
        readData = xlrd.open_workbook(self.file_name)  # 每次操作前需要打开并复制一次不然为空
        writeData = copy(readData)
        sheetData = writeData.get_sheet(0)
        sheetData.write(row, col, value)
        writeData.save(self.file_name)

    # 根据对应的caseid 找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)  # 行号
        rows_data = self.get_row_values(row_num)  # 行内容
        return rows_data

    # 根据对应的caseid找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num = num + 1

    # 根据行号，找到该行的内容
    def get_row_data(self, row):
        tables = self.data
        row_data = tables.row_values(row)  # 根据号获取行的内容，这就是行的内容了
        return row_data

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)  # 获取列的内容
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':

    opers = OperationExcel()
    # 测试get_lines
    print(opers.getLines())

    # 测试get_cell_value
    print(opers.getCellValue(0,0))