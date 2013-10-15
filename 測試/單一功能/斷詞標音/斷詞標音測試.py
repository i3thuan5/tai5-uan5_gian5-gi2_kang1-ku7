from unittest.case import TestCase
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 斷詞標音.型音辭典 import 型音辭典

class 斷詞標音測試(TestCase):
	def setUp(self):
		self.字典 = 型音辭典()
		self.初胚工具 = 文章初胚工具()
		self.分析器 = 拆文分析器()
		self.詞物件 = self.分析器.建立詞物件('你好無？')
		self.詞音標 = self.分析器.建立詞物件('li2-hoo2 bo5?')
		self.對齊詞 = self.分析器.產生對齊詞('你好無？', 'li2-hoo2 bo5?')
	def tearDown(self):
		pass
	def test_漢字加詞成功無(self):
		self.字典.加詞(self.詞物件)
		self.assertEqual(self.字典.查詞(self.詞物件), [self.詞物件])

	def test_多對齊加詞成功無(self):
		self.字典.加詞(self.對齊詞)
		self.字典.加詞(self.對齊詞)
		self.assertEqual(self.字典.查詞(self.對齊詞), [self.對齊詞, self.對齊詞])

	def test_查對齊詞成功無(self):
		self.字典.加詞(self.對齊詞)
		self.assertEqual(self.字典.查詞(self.詞物件), [self.對齊詞])
		self.assertEqual(self.字典.查詞(self.詞音標), [self.對齊詞])
		self.assertEqual(self.字典.查詞(self.對齊詞), [self.對齊詞])


