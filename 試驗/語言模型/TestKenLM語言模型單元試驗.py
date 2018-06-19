# -*- coding: utf-8 -*-
import itertools
from math import log10
import os
from unittest.case import TestCase


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.語言模型.KenLM語言模型 import KenLM語言模型


class KenLM語言模型單元試驗(TestCase):
    忍受 = 1e-7

    def setUp(self):
        self.媠媠巧靚語言模型 = KenLM語言模型(
            os.path.join(os.path.dirname(
                os.path.abspath(__file__)), '語料', 'sui2.lm')
        )
        self.媠媠巧靚組物件 = 拆文分析器.建立組物件('sui2 sui2 khiau2 tsiang5')

    def test_媠媠巧靚_評詞陣列分(self):
        self.assertEqual(self.媠媠巧靚語言模型.上濟詞數(), 3)
        self.陣列比較(
            list(self.媠媠巧靚語言模型.評詞陣列分(self.媠媠巧靚組物件.內底詞)),
            [log10(2 / 5), log10(1 / 2), log10(1 / 2), -0.0],
            self.忍受
        )
        self.陣列比較(
            list(self.媠媠巧靚語言模型.評詞陣列分(self.媠媠巧靚組物件.內底詞, 開始的所在=1)),
            [log10(1 / 2), log10(1 / 2), -0.0],
            self.忍受
        )

    def test_媠媠巧靚_評分(self):
        self.assertEqual(self.媠媠巧靚語言模型.上濟詞數(), 3)
        self.陣列比較(
            list(self.媠媠巧靚語言模型.評分(self.媠媠巧靚組物件)),
            [-0.0, log10(1 / 2), log10(1 / 2), -0.0, -0.0],
            self.忍受
        )

    def 陣列比較(self, 結果陣列, 答案陣列, 範圍):
        for 結果, 答案 in itertools.zip_longest(結果陣列, 答案陣列):
            self.assertAlmostEqual(結果, 答案, delta=範圍)
