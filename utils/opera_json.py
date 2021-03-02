#coding=utf-8

import json
from utils.get_path import *
"""
基础语法
fp = open("../cases/login.json")
data = json.load(fp)
print(data['login'])
"""

class OperationJson:
    def __init__(self):
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open("../cases/login.json") as fp:
            data = json.load(fp)
            return data

    # 根据关键字读取数据
    def get_data(self,id):
        return self.data[id]


if __name__ == '__main__':
    #进行测试
    oj = OperationJson()

    print(oj.read_data())# 原字典
    print(type(oj.get_data('info')))
    print(oj.get_data('info')) # 字典关键字的值
    # 变成json
    val = oj.get_data('info')
    val_js = json.dumps(val, sort_keys=True, indent=4, separators=(',', ':'))
    print(val_js)



