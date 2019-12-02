# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 維持本調


class 本調單元試驗(TestCase):
    def test_ptk入聲(self):
        原本 = ('k', 'ut', '8')
        變調了 = ('k', 'ut', '8')
        self.assertEqual(維持本調.變調(原本), 變調了)

    def test_有顯示名(self):
        self.assertEqual(str(維持本調), '本調#')
