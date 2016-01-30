# -*- coding: utf-8 -*-

from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.章 import 章
from itertools import repeat
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


class 座標揀集內組:

    @classmethod
    def 揀(cls, 物件, 集選擇=repeat(0)):
        集選擇指標 = iter(集選擇)
        if isinstance(物件, 章):
            return cls._揀章物件(物件, 集選擇指標)
        if isinstance(物件, 句):
            return cls._揀句物件(物件, 集選擇指標)
        return cls._揀集物件(物件, 集選擇指標)

    @classmethod
    def _揀章物件(cls, 章物件, 集選擇指標):
        揀出來的章物件 = 章()
        for 句物件 in 章物件.內底句:
            揀出來的章物件.內底句.append(cls._揀句物件(句物件, 集選擇指標))
        return 揀出來的章物件

    @classmethod
    def _揀句物件(cls, 句物件, 集選擇指標):
        集陣列 = []
        for 集物件 in 句物件.內底集:
            集陣列.append(cls._揀集物件(集物件, 集選擇指標))
        句物件 = 句()
        句物件.內底集 = 集陣列
        return 句物件

    @classmethod
    def _揀集物件(cls, 集物件, 集選擇指標):
        try:
            選擇 = next(集選擇指標)
        except StopIteration:
            raise 解析錯誤('選擇無夠濟！！')
        try:
            組物件 = 集物件.內底組[選擇]
        except IndexError:
            raise 解析錯誤('集物件內底數量：{}，選擇位置：{}'.format(len(集物件.內底組), 選擇))
        return 集([組物件])
