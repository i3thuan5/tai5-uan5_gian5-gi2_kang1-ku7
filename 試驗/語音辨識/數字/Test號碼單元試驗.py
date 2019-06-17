# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.正規.阿拉伯數字 import 阿拉伯數字


class 阿拉伯數字單元試驗(TestCase):
    def setUp(self):
        self.數字 = 阿拉伯數字()
        pass

    def tearDown(self):
        pass

    def test_判斷是數字無(self):
        self.assertEqual(self.數字.是數字無(''), False)
        self.assertEqual(self.數字.是數字無('0'), True)
        self.assertEqual(self.數字.是數字無('12312'), True)
        self.assertEqual(self.數字.是數字無('13３2312'), True)
        self.assertEqual(self.數字.是數字無('6'), True)
        self.assertEqual(self.數字.是數字無('013３2312三'), False)
        self.assertEqual(self.數字.是數字無('００13３27890'), True)
        self.assertEqual(self.數字.是數字無('000'), True)
        # 小數本來就會使拆開唸，予別的模組合起來
        self.assertEqual(self.數字.是數字無('00.30'), False)
        self.assertEqual(self.數字.是數字無('197.080'), False)
        self.assertEqual(self.數字.是數字無('197.08.0'), False)

    def test_轉號碼(self):
        問答 = [
            ('2', '二'),
            ('10', '一空'),
            ('23', '二三'),
            ('15', '一五'),
            ('120', '一二空'),
            ('230', '二三空'),
            ('602', '六空二'),
            ('1001', '一空空一'),
            ('1020', '一空二空'),
            ('1300', '一三空空'),
            ('4512', '四五一二'),
            ('5004', '五空空四'),
            ('6070', '六空七空'),
            ('9800', '九八空空'),  # 九千八百
            ('10800', '一空八空空'),
            ('400000800', '四空空空空空八空空'),
            ('1230567890980654', '一二三空五六七八九空九八空六五四'),
            ('1300130013', '一三空空一三空空一三'),
            ('2000000022222', '二空空空空空空空二二二二二'),
            ('10000000000000000', '一空空空空空空空空空空空空空空空空'),
            ('0830', '空八三空'),
        ]
        for 問, 答 in 問答:
            if 答 is None:
                self.assertEqual(self.數字.是號碼無(問), False)
                self.assertEqual(self.數字.轉號碼('空', 問), 問)
            else:
                self.assertEqual(self.數字.是號碼無(問), True)
                self.assertEqual(self.數字.轉號碼('空', 問), 答)
                self.assertEqual(self.數字.轉號碼('零', 問),
                                 答.replace('空', '零'))
