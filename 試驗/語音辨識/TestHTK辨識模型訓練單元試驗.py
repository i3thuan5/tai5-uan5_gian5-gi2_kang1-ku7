# -*- coding: utf-8 -*-
import os
from os.path import join
from tempfile import mkdtemp
from unittest.case import TestCase
from 臺灣言語工具.語音辨識.HTK工具.HTK辨識模型訓練 import HTK辨識模型訓練
from unittest.mock import patch
from 臺灣言語工具.語音辨識.HTK工具.安裝HTK語音辨識程式 import 安裝HTK語音辨識程式


class HTK辨識模型訓練單元試驗(TestCase):

    def test_混合數重估數愛仝(self):
        self.assertEqual(
            HTK辨識模型訓練.混合數重估擺 + HTK辨識模型訓練.混合數上尾重估擺,
            HTK辨識模型訓練.上尾重估擺
        )

    def test_音節標仔加短恬(self):
        結果 = HTK辨識模型訓練._音節標仔加短恬(
            ['sil', 'sui2', 'sui2', 'sil']
        )
        self.assertEqual(
            結果,
            ['sil', 'sui2', 'sp', 'sui2', 'sil']
        )

    def test_檔案前後愛加短恬(self):
        結果 = HTK辨識模型訓練._音節標仔加短恬(
            ['sui2']
        )
        self.assertEqual(
            結果,
            ['sp', 'sui2', 'sp']
        )

    def test_短恬愛加佇標仔內(self):
        結果 = HTK辨識模型訓練._音節標仔加短恬(
            [
                '#!MLF!#',
                '"*/01.lab"', 'sui2', '.',
                '"*/02.lab"', 'sil', '.'
            ]
        )
        self.assertEqual(
            結果,
            [
                '#!MLF!#',
                '"*/01.lab"', 'sp', 'sui2', 'sp', '.',
                '"*/02.lab"', 'sil', '.'
            ]
        )

    def test_恬音節標仔加短恬(self):
        結果 = HTK辨識模型訓練._音節標仔加短恬(
            ['sil']
        )
        self.assertEqual(
            結果,
            ['sil']
        )

    def test_恬音節邊仔莫加短恬(self):
        結果 = HTK辨識模型訓練._音節標仔加短恬(
            ['sil', 'sui2', 'sil', 'sui2', 'sui2', 'sil']
        )
        self.assertEqual(
            結果,
            ['sil', 'sui2', 'sil', 'sui2', 'sp', 'sui2', 'sil']
        )

    def test_短恬音節邊仔莫加短恬(self):
        結果 = HTK辨識模型訓練._音節標仔加短恬(
            ['sil', 'sui2', 'sp', 'sui2', 'sui2', 'sil']
        )
        self.assertEqual(
            結果,
            ['sil', 'sui2', 'sp', 'sui2', 'sp', 'sui2', 'sil']
        )

    def test_加短恬(self):
        這馬目錄 = os.path.dirname(os.path.abspath(__file__))
        無短恬的模型 = os.path.join(這馬目錄, '試料', '無短恬的模型')
        試加短恬的模型 = os.path.join(這馬目錄, '試料', '試加短恬的模型')
        加短恬的模型 = os.path.join(這馬目錄, '試料', '加短恬的模型')
        HTK辨識模型訓練._模型加短恬(無短恬的模型, 試加短恬的模型)
        self.assertEqual(
            HTK辨識模型訓練._讀檔案(試加短恬的模型),
            HTK辨識模型訓練._讀檔案(加短恬的模型)
        )
        os.remove(試加短恬的模型)

    @patch('shutil.copy')
    @patch('臺灣言語工具.系統整合.程式腳本.程式腳本._走指令')
    def test_模型重估調整參數失敗一擺了成功(self, 走指令mock, 複製檔案mock):
        暫時資料夾 = mkdtemp()
        暫時檔案 = join(暫時資料夾, '暫時檔案')
        模型所在 = join(暫時資料夾, '模型.macro')
        走指令mock.side_effect = [RuntimeError(), None, None]

        HTK辨識模型訓練._模型重估(
            安裝HTK語音辨識程式.htk執行檔目錄(), 暫時資料夾, 暫時檔案, 暫時檔案, 暫時檔案, 模型所在, 1
        )
        self.assertEqual(走指令mock.call_count, 2)

    @patch('shutil.copy')
    @patch('臺灣言語工具.系統整合.程式腳本.程式腳本._走指令')
    def test_模型重估調整參數失敗兩擺了成功(self, 走指令mock, 複製檔案mock):
        暫時資料夾 = mkdtemp()
        暫時檔案 = join(暫時資料夾, '暫時檔案')
        模型所在 = join(暫時資料夾, '模型.macro')
        走指令mock.side_effect = [RuntimeError(), RuntimeError(), None]

        HTK辨識模型訓練._模型重估(
            安裝HTK語音辨識程式.htk執行檔目錄(), 暫時資料夾, 暫時檔案, 暫時檔案, 暫時檔案, 模型所在, 1
        )
        self.assertEqual(走指令mock.call_count, 3)

    @patch('shutil.copy')
    @patch('臺灣言語工具.系統整合.程式腳本.程式腳本._走指令')
    def test_模型重估調整參數無效三擺攏失敗(self, 走指令mock, 複製檔案mock):
        暫時資料夾 = mkdtemp()
        暫時檔案 = join(暫時資料夾, '暫時檔案')
        模型所在 = join(暫時資料夾, '模型.macro')
        走指令mock.side_effect = [RuntimeError(), RuntimeError(), RuntimeError()]

        with self.assertRaises(RuntimeError):
            HTK辨識模型訓練._模型重估(
                安裝HTK語音辨識程式.htk執行檔目錄(), 暫時資料夾, 暫時檔案, 暫時檔案, 暫時檔案, 模型所在, 1
            )
        self.assertEqual(走指令mock.call_count, 3)
