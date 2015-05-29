# -*- coding: utf-8 -*-
from unittest.case import TestCase


from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
class 程式腳本單元試驗(TestCase):
	@classmethod
	def setUpClass(cls):
		cls.腳本=程式腳本()
	def test_空執行檔路徑加尾(self):
		self.assertEqual(self.腳本._執行檔路徑加尾(''),'')
	def test_根目錄執行檔路徑加尾(self):
		self.assertEqual(self.腳本._執行檔路徑加尾('/'),'/')
	def test_一般資料夾執行檔路徑加尾(self):
		self.assertEqual(
			self.腳本._執行檔路徑加尾('/home/git/mgiza/mgizapp/bin'),
			'/home/git/mgiza/mgizapp/bin/')
# 
# 	def test_細項目錄(self, 資料目錄, 細項名):
# 	def _陣列寫入檔案(self, 檔名, 陣列):
# 	def _字串寫入檔案(self, 檔名, 字串):
# 	def _讀檔案(self, 檔名):
# 	def _檔案合做一个(self, 平行檔名, 語言平行語料, 編碼器):