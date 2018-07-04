# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.基本物件.公用變數 import 敢是拼音字元


class 敢是拼音字元單元試驗(TestCase):

    def test_大寫(self):
        self.assertTrue(敢是拼音字元('A'))

    def test_調符(self):
        self.assertTrue(敢是拼音字元('ē'))

    def test_漢(self):
        self.assertFalse(敢是拼音字元('漢'))

    def test_漢羅(self):
        self.assertFalse(敢是拼音字元('媠sui2'))

    def test_羅漢(self):
        self.assertFalse(敢是拼音字元('sui媠'))

    def test_None(self):
        self.assertFalse(敢是拼音字元(None))

    def test_khang(self):
        self.assertFalse(敢是拼音字元(''))
