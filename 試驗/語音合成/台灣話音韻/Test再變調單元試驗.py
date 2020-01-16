# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 再變調


class 再變調單元試驗(TestCase):

    def test_再變調(self):
        原本 = ('kh', 'i', '3')
        變調了 = ('kh', 'i', '1')
        self.assertEqual(再變調.變調(原本), 變調了)

    def test_喉入聲(self):
        原本 = ('b', 'eh', '4')
        變調了 = ('b', 'e', '1')
        self.assertEqual(再變調.變調(原本), 變調了)

    def test_有顯示名(self):
        self.assertEqual(str(再變調), '再變調$')

    def test_無合法的音標愛錯誤(self):
        with self.assertRaises(解析錯誤):
            再變調.變調(('g', 'ua', '0'))
        with self.assertRaises(解析錯誤):
            再變調.變調(('g', 'ua', '4'))
        with self.assertRaises(解析錯誤):
            再變調.變調(('g', 'uah', '2'))
        with self.assertRaises(解析錯誤):
            再變調.變調(('g', 'uat', '2'))
