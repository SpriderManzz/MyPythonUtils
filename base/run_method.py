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
response_time_log = Logger("response_time:").get_logger()

class RunMethod:
    """
    封装get和post请求
    调用run_main函数会传递method,url,但是data和header有可能为空
    """
    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            #url,data,json
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
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
        response_time_log.info(res.elapsed.total_seconds())  # 接口响应时间(单位s)

        return res


if __name__ == '__main__':
    pass



