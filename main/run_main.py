# coding:utf-8
import sys
sys.path.append("F:\MyPythonUtils")# 手动加入项目路径
from base.run_method import RunMethod
from data.get_data import GetData
from utils.common_util import CommonUtil
from utils.send_email import SendEmail
from data.config_data import isemail



class RunTest:
    def __init__(self):
        self.runMethod = RunMethod()
        self.data = GetData()
        self.comUtil = CommonUtil()
        self.senEmail = SendEmail()

    # 程序执行
    def goOnRun(self):
        res = None
        passCount = []  # 定义成功个数，用列表，然后调用append方法即可累加，然后len()出长度
        failedCount = []
        rowsCount = self.data.getCaseLines()  # rowsCount整型，Excel的行数
        for row in range(1, rowsCount):  # 从第二行开始
            print(row)
            try:
                runValue = self.data.getRunValue(row)
                if runValue:
                    url = self.data.getUrlValue(row)
                    method = self.data.getRequestMethodValue(row)
                    run = self.data.getRunValue(row)
                    data = self.data.getDataValue(row)
                    header = self.data.getHeaderValue(row) # 此时已经是dict
                    expect = self.data.getExpectValue(row)
                    if run:
                        res = self.runMethod.run_main(method, url, data, header)
                        if self.comUtil.is_contain(expect, res.json()):
                            self.data.writeResultValue(row, 'pass')
                            passCount.append(row)
                        else:
                            self.data.writeResultValue(row, res.text)  # 错误的信息写进去
                            failedCount.append(row)
            except Exception as e:
                print("something error ", e)
        if isemail:
            self.senEmail.send_main(passCount, failedCount)

        print("成功用例数为：" + str(len(passCount)))
        print("失败用例数为：" + str(len(failedCount)))

if __name__ == '__main__':
    run = RunTest()
    run.goOnRun()





