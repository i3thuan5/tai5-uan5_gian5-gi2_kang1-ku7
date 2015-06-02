# -*- coding: utf-8 -*-
import os
from unittest.case import TestCase
from 臺灣言語工具.系統整合.外部程式 import 外部程式

class 外部程式單元試驗(TestCase):
	def setUp(self):
		self.外部程式 = 外部程式()
		self.這馬目錄 = os.path.dirname(os.path.abspath(__file__))
	def test_空執行檔路徑加尾(self):
		路徑=os.path.abspath(os.path.join(self.這馬目錄,'..','..','外部程式'))
		self.assertEqual(self.外部程式.目錄(), 路徑)
