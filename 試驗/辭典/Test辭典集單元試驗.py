# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.參數錯誤 import 參數錯誤
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from os import remove
from unittest.mock import patch, call
from 臺灣言語工具.辭典.型音辭典 import 型音辭典
from 臺灣言語工具.辭典.現掀辭典 import 現掀辭典


class 辭典集單元試驗:

    def test_無仝詞典攏愛揣出來(self):
        it = 型音辭典(4)
        ji = 現掀辭典(4)
        it.加詞(拆文分析器.對齊詞物件('你', 'li2'))
        ji.加詞(拆文分析器.對齊詞物件('你好', 'li2-ho2'))
        bue = 辭典集(it, ji)
        self.assertEqual(
            bue.查詞(拆文分析器.建立詞物件('li2')),
            [
                {拆文分析器.對齊詞物件('你', 'li2')},
                {拆文分析器.對齊詞物件('你好', 'li2-ho2')},
                set(),
                {self.詞物件}
            ]
        )

    def test_長度無仝以長的為主(self):
        it = 型音辭典(3)
        ji = 現掀辭典(33)
        bue = 辭典集(it, ji)
        self.assertEqual(bue.上濟字數(), 33)

    def test_揣出來愛有對應的長度(self):
        it = 型音辭典(3)
        ji = 現掀辭典(2)
        bue = 辭典集(it, ji)
        self.assertEqual(
            bue.查詞(拆文分析器.建立詞物件('li2')),
            [set(), set(), set()]
        )
