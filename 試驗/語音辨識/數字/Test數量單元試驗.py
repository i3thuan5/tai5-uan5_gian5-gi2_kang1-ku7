# -*- coding: utf-8 -*-
from unittest.case import TestCase, skip
from 臺灣言語工具.語音辨識.數字 import 台語數字
from 臺灣言語工具.語音辨識.數字 import 阿拉伯數字


class 數量單元試驗(TestCase):
    def tearDown(self):
        self.assertEqual(台語數字().轉數量(self.題目), self.答案)

    def test_10(self):
        self.題目 = 10
        self.答案 = '十'

    def test_15(self):
        self.題目 = 15
        self.答案 = '十五'

    @skip
    def test_單位詞kah數量(self):
        self.題目 = 180
        self.答案 = '百八'

    @skip
    def test_數量kah單位詞kah數量(self):
        self.題目 = 2300
        self.答案 = '兩千三'

    def test_一萬以下無0(self):
        self.題目 = 4512
        self.答案 = '四千五百一十二'

    def test_百空(self):
        self.題目 = 602
        self.答案 = '六百空二'

    def test_千空(self):
        self.題目 = 6078
        self.答案 = '六千空七十八'

    def test_萬空(self):
        self.題目 = 6078
        self.答案 = '一萬空九百'

    def test_空十幾(self):
        self.題目 = 1300130013
        self.答案 = '十三億空一十三萬空一十三'

    def test_大數字(self):
        self.題目 = 1230567890980654
        self.答案 = '一千兩百三十兆五千六百七十八億九千空九十八萬空六百五十四'

    def test_2ê(self):
        self.題目 = 2
        self.答案 = '兩'

    def test_20ê(self):
        self.題目 = 20
        self.答案 = '二十'

    def test_空二(self):
        self.題目 = 102
        self.答案 = '一百空二'

    def test_二單位(self):
        self.題目 = 2200000000
        self.答案 = '二十二億'

    def test_大單位(self):
        self.題目 = 2000000000000
        self.答案 = '兩兆'

    def test_siunn大(self):
        self.題目 = 10000000000000000
        self.答案 = None

    def test_x01x(self):
        self.題目 = 1010
        self.答案 = '一千空十'

    def test_x11x(self):
        self.題目 = 1110
        self.答案 = '一千一百十'

    def test_xx1x(self):
        self.題目 = 1310
        self.答案 = '一千三百十'


class 阿拉伯數字單元試驗():
    def setUp(self):
        self.數字 = 阿拉伯數字()
        pass

    def test_轉客家話數量省單位(self):
        問答 = [
            ('一百二十', '百二'),
            ('兩百三十', '兩百三'),
            ('六百零二', None),
            ('一千零一', None),
            ('一千零一十', None),
            ('一千零二十', None),
            ('一千一百一十', '一千一百一'),
            ('一千兩百', '千二'),
            ('一千三百', '千三'),
            ('一千三百一十三', None),
            ('四千五百一十二', None),
            ('五千零四', None),
            ('六千零七十', None),
            ('九千八百', '九千八'),
            ('十三億零一十三萬零一十三', None),
            ('一兆零一十六萬七千', '一兆零一十六萬七'),
            ('七十九億', None),
        ]
        self.檢查客家話數量(問答)

    def test_轉官話數量省上尾單位(self):
        問答 = [
            ('一百二十', '一百二'),
            ('兩百三十', '兩百三'),
            ('六百零二', None),
            ('一千零一', None),
            ('一千零一十', None),
            ('一千零二十', None),
            ('一千一百一十', '一千一百一'),
            ('一千兩百', '一千二'),
            ('一千三百', '一千三'),
            ('一千三百一十三', None),
            ('四千五百一十二', None),
            ('五千零四', None),
            ('六千零七十', None),
            ('九千八百', '九千八'),
            ('十三億零一十三萬零一十三', None),
            ('一兆零一十六萬七千', '一兆零一十六萬七'),
            ('七十九億', None),
        ]
        self.檢查官話數量(問答)

    def test_轉官話兩佮二數量(self):
        問答 = [
            ('十二', None),
            ('一百二十', '一百二'),
            ('一千兩百', '一千二'),
            ('三千兩百', '三千二'),
            ('四萬兩千', '四萬二'),
            ('九十二萬', None),
            ('八億兩千萬', None),
            ('一百二十萬', None),
            ('一千兩百萬', None),
            ('三千兩百萬', None),
            ('兩億', None),
        ]
        self.檢查官話數量(問答)

    def 檢查數量(self, 問答):
        for 問, 答 in 問答:
            if 答 is None:
                self.assertEqual(self.數字.是數量無(問), False, 問)
                self.assertEqual(self.數字.轉數量('空', 問), 問)
            else:
                self.assertEqual(self.數字.是數量無(問), True)
                self.assertEqual(self.數字.轉數量('空', 問), 答, 問)
                self.assertEqual(self.數字.轉數量('零', 問),
                                 答.replace('空', '零'), 問)

    def 檢查閩南語數量(self, 問答):
        for 問, 答 in 問答:
            if 答 is None:
                self.assertEqual(self.數字.轉閩南語數量無(問), False, 問)
                self.assertEqual(self.數字.轉閩南語數量(問), 問)
            else:
                self.assertEqual(self.數字.轉閩南語數量無(問), True, 問)
                self.assertEqual(self.數字.轉閩南語數量(問), 答, 問)

    def 檢查客家話數量(self, 問答):
        for 問, 答 in 問答:
            if 答 is None:
                self.assertEqual(self.數字.轉客家話數量無(問), False, 問)
                self.assertEqual(self.數字.轉客家話數量(問), 問)
            else:
                self.assertEqual(self.數字.轉客家話數量無(問), True, 問)
                self.assertEqual(self.數字.轉客家話數量(問), 答, 問)

    def 檢查官話數量(self, 問答):
        for 問, 答 in 問答:
            if 答 is None:
                self.assertEqual(self.數字.轉官話數量無(問), False, 問)
                self.assertEqual(self.數字.轉官話數量(問), 問)
            else:
                self.assertEqual(self.數字.轉官話數量無(問), True, 問)
                self.assertEqual(self.數字.轉官話數量(問), 答, 問)
