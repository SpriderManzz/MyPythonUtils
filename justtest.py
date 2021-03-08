# coding:utf-8
import requests
import json

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
expected = {'username': 'kaishui',
            "token": "bm_exist()"}
# 实际结果
result = {
    'code': 1,
    'username': 'kaishui',
    'token': 'ihbedvbwejhvkjvberkjvbkjgkesjvbbje'
}


def assert_dict(expected,result):
    flag = None
    for key in expected:
        if (key in result):
            if result[key] == expected[key]:
                flag = True
            elif expected[key] == "bm_exist()":
                flag = True
            else:
                flag = False
                break
        else:
            print('响应结果无该字段,请检查')
    return flag

res = assert_dict(expected, result)
if res:
    print("测试通过")
else:
    print("测试不通过")


