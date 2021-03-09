#coding:utf-8
import re
import json
import random
from random import randint
from data.config_data import *
from utils.common_util import CommonUtil


# 循环的时候可以获取行号，然后列的话可以调用data_config
from utils.opera_excel import OperationExcel


# 该类实现获取Excel单元格方法的封装

class GetData:
    def __init__(self):
        self.commonUtil = CommonUtil()
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
        if runValue == 'y':
            runValue = runValue.upper()
        if runValue == 'Y':
            flag = True
        else:
            flag = False
        return flag

    # 获取请求类型值
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
        data = self.opera_excel.getCellValue(row, requestDataLine).replace(" ", "").replace('\n', '')
        if data != '':
            data = json.loads(data)
            for key in data.keys():  # 在dict的字典里遍历每个key
                if isinstance(data[key], str):  # 判断每个key对应的value是否为str
                    if 'bm_' in data[key]:
                        number = int(re.sub('\D', '', data[key]))  # 获取目标字符的数字
                        method = data[key].split('(')[0] + "()"  # 完整方法名拼接
                        if method == 'bm_get_int()':
                            data[key] = self.commonUtil.bm_get_int(number)
                        elif method == 'bm_get_str()':
                            data[key] = self.commonUtil.bm_get_str(number)
        else:
            return None
        return data

    # 获取预期结果
    def getExpectValue(self, row):
        """
        因为在测试用例一般都是双引号的，所以目前采用json.loads()来处理
        """
        expect = self.opera_excel.getCellValue(row, expectDataLine).replace(" ", "").replace('\n', '')
        expect = json.loads(expect)# 字符串形式的数据转化为字典,但是字典是单引号
        #eval(expect)
        if expect == '':
            return None
        return expect

    # 写入数据到实际结果列
    def writeResultValue(self, row, vaule):
        self.opera_excel.geteCellValue(row, resultDataLine, vaule)


if __name__ == '__main__':
    gd = GetData()
    # 测试获取行数方法
    print(gd.getCaseLines())




