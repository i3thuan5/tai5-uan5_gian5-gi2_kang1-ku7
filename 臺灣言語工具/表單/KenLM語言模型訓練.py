# -*- coding: utf-8 -*-
import os
from 臺灣言語工具.翻譯.摩西工具.無編碼器 import 無編碼器
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本

class KenLM語言模型訓練(程式腳本):
	def 訓練(self, 語料,
			暫存資料夾,
			連紲詞長度=3,
			編碼器=無編碼器(),
			MOSES資料夾路徑=''):
		os.makedirs(暫存資料夾, exist_ok=True)
		目標語言檔名 = os.path.join(暫存資料夾, '語言模型.txt')
		self._檔案合做一个(目標語言檔名, 語料, 編碼器)
		語言模型檔 = os.path.join(暫存資料夾, '語言模型.lm')
		語言模型指令版 = \
			'{0}bin/lmplz -o {1} -S 80% -T /tmp < {2} > {3}'
		語言模型指令 = 語言模型指令版.format(
			self._執行檔路徑加尾(MOSES資料夾路徑),
			連紲詞長度,
			目標語言檔名,
			語言模型檔
			)
		self._走指令(語言模型指令)
		return 語言模型檔
