# -*- coding: utf-8 -*-
import unittest
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚

class 文章粗胚數字英文中央加分字單元試驗(unittest.TestCase):
	def setUp(self):
		self.粗胚 = 文章粗胚()
	def tearDown(self):
		pass

	def test_全加無空白分開的閩南語音標(self):
		答案 = 'sui2-sui2-e5-koo1-niu5'
		原本 = 答案.replace('-', '')
		結果 = self.粗胚.數字英文中央全加分字符號(原本)
		self.assertEqual(結果, 答案)
		
	def test_全加無空白分開的音調音標(self):
		答案 = 'sui55-sui51-e13-koo33-niu13'
		原本 = 答案.replace(' ', '')
		結果 = self.粗胚.數字英文中央全加分字符號(原本)
		self.assertEqual(結果, 答案)
		
	def test_全加大寫專有符號(self):
		原本 = 'H1N1 新型 流感 包含 四種 病毒'
		答案 = 'H1-N1 新型 流感 包含 四種 病毒'
		結果 = self.粗胚.數字英文中央全加分字符號(原本)
		self.assertEqual(結果, 答案)
		
	def test_全加小寫專有符號(self):
		原本 = 'g0v 是 咱 的 好 厝邊'
		答案 = 'g0-v 是 咱 的 好 厝邊'
		結果 = self.粗胚.數字英文中央全加分字符號(原本)
		self.assertEqual(結果, 答案)
		
	def test_全加對齊組大寫音標袂使拆開(self):
		原本 = 'Sui2sui2 是 咱 的 好 厝邊'
		答案 = 'Sui2-sui2 是 咱 的 好 厝邊'
		結果 = self.粗胚.數字英文中央全加分字符號(原本)
		self.assertEqual(結果, 答案)
		
	def test_全加對齊組小寫音標袂使拆開(self):
		原本 = 'sui2sui2 是 咱 的 好 厝邊'
		答案 = 'sui2-sui2 是 咱 的 好 厝邊'
		結果 = self.粗胚.數字英文中央全加分字符號(原本)
		self.assertEqual(結果, 答案)

	def test_看情形大寫專有符號袂使拆開(self):
		原本 = 'H1N1 新型 流感 包含 四種 病毒'
		結果 = self.粗胚.數字英文中央看情形加分字符號(原本, {'H1N1'})
		self.assertEqual(結果, 原本)
		
	def test_看情形小寫專有符號袂使拆開(self):
		原本 = 'g0v 是 咱 的 好 厝邊'
		結果 = self.粗胚.數字英文中央看情形加分字符號(原本, {'g0v'})
		self.assertEqual(結果, 原本)
		
	def test_看情形對齊組大寫音標袂使拆開(self):
		原本 = 'Sui2sui2 是 咱 的 好 厝邊'
		結果 = self.粗胚.數字英文中央看情形加分字符號(原本, {'Sui2Sui2'})
		self.assertEqual(結果, 原本)
		
	def test_看情形對齊組小寫音標袂使拆開(self):
		原本 = 'sui2sui2 是 咱 的 好 厝邊'
		結果 = self.粗胚.數字英文中央看情形加分字符號(原本, {'sui2sui2'})
		self.assertEqual(結果, 原本)
