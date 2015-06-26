# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本元素.詞 import 詞


class 組:
    內底詞 = None

    def __init__(self, 詞陣列=[]):
        try:
            self.內底詞 = []
            for 詞物件 in 詞陣列:
                if not isinstance(詞物件, 詞):
                    raise 型態錯誤(
                        '詞陣列內底有毋是詞的：詞陣列＝{0}，詞物件＝{1}'.format(str(詞陣列), str(詞物件)))
                self.內底詞.append(詞(詞物件.內底字))
        except TypeError as 問題:
            raise 型態錯誤('傳入來的詞陣列毋法度疊代：{0}，問題：{1}'
                       .format(str(詞陣列), 問題))

    def __eq__(self, 別个):
        return isinstance(別个, 組) and self.內底詞 == 別个.內底詞

    def __hash__(self):
        return hash(tuple(self.內底詞))

    def __str__(self):
        return '組：{0}'.format(self.內底詞)

    def __repr__(self):
        return self.__str__()
