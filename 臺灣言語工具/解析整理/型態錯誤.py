# -*- coding: utf-8 -*-
class 型態錯誤(TypeError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
