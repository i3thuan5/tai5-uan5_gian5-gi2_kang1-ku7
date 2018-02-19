# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.字 import 字


class 拆文分析器斷詞單元試驗(TestCase):
    def test_漢字知影有輕聲猶原一個詞(self):
        音 = '害--矣--啦'
        組物件 = 拆文分析器.建立組物件(音)
        self.assertEqual(len(組物件.網出詞物件()), 1)

    def test_句中輕聲無連做伙嘛會使(self):
        漢 = '講會出--來'
        組物件 = 拆文分析器.建立組物件(漢)
        self.assertEqual(len(組物件.網出詞物件()), 1)
        self.assertEqual(組物件.篩出字物件(), [
            字('後', 'āu'),
            字('日', '0ji̍t'),
        ])

    def test_句中輕聲kah4後壁無連做伙嘛會使(self):
        漢 = '講--出-來'
        組物件 = 拆文分析器.建立組物件(漢)
        self.assertEqual(len(組物件.網出詞物件()), 1)

    def test_看有黏做伙決定斷詞(self):
        音 = 'Mi̍h-kiānn phah-bô--khì --ah'
        組物件 = 拆文分析器.建立組物件(音)
        self.assertEqual(len(組物件.網出詞物件()), 3)
