# -*- coding: utf-8 -*-
# @File    : mail.py
# @Author  : LVFANGFANG
# @Time    : 2019/1/5 0005 16:52
# @Desc    :

import smtplib
from email.header import Header
from email.mime.text import MIMEText

from base import BaseMessage


class Email(BaseMessage):
    def __init__(self, mail_from, hostname, user, password):
        self.mail_from = mail_from
        self.hostname = hostname
        self.user = user
        self.password = password

    def send(self, to, body, subject):
        '''
        :param to: 收件人邮箱 列表
        :param body: 邮件内容
        :param subject: 邮件主题
        :return:
        '''
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['From'] = self.mail_from
        msg['To'] = ';'.join(to)
        msg['Subject'] = Header(subject, 'utf-8')

        server = smtplib.SMTP_SSL(self.hostname)
        server.login(self.user, self.password)
        server.sendmail(self.mail_from, to, msg.as_string())
        server.quit()


if __name__ == '__main__':
    email = Email('mailfrom@163.com', 'smtp.163.com', 'user', 'password')
    email.send('发送邮件', 'python 自动发送，请勿回复', ['mailto1@qq.com', 'mailto2@163.com'])
