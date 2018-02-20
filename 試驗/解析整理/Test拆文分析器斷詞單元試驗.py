# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 拆文分析器斷詞單元試驗(TestCase):
    def test_漢字知影有輕聲猶原一個詞(self):
        音 = '害--矣--啦'
        組物件 = 拆文分析器.建立組物件(音)
        self.assertEqual(len(組物件.網出詞物件()), 1)

    def test_句中輕聲無連做伙嘛會使(self):
        漢 = '講會出--來'
        組物件 = 拆文分析器.建立組物件(漢)
        self.assertEqual(len(組物件.網出詞物件()), 1)

    def test_句中輕聲kah4後壁無連做伙嘛會使(self):
        漢 = '講--出-來'
        組物件 = 拆文分析器.建立組物件(漢)
        self.assertEqual(len(組物件.網出詞物件()), 1)

    def test_看有黏做伙決定斷詞(self):
        音 = 'Mi̍h-kiānn phah-bô--khì --ah'
        組物件 = 拆文分析器.建立組物件(音)
        self.assertEqual(len(組物件.網出詞物件()), 3)

    def test_組字當作漢字(self):
        句 = '癩⿸疒哥人'
        組物件 = 拆文分析器.建立組物件(句)
        self.assertEqual(len(組物件.網出詞物件()), 1)

    def test_漢羅做伙(self):
        句 = '台文通訊Bóng報'
        組物件 = 拆文分析器.建立組物件(句)
        self.assertEqual(len(組物件.網出詞物件()), 1)

    def test_有連字符就認連字符(self):
        組物件 = 拆文分析器.建立組物件('無-？-bo5-?')
        self.assertEqual(len(組物件.內底詞), 1)
        self.assertEqual(len(組物件.篩出字物件()), 4)
