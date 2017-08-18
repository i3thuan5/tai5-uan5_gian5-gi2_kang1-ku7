# -*- coding: utf-8 -*-
import os
from shutil import rmtree
from unittest.case import TestCase


from 臺灣言語工具.語言模型.KenLM語言模型訓練 import KenLM語言模型訓練
from 臺灣言語工具.翻譯.摩西工具.無編碼器 import 無編碼器
from 臺灣言語工具.語言模型.安裝KenLM訓練程式 import 安裝KenLM訓練程式


class KenLM訓練程式kenlm整合試驗(TestCase):
    忍受 = 1e-7

    @classmethod
    def setUpClass(cls):
        安裝KenLM訓練程式.安裝kenlm()

    def setUp(self):
        self.這馬目錄 = os.path.dirname(os.path.abspath(__file__))
        資料目錄 = os.path.join(self.這馬目錄, '語料')
        self.閩南語語料陣列 = [os.path.join(資料目錄, '文本.txt'), ]

    def test_路徑設定毋著(self):
        with self.assertRaises(FileNotFoundError):
            KenLM語言模型訓練('/', '/')

    def test_訓練模型(self):
        self.模型訓練 = KenLM語言模型訓練()
        模型檔 = self.模型訓練.訓練(
            self.閩南語語料陣列,
            os.path.join(self.這馬目錄, '暫存資料夾'),
            連紲詞長度=1,
            編碼器=無編碼器(),
            使用記憶體量='20%',
        )
        self.assertTrue(os.path.isfile(模型檔))

        # 刣掉訓練出來的模型
        rmtree(os.path.join(self.這馬目錄, '暫存資料夾'))
