"""
著作權所有 (C) 民國103年 意傳文化科技
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
from 臺灣言語工具.字詞組集句章.解析整理.羅馬音仕上げ import 羅馬音仕上げ

#仕上げ
#しあげ
#ㄒㄧ˫ ㄚ ㆣㆤㆷ
#1si7_1a1_1geh4
class 羅馬音仕上げ試驗(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		self.羅馬音仕上げ = 羅馬音仕上げ()
		self.assertEqual(
			self.羅馬音仕上げ.しあげ(self.原來語句), self.處理好語句)

	def test_轉大寫字(self):
		self.原來語句 = 'gua2 ai2 sui2 koo1-niu5!'
		self.處理好語句 = 'Gua2 ai2 sui2 koo1-niu5!'
		
	def test_轉外來語(self):
		self.原來語句 = '1ōo-1too-1bái-tiam3'
		self.處理好語句 = '*ōo-*too-*bái-tiam3'

	def test_轉輕聲(self):
		self.原來語句 = '0aih! bo5-0ki3 0ah4.'
		self.處理好語句 = '--aih! bo5--ki3--ah4.'

	def test_綜合(self):
		self.原來語句 = 'āu-piah ê 1ōo-1too-1bái-tiàm bô-khì-0ah!'
		self.處理好語句 = 'Āu-piah ê *ōo-*too-*bái-tiàm bô-khì--ah!'
