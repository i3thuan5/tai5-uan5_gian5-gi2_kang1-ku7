# -*- coding: utf-8 -*-
import gzip
import io
import os
from itertools import zip_longest
from unittest.case import TestCase
from unittest.mock import call, patch

from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
from 臺灣言語工具.翻譯.摩西工具.無編碼器 import 無編碼器


class 程式腳本單元試驗(TestCase):
    def setUp(self):
        self.腳本 = 程式腳本()
        self.這馬目錄 = os.path.dirname(os.path.abspath(__file__))

    def test_空執行檔路徑加尾(self):
        self.assertEqual(self.腳本._執行檔路徑加尾(''), '')

    def test_根目錄執行檔路徑加尾(self):
        self.assertEqual(self.腳本._執行檔路徑加尾('/'), '/')

    def test_一般資料夾執行檔路徑加尾(self):
        self.assertEqual(
            self.腳本._執行檔路徑加尾('/home/git/mgiza/mgizapp/bin'),
            '/home/git/mgiza/mgizapp/bin/')

    def test_走正常指令(self):
        self.腳本._走指令('/bin/echo')

    def test_走正常指令陣列(self):
        self.腳本._走指令(['/bin/echo', 'tai5gi2'])

    def test_走正常指令有參數愛陣列(self):
        self.assertRaises(RuntimeError, self.腳本._走指令, '/bin/echo tai5gi2')

    def test_走錯誤正常指令(self):
        self.assertRaises(RuntimeError, self.腳本._走指令, '/bin/grep')

    def test_走錯誤正常指令陣列(self):
        self.assertRaises(RuntimeError, self.腳本._走指令, ['/bin/grep'])

    def test_走無指令(self):
        self.assertRaises(RuntimeError, self.腳本._走指令, '/bin/tai5gi2')

    def test_走無指令陣列(self):
        self.assertRaises(RuntimeError, self.腳本._走指令, ['/bin/tai5gi2'])

    def test_走指令錯誤輸出檔案(self):
        with io.open(os.path.join(self.這馬目錄, '暫檔'), 'w') as 檔案:
            self.assertRaises(RuntimeError,
                              self.腳本._走指令, ['/bin/grep', '----'], stdout=檔案)
        os.remove(os.path.join(self.這馬目錄, '暫檔'))

    def test_建細項目錄(self):
        if os.path.isdir(os.path.join(self.這馬目錄, '細項名')):
            os.rmdir(os.path.join(self.這馬目錄, '細項名'))
        self.腳本._細項目錄(self.這馬目錄, '細項名')
        self.assertTrue(os.path.isdir(os.path.join(self.這馬目錄, '細項名')))
        os.rmdir(os.path.join(self.這馬目錄, '細項名'))

    def test_建兩細項目錄嘛無要緊(self):
        self.腳本._細項目錄(self.這馬目錄, '細項名')
        self.腳本._細項目錄(self.這馬目錄, '細項名')
        os.rmdir(os.path.join(self.這馬目錄, '細項名'))

    def test_寫一般檔案(self):
        檔名 = os.path.join(self.這馬目錄, '文件.txt')
        self.腳本._陣列寫入檔案(檔名, ['臺灣', '建國'])
        with io.open(檔名, mode='rt') as 檔案:
            for 原本, 讀檔 in zip_longest(['臺灣', '建國'], 檔案.readlines()):
                self.assertEqual(原本, 讀檔.strip())
        os.remove(檔名)

    def test_讀寫一般檔案(self):
        檔名 = os.path.join(self.這馬目錄, '文件.txt')
        self.腳本._陣列寫入檔案(檔名, ['臺灣', '建國'])
        self.assertEqual(self.腳本._讀檔案(檔名), ['臺灣', '建國'])
        os.remove(檔名)

    def test_寫壓縮檔案(self):
        檔名 = os.path.join(self.這馬目錄, '文件.txt.gz')
        self.腳本._陣列寫入檔案(檔名, ['臺灣', '建國'])
        with gzip.open(檔名, mode='rt') as 檔案:
            for 原本, 讀檔 in zip_longest(['臺灣', '建國'], 檔案.readlines()):
                self.assertEqual(原本, 讀檔.strip())
        os.remove(檔名)

    def test_讀寫壓縮檔案(self):
        檔名 = os.path.join(self.這馬目錄, '文件.txt.gz')
        self.腳本._陣列寫入檔案(檔名, ['臺灣', '建國'])
        self.assertEqual(self.腳本._讀檔案(檔名), ['臺灣', '建國'])
        os.remove(檔名)

    @patch('臺灣言語工具.系統整合.程式腳本.程式腳本._字串寫入檔案')
    def test_寫檔案有用著字串(self, 字串mock):
        字串mock.return_value = '臺灣建國'
        檔名 = os.path.join(self.這馬目錄, '文件.txt.gz')
        self.腳本._陣列寫入檔案(檔名, ['臺灣', '建國'])
        字串mock.assert_called_once_with(檔名, '臺灣\n建國')

    def test_檔案合做一个(self):
        臺灣檔名 = os.path.join(self.這馬目錄, '臺灣.txt')
        self.腳本._字串寫入檔案(臺灣檔名, '臺灣')
        建國檔名 = os.path.join(self.這馬目錄, '建國.txt.gz')
        self.腳本._字串寫入檔案(建國檔名, '建國')
        上尾平行語料檔名 = os.path.join(self.這馬目錄, '文件.txt')
        self.腳本._檔案合做一个(上尾平行語料檔名, [臺灣檔名, 建國檔名], 無編碼器())
        self.assertEqual(self.腳本._讀檔案(上尾平行語料檔名), ['臺灣', '建國'])
        os.remove(臺灣檔名)
        os.remove(建國檔名)
        os.remove(上尾平行語料檔名)

    @patch('臺灣言語工具.翻譯.摩西工具.無編碼器.無編碼器.編碼')
    def test_檔案合做一个有用著編碼(self, 編碼mock):
        編碼mock.return_value = '臺灣建國'
        臺灣檔名 = os.path.join(self.這馬目錄, '臺灣.txt')
        self.腳本._字串寫入檔案(臺灣檔名, '臺灣')
        建國檔名 = os.path.join(self.這馬目錄, '建國.txt.gz')
        self.腳本._字串寫入檔案(建國檔名, '建國')
        上尾平行語料檔名 = os.path.join(self.這馬目錄, '文件.txt')
        self.腳本._檔案合做一个(上尾平行語料檔名, [臺灣檔名, 建國檔名], 無編碼器())
        編碼mock.assert_has_calls([call('臺灣'), call('建國')])
        os.remove(臺灣檔名)
        os.remove(建國檔名)
        os.remove(上尾平行語料檔名)

    def test_換目錄(self):
        原本目錄 = os.getcwd()
        self.assertNotEqual(os.getcwd(), self.這馬目錄)
        with self.腳本._換目錄(self.這馬目錄):
            self.assertEqual(os.getcwd(), self.這馬目錄)
        self.assertEqual(os.getcwd(), 原本目錄)
