# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.公用變數 import 分字符號
from 臺灣言語工具.基本物件.公用變數 import 分詞符號
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.基本物件.公用變數 import 分型音符號
from 臺灣言語工具.基本物件.功能 import 功能
from 臺灣言語工具.基本物件.公用變數 import 敢是拼音字元
import re


class 詞(功能):
    _sooji = re.compile(r'\d')

    def __init__(self, 字陣列=[]):
        # 愛產生新的物件
        try:
            self.內底字 = []
            for 字物件 in 字陣列:
                try:
                    self.內底字.append(字物件.khóopih字())
                except AttributeError:
                    raise 型態錯誤(
                        '字陣列內底有毋是字的：字陣列＝{0}，字物件＝{1}'.format(str(字陣列), str(字物件))
                    )
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

    def 看語句(self):
        字型陣列 = []
        頂字是羅馬字 = False
        bat輕聲 = False
        for 一字 in self.內底字:
            字串 = 一字.看語句()
            #
            # 先接符號才接字
            #
            # 接輕聲符（輕聲漢字、輕聲羅馬字）
            是輕聲字 = 一字.敢有輕聲標記()
            if 是輕聲字:
                bat輕聲 = True
            elif bat輕聲:
                字型陣列.append(分字符號)
            # 接連字符（羅-羅）
            elif (
                敢是拼音字元(字串[0]) or self._sooji.match(字串[0])
                or (字串[0] == '0' and 敢是拼音字元(字串[1]))
            ):
                if 頂字是羅馬字:
                    字型陣列.append(分字符號)
                頂字是羅馬字 = True
            else:
                頂字是羅馬字 = False

            # 接字
            字型陣列.append(字串)
        # 提掉ke的連字符
        if len(字型陣列) > 1 and 字型陣列[0] == 分字符號:
            字型陣列 = 字型陣列[1:]
        return ''.join(字型陣列)

    def 看音(self, 物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        if 物件分字符號 == 分字符號:
            return self.看羅馬字()
        susia = []
        for 一字 in self.內底字:
            susia.append(一字.音)
        return 物件分字符號.join(susia)

    def 看羅馬字(self, 欄位='音'):
        羅馬字 = []
        for kui, 一字 in enumerate(self.內底字):
            if 一字.輕聲標記:
                pass
            elif kui != 0:
                羅馬字.append('-')
            羅馬字.append(getattr(一字, 欄位))
        return ''.join(羅馬字)

    def 看分詞(self):
        if self.敢有2種書寫():
            return (
                self.看羅馬字('型') +
                分型音符號 +
                self.看羅馬字()
            )
        return self.看羅馬字('型')

    def 綜合標音(self, 語言綜合標音):
        詞組綜合標音 = {}
        for 一字 in self.內底字:
            for 欄位, 內容 in 一字.綜合標音(語言綜合標音)[0].items():
                try:
                    詞組綜合標音[欄位].append(內容)
                except KeyError:
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
        return list(self.內底字)

    def 網出詞物件(self):
        return [self]

    def 轉音(self, 音標工具, 函式='預設音標'):
        # 逐个函式攏愛產生新的物件
        新詞物件 = 詞()
        for 字物件 in self.內底字:
            新詞物件.內底字.append(字物件.轉音(音標工具, 函式))
        return 新詞物件

    def 敢有2種書寫(self):
        for 字物件 in self.內底字:
            if 字物件.音 != 無音:
                return True
        return False
