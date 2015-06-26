# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本元素.字 import 字


class 詞:
    內底字 = None

    def __init__(self, 字陣列=[]):
        try:
            self.內底字 = []
            for 字物件 in 字陣列:
                if not isinstance(字物件, 字):
                    raise 型態錯誤(
                        '字陣列內底有毋是字的：字陣列＝{0}，字物件＝{1}'.format(str(字陣列), str(字物件)))
                self.內底字.append(字(字物件.型, 字物件.音))
        except TypeError as 問題:
            raise 型態錯誤('傳入來的字陣列毋法度疊代：{0}，問題：{1}'
                       .format(str(字陣列), 問題))

    def __eq__(self, 別个):
        return isinstance(別个, 詞) and self.內底字 == 別个.內底字

    def __hash__(self):
        return hash(tuple(self.內底字))

    def __str__(self):
        return '詞：{0}'.format(self.內底字)

    def __repr__(self):
        return self.__str__()
