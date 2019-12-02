# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.語音合成 import 台灣話口語講法


class 口語單元試驗(TestCase):
    def tearDown(self):
        句物件 = (
            拆文分析器.對齊句物件(self.漢字, self.臺羅)
        )
        self.assertEqual(台灣話口語講法(句物件), self.答案)

    def test_一句(self):
        self.漢字 = '我愛媠媠'
        self.臺羅 = 'guá ài suí-suí'
        self.答案 = 'gua1 ʔai2 sui1-sui2'

    def test_標點(self):
        self.漢字 = '我愛媠媠。我愛媠媠。'
        self.臺羅 = 'guá ài suí-suí. guá ài suí-suí.'
        self.答案 = 'gua1 ʔai2 sui1-sui2 . gua1 ʔai2 sui1-sui2 .'

    def test_井前無變調原本物件無變(self):
        self.漢字 = '我#愛媠媠'
        self.臺羅 = 'guá # ài suí-suí'
        self.答案 = 'gua2 ʔai2 sui1-sui2'
