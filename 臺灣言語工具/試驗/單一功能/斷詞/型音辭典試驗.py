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
from 臺灣言語工具.字詞組集句章.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.字詞組集句章.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.斷詞.型音辭典 import 型音辭典
from 臺灣言語工具.字詞組集句章.基本元素.詞 import 詞
from 臺灣言語工具.字詞組集句章.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.字詞組集句章.解析整理.參數錯誤 import 參數錯誤

class 型音辭典試驗(TestCase):
	辭典型態=型音辭典
	def setUp(self):
		self.字典 = self.辭典型態(4)
		self.粗胚 = 文章粗胚()
		self.分析器 = 拆文分析器()
		self.孤詞物 = self.分析器.建立詞物件('你')
		self.孤詞音 = self.分析器.建立詞物件('li2')
		self.二詞物 = self.分析器.建立詞物件('好')
		self.二詞音 = self.分析器.建立詞物件('hoo2')
		self.短詞物 = self.分析器.建立詞物件('你好')
		self.短詞音 = self.分析器.建立詞物件('li2-hoo2')
		self.詞物件 = self.分析器.建立詞物件('你好無？')
		self.詞音標 = self.分析器.建立詞物件('li2-hoo2-bo5-?')
		self.對齊詞 = self.分析器.產生對齊詞('你好無？', 'li2-hoo2-bo5-?')
		self.無仝詞 = self.分析器.產生對齊詞('你有無？', 'li2-u7-bo5-?')
		self.傷長詞 = self.分析器.產生對齊詞('你有好無？', 'li2-u7-hoo2-bo5-?')
		
	def tearDown(self):
		pass
	def test_漢字加詞成功無(self):
		self.字典.加詞(self.詞物件)
		self.assertEqual(self.字典.查詞(self.詞物件), [set(), set(), set(), {self.詞物件}])

	def test_多對齊加詞成功無(self):
		self.字典.加詞(self.對齊詞)
		self.字典.加詞(self.對齊詞)
		self.assertEqual(self.字典.查詞(self.對齊詞), [set(), set(), set(), {self.對齊詞}])

	def test_查對齊詞成功無(self):
		self.字典.加詞(self.對齊詞)
		self.assertEqual(self.字典.查詞(self.詞物件), [set(), set(), set(), {self.對齊詞}])
		self.assertEqual(self.字典.查詞(self.詞音標), [set(), set(), set(), {self.對齊詞}])
		self.assertEqual(self.字典.查詞(self.對齊詞), [set(), set(), set(), {self.對齊詞}])
		self.assertEqual(self.字典.查詞(self.無仝詞), [set(), set(), set(), set()])

	def test_相近詞無使查著(self):
		self.字典.加詞(self.無仝詞)
		self.assertEqual(self.字典.查詞(self.詞物件), [set(), set(), set(), set()])
		self.assertEqual(len(self.詞音標.內底字), 4)
		self.assertEqual(self.字典.查詞(self.詞音標), [set(), set(), set(), set()])
		self.assertEqual(self.字典.查詞(self.對齊詞), [set(), set(), set(), set()])
		self.assertEqual(self.字典.查詞(self.無仝詞), [set(), set(), set(), {self.無仝詞}])
		
	def test_傷長詞無使查著(self):
		self.字典.加詞(self.對齊詞)
		self.字典.加詞(self.傷長詞)
		self.assertEqual(self.字典.查詞(self.詞物件), [set(), set(), set(), {self.對齊詞}])
		self.assertEqual(self.字典.查詞(self.詞音標), [set(), set(), set(), {self.對齊詞}])
		self.assertEqual(self.字典.查詞(self.對齊詞), [set(), set(), set(), {self.對齊詞}])
		self.assertEqual(self.字典.查詞(self.傷長詞), [set(), set(), set(), set(), set()])
		
	def test_長短詞攏愛揣出來(self):
		self.字典.加詞(self.孤詞物)
		self.字典.加詞(self.二詞物)
		self.字典.加詞(self.短詞物)
		self.字典.加詞(self.詞物件)
		self.字典.加詞(self.孤詞音)
		self.字典.加詞(self.二詞音)
		self.字典.加詞(self.短詞音)
		self.字典.加詞(self.詞音標)
		self.assertEqual(self.字典.查詞(self.詞物件),
			[{self.孤詞物}, {self.短詞物}, set(), {self.詞物件}])
		self.assertEqual(self.字典.查詞(self.詞音標),
			[{self.孤詞音}, {self.短詞音}, set(), {self.詞音標}])

	def test_長度零的詞愛錯誤(self):
		self.assertRaises(解析錯誤, self.字典.加詞, 詞())
		
	def test_零連詞(self):
		self.assertRaises(參數錯誤, self.辭典型態, 0)
		self.assertRaises(參數錯誤, self.辭典型態, -10)
