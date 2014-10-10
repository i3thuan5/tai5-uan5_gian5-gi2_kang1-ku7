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
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音轉音值模組 import 臺灣客家話拼音對照音值聲母表
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音轉音值模組 import 臺灣客家話拼音對照音值韻母表
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音聲母對照表
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音韻母對照表

class 臺灣客家話拼音轉音值模組試驗(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
		
	def test_定看音標(self):
		self.assertEqual(臺灣客家話拼音('er').音值(), ('ʔ', 'ə', ''))
		self.assertEqual(臺灣客家話拼音('imˊ').音值(), ('ʔ', 'im', 'ˊ'))
		self.assertEqual(臺灣客家話拼音('iongˇ').音值(), ('ʔ', 'ioŋ', 'ˇ'))
		self.assertEqual(臺灣客家話拼音('giangˊ').音值(), ('k', 'iaŋ', 'ˊ'))
		self.assertEqual(臺灣客家話拼音('zauˊ').音值(), ('ts', 'au', 'ˊ'))
		self.assertEqual(臺灣客家話拼音('caˋ').音值(), ('tsʰ', 'a', 'ˋ'))
		self.assertEqual(臺灣客家話拼音('pon+').音值(), ('pʰ', 'on', '+'))
		self.assertEqual(臺灣客家話拼音('ng').音值(), ('ʔ', 'ŋ̩', ''))
		self.assertEqual(臺灣客家話拼音('ngiˋ').音值(), ('ȵ', 'i', 'ˋ'))
		self.assertEqual(臺灣客家話拼音('mug').音值(), ('m', 'uk', ''))
		self.assertEqual(臺灣客家話拼音('ngedˋ').音值(), ('ŋ', 'et', 'ˋ'))
		self.assertEqual(臺灣客家話拼音('ngin').音值(), ('ȵ', 'in', ''))
		self.assertEqual(臺灣客家話拼音('tongˋ').音值(), ('tʰ', 'oŋ', 'ˋ'))
		self.assertEqual(臺灣客家話拼音('bainnˋ').音值(), ('p', 'aⁿiⁿ', 'ˋ'))
		
	def test_大寫音標(self):
		self.assertEqual(臺灣客家話拼音('JIANGˊ').音值(), ('tɕ', 'iaŋ', 'ˊ'))
		self.assertEqual(臺灣客家話拼音('Jiangˊ').音值(), ('tɕ', 'iaŋ', 'ˊ'))

	def test_違法音標(self):
		self.assertEqual(臺灣客家話拼音('@@').音值(), (None,))
		self.assertEqual(臺灣客家話拼音('pe̍m').音值(), (None,))
		self.assertEqual(臺灣客家話拼音('xxtsé--á').音值(), (None,))
		self.assertEqual(臺灣客家話拼音('óonn').音值(), (None,))
		self.assertEqual(臺灣客家話拼音('Jiumˊ').音值(), (None,))
		
	def test_全部攏會使產生方音物件(self):
		for 母 in 臺灣客家話拼音聲母對照表:
			self.assertIn(母, 臺灣客家話拼音對照音值聲母表)
		for 母 in 臺灣客家話拼音韻母對照表:
			self.assertIn(母, 臺灣客家話拼音對照音值韻母表)
		
	def test_鼻化韻逐个元音攏愛有鼻化(self):
		for 韻 in 臺灣客家話拼音對照音值韻母表.values():
			for 切 in 韻.split('ⁿ')[:-1]:
				self.assertEqual(len(切), 1, '{}有問題'.format(韻))
