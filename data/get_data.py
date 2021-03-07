#coding:utf-8
import json
from data.config_data import *

# 循环的时候可以获取行号，然后列的话可以调用data_config
from utils.opera_excel import OperationExcel


# 该类实现获取Excel单元格方法的封装

class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    '''
    获取Excel的行数，也就是测试用例的case个数
    返回的是int类型
    '''
    def getCaseLines(self):
        return self.opera_excel.getLines()

    # 获取是否执行，如果运行flag赋值为True
    def getRunValue(self, row):
        flag = None
        runValue = self.opera_excel.getCellValue(row, isRunLine)
        if runValue == 'Y':
            flag = True
        else:
            flag = False
        return flag

    # 获取请求类型
    def getRequestMethodValue(self, row):
        request_method = self.opera_excel.getCellValue(row, requestMethodLine)
        return request_method

    # 判断header是否为空
    def getHeaderValue(self, row):
        headerValue = self.opera_excel.getCellValue(row, headerLine)

        if headerValue == '':
            return None
        else:
            headerValue = json.loads(headerValue)  # 转成json
            return headerValue

    # 获取url
    def getUrlValue(self, row):
        url = self.opera_excel.getCellValue(row, urlLine)
        return url

    # 获取请求数据
    def getDataValue(self, row):
        data = self.opera_excel.getCellValue(row, requestDataLine)
        if data == '':
            return None
        return data

    # 获取预期结果
    def getExpectValue(self, row):
        #col = int(data_config.getExpectLine())
        expect = self.opera_excel.getCellValue(row, expectDataLine)
        if expect == '':
            return None
        return expect

    def writeResultValue(self,row,vaule):
        #col = int(data_config.getResultLine())
        self.opera_excel.geteCellValue(row, resultDataLine, vaule)


if __name__ == '__main__':
    gd = GetData()
    # 测试获取行数方法
    print(gd.getCaseLines())




