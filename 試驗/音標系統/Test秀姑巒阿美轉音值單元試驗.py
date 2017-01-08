# -*- coding: utf-8 -*-
from unittest.case import TestCase


class 秀姑巒阿美轉音值單元試驗(TestCase):

    def test_一般(self):
        self.assertEqual(秀姑巒阿美("kako").音值(), [['k', 'a'], ['k', 'u']])

    def test_一个符號(self):
        self.assertEqual(秀姑巒阿美("o").音值(), [['o']])

    def test_ng(self):
        self.assertEqual(秀姑巒阿美("nga'ay").音值(), [['ŋ', 'a'], ['ʔ', 'a', 'y']])

    def test_大寫(self):
        self.assertEqual(秀姑巒阿美("O").音值(), [['o']])

    def test_無合法(self):
        self.assertEqual(秀姑巒阿美("！").音值(), None)
