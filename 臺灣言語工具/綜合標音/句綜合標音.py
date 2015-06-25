# -*- coding: utf-8 -*-
from 臺灣言語工具.綜合標音.集綜合標音 import 集綜合標音
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.基本元素.章 import 章


class 句綜合標音():
    綜合集 = []

    def __init__(self, 字綜合標音型態, 章句物件):
        self.綜合集 = []
        if isinstance(章句物件, 句):
            句物件 = 章句物件
            for 集物件 in 句物件.內底集:
                self.綜合集.append(集綜合標音(字綜合標音型態, 集物件))
        elif isinstance(章句物件, 章):
            章物件 = 章句物件
            for 句物件 in 章物件.內底句:
                for 集物件 in 句物件.內底集:
                    self.綜合集.append(集綜合標音(字綜合標音型態, 集物件))
        else:
            raise 型態錯誤('傳入來的毋是句或章物件！{0}，{1}'.format(type(章句物件), str(章句物件)))

    def 轉json格式(self):
        return [標音.轉json格式() for 標音 in self.綜合集]

    def __eq__(self, 別个):
        return isinstance(別个, 句綜合標音) and self.綜合集 == 別个.綜合集
