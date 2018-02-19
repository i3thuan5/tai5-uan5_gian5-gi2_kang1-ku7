# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.字 import 字


class 拆文分析器連字符單元試驗(TestCase):
    def test_句頭輕聲無連做伙嘛會使(self):
        型 = '-- 啊'
        音 = '-- ah'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(組物件.篩出字物件(), [
            字('啊', '0ah'),
        ])

    def test_有處理減號的輕聲(self):
        self.fail()
        句 = '-tiong7-tiam2-'
        組物件 = 拆文分析器.建立組物件(句)
        self.assertTrue(組物件.篩出字物件()[-1].敢是輕聲())

    def test_有處理減號的輕聲(self):
        self.fail()
        句 = '--tsit8--puann3--'
        組物件 = 拆文分析器.建立組物件(句)
        self.assertTrue(組物件.篩出字物件()[-1].敢是輕聲())

    def test_有處理減號的輕聲(self):
        self.fail()
        句 = '---pun---khui---'
        組物件 = 拆文分析器.建立組物件(句)
        self.assertEqual(len(組物件.網出詞物件()), 3)
