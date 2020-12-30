# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 物件轉分詞整合試驗(TestCase):
    '原本物件生按ná，經過分詞kah分析去了後愛原本的物件'

    def tearDown(self):
        分詞 = self.物件.看分詞()
        self.assertEqual(拆文分析器.分詞句物件(分詞), self.物件, 分詞)

    def test_全羅(self):
        self.物件 = 拆文分析器.建立句物件('Kín--tshut-lâi --lah')

    def test_漢羅對照(self):
        self.物件 = 拆文分析器.建立句物件('緊出來啦', 'Kín--tshut-lâi --lah')

    def test_分詞ê符號(self):
        self.物件 = 拆文分析器.建立句物件('Kín!｜｜｜好~')
