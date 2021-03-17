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
        self.data_dic = {}

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
                if isinstance(data[key], str):  # 判断每个key对应的value是否为str,如果是str才处理，而且还要看看是不是bm_开头的
                    if 'bm_get' in data[key]:
                        number = self.commonUtil.get_method_num(data[key])  # 获取用户输入的数字
                        var_name = data[key].split(',')[1][:-1]  # 获取用户定义的的变量名
                        method = data[key].split('(')[0] + "()"  # 完整方法名拼接
                        if method == 'bm_get_int()':
                            data[key] = self.commonUtil.bm_get_int(number)
                            self.data_dic[var_name] = data[key]  # 定义大字典的key值
                        elif method == 'bm_get_str()':
                            data[key] = self.commonUtil.bm_get_str(number)
                            self.data_dic[var_name] = data[key]# 定义大字典的key值
                        """如果是get類型才這樣處理"""
                    data = json.dumps(data)# 转成字符串
                    self.data_dic['req_data'] = data  # 处理完后追加到大的字典中
                    data = json.loads(data)# 再次把data从字符串变回去字典
                    if 'bm_set' in data[key]:
                        set_var_name = data[key].split('(')[1][:-1]  # 获取set函数的变量名
                        if set_var_name in self.data_dic.keys():
                            data[key] = self.data_dic[set_var_name]
                    data = json.dumps(data)  # 转成字符串
                    self.data_dic['req_data'] = data  # 处理完后追加到大的字典中
                    data = json.loads(data)  # 再次把data从字符串变回去字典
            return json.loads(self.data_dic['req_data'])
        return  None
    def getExpectValue(self, row):
        """
        因为在测试用例一般都是双引号的，所以目前采用json.loads()来处理
        """
        expect = self.opera_excel.getCellValue(row, expectDataLine).replace(" ", "").replace('\n', '')
        # 这里容易报错,返回结果的key必须要是""的格式
        expect = json.loads(expect)# 字符串形式的数据转化为字典,但是字典是单引号
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




