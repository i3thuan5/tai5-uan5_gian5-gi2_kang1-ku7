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
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音

class 文章粗胚數字英文中央加分字試驗(unittest.TestCase):
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

	@unittest.expectedFailure
	def test_看情形大寫專有符號袂使拆開(self):
		原本 = 'H1N1 新型 流感 包含 四種 病毒'
		答案 = 'H1N1 新型 流感 包含 四種 病毒'
		結果 = self.粗胚.數字英文中央看情形加分字符號(原本)
		self.assertEqual(結果, 答案)
		
	@unittest.expectedFailure
	def test_看情形小寫專有符號袂使拆開(self):
		原本 = 'g0v 是 咱 的 好 厝邊'
		答案 = 'g0v 是 咱 的 好 厝邊'
		結果 = self.粗胚.數字英文中央看情形加分字符號(原本)
		self.assertEqual(結果, 答案)
		
	@unittest.expectedFailure
	def test_看情形對齊組大寫音標袂使拆開(self):
		原本 = 'Sui2sui2 是 咱 的 好 厝邊'
		答案 = 'Sui2 sui2 是 咱 的 好 厝邊'
		結果 = self.粗胚.數字英文中央看情形加分字符號(原本)
		self.assertEqual(結果, 答案)
		
	@unittest.expectedFailure
	def test_看情形對齊組小寫音標袂使拆開(self):
		原本 = 'sui2sui2 是 咱 的 好 厝邊'
		答案 = 'sui2 sui2 是 咱 的 好 厝邊'
		結果 = self.粗胚.數字英文中央看情形加分字符號(原本)
		self.assertEqual(結果, 答案)
