#coding=utf-8
from utils.read_config import ReadConfig
"""
    调用readConfig从配置文件获取配置文件中的参数
"""

#   Excel用例的列号
isRunLine = ReadConfig().get_isRun('isRun')
caseIdLine = ReadConfig().get_caseId('caseId')
modelNameLine = ReadConfig().get_modelName('modelName')
descLine = ReadConfig().get_desc('desc')
urlLine = ReadConfig().get_url('url')
requestMethodLine = ReadConfig().get_requestMethod('requestMethod')
headerLine = ReadConfig().get_header('header')
caseDependLine = ReadConfig().get_caseDepend('caseDepend')
dataDependLine = ReadConfig().get_dataDepend('dataDepend')
fieldDependLine = ReadConfig().get_fieldDepend('fieldDepend')
requestDataLine = ReadConfig().get_requestData('requestData')
expectDataLine = ReadConfig().get_expectData('expectData')
resultDataLine = ReadConfig().get_resultData('resultData')


#   HTTP协议相关
protocol = ReadConfig().get_protocol('protocol')
domin = ReadConfig().get_domin('domin')
basepath = ReadConfig().get_basepath('basepath')
port = ReadConfig().get_port('port')
base_url = protocol + '://' + domin + ':' + port + basepath


#   邮箱相关
smtpserver =ReadConfig().get_smtpserver('smtpserver')
isemail = ReadConfig().get_is_email('isemail')
senduser = ReadConfig().get_senduser('senduser')
password =ReadConfig().get_password('password')
receive_user = ReadConfig().get_receive_user('receive_user')
receive_user_list = receive_user.strip(',').split(',') # 字符串转变成list列表
