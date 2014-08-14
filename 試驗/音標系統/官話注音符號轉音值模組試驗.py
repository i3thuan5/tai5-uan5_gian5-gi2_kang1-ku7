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
from 臺灣言語工具.音標系統.官話.官話注音符號 import 官話注音符號
from 臺灣言語工具.音標系統.官話.官話注音符號 import 官話注音符號聲
from 臺灣言語工具.音標系統.官話.官話注音符號 import 官話注音符號韻
from 臺灣言語工具.音標系統.官話.官話注音符號轉音值模組 import 官話注音符號對照音值聲母表
from 臺灣言語工具.音標系統.官話.官話注音符號轉音值模組 import 官話注音符號對照音值韻母表

class 官話注音符號轉音值模組試驗(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
		
	def test_單音(self):
		self.assertEqual(官話注音符號('ㄧˋ').音值(), ('ʔ', 'i', 'ˋ'))
	def test_三符號有調(self):
		self.assertEqual(官話注音符號('ㄔㄨㄢˊ').音值(), ('tʂʰ', 'uan', 'ˊ'))
	def test_三符號無調(self):
		self.assertEqual(官話注音符號('ㄒㄩㄝ').音值(), ('ɕ', 'ye', ''))
	def test_無聲(self):
		self.assertEqual(官話注音符號('ㄨㄟˇ').音值(), ('ʔ', 'uei', 'ˇ'))
	def test_輕聲(self):
		self.assertEqual(官話注音符號('ㄉㄜ˙').音值(), ('t', 'ɤ', '˙'))
	def test_空韻(self):
		self.assertEqual(官話注音符號('ㄗ').音值(), ('ts', 'ɿ', ''))
		self.assertEqual(官話注音符號('ㄓ').音值(), ('tʂ', 'ʅ', ''))
		self.assertEqual(官話注音符號('ㄖˋ').音值(), ('ʐ', 'ʅ', 'ˋ'))
	def test_喔我婆(self):
		self.assertEqual(官話注音符號('ㄛ').音值(), ('ʔ', 'o', ''))
		self.assertEqual(官話注音符號('ㄨㄛˇ').音值(), ('ʔ', 'uo', 'ˇ'))
		self.assertEqual(官話注音符號('ㄆㄛˊ').音值(), ('pʰ', 'uo', 'ˊ'))
	def test_翁東(self):
		self.assertEqual(官話注音符號('ㄨㄥ').音值(), ('ʔ', 'uŋ', ''))
		self.assertEqual(官話注音符號('ㄉㄨㄥ').音值(), ('t', 'oŋ', ''))
	def test_無合法(self):
		self.assertEqual(官話注音符號('ㄗㄧㄨ').音值(), None)
		self.assertEqual(官話注音符號('').音值(), None)
	
	def test_全部攏會使產生方音物件(self):
		for 母 in 官話注音符號聲:
			self.assertIn(母, 官話注音符號對照音值聲母表)
		for 母 in 官話注音符號韻:
			self.assertIn(母, 官話注音符號對照音值韻母表)
