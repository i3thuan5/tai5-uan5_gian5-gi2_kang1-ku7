# -*- coding: utf-8 -*-
import os
from unittest.case import TestCase


from 臺灣言語工具.翻譯.摩西工具.摩西翻譯模型訓練 import 摩西翻譯模型訓練


class 摩西翻譯模型訓練單元試驗(TestCase):

    def setUp(self):
        self.這馬目錄 = os.path.dirname(os.path.abspath(__file__))

    def test_空執行檔路徑加尾(self):
        self.assertEqual(摩西翻譯模型訓練._執行檔路徑加尾(''), '')

    def test_根目錄執行檔路徑加尾(self):
        self.assertEqual(摩西翻譯模型訓練._執行檔路徑加尾('/'), '/')

    def test_一般資料夾執行檔路徑加尾(self):
        self.assertEqual(
            摩西翻譯模型訓練._執行檔路徑加尾('/home/git/mgiza/mgizapp/bin'),
            '/home/git/mgiza/mgizapp/bin/')
