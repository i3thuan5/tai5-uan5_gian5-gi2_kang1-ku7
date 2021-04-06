# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.羅馬字.台語 import 白話字


class 白話字單元試驗(TestCase):

    def test_合法(self):
        self.assertIsNotNone(白話字('chhō͘').音標)

    def test_違法(self):
        self.assertIsNone(白話字('cō͘').音標)

    def test_違法轉教育部就mài改(self):
        self.assertIsNone(白話字('cō͘').轉換到臺灣閩南語羅馬字拼音())

    def test_音值(self):
        self.assertEqual(白話字('chō͘').音值(), ('ts', 'o', '7'))

    def test_無這音音值(self):
        self.assertIsNone(白話字('cō͘').音值())
