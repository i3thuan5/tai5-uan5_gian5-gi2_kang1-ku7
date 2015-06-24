# -*- coding: utf-8 -*-
import unittest
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔


class 揀集內組單元試驗(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.粗胚 = 文章粗胚()
		self.網仔 = 詞物件網仔()

	def tearDown(self):
		pass
	
	@unittest.expectedFailure
	def test_章物件(self):
		raise NotImplementedError
		self.assertEqual(0, 1)
		#空集
# 	def test_章句集物件(self):
# 	def test_組詞字物件(self):
