# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.基本元素.公用變數 import 分字符號
from 臺灣言語工具.基本元素.公用變數 import 分詞符號
from 臺灣言語工具.基本元素.公用變數 import 無音
from 臺灣言語工具.基本元素.公用變數 import 分型音符號


class 章:
    內底句 = None

    def __init__(self, 句陣列=[]):
        try:
            self.內底句 = []
            for 句物件 in 句陣列:
                if not isinstance(句物件, 句):
                    raise 型態錯誤(
                        '句陣列內底有毋是句的：句陣列＝{0}，句物件＝{1}'.format(str(句陣列), str(句物件)))
                self.內底句.append(句(句物件.內底集))
        except TypeError as 問題:
            raise 型態錯誤('傳入來的句陣列毋法度疊代：{0}，問題：{1}'
                       .format(str(句陣列), 問題))

    def __eq__(self, 別个):
        return isinstance(別个, 章) and self.內底句 == 別个.內底句

    def __str__(self):
        return '章：{0}'.format(self.內底句)

    def __repr__(self):
        return self.__str__()

    def 看型(self, 物件分字符號='', 物件分詞符號='', 物件分句符號=''):
        句的型 = []
        for 一句 in self.內底句:
            句的型.append(一句.看型(物件分字符號, 物件分詞符號))
        return 物件分句符號.join(句的型)

    def 看音(self, 物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        句的音 = []
        for 一句 in self.內底句:
            音標 = 一句.看音(物件分字符號, 物件分詞符號)
            if 音標 != 無音:
                句的音.append(音標)
        return 物件分句符號.join(句的音)

    def 看分詞(self, 物件分型音符號=分型音符號,
            物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        句的音 = []
        for 一句 in self.內底句:
            音標 = 一句.看分詞(物件分型音符號, 物件分字符號, 物件分詞符號)
            if 音標 != 無音:
                句的音.append(音標)
        return 物件分句符號.join(句的音)

    def 篩出字物件(self):
        字陣列 = []
        for 句物件 in self.內底句:
            字陣列.extend(句物件.篩出字物件())
        return 字陣列