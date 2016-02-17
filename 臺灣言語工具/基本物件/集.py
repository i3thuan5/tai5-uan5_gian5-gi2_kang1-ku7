# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.組 import 組
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.基本物件.公用變數 import 分字符號
from 臺灣言語工具.基本物件.公用變數 import 分詞符號
from 臺灣言語工具.基本物件.公用變數 import 分型音符號
from 臺灣言語工具.基本物件.功能 import 功能


class 集(功能):
    內底組 = None

    def __init__(self, 組陣列=[]):
        # 愛產生新的物件
        try:
            self.內底組 = []
            for 組物件 in 組陣列:
                if not isinstance(組物件, 組):
                    raise 型態錯誤(
                        '組陣列內底有毋是組的：組陣列＝{0}，組物件＝{1}'.format(str(組陣列), str(組物件)))
                self.內底組.append(組(組物件.內底詞))
        except TypeError as 問題:
            raise 型態錯誤('傳入來的組陣列毋法度疊代：{0}，問題：{1}'
                       .format(str(組陣列), 問題))

    def __eq__(self, 別个):
        return isinstance(別个, 集) and self.內底組 == 別个.內底組

    def __str__(self):
        return '集：{0}'.format(self.內底組)

    def __repr__(self):
        return self.__str__()

    def 看型(self, 物件分字符號='', 物件分詞符號='', 物件分句符號=''):
        if len(self.內底組) == 0:
            raise 解析錯誤('內底組是空的！！')
        if len(self.內底組) > 1:
            raise 解析錯誤('內底組毋焦一个！！{0}'.format(str(self)))
        return self.內底組[0].看型(物件分字符號, 物件分詞符號)

    def 看音(self, 物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        if len(self.內底組) == 0:
            raise 解析錯誤('內底組是空的！！')
        if len(self.內底組) > 1:
            raise 解析錯誤('內底組毋焦一个！！{0}'.format(str(self)))
        return self.內底組[0].看音(物件分字符號, 物件分詞符號)

    def 看分詞(self, 物件分型音符號=分型音符號,
            物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        if len(self.內底組) == 0:
            raise 解析錯誤('內底組是空的！！')
        if len(self.內底組) > 1:
            raise 解析錯誤('內底組毋焦一个！！{0}'.format(str(self)))
        return self.內底組[0].看分詞(物件分型音符號, 物件分字符號, 物件分詞符號)

    def 綜合標音(self, 語言綜合標音):
        try:
            return self.內底組[0].綜合標音(語言綜合標音)
        except:
            return [{}]

    def 篩出字物件(self):
        if len(self.內底組) == 0:
            return []
        if len(self.內底組) > 1:
            raise 解析錯誤('內底組毋焦一个！！{0}'.format(str(self)))
        return self.內底組[0].篩出字物件()

    def 網出詞物件(self):
        if len(self.內底組) == 0:
            return []
        if len(self.內底組) > 1:
            raise 解析錯誤('內底組毋焦一个！！{0}'.format(str(self)))
        return self.內底組[0].網出詞物件()

    def 轉音(self, 音標工具, 函式='預設音標'):
        # 逐个函式攏愛產生新的物件
        新集物件 = 集()
        for 組物件 in self.內底組:
            新集物件.內底組.append(組物件.轉音(音標工具, 函式))
        return 新集物件
