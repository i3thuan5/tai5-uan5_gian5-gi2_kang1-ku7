# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本元素.句 import 句


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
