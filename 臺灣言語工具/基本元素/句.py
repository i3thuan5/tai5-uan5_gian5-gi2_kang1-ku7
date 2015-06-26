# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本元素.集 import 集


class 句:
    內底集 = None

    def __init__(self, 集陣列=[]):
        try:
            self.內底集 = []
            for 集物件 in 集陣列:
                if not isinstance(集物件, 集):
                    raise 型態錯誤(
                        '集陣列內底有毋是集的：集陣列＝{0}，集物件＝{1}'.format(str(集陣列), str(集物件)))
                self.內底集.append(集(集物件.內底組))
        except TypeError as 問題:
            raise 型態錯誤('傳入來的集陣列毋法度疊代：{0}，問題：{1}'
                       .format(str(集陣列), 問題))

    def __eq__(self, 別个):
        return isinstance(別个, 句) and self.內底集 == 別个.內底集

    def __str__(self):
        return '句：{0}'.format(self.內底集)

    def __repr__(self):
        return self.__str__()
