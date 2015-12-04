# -*- coding: utf-8 -*-
import unittest
import os
from 臺灣言語工具.語音合成.音檔頭前表 import 音檔頭前表


class 音檔頭前表單元試驗(unittest.TestCase):
    def setUp(self):
        這馬所在 = os.path.dirname(os.path.abspath(__file__))
        self.音檔目錄 = os.path.join(這馬所在, '音檔')
        self.音檔 = os.path.join(self.音檔目錄, '我.wav')
        self.原始檔 = os.path.join(self.音檔目錄, '我.raw')

    def tearDown(self):
        pass

    def test_提掉頭前表(self):
        音 = open(self.音檔, 'rb')
        原始 = open(self.原始檔, 'rb')
        self.assertEqual(
            音檔頭前表.提掉(音.read()), 原始.read())
        音.close()
        原始.close()

    def test_加起哩頭前表(self):
        音 = open(self.音檔, 'rb')
        原始 = open(self.原始檔, 'rb')
        self.assertEqual(
            音檔頭前表.加起哩(原始.read(), 2, 16000, 1),
            音.read())
        音.close()
        原始.close()
