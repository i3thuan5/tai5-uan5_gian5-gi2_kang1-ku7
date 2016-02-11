# -*- coding: utf-8 -*-
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
from 臺灣言語工具.基本物件.句 import 句
from 試驗.斷詞.辭典揣詞單元試驗 import 辭典揣詞單元試驗
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 拄好長度辭典揣詞單元試驗(辭典揣詞單元試驗, TestCase):
    辭典揣詞 = 拄好長度辭典揣詞

    def test_兩三切比一四切閣較好(self):
        self.test_基本揣詞()

        一四分數 = []
        self.一張椅仔對齊詞 = 拆文分析器.對齊詞物件('一張椅仔', 'tsit8-tiunn1-i2-a2')
        self.辭典.加詞(self.一張椅仔對齊詞)
        self.一張椅仔集 = 拆文分析器.對齊集物件('一張椅仔', 'tsit8-tiunn1-i2-a2')
        新句物件 = 句([self.我對齊集, self.有對齊集,
                  self.一張椅仔集, self.驚對齊集, self.驚對齊集])
        揣詞結果, 分數, 詞數 = self.揣詞.揣詞分析(self.辭典, self.對齊句)
        self.assertEqual(揣詞結果, 新句物件)
        self.檢查分數詞數(分數, 詞數, 0, 5)
        一四分數.append(分數)
        揣詞結果, 分數, 詞數 = self.揣詞.揣詞分析(self.辭典, self.型句)
        self.assertEqual(揣詞結果, 新句物件)
        self.檢查分數詞數(分數, 詞數, 0, 5)
        一四分數.append(分數)
        揣詞結果, 分數, 詞數 = self.揣詞.揣詞分析(self.辭典, self.音句)
        self.assertEqual(揣詞結果, 新句物件)
        self.檢查分數詞數(分數, 詞數, 0, 5)
        一四分數.append(分數)
        揣詞結果, 分數, 詞數 = self.揣詞.揣詞分析(self.辭典, self.有詞漢羅)
        self.assertEqual(揣詞結果, 新句物件)
        self.檢查分數詞數(分數, 詞數, 0, 5)
        一四分數.append(分數)
        揣詞結果, 分數, 詞數 = self.揣詞.揣詞分析(self.辭典, self.無詞漢羅)
        self.assertEqual(揣詞結果, 新句物件)
        self.檢查分數詞數(分數, 詞數, 0, 5)
        一四分數.append(分數)

        兩三分數 = []
        self.有一張對齊詞 = 拆文分析器.對齊詞物件('有一張', 'u7-tsit8-tiunn1')
        self.辭典.加詞(self.有一張對齊詞)
        self.有一張集 = 拆文分析器.對齊集物件('有一張', 'u7-tsit8-tiunn1')
        新句物件 = 句([self.我對齊集, self.有一張集,
                  self.椅仔對齊集, self.驚對齊集, self.驚對齊集])
        揣詞結果, 分數, 詞數 = self.揣詞.揣詞分析(self.辭典, self.對齊句)
        self.assertEqual(揣詞結果, 新句物件)
        self.檢查分數詞數(分數, 詞數, 0, 5)
        兩三分數.append(分數)
        揣詞結果, 分數, 詞數 = self.揣詞.揣詞分析(self.辭典, self.型句)
        self.assertEqual(揣詞結果, 新句物件)
        self.檢查分數詞數(分數, 詞數, 0, 5)
        兩三分數.append(分數)
        揣詞結果, 分數, 詞數 = self.揣詞.揣詞分析(self.辭典, self.音句)
        self.assertEqual(揣詞結果, 新句物件)
        self.檢查分數詞數(分數, 詞數, 0, 5)
        兩三分數.append(分數)
        揣詞結果, 分數, 詞數 = self.揣詞.揣詞分析(self.辭典, self.有詞漢羅)
        self.assertEqual(揣詞結果, 新句物件)
        self.檢查分數詞數(分數, 詞數, 0, 5)
        兩三分數.append(分數)
        揣詞結果, 分數, 詞數 = self.揣詞.揣詞分析(self.辭典, self.無詞漢羅)
        self.assertEqual(揣詞結果, 新句物件)
        self.檢查分數詞數(分數, 詞數, 0, 5)
        兩三分數.append(分數)
        for 分數 in 一四分數[1:]:
            self.assertEqual(分數, 一四分數[0])
        for 分數 in 兩三分數[1:]:
            self.assertEqual(分數, 兩三分數[0])
        self.assertLess(一四分數[0], 兩三分數[0])
