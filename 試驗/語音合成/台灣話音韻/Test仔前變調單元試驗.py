# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 仔前變調


class 仔前變調單元試驗(TestCase):

    def test_一般韻(self):
        原本 = ('t', 'i', '1')
        變調了 = ('t', 'i', '7')
        self.assertEqual(仔前變調.變調(原本), 變調了)

    def test_喉入聲(self):
        原本 = ('tsh', 'ioh', '8')
        變調了 = ('tsh', 'io', '7')
        self.assertEqual(仔前變調.變調(原本), 變調了)

    def test_ptk入聲(self):
        原本 = ('g', 'iap', '8')
        變調了 = ('g', 'iap', '4')
        self.assertEqual(仔前變調.變調(原本), 變調了)

    def test_sió_khua̋_á(self):
        原本 = ('kh', 'ua', '9')
        變調了 = ('kh', 'ua', '9')
        self.assertEqual(仔前變調.變調(原本), 變調了)

    def test_無合法的音標愛錯誤(self):
        with self.assertRaises(解析錯誤):
            仔前變調.變調(('g', 'ua', '0'))
        with self.assertRaises(解析錯誤):
            仔前變調.變調(('g', 'ua', '4'))
        with self.assertRaises(解析錯誤):
            仔前變調.變調(('g', 'uah', '2'))
        with self.assertRaises(解析錯誤):
            仔前變調.變調(('g', 'uat', '2'))
