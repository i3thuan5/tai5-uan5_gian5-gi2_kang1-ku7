# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.字 import 字


class 拆文分析器對齊輕聲單元試驗(TestCase):
    def test_句頭輕聲(self):
        型 = '--啊'
        音 = '--ah'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(組物件.篩出字物件(), [
            字('啊', '0ah'),
        ])

    def test_句中輕聲(self):
        型 = '後--日'
        音 = 'āu--ji̍t'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(len(組物件.網出詞物件()), 1)
        self.assertEqual(組物件.篩出字物件(), [
            字('後', 'āu'),
            字('日', '0ji̍t'),
        ])

    def test_句中分開輕聲(self):
        型 = '食飽矣'
        音 = 'tsia̍h-pá --ah'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(len(組物件.網出詞物件()), 2)
        self.assertEqual(組物件.網出詞物件()[1].篩出字物件(), [
            字('矣', '0ah'),
        ])

    def test_看有黏做伙決定斷詞(self):
        音 = 'Mi̍h-kiānn phah-bô--khì --ah '
        組物件 = 拆文分析器.建立組物件(音)
        self.assertEqual(len(組物件.網出詞物件()), 3)

    def test_有處理減號的輕聲(self):
        型 = '後日'
        音 = 'āu-0ji̍t'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertTrue(組物件.篩出字物件()[-1].敢是輕聲())

    def test_輕聲以音為主_音有(self):
        型 = '後日'
        音 = 'āu--ji̍t'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertTrue(組物件.篩出字物件()[-1].敢是輕聲())

    def test_輕聲以音為主_音無(self):
        型 = '後--日'
        音 = 'āu-ji̍t'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertFalse(組物件.篩出字物件()[-1].敢是輕聲())
