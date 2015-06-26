# -*- coding: utf-8 -*-
class 解析錯誤(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
