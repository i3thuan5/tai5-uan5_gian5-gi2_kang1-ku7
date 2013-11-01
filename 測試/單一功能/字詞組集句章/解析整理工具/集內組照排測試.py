from unittest.case import TestCase
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 斷詞標音.排標音結果 import 排標音結果
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.解析整理工具.集內組照排 import 集內組照排
from 字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡

class 集內組照排測試(TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.組照排=集內組照排()

	def tearDown(self):
		pass

	def test_白文照排(self):
		排標音 = 排標音結果()
		白詞 = self.分析器.建立詞物件('泅水')
		白詞.屬性 = {排標音.白話層:1, 排標音.文讀層:0}
		白組= self.分析器.建立組物件('')
		白組.內底詞.append(白詞)
		文詞 = self.分析器.建立詞物件('游泳')
		文詞.屬性 = {排標音.白話層:0, 排標音.文讀層:1}
		文組= self.分析器.建立組物件('')
		文組.內底詞.append(文詞)
		顛倒集=集()
		顛倒集.內底組=[文組,白組]
		答案集=集()
		答案集.內底組=[白組,文組]
		self.assertEqual(排標音.照白文層排(顛倒集), 答案集)
		self.assertEqual(排標音.照白文層排(答案集), 答案集)

	def test_型照排(self):
		顛倒集=集([self.分析器.建立組物件('1一'),self.分析器.建立組物件('0零')])
		答案集=集([self.分析器.建立組物件('0零'),self.分析器.建立組物件('1一')])
		譀鏡=物件譀鏡()
		排法=lambda 組物件:譀鏡.看型(組物件)
		self.assertEqual(self.組照排.排好(排法, 顛倒集), 答案集)
		self.assertEqual(self.組照排.排好(排法, 答案集), 答案集)
		
	def test_排句(self):
		self.assertEqual(0, 1)
	def test_排章(self):
		self.assertEqual(0, 1)
	def test_排章多句多集(self):
		self.assertEqual(0, 1)
