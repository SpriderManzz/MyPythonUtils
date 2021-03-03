import os
import configparser
from utils.get_path import PathUtil

rootPath = PathUtil().rootPath  # 路径类的类变量
config_path = os.path.join(rootPath, 'config.ini')  # 将路径进行拼接成F:\项目名称\config.ini

config = configparser.ConfigParser()#  实例化configParser对象
config.read(config_path, encoding='utf-8')


class ReadConfig():
    """
    获取配置文件的参数
    """

    def get_isRun(self, isRun):
        isRun = config.getint('EXCEL_LINE_INFO', isRun)
        return isRun

    def get_caseId(self, caseId):
        caseId = config.getint('EXCEL_LINE_INFO', caseId)
        return caseId

    def get_modelName(self, modelName):
        modelName = config.getint('EXCEL_LINE_INFO', modelName)
        return modelName

    def get_desc(self, desc):
        desc = config.getint('EXCEL_LINE_INFO', desc)
        return desc

    def get_url(self, url):
        url = config.getint('EXCEL_LINE_INFO', url)
        return url

    def get_requestMethod(self, requestMethod):
        requestMethod = config.getint('EXCEL_LINE_INFO', requestMethod)
        return requestMethod

    def get_header(self, header):
        header = config.getint('EXCEL_LINE_INFO', header)
        return header

    def get_caseDepend(self, caseDepend):
        caseDepend = config.getint('EXCEL_LINE_INFO', caseDepend)
        return caseDepend

    def get_dataDepend(self, dataDepend):
        dataDepend = config.getint('EXCEL_LINE_INFO', dataDepend)
        return dataDepend

    def get_fieldDepend(self, fieldDepend):
        fieldDepend = config.getint('EXCEL_LINE_INFO', fieldDepend)
        return fieldDepend

    def get_requestData(self, requestData):
        requestData = config.getint('EXCEL_LINE_INFO', requestData)
        return requestData

    def get_caseDepend(self, caseDepend):
        caseDepend = config.getint('EXCEL_LINE_INFO', caseDepend)
        return caseDepend

    def get_caseDepend(self, caseDepend):
        caseDepend = config.getint('EXCEL_LINE_INFO', caseDepend)
        return caseDepend

    def get_expectData(self, expectData):
        expectData = config.getint('EXCEL_LINE_INFO', expectData)
        return expectData

    def get_resultData(self, resultData):
        resultData = config.getint('EXCEL_LINE_INFO', resultData)
        return resultData

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


    #http://localhost:8773/get/with/headers1
    def get_base_url(self, protocol, domin, basepath, port):
        base_url = config.get('HTTP', protocol) + '://' + config.get('HTTP', domin) + ":" + config.get('HTTP', port)+config.get('HTTP', basepath)
        return base_url

    def get_smtpserver(self, smtpserver):
        smtpserver = config.get('EMAIL_INFO', smtpserver)
        return smtpserver

    def get_is_email(self,isemail):
        isemail = config.getboolean('EMAIL_INFO', isemail)
        return isemail

    def get_senduser(self,senduser):
        senduser = config.get('EMAIL_INFO', senduser)
        return senduser

    def get_password(self, password):
        password = config.get('EMAIL_INFO', password)
        return password

    def get_receive_user(self, receive_user):
        receive_user = config.get('EMAIL_INFO', receive_user)
        return receive_user




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






