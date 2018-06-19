# -*- coding: utf-8 -*-
import os
from unittest.case import TestCase
from unittest.mock import patch


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.語言模型.KenLM語言模型 import KenLM語言模型


class 語言模型ppl單元試驗(TestCase):
    忍受 = 1e-7

    def setUp(self):
        self.媠媠巧靚語言模型 = KenLM語言模型(
            os.path.join(os.path.dirname(
                os.path.abspath(__file__)), '語料', 'sui2.lm')
        )
        self.媠媠巧靚組物件 = 拆文分析器.建立組物件('sui2 sui2 khiau2 tsiang5')

    @patch('臺灣言語工具.語言模型.語言模型.語言模型.評分')
    def test_媠媠巧靚_perplexity(self, 評分mock):
        評分mock.return_value = [-1., -0.1, -4., -2.9]
        self.assertAlmostEqual(
            self.媠媠巧靚語言模型.perplexity(self.媠媠巧靚組物件),
            10 ** 2,
            delta=self.忍受
        )
