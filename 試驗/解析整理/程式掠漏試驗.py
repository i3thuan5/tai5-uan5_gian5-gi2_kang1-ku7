# -*- coding: utf-8 -*-
import unittest
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.程式掠漏 import 程式掠漏

class 程式掠漏試驗(unittest.TestCase):
	def setUp(self):
		self.掠漏 = 程式掠漏()
		self.分析器 = 拆文分析器()
	def tearDown(self):
		pass

	def test_毋是物件(self):
		self.掠漏.毋是字物件就毋著(self.分析器.建立字物件('語句'))
		self.掠漏.毋是詞物件就毋著(self.分析器.建立詞物件('語句'))
		self.掠漏.毋是組物件就毋著(self.分析器.建立組物件('語句'))
		self.掠漏.毋是集物件就毋著(self.分析器.建立集物件('語句'))
		self.掠漏.毋是句物件就毋著(self.分析器.建立句物件('語句'))
		self.掠漏.毋是章物件就毋著(self.分析器.建立章物件('語句'))
		self.assertRaises(型態錯誤, self.掠漏.毋是字物件就毋著, None)
		self.assertRaises(型態錯誤, self.掠漏.毋是詞物件就毋著, 2)
		self.assertRaises(型態錯誤, self.掠漏.毋是組物件就毋著, 'sui2')
		self.assertRaises(型態錯誤, self.掠漏.毋是集物件就毋著, '我')
		self.assertRaises(型態錯誤, self.掠漏.毋是句物件就毋著, self.分析器.建立章物件('語句'))
		self.assertRaises(型態錯誤, self.掠漏.毋是章物件就毋著, self.分析器.建立句物件('語句'))
		# 大部份工具攏會家己共無仝的物件分掉，所以賰的一定毋是物件，直接錯誤就好
		self.assertRaises(型態錯誤, self.掠漏.毋是字詞組集句章的毋著, '語句')
		self.assertRaises(型態錯誤, self.掠漏.毋是字詞組集句章的毋著, self.分析器.建立句物件('語句'))
