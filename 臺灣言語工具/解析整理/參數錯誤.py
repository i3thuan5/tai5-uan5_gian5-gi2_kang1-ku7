# -*- coding: utf-8 -*-
class 參數錯誤(TypeError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
