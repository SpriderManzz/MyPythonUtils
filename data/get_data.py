#coding:utf-8
import json


# 循环的时候可以获取行号，然后列的话可以调用data_config
from utils.opera_excel import OperationExcel
from data import data_config
from utils.opera_json import OperationJson

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
        col = int(data_config.getIsRunLine()) # 获取列号，因为getIsRun()返回字符串所以需要强制转型为int
        runValue = self.opera_excel.getCellValue(row,col)
        if runValue == 'Y':
            flag = True
        else:
            flag = False
        return flag

    # 获取请求类型
    def getRequestMethodValue(self, row):
        col = int(data_config.getRquestMethodLine())
        request_method = self.opera_excel.getCellValue(row, col)
        return request_method

    #
    # 判断header是否为空
    def getHeaderValue(self, row):
        col = int(data_config.getHeaderLine())# Excel表的header列行数

        headerValue = self.opera_excel.getCellValue(row, col)

        if headerValue == '':
            return None
        else:
            headerValue = json.loads(headerValue)# 转成json
            return headerValue

    # 获取url
    def getUrlValue(self, row):
        col = int(data_config.getUrlLine())
        url = self.opera_excel.getCellValue(row, col)
        return url

    # 获取请求数据
    def getDataValue(self, row):
        col = int(data_config.getDataLine())
        data = self.opera_excel.getCellValue(row, col)
        if data == '':
            return None
        return data

    # # 通过获取关键字拿到data数据
    # def get_data_for_json(self, row):
    #     opera_json = OperationJson()
    #     request_data = opera_json.get_data(self.get_request_data(row))
    #     return request_data

    # 获取预期结果
    def getExpectValue(self, row):
        col = int(data_config.getExpectLine())
        expect = self.opera_excel.getCellValue(row, col)
        if expect == '':
            return None
        return expect


    def writeResultValue(self,row,vaule):
        col = int(data_config.getResultLine())
        self.opera_excel.geteCellValue(row, col, vaule)



if __name__ == '__main__':
    gd = GetData()

    # 测试获取行数方法
    print(gd.getCaseLines())




