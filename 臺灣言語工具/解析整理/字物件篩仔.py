# -*- coding: utf-8 -*-
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.基本元素.字 import 字
from 臺灣言語工具.基本元素.章 import 章
from 臺灣言語工具.基本元素.組 import 組
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


class 字物件篩仔:
    def _篩字(self, 字物件):
        if not isinstance(字物件, 字):
            raise 型態錯誤('傳入來的毋是字物件：{0}'.format(str(字物件)))
        return [字物件]

    def _篩詞(self, 詞物件):
        if not isinstance(詞物件, 詞):
            raise 型態錯誤('傳入來的毋是詞物件：{0}'.format(str(詞物件)))
        return 詞物件.內底字

    def _篩組(self, 組物件):
        if not isinstance(組物件, 組):
            raise 型態錯誤('傳入來的毋是組物件：{0}'.format(str(組物件)))
        字陣列 = []
        for 詞物件 in 組物件.內底詞:
            字陣列.extend(self._篩詞(詞物件))
        return 字陣列

    def _篩集(self, 集物件):
        if not isinstance(集物件, 集):
            raise 型態錯誤('傳入來的毋是集物件：{0}'.format(str(集物件)))
        if len(集物件.內底組) == 0:
            return []
        if len(集物件.內底組) > 1:
            raise 解析錯誤('內底組毋焦一个！！{0}'.format(str(集物件)))
        return self._篩組(集物件.內底組[0])

    def _篩句(self, 句物件):
        if not isinstance(句物件, 句):
            raise 型態錯誤('傳入來的毋是句物件：{0}'.format(str(句物件)))
        字陣列 = []
        for 集物件 in 句物件.內底集:
            字陣列.extend(self._篩集(集物件))
        return 字陣列

    def _篩章(self, 章物件):
        if not isinstance(章物件, 章):
            raise 型態錯誤('傳入來的毋是章物件：{0}'.format(str(章物件)))
        字陣列 = []
        for 句物件 in 章物件.內底句:
            字陣列.extend(self._篩句(句物件))
        return 字陣列

    def 篩出字物件(self, 物件):
        if isinstance(物件, 字):
            return self._篩字(物件)
        if isinstance(物件, 詞):
            return self._篩詞(物件)
        if isinstance(物件, 組):
            return self._篩組(物件)
        if isinstance(物件, 集):
            return self._篩集(物件)
        if isinstance(物件, 句):
            return self._篩句(物件)
        if isinstance(物件, 章):
            return self._篩章(物件)
        raise 型態錯誤('傳入來的毋是字詞組集句章其中一種物件：{0}，{1}'
                   .format(type(物件), str(物件)))
