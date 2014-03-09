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
from 臺灣言語工具.字詞組集句章.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.字詞組集句章.基本元素.集 import 集
from 臺灣言語工具.字詞組集句章.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.字詞組集句章.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.字詞組集句章.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.字詞組集句章.解析整理.詞物件網仔 import 詞物件網仔

class 詞物件網仔試驗(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.粗胚 = 文章粗胚()
		self.網仔 = 詞物件網仔()
	def tearDown(self):
		pass
	def test_網字詞(self):
		型 = '媠'
		字物件 = self.分析器.建立字物件(型)
		詞物件 = self.分析器.建立詞物件(型)
		self.assertEqual(self.網仔.網出詞物件(字物件), [詞物件])
		self.assertEqual(self.網仔.網出詞物件(詞物件), [詞物件])
#＃＃＃＃＃＃＃
	def test_網詞孤字(self):
		型 = '媠'
		字物件 = self.分析器.建立字物件(型)
		詞物件 = self.分析器.建立詞物件(型)
		self.assertEqual(self.網仔.網出字物件(詞物件), [字物件])
# 
# 	def test_網詞無字(self):
# 		型 = ''
# 		詞物件 = self.分析器.建立詞物件(型)
# 		self.assertEqual(self.網仔.網出字物件(詞物件), [])
# 
# 	def test_網詞濟字漢字(self):
# 		語句 = '椅仔！'
# 		self.assertEqual(
# 			self.網仔.網出字物件(self.分析器.建立詞物件(語句)),
# 			[self.分析器.建立字物件('椅'), self.分析器.建立字物件('仔'), self.分析器.建立字物件('！')])
# 
# 	def test_網詞濟字音標(self):
# 		語句 = 'tsit8-tiunn1 !'
# 		self.assertEqual(
# 			self.網仔.網出字物件(self.分析器.建立詞物件(語句)),
# 			[self.分析器.建立字物件('tsit8'), self.分析器.建立字物件('tiunn1'), self.分析器.建立字物件('!')])
# 
# 	def test_網詞濟字漢羅(self):
# 		語句 = 'tsit8-張!'
# 		self.assertEqual(
# 			self.網仔.網出字物件(self.分析器.建立詞物件(語句)),
# 			[self.分析器.建立字物件('tsit8'), self.分析器.建立字物件('張'), self.分析器.建立字物件('!')])
# 
# 	def test_網組孤字(self):
# 		型 = '媠'
# 		字物件 = self.分析器.建立字物件(型)
# 		組物件 = self.分析器.建立組物件(型)
# 		self.assertEqual(self.網仔.網出字物件(組物件), [字物件])
# 
# 	def test_網組無字(self):
# 		型 = ''
# 		組物件 = self.分析器.建立組物件(型)
# 		self.assertEqual(self.網仔.網出字物件(組物件), [])
# 
# 	def 建立組檢查(self, 原來語句, 切好語句):
# 		字陣列 = []
# 		[字陣列.extend(self.網仔.網出字物件(self.分析器.建立詞物件(詞)))
# 			for 詞 in 切好語句]
# 		return (self.分析器.建立組物件(原來語句), 字陣列)
# 
# 	def test_網組濟字(self):
# 		原來語句 = '我有一張椅仔！'
# 		切好語句 = ['我', '有', '一', '張', '椅', '仔', '！']
# 		組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
# 		self.assertEqual(self.網仔.網出字物件(組物件), 詞陣列)
# 
# 	# 為著通用佮一致性，這愛家己建立詞來鬥。大部份攏是無細字揤著，親像平行語料庫才另外閣包一層
# 	def test_網組濟字配空白(self):
# 		原來語句 = '我 有 一張 椅仔！'
# 		切好語句 = ['我', '有', '一', '張', '椅', '仔', '！']
# 		組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
# 		self.assertEqual(self.網仔.網出字物件(組物件), 詞陣列)
# 
# 	def test_網組濟音標(self):
# 		原來語句 = 'gua2 u7 tsit8-tiunn1 i2-a2'
# 		處理好語句 = 'gua2 u7 tsit8-tiunn1 i2-a2'
# 		加空白後語句 = 'gua2 u7 tsit8-tiunn1 i2-a2'
# 		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
# 		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)
# 		切好語句 = ['gua2', 'u7', 'tsit8-tiunn1', 'i2-a2']
# 		組物件, 詞陣列 = self.建立組檢查(處理好語句, 切好語句)
# 		self.assertEqual(self.網仔.網出字物件(組物件), 詞陣列)
# 
# 	def test_網組濟字輕聲(self):
# 		原來語句 = 'mi2-kiann7 boo5-0ki3 ah!'
# 		處理好語句 = 'mi2-kiann7 boo5-0ki3 ah!'
# 		加空白後語句 = 'mi2-kiann7 boo5-0ki3 ah ! '
# 		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
# 		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)
# 		切好語句 = ['mi2-kiann7', 'boo5-0ki3', 'ah', '!']
# 		組物件, 詞陣列 = self.建立組檢查(處理好語句, 切好語句)
# 		self.assertEqual(self.網仔.網出字物件(組物件), 詞陣列)
# 
# 	def test_網句濟字佮符號(self):
# 		原來語句 = '枋寮漁港「大條巷」上闊兩公尺。'
# 		切好語句 = ['枋', '寮', '漁', '港', '「', '大', '條', '巷', '」', '上', '闊', '兩', '公', '尺', '。']
# 		組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
# 		self.assertEqual(self.網仔.網出字物件(
# 			self.分析器.建立句物件(原來語句)), 詞陣列)
# 		組物件 = 組物件
# 
# 	def test_網章濟連字佮符號(self):
# 		原來語句 = '枋-寮漁-港「大-條-巷」。上-闊兩-公-尺'
# 		切好語句 = ['枋寮', '漁港', '「', '大條巷', '」', '。', '上闊', '兩公尺']
# 		組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
# 		self.assertEqual(self.網仔.網出字物件(
# 			self.分析器.建立章物件(原來語句)), 詞陣列)
# 		組物件 = 組物件
# 
# 	def test_網集濟組(self):
# 		原來語句 = '我有一張椅仔！'
# 		組陣列 = [self.分析器.建立組物件(原來語句),
# 			self.分析器.建立組物件(原來語句), ]
# 		self.assertRaises(解析錯誤, self.網仔.網出字物件, 集(組陣列))
# 
# 	def test_網集無字(self):
# 		型 = ''
# 		集物件 = self.分析器.建立集物件(型)
# 		self.assertEqual(self.網仔.網出字物件(集物件), [])
# 
# 	def test_網句無字(self):
# 		型 = ''
# 		句物件 = self.分析器.建立句物件(型)
# 		self.assertEqual(self.網仔.網出字物件(句物件), [])
# 
# 	def test_網章無字(self):
# 		型 = ''
# 		章物件 = self.分析器.建立章物件(型)
# 		self.assertEqual(self.網仔.網出字物件(章物件), [])
# 
# 	def test_烏白擲物件(self):
# 		self.assertRaises(型態錯誤, self.網仔.網出字物件, 2123)
# 		self.assertRaises(型態錯誤, self.網仔.網出字物件, self.網仔)
# 		self.assertRaises(型態錯誤, self.網仔.網出字物件, None)
# 
# if __name__ == '__main__':
# 	unittest.main()
