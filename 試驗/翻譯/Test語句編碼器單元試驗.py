# -*- coding: utf-8 -*-
import unittest

from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器


class 語句編碼器單元試驗(unittest.TestCase):
    def setUp(self):
        self.編碼器 = 語句編碼器()

    def tearDown(self):
        pass

    def test_𪜶飼pig(self):
        原 = '𪜶飼pig'
        後 = '\\U0002a736\\u98fcpig'
        self.assertEqual(self.編碼器.編碼(原), 後)
        self.assertEqual(self.編碼器.解碼(後), 原)
        self.assertEqual(self.編碼器.解碼(self.編碼器.編碼(原)), 原)
        self.assertEqual(self.編碼器.編碼(self.編碼器.解碼(後)), 後)
