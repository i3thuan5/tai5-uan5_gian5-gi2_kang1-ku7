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
from 臺灣言語工具.字詞組集句章.基本元素.字 import 字
from 臺灣言語工具.字詞組集句章.綜合標音.國語字綜合標音 import 國語字綜合標音
from 臺灣言語工具.字詞組集句章.基本元素.公用變數 import 無音
from 臺灣言語工具.字詞組集句章.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.字詞組集句章.解析整理.解析錯誤 import 解析錯誤

class 國語字綜合標音試驗(unittest.TestCase):
	def setUp(self):
		self.我型 = '我'
		self.我音 = 'ㄨㄛˇ'
		self.我標音 = '⿳⿳ㄨㄛˇ'
		self.你型 = '你'
		self.你音 = 'ㄋㄧˇ'
	def tearDown(self):
		pass
	def test_合法(self):
		綜合標音 = 國語字綜合標音(字(self.我型, self.我音))
		self.assertEqual(綜合標音.標音完整無(), True)
	def test_兩个字合法(self):
		我綜合標音 = 國語字綜合標音(字(self.我型, self.我音))
		你綜合標音 = 國語字綜合標音(字(self.你型, self.你音))
		self.assertEqual(我綜合標音.型體, self.我型)
		self.assertEqual(你綜合標音.型體, self.你型)
	def test_轉json格式(self):
		綜合標音 = 國語字綜合標音(字(self.我型, self.我音))
		self.assertEqual(綜合標音.轉json格式(),
			{"型體":self.我型, "注音符號":self.我標音})
	def test_標點合法(self):
		標點 = 國語字綜合標音(字('，', 無音))
		self.assertEqual(標點.標音完整無(), True)
	def test_標點轉json格式(self):
		標點 = 國語字綜合標音(字('，', 無音))
		self.assertEqual(標點.轉json格式(), {"型體":"，", "注音符號":""})
	def test_標點音無合法(self):
		self.assertRaises(解析錯誤, 國語字綜合標音, 字('我', 'ㄆㄨㄧˋ'))
	def test_烏白傳(self):
		self.assertRaises(型態錯誤, 國語字綜合標音, '我')
	def test_輕聲轉json格式(self):
		型='的'
		音='ㄉㄜ˙'
		綜合標音 = 國語字綜合標音(字(型, 音))
		self.assertEqual(綜合標音.轉json格式(),
			{"型體":型, "注音符號":'⿳⿳˙ㄉㄜ'})

if __name__ == '__main__':
	unittest.main()
