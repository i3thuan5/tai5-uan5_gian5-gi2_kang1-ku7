# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.基本元素.公用變數 import 分字符號
from 臺灣言語工具.基本元素.公用變數 import 分詞符號
from 臺灣言語工具.基本元素.公用變數 import 無音
from 臺灣言語工具.基本元素.公用變數 import 分型音符號


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

    def 看型(self, 物件分字符號='', 物件分詞符號='', 物件分句符號=''):
        集的型 = []
        for 一集 in self.內底集:
            集的型.append(一集.看型(物件分字符號, 物件分詞符號))
        return 物件分詞符號.join(集的型)

    def 看音(self, 物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        集的音 = []
        for 一集 in self.內底集:
            音標 = 一集.看音(物件分字符號, 物件分詞符號)
            if 音標 != 無音:
                集的音.append(音標)
        return 物件分詞符號.join(集的音)

    def 看分詞(self, 物件分型音符號=分型音符號,
            物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        集的音 = []
        for 一集 in self.內底集:
            音標 = 一集.看分詞(物件分型音符號, 物件分字符號, 物件分詞符號)
            if 音標 != 無音:
                集的音.append(音標)
        return 物件分詞符號.join(集的音)

    def 篩出字物件(self):
        字陣列 = []
        for 集物件 in self.內底集:
            字陣列.extend(集物件.篩出字物件())
        return 字陣列

    def 網出詞物件(self):
        詞陣列 = []
        for 集物件 in self.內底集:
            詞陣列.extend(集物件.網出詞物件())
        return 詞陣列
