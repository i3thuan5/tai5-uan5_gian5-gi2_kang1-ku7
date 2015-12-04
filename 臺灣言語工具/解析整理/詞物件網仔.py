# -*- coding: utf-8 -*-
from 臺灣言語工具.基本元素.字 import 字
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.基本元素.組 import 組
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.基本元素.章 import 章
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.程式掠漏 import 程式掠漏


class 詞物件網仔:
    _掠漏 = 程式掠漏()

    @classmethod
    def _網字(cls, 字物件):
        cls._掠漏.毋是字物件就毋著(字物件)
        詞物件 = 詞()
        詞物件.內底字.append(字物件)
        return [詞物件]

    @classmethod
    def _網詞(cls, 詞物件):
        cls._掠漏.毋是詞物件就毋著(詞物件)
        return [詞物件]

    @classmethod
    def _網組(cls, 組物件):
        cls._掠漏.毋是組物件就毋著(組物件)
        return 組物件.內底詞

    @classmethod
    def _網集(cls, 集物件):
        cls._掠漏.毋是集物件就毋著(集物件)
        if len(集物件.內底組) == 0:
            return []
        if len(集物件.內底組) > 1:
            raise 解析錯誤('內底組毋焦一个！！{0}'.format(str(集物件)))
        return cls._網組(集物件.內底組[0])

    @classmethod
    def _網句(cls, 句物件):
        cls._掠漏.毋是句物件就毋著(句物件)
        詞陣列 = []
        for 集物件 in 句物件.內底集:
            詞陣列.extend(cls._網集(集物件))
        return 詞陣列

    @classmethod
    def _網章(cls, 章物件):
        cls._掠漏.毋是章物件就毋著(章物件)
        詞陣列 = []
        for 句物件 in 章物件.內底句:
            詞陣列.extend(cls._網句(句物件))
        return 詞陣列

    @classmethod
    def 網出詞物件(cls, 物件):
        if isinstance(物件, 字):
            return cls._網字(物件)
        if isinstance(物件, 詞):
            return cls._網詞(物件)
        if isinstance(物件, 組):
            return cls._網組(物件)
        if isinstance(物件, 集):
            return cls._網集(物件)
        if isinstance(物件, 句):
            return cls._網句(物件)
        if isinstance(物件, 章):
            return cls._網章(物件)
        cls._掠漏.毋是字詞組集句章的毋著(物件)
