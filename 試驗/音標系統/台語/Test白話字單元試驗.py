# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.音標系統.台語 import 白話字


class 白話字單元試驗(TestCase):

    def test_合法(self):
        self.assertIsNotNone(白話字('chhō͘').音標)

    def test_違法(self):
        self.assertIsNone(白話字('cō͘').音標)
