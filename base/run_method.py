#coding:utf-8
import requests
from data.config_data import base_url
import json
from utils.log import Logger

url_log = Logger('UrlForWrite:').get_logger()
method_log = Logger('method:').get_logger()
header_log = Logger('header:').get_logger()
data_log = Logger('req_data:').get_logger()
status_log = Logger('status:').get_logger()
res_log = Logger("response:").get_logger()


class RunMethod:
    """
    封装get和post请求
    调用run_main函数会传递method,url,但是data和header有可能为空
    """
    def post_main(self, url, data, header=None):
        res = None
        """
        进行数据处理：将data的str类型变成dict(json)
        """


        if header != None:
            res = requests.post(url=url, json=data, headers=header)
        else:
            res = requests.post(url=url, json=data)
        return res

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data={}, headers=header)
        else:
            res = requests.get(url=url, params=data)
        return res

    def run_main(self, method, url, data=None, header=None):
        url = base_url+url  # 如果Excel测试数据url路径想用完整的URL注释此行即可
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
        elif method == 'get':
            res = self.get_main(url, data, header)
        else:
            print("暂时只支持post和get,请检查参数！")
        url_log.info(url)  # 输出请求URL
        method_log.info(method)
        header_log.info(header)
        data_log.info(data)
        status_log.info(res.status_code)  # 输出请求状态码
        res_log.info(res.text)


        return res


if __name__ == '__main__':
    pass
"""  知识补充
    r.encoding               #获取当前的编码
    r.encoding = 'utf-8'     #设置编码
    r.text                   #以encoding解析返回内容。字符串方式的响应体，会自动根据响应头部的字符编码进行解码。
    r.content                #以字节形式（二进制）返回。字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩。
    r.headers                #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
    r.status_code            #响应状态码
    r.raw                    #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read()   
    r.ok                     #查看r.ok的布尔值便可以知道是否登陆成功
    特殊方法
    r.json()                 #Requests中内置的JSON解码器，以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常
    r.raise_for_status()     #失败请求(非200响应)抛出异常
"""


