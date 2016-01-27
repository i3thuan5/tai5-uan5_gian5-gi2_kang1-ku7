# -*- coding: utf-8 -*-
from 臺灣言語工具.基本元素.公用變數 import 無音
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.基本元素.公用變數 import 標點符號
from 臺灣言語工具.基本元素.公用變數 import 分字符號
from 臺灣言語工具.基本元素.公用變數 import 分詞符號
from 臺灣言語工具.基本元素.公用變數 import 分型音符號


class 字:
    型 = None
    音 = None

    def __init__(self, 型, 音=無音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        try:
            音.__iter__
        except:
            raise 型態錯誤('傳入來的音毋是字串佮字串對：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '':
            raise 解析錯誤('傳入來的型是空的！')
        self.型 = 型
        self.音 = 音

    def 有音(self):
        return self.音 != 無音 and self.音 not in 標點符號

    def __eq__(self, 別个):
        return isinstance(別个, 字) and self.型 == 別个.型 and self.音 == 別个.音

    def __hash__(self):
        return hash((self.型, self.音))

    def __str__(self):
        return '字：{0} {1}'.format(self.型, self.音)

    def __repr__(self):
        return self.__str__()

    def 看型(self, 物件分字符號='', 物件分詞符號='', 物件分句符號=''):
        return self.型

    def 看音(self, 物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        return self.音

    def 看分詞(self, 物件分型音符號=分型音符號,
            物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        if self.音 == 無音:
            return self.看型(物件分字符號, 物件分詞符號)
        return self.看型( 物件分字符號, 物件分詞符號) + 物件分型音符號\
            + self.看音(物件分字符號, 物件分詞符號)
