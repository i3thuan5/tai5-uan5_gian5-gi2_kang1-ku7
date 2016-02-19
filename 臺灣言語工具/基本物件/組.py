# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.基本物件.公用變數 import 分字符號
from 臺灣言語工具.基本物件.公用變數 import 分詞符號
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.基本物件.公用變數 import 分型音符號
from 臺灣言語工具.基本物件.功能 import 功能


class 組(功能):
    內底詞 = None

    def __init__(self, 詞陣列=[]):
        # 愛產生新的物件
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

    def 看型(self, 物件分字符號='', 物件分詞符號='', 物件分句符號=''):
        詞的型 = []
        for 一詞 in self.內底詞:
            詞的型.append(一詞.看型(物件分字符號, 物件分詞符號))
        return 物件分詞符號.join(詞的型)

    def 看音(self, 物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        詞的音 = []
        for 一詞 in self.內底詞:
            音標 = 一詞.看音(物件分字符號, 物件分詞符號)
            if 音標 != 無音:
                詞的音.append(音標)
        return 物件分詞符號.join(詞的音)

    def 看分詞(self, 物件分型音符號=分型音符號,
            物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        詞的音 = []
        for 一詞 in self.內底詞:
            音標 = 一詞.看分詞(物件分型音符號, 物件分字符號, 物件分詞符號)
            if 音標 != '':
                詞的音.append(音標)
        return 物件分詞符號.join(詞的音)

    def 綜合標音(self, 語言綜合標音):
        詞組綜合標音 = {}
        for 一詞 in self.內底詞:
            for 欄位, 內容 in 一詞.綜合標音(語言綜合標音)[0].items():
                try:
                    詞組綜合標音[欄位].append(內容)
                except:
                    詞組綜合標音[欄位] = [內容]
        結果 = {}
        for 欄位, 內容 in 詞組綜合標音.items():
            結果[欄位] = ' '.join(內容)
        return [結果]

    def 篩出字物件(self):
        字陣列 = []
        for 詞物件 in self.內底詞:
            字陣列.extend(詞物件.篩出字物件())
        return 字陣列

    def 網出詞物件(self):
        return self.內底詞

    def 轉音(self, 音標工具, 函式='預設音標'):
        # 逐个函式攏愛產生新的物件
        新組物件 = 組()
        for 詞物件 in self.內底詞:
            新組物件.內底詞.append(詞物件.轉音(音標工具, 函式))
        return 新組物件
