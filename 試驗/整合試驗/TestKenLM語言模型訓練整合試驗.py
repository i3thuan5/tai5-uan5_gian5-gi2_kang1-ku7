# -*- coding: utf-8 -*-
import os
from unittest.case import TestCase


from 臺灣言語工具.語言模型.KenLM語言模型訓練 import KenLM語言模型訓練
from 臺灣言語工具.翻譯.摩西工具.無編碼器 import 無編碼器
from shutil import rmtree
'''
甲乙丙
數量=C(丙), C(乙丙), C(甲乙丙)
機率=P(丙), P(乙丙), P(甲乙丙)
條件=P(丙), P(乙丙)/P(乙), P(甲乙丙)/P(甲乙)
'''
class KenLM語言模型訓練整合試驗(TestCase):
	忍受 = 1e-7
	def setUp(self):
		self.這馬目錄 = os.path.dirname(os.path.abspath(__file__))
		資料目錄 = os.path.join(self.這馬目錄, '翻譯語料')
		self.閩南語語料陣列 = [os.path.join(資料目錄, '閩'), ]
	def tearDown(self):
		pass
	def test_路徑設定毋著(self):
		self.assertRaises(FileNotFoundError, KenLM語言模型訓練, '/')
	def test_訓練模型(self):
		self.模型訓練 = KenLM語言模型訓練('/home/tshau/git/mosesdecoder-depth1')
		模型檔 = self.模型訓練.訓練(self.閩南語語料陣列,
				os.path.join(self.這馬目錄, '暫存資料夾'),
				連紲詞長度=2,
				編碼器=無編碼器(),
				使用記憶體量='20%',
			)
		self.assertTrue(os.path.isfile(模型檔))
	
		# 刣掉訓練出來的模型
		rmtree(os.path.join(self.這馬目錄, '暫存資料夾'))
