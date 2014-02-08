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
from 字詞組集句章.解析整理工具.文章粗胚工具 import 文章粗胚工具
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 斷詞標音.型音辭典 import 型音辭典
from 斷詞標音.動態規劃斷詞標音 import 動態規劃斷詞標音
from 字詞組集句章.基本元素.組 import 組
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.基本元素.章 import 章
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤

class 動態規劃斷詞標音測試(TestCase):
	def setUp(self):
		self.字典 = 型音辭典(4)
		self.粗胚工具 = 文章粗胚工具()
		self.分析器 = 拆文分析器()
		self.斷詞標音 = 動態規劃斷詞標音()

		self.我對齊詞 = self.分析器.產生對齊詞('我', 'gua2')
		self.文我對齊詞 = self.分析器.產生對齊詞('我', 'ngoo2')
		self.有對齊詞 = self.分析器.產生對齊詞('有', 'u7')
		self.一張對齊詞 = self.分析器.產生對齊詞('一張', 'tsit8-tiunn1')
		self.椅仔對齊詞 = self.分析器.產生對齊詞('椅仔', 'i2-a2')
		self.驚對齊詞 = self.分析器.產生對齊詞('！', '!')

		self.我對齊組 = 組([self.我對齊詞])
		self.文我對齊組 = 組([self.文我對齊詞])
		self.有對齊組 = 組([self.有對齊詞])
		self.一張對齊組 = 組([self.一張對齊詞])
		self.椅仔對齊組 = 組([self.椅仔對齊詞])
		self.驚對齊組 = 組([self.驚對齊詞])
		
		我詞順序 = list({self.我對齊詞, self.文我對齊詞})
		self.我對齊集 = 集([self.我對齊組])
		self.文我對齊集 = 集([組([我詞順序[0]]), 組([我詞順序[1]])])
		self.有對齊集 = 集([self.有對齊組])
		self.一張對齊集 = 集([self.一張對齊組])
		self.椅仔對齊集 = 集([self.椅仔對齊組])
		self.驚對齊集 = 集([self.驚對齊組])

		self.句物件 = 句([self.我對齊集, self.有對齊集, self.一張對齊集,
			self.椅仔對齊集, self.驚對齊集, self.驚對齊集])
		self.文我句物件 = 句([self.文我對齊集, self.有對齊集, self.一張對齊集,
			self.椅仔對齊集, self.驚對齊集, self.驚對齊集])

		self.對齊句 = self.分析器.產生對齊句(
			'我有一張椅仔！！', 'gua2 u7 tsit8-tiunn1 i2-a2!!')
		self.型句 = self.分析器.建立句物件('我有一張椅仔！！')
		self.音句 = self.分析器.建立句物件('gua2 u7 tsit8-tiunn1 i2-a2!!')
		self.有詞漢羅 = self.分析器.建立句物件('我 u7 一張 i2-a2!!')
		self.無詞漢羅 = self.分析器.建立句物件('gua2 u7 一張 i2-a2!!')
	def tearDown(self):
		pass
	def test_斷詞標音結果型態(self):
		self.assertIsInstance(self.斷詞標音.斷詞標音(self.字典, self.分析器.產生對齊字('我', 'gua2')),句)
		self.assertIsInstance(self.斷詞標音.斷詞標音(self.字典, self.我對齊詞),句)
		self.assertIsInstance(self.斷詞標音.斷詞標音(self.字典, self.我對齊組),句)
		self.assertIsInstance(self.斷詞標音.斷詞標音(self.字典, self.我對齊集),句)
		self.assertIsInstance(self.斷詞標音.斷詞標音(self.字典, self.句物件),句)
		self.assertIsInstance(self.斷詞標音.斷詞標音(self.字典, 章()),章)
	
	def test_基本斷詞標音(self):
		self.字典.加詞(self.我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.字典.加詞(self.驚對齊詞)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.對齊句),
			self.句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.型句),
			self.句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.音句),
			self.句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.有詞漢羅),
			self.句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.無詞漢羅),
			self.句物件)
	def test_多詞斷詞標音(self):
		self.字典.加詞(self.我對齊詞)
		self.字典.加詞(self.文我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.字典.加詞(self.驚對齊詞)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.對齊句),
			self.句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.型句),
			self.文我句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.音句),
			self.句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.有詞漢羅),
			self.文我句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.無詞漢羅),
			self.句物件)
	def test_集無使有多組(self):
		self.字典.加詞(self.我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.字典.加詞(self.驚對齊詞)
		self.assertRaises(解析錯誤,
			self.斷詞標音.斷詞標音, self.字典, self.文我句物件)
	def test_章斷詞標音(self):
		self.字典.加詞(self.我對齊詞)
		self.字典.加詞(self.文我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.字典.加詞(self.驚對齊詞)
		章物件 = 章([self.對齊句, self.句物件])
		結果章 = 章([self.句物件, self.句物件])
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, 章物件), 結果章)
	def test_空白斷詞標音(self):
		self.字典.加詞(self.我對齊詞)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.分析器.建立句物件('')),
			句())
	def test_辭典無夠斷詞標音(self):
		self.字典.加詞(self.我對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.字典.加詞(self.驚對齊詞)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.對齊句),
			self.句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.無詞漢羅).內底集[1].內底組[0].內底詞[0].屬性,
			{'無佇辭典':True})
		新句物件 = self.句物件
		新句物件.內底集[1] = self.分析器.建立集物件('有')
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.型句),
			新句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.無詞漢羅).內底集[1].內底組[0].內底詞[0].屬性,
			{'無佇辭典':True})
		新句物件 = self.句物件
		新句物件.內底集[1].內底組[0] = self.分析器.建立組物件('u7')
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.音句),
			新句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.無詞漢羅).內底集[1].內底組[0].內底詞[0].屬性,
			{'無佇辭典':True})
		新句物件 = self.句物件
		新句物件.內底集[1].內底組[0] = self.分析器.建立組物件('u7')
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.有詞漢羅),
			新句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.無詞漢羅).內底集[1].內底組[0].內底詞[0].屬性,
			{'無佇辭典':True})
		新句物件 = self.句物件
		新句物件.內底集[1].內底組[0] = self.分析器.建立組物件('u7')
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.無詞漢羅),
			新句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.無詞漢羅).內底集[1].內底組[0].內底詞[0].屬性,
			{'無佇辭典':True})
		
	def test_兩三切比四一切閣較好(self):
		self.test_基本斷詞標音()

		self.一張椅仔對齊詞 = self.分析器.產生對齊詞('一張椅仔', 'tsit8-tiunn1-i2-a2')
		self.字典.加詞(self.一張椅仔對齊詞)
		self.一張椅仔集 = self.分析器.產生對齊集('一張椅仔', 'tsit8-tiunn1-i2-a2')
		新句物件 = 句([self.我對齊集, self.有對齊集,
			self.一張椅仔集, self.驚對齊集, self.驚對齊集])
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.對齊句),
			新句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.型句),
			新句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.音句),
			新句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.有詞漢羅),
			新句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.無詞漢羅),
			新句物件)

		self.有一張對齊詞 = self.分析器.產生對齊詞('有一張', 'u7-tsit8-tiunn1')
		self.字典.加詞(self.有一張對齊詞)
		self.有一張集 = self.分析器.產生對齊集('有一張', 'u7-tsit8-tiunn1')
		新句物件 = 句([self.我對齊集, self.有一張集,
			self.椅仔對齊集, self.驚對齊集, self.驚對齊集])
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.對齊句),
			新句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.型句),
			新句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.音句),
			新句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.有詞漢羅),
			新句物件)
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.無詞漢羅),
			新句物件)
	def test_詞屬性愛留咧(self):
		self.字典.加詞(self.我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.驚對齊詞.屬性 = '袂使無去'
		self.字典.加詞(self.驚對齊詞)
		句物件 = self.斷詞標音.斷詞標音(self.字典, self.對齊句)
		上尾第二詞 = 句物件.內底集[-2].內底組[0].內底詞[0]
		上尾詞 = 句物件.內底集[-1].內底組[0].內底詞[0]
		self.assertEqual(上尾第二詞, self.驚對齊詞)
		self.assertEqual(上尾詞, self.驚對齊詞)
		self.assertEqual(上尾第二詞.屬性, self.驚對齊詞.屬性)
		self.assertEqual(上尾詞.屬性, self.驚對齊詞.屬性)
	def test_章斷詞詞屬性愛留咧(self):
		self.字典.加詞(self.我對齊詞)
		self.字典.加詞(self.文我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.驚對齊詞.屬性 = '袂使無去'
		self.字典.加詞(self.驚對齊詞)
		章物件 = self.分析器.產生對齊章(
			'我有一張椅仔！！', 'gua2 u7 tsit8-tiunn1 i2-a2!!')
		斷好句物件 = self.斷詞標音.斷詞標音(self.字典, 章物件)
		上尾第二詞 = 斷好句物件.內底句[-1].內底集[-2].內底組[0].內底詞[-1]
		上尾詞 = 斷好句物件.內底句[-1].內底集[-1].內底組[0].內底詞[-1]
		self.assertEqual(上尾第二詞, self.驚對齊詞)
		self.assertEqual(上尾詞, self.驚對齊詞)
		self.assertEqual(上尾第二詞.屬性, self.驚對齊詞.屬性)
		self.assertEqual(上尾詞.屬性, self.驚對齊詞.屬性)
	
	def test_加數字但是無斷詞標音(self):
		self.字典.加詞(self.我對齊詞)
		題目='我1231我2+2'
		答案='我你我你你你'
		結果=self.斷詞標音.斷詞標音(self.字典, self.分析器.建立句物件(答案))
		結果.內底集[1].內底組[0].內底詞[0].內底字[0].型='1231'
		結果.內底集[3].內底組[0].內底詞[0].內底字[0].型='2'
		結果.內底集[4].內底組[0].內底詞[0].內底字[0].型='+'
		結果.內底集[5].內底組[0].內底詞[0].內底字[0].型='2'
		self.assertEqual(
			self.斷詞標音.斷詞標音(self.字典, self.分析器.建立句物件(題目)),
			結果)
