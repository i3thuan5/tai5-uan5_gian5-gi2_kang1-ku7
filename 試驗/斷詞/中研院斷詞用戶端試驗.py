# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
import unittest
from unittest.mock import patch, call


from 臺灣言語工具.斷詞.中研院.斷詞用戶端 import 斷詞用戶端
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本元素.組 import 組
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.基本元素.章 import 章
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔

@patch('臺灣言語工具.斷詞.中研院.斷詞用戶端.斷詞用戶端.語句斷詞做語句')
class 中研院斷詞用戶端試驗(unittest.TestCase):
	def setUp(self):
		self.用戶端 = 斷詞用戶端()
		
		self.分析器 = 拆文分析器()
		self.網仔 = 詞物件網仔()
	def tearDown(self):
		pass

	def test_物件斷一句話句物件內容(self, 語句斷詞做語句mock):
		輸入句物件 = self.分析器.建立句物件('我想吃飯。')
		語句斷詞做語句mock.return_value = [
			'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)'
			]
		斷詞後章物件 = self.用戶端.斷物件詞(輸入句物件)
		答案組物件 = 組()
		答案組物件.內底詞 = [
				self.分析器.建立詞物件('我'),
				self.分析器.建立詞物件('想'),
				self.分析器.建立詞物件('吃飯'),
				self.分析器.建立詞物件('。'),
			]
		答案集物件 = 集()
		答案集物件.內底組 = [答案組物件]
		答案句物件 = 句()
		答案句物件.內底集 = [答案集物件]
		答案章物件 = 章()
		答案章物件.內底集 = [答案句物件]
		self.assertEqual(斷詞後章物件, 答案章物件)
	def test_物件斷一句話句物件詞性(self, 語句斷詞做語句mock):
		輸入句物件 = self.分析器.建立句物件('我想吃飯。')
		語句斷詞做語句mock.return_value = [
			'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)'
			]
		斷詞後章物件 = self.用戶端.斷物件詞(輸入句物件)
		for 詞物件, 詞性 in zip(
					self.網仔.網出詞物件(斷詞後章物件),
					['N', 'Vt', 'Vi', 'PERIODCATEGORY']
				, 語句斷詞做語句mock):
			self.assertEqual(詞物件.屬性['詞性'], 詞性)
	def test_物件斷一句話章物件內容(self, 語句斷詞做語句mock):
		輸入章物件 = self.分析器.建立章物件('我想吃飯。')
		語句斷詞做語句mock.return_value = [
			'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)'
			]
		斷詞後章物件 = self.用戶端.斷物件詞(輸入章物件)
		答案組物件 = 組()
		答案組物件.內底詞 = [
				self.分析器.建立詞物件('我'),
				self.分析器.建立詞物件('想'),
				self.分析器.建立詞物件('吃飯'),
				self.分析器.建立詞物件('。'),
			]
		答案集物件 = 集()
		答案集物件.內底組 = [答案組物件]
		答案句物件 = 句()
		答案句物件.內底集 = [答案集物件]
		答案章物件 = 章()
		答案章物件.內底集 = [答案句物件]
		self.assertEqual(斷詞後章物件, 答案章物件)
	def test_物件斷一句話章物件詞性(self, 語句斷詞做語句mock):
		輸入章物件 = self.分析器.建立章物件('我想吃飯。')
		語句斷詞做語句mock.return_value = [
			'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)'
			]
		斷詞後章物件 = self.用戶端.斷物件詞(輸入章物件)
		for 詞物件, 詞性 in zip(
					self.網仔.網出詞物件(斷詞後章物件),
					['N', 'Vt', 'Vi', 'PERIODCATEGORY']
				, 語句斷詞做語句mock):
			self.assertEqual(詞物件.屬性['詞性'], 詞性)
	@patch('臺灣言語工具.斷詞.中研院.斷詞用戶端.斷詞用戶端._斷句物件詞')
	def test_物件斷一逝字(self, 斷句物件詞mock, 語句斷詞做語句mock):
		輸入章物件 = self.分析器.建立章物件('我想吃飯。我想吃很多飯。')
		語句斷詞做語句mock.return_value = [
				'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
				'\u3000我(N)\u3000想(Vt)\u3000吃(Vt)\u3000很多(DET)\u3000飯(N)\u3000。(PERIODCATEGORY)',
			]
		self.用戶端.斷物件詞(輸入章物件)
		斷句物件詞mock.assert_has_calls([
				call(self.分析器.建立句物件('我想吃飯。')),
				call(self.分析器.建立句物件('我想吃很多飯。'))
			])
	def test_物件上尾有換逝符號詞數檢查(self, 語句斷詞做語句mock):
		輸入章物件 = self.分析器.建立章物件('我想吃飯。\n')
		語句斷詞做語句mock.return_value = [
				'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
			]
		斷詞後章物件 = self.用戶端.斷物件詞(輸入章物件)
		self.assertEqual(
				self.網仔.網出詞物件(輸入章物件),
				self.網仔.網出詞物件(斷詞後章物件),
			)
	def test_物件上尾有換逝符號結構檢查(self, 語句斷詞做語句mock):
		輸入章物件 = self.分析器.建立章物件('我想吃飯。\n')
		語句斷詞做語句mock.return_value = [
				'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
			]
		斷詞後章物件 = self.用戶端.斷物件詞(輸入章物件)
		答案組物件 = 組()
		答案組物件.內底詞 = [
				self.分析器.建立詞物件('我'),
				self.分析器.建立詞物件('想'),
				self.分析器.建立詞物件('吃飯'),
				self.分析器.建立詞物件('。'),
				self.分析器.建立詞物件('\n'),
			]
		答案集物件 = 集()
		答案集物件.內底組 = [答案組物件]
		答案句物件 = 句()
		答案句物件.內底集 = [答案集物件]
		答案章物件 = 章()
		答案章物件.內底集 = [答案句物件]
		self.assertEqual(斷詞後章物件, 答案章物件)
	def test_物件上尾有換逝符號詞性檢查(self, 語句斷詞做語句mock):
		輸入章物件 = self.分析器.建立章物件('我想吃飯。\n')
		語句斷詞做語句mock.return_value = [
				'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
			]
		斷詞後章物件 = self.用戶端.斷物件詞(輸入章物件)
		for 詞物件, 詞性 in zip(
					self.網仔.網出詞物件(斷詞後章物件),
					['N', 'Vt', 'Vi', 'PERIODCATEGORY', '']
				, 語句斷詞做語句mock):
			self.assertEqual(詞物件.屬性['詞性'], 詞性)
	def test_物件空白逝句物件詞數檢查(self, 語句斷詞做語句mock):
		輸入章物件 = self.分析器.建立章物件('\n \n')
		語句斷詞做語句mock.return_value = []
		斷詞後章物件 = self.用戶端.斷物件詞(輸入章物件)
		self.assertEqual(
				self.網仔.網出詞物件(輸入章物件),
				self.網仔.網出詞物件(斷詞後章物件),
			)
	def test_物件空白逝句物件結構檢查(self, 語句斷詞做語句mock):
		輸入章物件 = self.分析器.建立章物件('\n \n')
		語句斷詞做語句mock.return_value = []
		斷詞後章物件 = self.用戶端.斷物件詞(輸入章物件)
		答案組物件 = 組()
		答案組物件.內底詞 = [
				self.分析器.建立詞物件('\n'),
				self.分析器.建立詞物件('\n'),
			]
		答案集物件 = 集()
		答案集物件.內底組 = [答案組物件]
		答案句物件 = 句()
		答案句物件.內底集 = [答案集物件]
		答案章物件 = 章()
		答案章物件.內底集 = [答案句物件]
		self.assertEqual(斷詞後章物件, 答案章物件)
	def test_物件空白逝句物件詞性檢查(self, 語句斷詞做語句mock):
		輸入章物件 = self.分析器.建立章物件('\n \n')
		語句斷詞做語句mock.return_value = []
		斷詞後章物件 = self.用戶端.斷物件詞(輸入章物件)
		for 詞物件, 詞性 in zip(
					self.網仔.網出詞物件(斷詞後章物件),
					['', '']
				, 語句斷詞做語句mock):
			self.assertEqual(詞物件.屬性['詞性'], 詞性)

	def test_結構斷一句話(self, 語句斷詞做語句mock):
		語句斷詞做語句mock.return_value = [
				'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
			]
		self.assertEqual(self.用戶端.語句斷詞後結構化('我想吃飯。'), [[
			[('我', 'N'), ('想', 'Vt'), ('吃飯', 'Vi'), ('。', 'PERIODCATEGORY')],
			]])
	def test_結構斷一逝字(self, 語句斷詞做語句mock):
		語句斷詞做語句mock.return_value = [
				'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
				'\u3000我(N)\u3000想(Vt)\u3000吃(Vt)\u3000很多(DET)\u3000飯(N)\u3000。(PERIODCATEGORY)',
			]
		self.assertEqual(self.用戶端.語句斷詞後結構化('我想吃飯。我想吃很多飯。'), [[
			[('我', 'N'), ('想', 'Vt'), ('吃飯', 'Vi'), ('。', 'PERIODCATEGORY')],
			[('我', 'N'), ('想', 'Vt'), ('吃', 'Vt'), ('很多', 'DET'), ('飯', 'N'), ('。', 'PERIODCATEGORY')]
			]])
	def test_結構斷兩逝字(self, 語句斷詞做語句mock):
		語句斷詞做語句mock.return_value = [
				'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
				'\u3000我(N)\u3000想(Vt)\u3000吃(Vt)\u3000很多(DET)\u3000飯(N)\u3000。(PERIODCATEGORY)',
				'\u3000',
				'\u3000我(N)\u3000吃飽(Vi)\u3000了(T)\u3000。(PERIODCATEGORY)',
			]
		self.assertEqual(self.用戶端.語句斷詞後結構化('我想吃飯。我想吃很多飯。\n我吃飽了。'), [
			[
				[('我', 'N'), ('想', 'Vt'), ('吃飯', 'Vi'), ('。', 'PERIODCATEGORY')],
				[('我', 'N'), ('想', 'Vt'), ('吃', 'Vt'), ('很多', 'DET'), ('飯', 'N'), ('。', 'PERIODCATEGORY')]
			],
			[
				[('我', 'N'), ('吃飽', 'Vi'), ('了', 'T'), ('。', 'PERIODCATEGORY')],
			],
			])
	def test_結構斷大於符號(self, 語句斷詞做語句mock):
		語句斷詞做語句mock.return_value = [
				'\u3000我(N)\u3000想(Vt)\u3000)(PARENTHESISCATEGORY)\u3000:(COLONCATEGORY)\u3000&gt;(PARENTHESISCATEGORY)'
			]
		self.assertEqual(self.用戶端.語句斷詞後結構化('我想) :>'), [[
			[('我', 'N'), ('想', 'Vt'), (')', 'PARENTHESISCATEGORY'), (':', 'COLONCATEGORY'), ('&gt;', 'PARENTHESISCATEGORY')],
			]])
	def test_結構斷小於符號的空白結果(self, 語句斷詞做語句mock):
		語句斷詞做語句mock.return_value = []
		self.assertEqual(self.用戶端.語句斷詞後結構化('我想) :<'), [[
			]])
