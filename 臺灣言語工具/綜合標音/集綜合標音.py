# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.綜合標音.詞組綜合標音 import 詞組綜合標音


class 集綜合標音():
    綜合詞組 = []

    def __init__(self, 字綜合標音型態, 集物件):
        self.綜合詞組 = []
        if not isinstance(集物件, 集):
            raise 型態錯誤('傳入來的毋是集物件！{0}，{1}'.format(type(集物件), str(集物件)))
        for 組物件 in 集物件.內底組:
            self.綜合詞組.append(詞組綜合標音(字綜合標音型態, 組物件))

    def 轉json格式(self):
        return [標音.轉json格式() for 標音 in self.綜合詞組]

    def __eq__(self, 別个):
        return isinstance(別个, 集綜合標音) and self.綜合詞組 == 別个.綜合詞組
