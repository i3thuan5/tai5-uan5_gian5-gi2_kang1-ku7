# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.字 import 字


class 敢是標點符號單元試驗(TestCase):

    def test_兩種書寫(self):
        字物件 = 字('，', ',')
        self.assertTrue(字物件.敢是標點符號())

    def test_一種書寫(self):
        字物件 = 字(',')
        self.assertTrue(字物件.敢是標點符號())

    def test_漢(self):
        字物件 = 字('媠', '')
        self.assertFalse(字物件.敢是標點符號())

    def test_羅(self):
        字物件 = 字('sui2', '')
        self.assertFalse(字物件.敢是標點符號())

    def test_漢羅(self):
        字物件 = 字('媠', 'sui2')
        self.assertFalse(字物件.敢是標點符號())

    def test_詞物件(self):
        句物件 = 拆文分析器.對齊詞物件('，', ',')
        self.assertTrue(句物件.敢是標點符號())

    def test_台文物件(self):
        句物件 = 拆文分析器.對齊詞物件('媠巧', 'sui2-khiau2')
        self.assertFalse(句物件.敢是標點符號())

    def test_句物件(self):
        句物件 = 拆文分析器.對齊句物件('，', ',')
        self.assertTrue(句物件.敢是標點符號())
