# coding:utf-8
import requests
import json
import random
from random import randint
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

# get只有url是必填，params是选填参数

# 响应内容
# r.content 响应内容的字节码，一般处理二进制文件
# r.text 自动选择适当的编码，对r.content解码
# r.json() 解析json格式的数据，如果无法解析，则抛出异常
# url 请求的URL地址
# params GET请求参数
# data POST请求参数
# json 同样是POST请求参数，要求服务端接收json格式的数据
# headers 请求头字典
# cookies cookies信息（字典或CookieJar）
# files 上传文件
# auth HTTP鉴权信息
# timeout 等待响应时间，单位秒
# allow_redirects 是否允许重定向
# proxies 代理信息
# verify 是否校验证书
# stream 如果为False，则响应内容将直接全部下载
# cert 客户端证书地址
# 预期结果




def bm_get_int(n):
    """
    :param n: 指定长度随机数字
    :return:
    """
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def bm_get_str(randomlength):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str
print(bm_get_str(34))



"""
思路：循环读取每一个list元素，然后判断前面3个元素是否为'bm_'
"""


# for l in list:
#     print(l)
#     if (l.find('bm_', 0, -1)) != -1:
#         print(l[0:3])

#print(list[0:3])

list = ['bm_get_int()', 'bm_get_str()']
dict = {
        "userName": "bm_get_str(5)",
        "password": 123456,
        "age": "bm_get_int(3)",
        "type": "http"
       }
for key in dict.keys():  # 在dict的字典里遍历每个key
    if isinstance(dict[key], str):  # 判断每个key对应的value是否为str
        if 'bm_' in dict[key]:
            number = int(re.sub('\D', '', dict[key]))  # 获取目标字符的数字
            method = dict[key].split('(')[0] + "()"    # 完整方法名拼接
            if method == 'bm_get_int()':
                dict[key] = bm_get_int(number)
            elif method == 'bm_get_str()':
                dict[key] = bm_get_str(number)
print("调用方法修改后的dict："+str(dict))







req = requests.post('http://localhost:8882/ReturnYourJson', json=dict)
print(req.json())


