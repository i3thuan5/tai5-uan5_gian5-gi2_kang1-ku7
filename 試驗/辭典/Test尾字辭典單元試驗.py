# -*- coding: utf-8 -*-
from unittest.case import TestCase


from 試驗.辭典.辭典單元試驗 import 辭典單元試驗
from 臺灣言語工具.辭典.尾字辭典 import 尾字辭典
from 臺灣言語工具.辭典.型音辭典 import 型音辭典
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 尾字辭典單元試驗(辭典單元試驗, TestCase):
    辭典型態 = 尾字辭典(型音辭典)

    def test_長短詞攏愛揣出來(self):
        self.字典.加詞(self.孤詞物)
        self.字典.加詞(self.二詞物)
        self.字典.加詞(self.短詞物)
        self.字典.加詞(self.詞物件)
        self.字典.加詞(self.孤詞音)
        self.字典.加詞(self.二詞音)
        self.字典.加詞(self.短詞音)
        self.字典.加詞(self.詞音標)
        self.字典.加詞(self.對齊詞)
        問號型物件 = 拆文分析器.建立詞物件('？')
        問號音物件 = 拆文分析器.建立詞物件('?')
        問號對齊物件 = 拆文分析器.對齊詞物件('？', '?')
        無型物件 = 拆文分析器.建立詞物件('無-？')
        無音物件 = 拆文分析器.建立詞物件('bo5-?')
        好無型物件 = 拆文分析器.建立詞物件('好無')
        好無音物件 = 拆文分析器.建立詞物件('ho2-bo5')
        好無對齊物件 = 拆文分析器.對齊詞物件('好無', 'ho2-bo5')
        for 詞物件 in [問號型物件, 問號音物件, 問號對齊物件,
                    無型物件, 無音物件,
                    好無型物件, 好無音物件, 好無對齊物件]:
            self.字典.加詞(詞物件)
        self.assertEqual(self.字典.查詞(self.詞物件),
                         [{問號型物件, 問號對齊物件}, {無型物件},
                          set(), {self.詞物件, self.對齊詞}])
        self.assertEqual(self.字典.查詞(self.詞音標),
                         [{問號音物件, 問號對齊物件}, {無音物件},
                          set(), {self.詞音標, self.對齊詞}])
        self.assertEqual(self.字典.查詞(self.對齊詞),
                         [{問號對齊物件}, set(),
                          set(), {self.對齊詞}])

    def test_加檔案的詞(self):
        # 無法度mock到`臺灣言語工具.辭典.尾字辭典._加詞`。因為伊是用家己的指標，mocka無到
        pass
