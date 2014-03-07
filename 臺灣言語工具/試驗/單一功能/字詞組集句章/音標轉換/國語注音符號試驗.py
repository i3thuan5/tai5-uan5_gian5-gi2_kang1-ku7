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
from unittest.case import TestCase
from 臺灣言語工具.字詞組集句章.音標系統.國語.國語注音符號 import 國語注音符號

class 國語注音符號試驗(TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass

#---------------------------------------------
		
	def test_介音(self):
		注音 = 國語注音符號('ㄧˋ')
		self.assertEqual(注音.音標, 'ㄧˋ')
		self.assertEqual(注音.聲, '')
		self.assertEqual(注音.韻, 'ㄧ')
		self.assertEqual(注音.調, 'ˋ')
		self.assertEqual(注音.聲韻, 'ㄧ')
		
	def test_完整音(self):
		注音 = 國語注音符號('ㄔㄨㄢˊ')
		self.assertEqual(注音.音標, 'ㄔㄨㄢˊ')
		self.assertEqual(注音.聲, 'ㄔ')
		self.assertEqual(注音.韻, 'ㄨㄢ')
		self.assertEqual(注音.調, 'ˊ')
		self.assertEqual(注音.聲韻, 'ㄔㄨㄢ')
		
	def test_一聲(self):
		注音 = 國語注音符號('ㄒㄩㄝ')
		self.assertEqual(注音.音標, 'ㄒㄩㄝ')
		self.assertEqual(注音.聲, 'ㄒ')
		self.assertEqual(注音.韻, 'ㄩㄝ')
		self.assertEqual(注音.調, '')
		self.assertEqual(注音.聲韻, 'ㄒㄩㄝ')
		
	def test_零聲母(self):
		注音 = 國語注音符號('ㄨㄛˇ')
		self.assertEqual(注音.音標, 'ㄨㄛˇ')
		self.assertEqual(注音.聲, '')
		self.assertEqual(注音.韻, 'ㄨㄛ')
		self.assertEqual(注音.調, 'ˇ')
		self.assertEqual(注音.聲韻, 'ㄨㄛ')
		
	def test_輕聲(self):
		注音 = 國語注音符號('ㄉㄜ˙')
		self.assertEqual(注音.音標, 'ㄉㄜ˙')
		self.assertEqual(注音.聲, 'ㄉ')
		self.assertEqual(注音.韻, 'ㄜ')
		self.assertEqual(注音.調, '˙')
		self.assertEqual(注音.聲韻, 'ㄉㄜ')
		
	def test_空韻(self):
		注音 = 國語注音符號('ㄗ')
		self.assertEqual(注音.音標, 'ㄗ')
		self.assertEqual(注音.聲, 'ㄗ')
		self.assertEqual(注音.韻, '')
		self.assertEqual(注音.調, '')
		self.assertEqual(注音.聲韻, 'ㄗ')
		
	def test_無合法(self):
		self.assertEqual(國語注音符號('˙ㄉㄜ').音標, None)
		self.assertEqual(國語注音符號('ㄉㄜ˙').音標, 'ㄉㄜ˙')
		self.assertEqual(國語注音符號('˙ㄉㄜ').音標, None)
		self.assertEqual(國語注音符號('ㄆㄢ').音標, 'ㄆㄢ')
		self.assertEqual(國語注音符號('ㄆㄢ+').音標, None)
		self.assertEqual(國語注音符號('ㄗㄧㄨ').音標, None)
		self.assertEqual(國語注音符號('ㄐ').音標, None)
		self.assertEqual(國語注音符號('').音標, None)
		self.assertEqual(國語注音符號('Ⅹㄛˇ').音標, None)#怪怪的「ㄨ」