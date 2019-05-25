# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 三連音變調


class 三連音變調單元試驗(TestCase):

    def test_一般韻(self):
        原本 = ('s', 'ui', '2')
        變調了 = ('s', 'ui', '1')
        self.assertEqual(三連音變調.變調(原本), 變調了)

    def test_喉入聲(self):
        原本 = ('b', 'ah', '4')
        變調了 = ('b', 'a', '2')
        self.assertEqual(三連音變調.變調(原本), 變調了)

    def test_ptk入聲(self):
        原本 = ('t', 'it', '8')
        變調了 = ('t', 'it', '9')
        self.assertEqual(三連音變調.變調(原本), 變調了)

    def test_第9調_揣無例_先假設(self):
        原本 = ('ts', 'aŋ', '9')
        變調了 = ('ts', 'aŋ', '9')
        self.assertEqual(三連音變調.變調(原本), 變調了)

    def test_無合法的音標愛錯誤(self):
        with self.assertRaises(解析錯誤):
            三連音變調.變調(('g', 'ua', '0'))
        with self.assertRaises(解析錯誤):
            三連音變調.變調(('g', 'ua', '4'))
        with self.assertRaises(解析錯誤):
            三連音變調.變調(('g', 'uah', '2'))
        with self.assertRaises(解析錯誤):
            三連音變調.變調(('g', 'uat', '2'))
