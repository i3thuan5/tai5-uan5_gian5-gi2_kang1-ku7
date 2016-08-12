# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.基本物件.公用變數 import 分字符號
from 臺灣言語工具.基本物件.公用變數 import 分詞符號
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.基本物件.公用變數 import 分型音符號
from 臺灣言語工具.基本物件.功能 import 功能


class 詞(功能):
    內底字 = None

    def __init__(self, 字陣列=[]):
        # 愛產生新的物件
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

    def 看型(self, 物件分字符號='', 物件分詞符號='', 物件分句符號=''):
        字的型 = []
        for 一字 in self.內底字:
            字的型.append(一字.看型(物件分字符號, 物件分詞符號, 物件分句符號))
        return 物件分字符號.join(字的型)

    def 看音(self, 物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        字的音 = self._提著詞物件的字物件音陣列(物件分字符號, 物件分詞符號)
        攏有音 = []
        for 音標 in 字的音:
            if 音標 != 無音:
                攏有音.append(音標)
        return 物件分字符號.join(攏有音)

    def _提著詞物件的字物件音陣列(self, 物件分字符號, 物件分詞符號):
        字的音 = []
        for 一字 in self.內底字:
            音標 = 一字.看音(物件分字符號, 物件分詞符號)
            字的音.append(音標)
        return 字的音

    def 看分詞(self, 物件分型音符號=分型音符號,
            物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        字的音 = self._提著詞物件的字物件音陣列(物件分字符號, 物件分詞符號)
        無音數量 = 0
        for 音 in 字的音:
            if 音 == 無音:
                無音數量 += 1
        if 無音數量 == len(字的音):
            return self.看型(物件分字符號, 物件分詞符號)
        if 無音數量 == 0:
            return (
                self.看型(物件分字符號, 物件分詞符號) +
                物件分型音符號 +
                self.看音(物件分字符號, 物件分詞符號)
            )
        return (
            self.看型(物件分字符號, 物件分詞符號) +
            物件分型音符號 +
            物件分字符號.join(self._提著詞物件的字物件音陣列(物件分字符號, 物件分詞符號))
        )

    def 綜合標音(self, 語言綜合標音):
        詞組綜合標音 = {}
        for 一字 in self.內底字:
            for 欄位, 內容 in 一字.綜合標音(語言綜合標音)[0].items():
                try:
                    詞組綜合標音[欄位].append(內容)
                except:
                    詞組綜合標音[欄位] = [內容]
        結果 = {}
        for 欄位, 內容 in 詞組綜合標音.items():
            if 欄位 == '漢字':
                結果[欄位] = ''.join(內容)
            else:
                結果[欄位] = '-'.join(內容)
        if len(結果) > 0:
            結果['分詞'] = self.看分詞()
        return [結果]

    def 篩出字物件(self):
        return self.內底字

    def 網出詞物件(self):
        return [self]

    def 轉音(self, 音標工具, 函式='預設音標'):
        # 逐个函式攏愛產生新的物件
        新詞物件 = 詞()
        for 字物件 in self.內底字:
            新詞物件.內底字.append(字物件.轉音(音標工具, 函式))
        return 新詞物件
