# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 輕聲


class 輕聲單元試驗(TestCase):

    def test_輕聲(self):
        原本 = ('s', 'i', '2')
        變調了 = ('s', 'i', '3')
        self.assertEqual(輕聲.變調(原本), 變調了)

    def test_喉入聲(self):
        原本 = ('ʔ', 'ah', '4')
        變調了 = ('ʔ', 'a', '3')
        self.assertEqual(輕聲.變調(原本), 變調了)

    def test_ptk入聲(self):
        原本 = ('tsh', 'it', '4')
        變調了 = ('tsh', 'it', '10')
        self.assertEqual(輕聲.變調(原本), 變調了)

    def test_輕聲無調(self):
        原本 = ('s', 'i', '0')
        變調了 = ('s', 'i', '3')
        self.assertEqual(輕聲.變調(原本), 變調了)

    def test_喉入聲無調(self):
        原本 = ('ʔ', 'ah', '0')
        變調了 = ('ʔ', 'a', '3')
        self.assertEqual(輕聲.變調(原本), 變調了)

    def test_ptk入聲無調(self):
        原本 = ('tsh', 'it', '0')
        變調了 = ('tsh', 'it', '10')
        self.assertEqual(輕聲.變調(原本), 變調了)

    def test_第9調_揣無例_先假設(self):
        原本 = ('s', 'i', '9')
        變調了 = ('s', 'i', '3')
        self.assertEqual(輕聲.變調(原本), 變調了)
