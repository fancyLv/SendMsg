# -*- coding: utf-8 -*-
# @File    : base.py
# @Author  : LVFANGFANG
# @Time    : 2019/1/5 0005 16:49
# @Desc    :

class BaseMessage:
    def send(self, subject, body, to):
        raise NotImplementedError
