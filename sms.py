# -*- coding: utf-8 -*-
# @File    : sms.py
# @Author  : LVFANGFANG
# @Time    : 2019/1/5 0005 17:26
# @Desc    :

from twilio.rest import Client

from base import BaseMessage


class Message(BaseMessage):
    def __init__(self, account_sid, auth_token):
        '''
        :param account_sid: 
        :param auth_token:
        '''
        self.client = Client(account_sid, auth_token)
        self.msg_from = 'your_twilio_number'

    def send(self, to, body, subject=None):
        '''
        :param to: 收信人号码，中国的号码前面需要加+86
        :param body: 短信内容
        :param subject: 短信主题
        :return:
        '''
        message = self.client.messages.create(
            to=to,
            from_=self.msg_from,
            body=body)
        print('短信发送成功')
        return message.sid


if __name__ == '__main__':
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    sms = Message(account_sid,auth_token)
    sms.send('+86135xxxx8857','from python test')