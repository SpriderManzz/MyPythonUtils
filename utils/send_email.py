# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from data.config_data import smtpserver, senduser, password, receive_user_list


class SendEmail:

    def send_mail(self, user_list, sub, content):
        user = "张三" + "<" + senduser + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub  # 定义标题
        message['From'] = user  # 发送人
        message['To'] = ";".join(user_list)  # 接收人
        server = smtplib.SMTP()
        server.connect(smtpserver)
        server.login(senduser, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)
        sub = "接口自动化测试报告"
        content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" % (
        count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_mail(receive_user_list, sub, content)


if __name__ == '__main__':
    sen = SendEmail()
    sen.send_main([1, 2, 3, 4], [2, 3, 4, 5, 6, 7])
