import os
import configparser
from utils.get_path import PathUtil

rootPath = PathUtil().rootPath  # 路径类的类变量
config_path = os.path.join(rootPath, 'config.ini')  # 将路径进行拼接成F:\项目名称\config.ini
#  实例化configParser对象
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')


class ReadConfig():
    """
    获取配置文件的参数
    """


    def get_protocol(self, protocol):
        protocol = config.get('HTTP', protocol)
        return protocol

    def get_domin(self, domin):
        domin = config.get('HTTP', domin)
        return domin

    def get_basepath(self, basepath):
        basepath = config.get('HTTP', basepath)
        return basepath

    def get_port(self, port):
        port = config.get('HTTP', port)
        return port

    def get_smtpserver(self, smtpserver):
        smtpserver = config.get('EMAIL_INFO', smtpserver)
        return smtpserver

    #http://localhost:8773/get/with/headers1
    def get_base_url(self, protocol, domin, basepath, port):
        base_url = config.get('HTTP', protocol) + '://' + config.get('HTTP', domin) + ":" + config.get('HTTP', port)+config.get('HTTP', basepath)
        return base_url

    def get_is_email(self,isemail):
        isemail = config.getboolean('EMAIL_INFO', isemail)
        return isemail

#   可以写成一个模块(get_base_url.py)来提供调用，暂不这样实现
protocol = ReadConfig().get_protocol('protocol')
domin = ReadConfig().get_domin('domin')
basepath = ReadConfig().get_basepath('basepath')
port = ReadConfig().get_port('port')
base_url = protocol + '://' + domin + ':' + port + basepath


# 邮箱相关
smtpserver =ReadConfig().get_smtpserver('smtpserver')
isemail =ReadConfig().get_is_email('isemail')




if __name__ == '__main__':
    # -sections得到所有的section，并以列表的形式返回
    print('sections:', config.sections())
    # 获取某section的所有option
    print('options:',  config.options('EMAIL_INFO'))
    # 获取某section的所有键值对
    print('items:', config.items('HTTP'))
    # 获取section中option的值，返回为string类型
    print('get:', config.get('HTTP', 'domin'))

    print('getint:', config.getint('JUST_TEST', 'id'))
    print('getfloat:', config.getfloat('JUST_TEST', 'weight'))
    print('getboolean:', config.getboolean('JUST_TEST', 'isChoice'))



    print('HTTP中的protocol值为:', ReadConfig().get_protocol('protocol'))
    print('HTTP中的domin值为:', ReadConfig().get_domin('domin'))
    print('HTTP中的basepath值为:', ReadConfig().get_basepath('basepath'))
    print('HTTP中的port值为:', ReadConfig().get_port('port'))
    print('HTTP中的baseurl值为:', ReadConfig().get_base_url('protocol', 'domin', 'basepath', 'port'))



