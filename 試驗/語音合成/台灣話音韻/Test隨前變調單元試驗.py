# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 隨前變調


class 隨前變調單元試驗(TestCase):

    def test_一般韻_裡(self):
        原本 = ('l', 'i', '2')
        變調了 = ('l', 'i', '7')
        self.assertEqual(隨前變調('7').變調(原本), 變調了)

    def test_tsa̋ng__ê(self):
        原本 = ('ʔ', 'e', '5')
        變調了 = ('ʔ', 'e', '1')
        self.assertEqual(隨前變調('9').變調(原本), 變調了)

    def test_喉入聲_矣(self):
        原本 = ('ʔ', 'ah', '4')
        變調了 = ('ʔ', 'a', '3')
        self.assertEqual(隨前變調('3').變調(原本), 變調了)

    def test_ptk入聲_揣無例_假設有_中(self):
        原本 = ('g', 'iap', '8')
        變調了 = ('g', 'iap', '4')
        self.assertEqual(隨前變調('7').變調(原本), 變調了)

    def test_ptk入聲_揣無例_假設有_低(self):
        原本 = ('t', 'ik', '8')
        變調了 = ('t', 'ik', '10')
        self.assertEqual(隨前變調('2').變調(原本), 變調了)

    def test_有顯示名(self):
        self.assertEqual(str(隨前變調('2')), '隨前變調@')
