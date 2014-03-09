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
from 臺灣言語工具.字詞組集句章.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.字詞組集句章.基本元素.字 import 字
from 臺灣言語工具.字詞組集句章.基本元素.詞 import 詞
from 臺灣言語工具.字詞組集句章.基本元素.組 import 組
from 臺灣言語工具.字詞組集句章.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 臺灣言語工具.字詞組集句章.綜合標音.詞組綜合標音 import 詞組綜合標音
from 臺灣言語工具.字詞組集句章.基本元素.公用變數 import 無音

class 詞組綜合標音試驗(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.粗胚 = 文章粗胚()
	def tearDown(self):
		pass
	def test_基本試驗(self):
		組物件 = self.分析器.產生對齊組('大美女', 'tua7 sui2-boo2')
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 組物件)
		self.assertEqual(len(標音詞組.綜合字), 3)
		self.assertEqual(標音詞組.綜合字[0], 閩南語字綜合標音(字('大', 'tua7')))
		self.assertEqual(標音詞組.綜合字[1], 閩南語字綜合標音(字('美', 'sui2')))
		self.assertEqual(標音詞組.綜合字[2], 閩南語字綜合標音(字('女', 'boo2')))
		self.assertEqual(標音詞組.連字音, 'tua7 sui2-boo2')

	def test_連字音檢查(self):
		組物件 = 組([self.分析器.產生對齊詞('大', 'tua7'),
			self.分析器.產生對齊詞('美女', 'sui2-boo2')])
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 組物件)
		self.assertEqual(len(標音詞組.綜合字), 3)
		self.assertEqual(標音詞組.綜合字[0], 閩南語字綜合標音(字('大', 'tua7')))
		self.assertEqual(標音詞組.綜合字[1], 閩南語字綜合標音(字('美', 'sui2')))
		self.assertEqual(標音詞組.綜合字[2], 閩南語字綜合標音(字('女', 'boo2')))
		self.assertEqual(標音詞組.連字音, 'tua7 sui2-boo2')

	def test_有標點符號(self):
		詞型 = '點仔膠，黏著跤，'
		詞音 = 'tiam2-a2-ka1 , liam5-tioh8 kha1 ,'
		組物件 = self.分析器.產生對齊組(詞型, 詞音)
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 組物件)
		self.assertEqual(len(標音詞組.綜合字), 8)
		self.assertEqual(標音詞組.綜合字[0], 閩南語字綜合標音(字('點', 'tiam2')))
		self.assertEqual(標音詞組.綜合字[1], 閩南語字綜合標音(字('仔', 'a2')))
		self.assertEqual(標音詞組.綜合字[2], 閩南語字綜合標音(字('膠', 'ka1')))
		self.assertEqual(標音詞組.綜合字[3], 閩南語字綜合標音(字('，', ',')))
		self.assertEqual(標音詞組.綜合字[4], 閩南語字綜合標音(字('黏', 'liam5')))
		self.assertEqual(標音詞組.綜合字[5], 閩南語字綜合標音(字('著', 'tioh8')))
		self.assertEqual(標音詞組.綜合字[6], 閩南語字綜合標音(字('跤', 'kha1')))
		self.assertEqual(標音詞組.綜合字[7], 閩南語字綜合標音(字('，', ',')))
		self.assertEqual(標音詞組.連字音, 'tiam2-a2-ka1 , liam5-tioh8 kha1 ,')

	def test_有無音字(self):
		組物件 = 組([self.分析器.產生對齊詞('點仔膠', 'tiam2-a2-ka1'),
				self.分析器.建立詞物件('，'),
				self.分析器.產生對齊詞('黏著', 'liam5-tioh8'),
				self.分析器.產生對齊詞('跤', 'kha1'),
				self.分析器.建立詞物件('，'),
				])
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 組物件)
		self.assertEqual(len(標音詞組.綜合字), 8)
		self.assertEqual(標音詞組.綜合字[0], 閩南語字綜合標音(字('點', 'tiam2')))
		self.assertEqual(標音詞組.綜合字[1], 閩南語字綜合標音(字('仔', 'a2')))
		self.assertEqual(標音詞組.綜合字[2], 閩南語字綜合標音(字('膠', 'ka1')))
		self.assertEqual(標音詞組.綜合字[3], 閩南語字綜合標音(字('，', 無音)))
		self.assertEqual(標音詞組.綜合字[4], 閩南語字綜合標音(字('黏', 'liam5')))
		self.assertEqual(標音詞組.綜合字[5], 閩南語字綜合標音(字('著', 'tioh8')))
		self.assertEqual(標音詞組.綜合字[6], 閩南語字綜合標音(字('跤', 'kha1')))
		self.assertEqual(標音詞組.綜合字[7], 閩南語字綜合標音(字('，', 無音)))
		self.assertEqual(標音詞組.連字音, 'tiam2-a2-ka1 liam5-tioh8 kha1')

	def test_詞中有無音字(self):
		組物件 = 組([
				詞([self.分析器.產生對齊字('點', 'tiam2'),
					self.分析器.建立字物件('仔'),
					self.分析器.產生對齊字('膠', 'ka1')]),
				self.分析器.建立詞物件('，'),
				self.分析器.產生對齊詞('黏著', 'liam5-tioh8'),
				self.分析器.產生對齊詞('跤', 'kha1'),
				self.分析器.建立詞物件('，'),
				])
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 組物件)
		self.assertEqual(len(標音詞組.綜合字), 8)
		self.assertEqual(標音詞組.綜合字[0], 閩南語字綜合標音(字('點', 'tiam2')))
		self.assertEqual(標音詞組.綜合字[1], 閩南語字綜合標音(字('仔')))
		self.assertEqual(標音詞組.綜合字[2], 閩南語字綜合標音(字('膠', 'ka1')))
		self.assertEqual(標音詞組.綜合字[3], 閩南語字綜合標音(字('，', 無音)))
		self.assertEqual(標音詞組.綜合字[4], 閩南語字綜合標音(字('黏', 'liam5')))
		self.assertEqual(標音詞組.綜合字[5], 閩南語字綜合標音(字('著', 'tioh8')))
		self.assertEqual(標音詞組.綜合字[6], 閩南語字綜合標音(字('跤', 'kha1')))
		self.assertEqual(標音詞組.綜合字[7], 閩南語字綜合標音(字('，', 無音)))
		self.assertEqual(標音詞組.連字音, 'tiam2-ka1 liam5-tioh8 kha1')

	def test_空組(self):
		組物件 = 組()
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 組物件)
		self.assertEqual(len(標音詞組.綜合字), 0)

	def test_傳詞檢查(self):
		詞物件 = self.分析器.產生對齊詞('大美女', 'tua7-sui2-boo2')
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 詞物件)
		self.assertEqual(len(標音詞組.綜合字), 3)
		self.assertEqual(標音詞組.綜合字[0], 閩南語字綜合標音(字('大', 'tua7')))
		self.assertEqual(標音詞組.綜合字[1], 閩南語字綜合標音(字('美', 'sui2')))
		self.assertEqual(標音詞組.綜合字[2], 閩南語字綜合標音(字('女', 'boo2')))
		self.assertEqual(標音詞組.連字音, 'tua7-sui2-boo2')

	def test_空詞檢查(self):
		詞物件 = self.分析器.建立詞物件('')
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 詞物件)
		self.assertEqual(標音詞組.綜合字, [])
		self.assertEqual(標音詞組.連字音, '')
		
	def test_一詞轉json格式(self):
		詞物件 = self.分析器.產生對齊詞('椅仔','i2-a2')
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 詞物件)
		self.assertEqual(標音詞組.轉json格式(),
			{"詞組綜合標音":[
			{"型體":"椅","臺羅數字調":"i2","臺羅閏號調":"í","通用數字調":"i4","吳守禮方音":"⿳ㄧˋ"},
			{"型體":"仔","臺羅數字調":"a2","臺羅閏號調":"á","通用數字調":"a4","吳守禮方音":"⿳ㄚˋ"}
			],"連字音":"i2-a2"}
			)
		
	def test_一組轉json格式(self):
		組物件 = self.分析器.產生對齊組('椅仔','i2-a2')
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 組物件)
		self.assertEqual(標音詞組.轉json格式(),
			{"詞組綜合標音":[
			{"型體":"椅","臺羅數字調":"i2","臺羅閏號調":"í","通用數字調":"i4","吳守禮方音":"⿳ㄧˋ"},
			{"型體":"仔","臺羅數字調":"a2","臺羅閏號調":"á","通用數字調":"a4","吳守禮方音":"⿳ㄚˋ"}
			],"連字音":"i2-a2"}
			)
		
	def test_一組兩詞轉json格式(self):
		組物件 = self.分析器.產生對齊組('椅仔','i2 a2')
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 組物件)
		self.assertEqual(標音詞組.轉json格式(),
			{"詞組綜合標音":[
			{"型體":"椅","臺羅數字調":"i2","臺羅閏號調":"í","通用數字調":"i4","吳守禮方音":"⿳ㄧˋ"},
			{"型體":"仔","臺羅數字調":"a2","臺羅閏號調":"á","通用數字調":"a4","吳守禮方音":"⿳ㄚˋ"}
			],"連字音":"i2 a2"}
			)
		
if __name__ == '__main__':
	unittest.main()
