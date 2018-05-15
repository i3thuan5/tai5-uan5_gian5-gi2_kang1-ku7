# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 拆文分析器斷字單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.建立句物件(self.語句)
        self.assertEqual(len(句物件.篩出字物件()), self.字數, self.語句)

    def test_漢羅(self):
        self.語句 = '我ê腹肚枵ah'
        self.字數 = len(['我', 'ê', '腹', '肚', '枵', 'ah'])

    def test_漢羅空白(self):
        self.語句 = '我ê pak tóo枵ah'
        self.字數 = len(['我', 'ê', 'pak', 'tóo', '枵', 'ah'])

    def test_漢羅連字符(self):
        self.語句 = '我ê pak-tóo枵ah'
        self.字數 = len(['我', 'ê', 'pak', 'tóo', '枵', 'ah'])

    def test_漢羅減號(self):
        self.語句 = '我ê pak - tóo枵ah'
        self.字數 = len(['我', 'ê', 'pak', '-', 'tóo', '枵', 'ah'])

    def test_本調符號接輕聲(self):
        self.語句 = 'Hó#--ah'
        self.字數 = len(['Hó', '#', '--ah'])

    def test__拆句做巢狀詞摻組字式(self):
        self.語句 = '⿰---⿰-- - ⿱--,⿰-,⿱⿰-,--⿱--'
        self.字數 = len(['⿰--', '⿰--', '-', '⿱--', ',', '⿰-,', '⿱⿰-,-', '⿱--'])
