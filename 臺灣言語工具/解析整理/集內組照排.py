# -*- coding: utf-8 -*-
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤


class 集內組照排:

    @classmethod
    def 排(cls, 排法, 物件):
        if isinstance(物件, 集):
            return cls._排好集物件(排法, 物件)
        if isinstance(物件, 句):
            return cls._排好句物件(排法, 物件)
        if isinstance(物件, 章):
            return cls._排好章物件(排法, 物件)
        raise 型態錯誤('傳入來的毋是集句章其中一種物件：{0}，{1}'
                   .format(type(物件), str(物件)))

    @classmethod
    def _排好集物件(cls, 排法, 集物件):
        if not isinstance(集物件, 集):
            raise 型態錯誤('傳入來的毋是集物件：{0},{1}'
                       .format(type(集物件), str(集物件)))
        排好集 = 集()
        排好集.內底組 = sorted(集物件.內底組, key=排法)
        return 排好集

    @classmethod
    def _排好句物件(cls, 排法, 句物件):
        if not isinstance(句物件, 句):
            raise 型態錯誤('傳入來的毋是句物件：{0},{1}'
                       .format(type(句物件), str(句物件)))
        集陣列 = []
        for 一集 in 句物件.內底集:
            集陣列.append(cls._排好集物件(排法, 一集))
        排好句 = 句()
        排好句.內底集 = 集陣列
        return 排好句

    @classmethod
    def _排好章物件(cls, 排法, 章物件):
        if not isinstance(章物件, 章):
            raise 型態錯誤('傳入來的毋是章物件：{0},{1}'
                       .format(type(章物件), str(章物件)))
        句陣列 = []
        for 一句 in 章物件.內底句:
            句陣列.append(cls._排好句物件(排法, 一句))
        排好章 = 章()
        排好章.內底句 = 句陣列
        return 排好章
