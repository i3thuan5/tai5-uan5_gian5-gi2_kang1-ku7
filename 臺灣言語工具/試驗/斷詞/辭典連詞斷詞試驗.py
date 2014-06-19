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
from unittest.case import TestCase
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.表單.型音辭典 import 型音辭典
from 臺灣言語工具.斷詞.辭典揣詞 import 辭典揣詞
from 臺灣言語工具.基本元素.組 import 組
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.基本元素.章 import 章
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.表單.語句連詞 import 語句連詞
from 臺灣言語工具.斷詞.連詞揀集內組 import 連詞揀集內組
from 臺灣言語工具.斷詞.辭典連詞斷詞 import 辭典連詞斷詞

class 辭典連詞斷詞試驗(TestCase):
	忍受 = 1e-10
	def setUp(self):
		self.斷詞 = 辭典連詞斷詞()
		self.字典 = 型音辭典(4)
		self.連詞 = 語句連詞(3)

		self.分析器 = 拆文分析器()

	def tearDown(self):
		pass
		
	def test_一集一詞(self):
		self.加鞋仔的資料()
		self.字典.加詞(self.鞋仔詞)
		集物件 = self.分析器.建立集物件('e5 a2')
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, 集物件)
		self.assertEqual(斷詞結果, self.孤詞鞋仔句)
		self.assertLess(分數, 0)
		self.assertEqual(詞數, 1)
		
	def test_一集兩詞(self):
		self.加鞋仔的資料()
		self.字典.加詞(self.鞋詞)
		self.字典.加詞(self.仔詞)
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.鞋仔兩集句物件)
		self.assertEqual(斷詞結果, self.兩詞鞋仔句)
		self.assertLess(分數, 0)
		self.assertEqual(詞數, 2)
		
	def test_兩集一詞(self):
		self.加鞋仔的資料()
		self.字典.加詞(self.鞋仔詞)
		集物件 = self.分析器.建立集物件('e5 a2')
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, 集物件)
		self.assertEqual(斷詞結果, self.孤詞鞋仔句)
		self.assertLess(分數, 0)
		self.assertEqual(詞數, 1)
		
	def test_兩集兩詞(self):
		self.加鞋仔的資料()
		self.字典.加詞(self.鞋詞)
		self.字典.加詞(self.仔詞)
		集物件 = self.分析器.建立集物件('e5 a2')
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.鞋仔兩集句物件)
		self.assertEqual(斷詞結果, self.兩詞鞋仔句)
		self.assertLess(分數, 0)
		self.assertEqual(詞數, 2)
		
	def test_看機率選詞(self):
		self.加我的鞋仔的資料()
		self.字典.加詞(self.我詞)
		self.字典.加詞(self.的詞)
		self.字典.加詞(self.鞋詞)
		self.字典.加詞(self.仔詞)
		self.連詞.看(self.分析器.產生對齊句('我穿布鞋。', 'gua2 tshng1 poo3 e5.'))
		self.連詞.看(self.分析器.產生對齊句('我鞋仔歹去矣。', 'gua2 e5 a2 phainn2-0khi3 0ah4.'))
		我的 = [self.分析器.產生對齊詞('我', 'gua2'), self.分析器.產生對齊詞('的', 'e5')]
		self.assertEqual(self.連詞.數量(我的), [0, 0])
		我鞋 = [self.分析器.產生對齊詞('我', 'gua2'), self.分析器.產生對齊詞('鞋', 'e5')]
		self.assertEqual(self.連詞.數量(我鞋), [2, 1])
		
		self.試斷我的鞋仔(self.我鞋鞋仔)
		
		self.連詞.看(self.分析器.產生對齊句('我的冊佇你遐。', 'gua2 e5 tsheh4 ti7 li2 hia1.'))
		self.試斷我的鞋仔(self.我鞋鞋仔)
		
		self.連詞.看(self.分析器.產生對齊句('我的故鄉佇花蓮。', 'gua2 e5 koo3-hiong1 ti7 hua1-lian1.'))
		self.試斷我的鞋仔(self.我的鞋仔)

		self.的.內底詞[0].屬性 = {'機率':self.連詞.對數(0.01)}
		self.鞋.內底詞[0].屬性 = {'機率':self.連詞.對數(0.99)}
		self.試斷我的鞋仔(self.我鞋鞋仔)
		
	def test_多詞斷詞(self):
		self.加我有一張椅仔的資料()
		self.字典.加詞(self.白我對齊詞)
		self.字典.加詞(self.文我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.字典.加詞(self.驚對齊詞)
		self.連詞.看(self.白我有對齊組)
		self.連詞.看(self.文我有對齊組)
		白我有錢對齊組 = self.分析器.產生對齊組('我有錢', 'gua2 u7 tsinn5')
		self.連詞.看(白我有錢對齊組)
		self.斷逐種我有一張椅仔(self.對齊句, 0, 6)

	def test_句無連詞(self):
		self.加我有一張椅仔的資料()
		self.字典.加詞(self.白我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.字典.加詞(self.驚對齊詞)
		self.斷逐種我有一張椅仔(self.對齊句, 0, 6)

	def test_句毋是愈長愈好(self):
		self.加予伊出去耍的資料()
		self.字典.加詞(self.予對齊詞)
		self.字典.加詞(self.伊對齊詞)
		self.字典.加詞(self.出去對齊詞)
		self.字典.加詞(self.耍對齊詞)
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.予伊出去耍全羅)
		self.assertEqual(斷詞結果, self.予伊對齊句)
		self.檢查分數詞數(分數, 詞數, 0, 4)

		self.字典.加詞(self.雨衣對齊詞)
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.予伊出去耍全羅)
		self.assertEqual(斷詞結果, self.雨衣對齊句)
		self.檢查分數詞數(分數, 詞數, 0, 3)

		self.連詞.看(self.予伊耍對齊句)
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.予伊出去耍全羅)
		self.assertEqual(斷詞結果, self.予伊對齊句)
		self.檢查分數詞數(分數, 詞數, 0, 4)
		
	def test_兩三切比一四切閣較好(self):
		self.加我有一張椅仔的資料()
		self.字典.加詞(self.白我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.字典.加詞(self.驚對齊詞)
		原本分數 = self.斷逐種我有一張椅仔(self.對齊句, 0, 6)
		
		self.加我有一張椅仔的集資料()
		self.一張椅仔對齊詞 = self.分析器.產生對齊詞('一張椅仔', 'tsit8-tiunn1-i2-a2')
		self.字典.加詞(self.一張椅仔對齊詞)
		self.連詞.看(self.一張椅仔對齊詞)
		一四新組物件 = 組([self.白我對齊詞, self.有對齊詞,
			self.一張椅仔對齊詞, self.驚對齊詞, self.驚對齊詞, ])
		一四新句物件 = 句([集([一四新組物件])])
		一四分數 = self.斷逐種我有一張椅仔(一四新句物件, 0, 5)

		self.有一張對齊詞 = self.分析器.產生對齊詞('有一張', 'u7-tsit8-tiunn1')
		self.字典.加詞(self.有一張對齊詞)
		有一張的一四分數 = self.斷逐種我有一張椅仔(一四新句物件, 0, 5)
		self.assertEqual(有一張的一四分數, 一四分數)
		
		self.連詞.看(self.有一張對齊詞)
		self.連詞.看(self.有一張對齊詞)
		self.連詞.看(self.椅仔對齊詞)
# 		self.有一張集 = self.分析器.產生對齊集('有一張', 'u7-tsit8-tiunn1')
		兩三新組物件 = 組([self.白我對齊詞, self.有一張對齊詞,
			self.椅仔對齊詞, self.驚對齊詞, self.驚對齊詞])
		兩三新句物件 = 句([集([兩三新組物件])])
		兩三分數 = self.斷逐種我有一張椅仔(兩三新句物件, 0, 5)
			
		self.assertLess(原本分數[0], 一四分數[0])
		self.assertLess(一四分數[0], 兩三分數[0])
		
	def test_章斷詞(self):
		self.加我有一張椅仔的資料()
		self.字典.加詞(self.白我對齊詞)
		self.字典.加詞(self.文我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.字典.加詞(self.驚對齊詞)
		self.加我有一張椅仔的集資料()
		章物件 = 章([self.對齊句, self.句物件])
		結果章 = 章([self.對齊句, self.對齊句])
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, 章物件)
		self.assertEqual(斷詞結果, 結果章)
		self.檢查分數詞數(分數, 詞數, 0, 12)
		
	def test_標空的物件(self):
		# 字物件有限制毋是空的
		詞物件 = self.分析器.建立詞物件('')
		組物件 = self.分析器.建立組物件('')
		集物件 = self.分析器.建立集物件('')
		句物件 = self.分析器.建立句物件('')
		章物件 = self.分析器.建立章物件('')
		空句物件 = 句([集([組()])])
		結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, 詞物件)
		全部分數 = {}
		for 物件, 結果物件, 詞數答案 in \
			zip([詞物件, 組物件, 句物件, 章物件], \
				[空句物件, 空句物件, 空句物件, 章物件], \
			 	[0, 0, 0, 0]):
			結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, 物件)
			self.assertEqual(結果, 結果物件)
			self.assertEqual(詞數, 詞數答案)
			if 詞數 not in 全部分數:
				全部分數[詞數] = 分數
			self.assertEqual(分數, 全部分數[詞數], 物件)
		self.assertRaises(解析錯誤, self.斷詞.斷詞, self.字典, self.連詞, 集物件,)
		
	def 加我有一張椅仔的資料(self):
		self.白我對齊詞 = self.分析器.產生對齊詞('我', 'gua2')
		self.文我對齊詞 = self.分析器.產生對齊詞('我', 'ngoo2')
		self.有對齊詞 = self.分析器.產生對齊詞('有', 'u7')
		self.一張對齊詞 = self.分析器.產生對齊詞('一張', 'tsit8-tiunn1')
		self.椅仔對齊詞 = self.分析器.產生對齊詞('椅仔', 'i2-a2')
		self.驚對齊詞 = self.分析器.產生對齊詞('！', '!')
		
		self.白我有對齊組 = self.分析器.產生對齊組('我有', 'gua2 u7')
		self.文我有對齊組 = self.分析器.產生對齊組('我有', 'ngoo2 iu2')
		
		self.對齊句 = self.分析器.產生對齊句(
			'我有一張椅仔！！', 'gua2 u7 tsit8-tiunn1 i2-a2!!')
		self.型句 = self.分析器.建立句物件('我有一張椅仔！！')
		self.音句 = self.分析器.建立句物件('gua2 u7 tsit8-tiunn1 i2-a2!!')
		self.有詞漢羅 = self.分析器.建立句物件('我 u7 一張 i2-a2!!')
		self.無詞漢羅 = self.分析器.建立句物件('gua2 u7 一張 i2-a2!!')
		
	def 加我有一張椅仔的集資料(self):
		self.我對齊組 = 組([self.白我對齊詞])
		self.文我對齊組 = 組([self.文我對齊詞])
		self.有對齊組 = 組([self.有對齊詞])
		self.一張對齊組 = 組([self.一張對齊詞])
		self.椅仔對齊組 = 組([self.椅仔對齊詞])
		self.驚對齊組 = 組([self.驚對齊詞])
		
		我詞順序 = list({self.白我對齊詞, self.文我對齊詞})
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
		
		self.句物件 = 句([self.我對齊集, self.有對齊集, self.一張對齊集,
			self.椅仔對齊集, self.驚對齊集, self.驚對齊集])
		self.文我句物件 = 句([self.文我對齊集, self.有對齊集, self.一張對齊集,
			self.椅仔對齊集, self.驚對齊集, self.驚對齊集])
		
	def 斷逐種我有一張椅仔(self, 答案, 答案分數, 答案詞數):
		全部分數 = []
		for 題目 in [self.對齊句, self.型句, self.音句,
				self.有詞漢羅, self.無詞漢羅, ]:
			斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, 題目)
			self.assertEqual(斷詞結果, 答案)
			self.檢查分數詞數(分數, 詞數, 答案分數, 答案詞數)
			全部分數.append(分數)
		for 分數 in 全部分數[1:]:
			self.assertEqual(分數, 全部分數[0])
		return 全部分數
		
	def 加我的鞋仔的資料(self):
		self.我詞 = self.分析器.產生對齊詞('我', 'gua2')
		self.的詞 = self.分析器.產生對齊詞('的', 'e5')
		self.鞋詞 = self.分析器.產生對齊詞('鞋', 'e5')
		self.仔詞 = self.分析器.產生對齊詞('仔', 'a2')
		self.我 = self.分析器.產生對齊集('我', 'gua2')
		self.的 = self.分析器.產生對齊組('的', 'e5')
		self.鞋 = self.分析器.產生對齊組('鞋', 'e5')
		self.仔 = self.分析器.產生對齊集('仔', 'a2')
		e5_鞋的 = 集()
		e5_鞋的.內底組 = [self.鞋, self.的, ]
		self.我_e5_e5_仔_鞋的 = 句()
		self.我_e5_e5_仔_鞋的.內底集 = [self.我, e5_鞋的, e5_鞋的, self.仔]
		e5_的鞋 = 集()
		e5_的鞋.內底組 = [self.的, self.鞋, ]
		self.我_e5_e5_仔_的鞋 = 句()
		self.我_e5_e5_仔_的鞋.內底集 = [self.我, e5_的鞋, e5_的鞋, self.仔]
		self.我_e5_e5_仔 = self.分析器.建立句物件('我 e5 e5 仔')
		鞋集 = 集()
		鞋集.內底組 = [self.鞋, ]
		的集 = 集()
		的集.內底組 = [self.的, ]
		self.我鞋鞋仔 = self.分析器.產生對齊句('我鞋鞋仔', 'gua2 e5 e5 a2')
		self.我的鞋仔 = self.分析器.產生對齊句('我的鞋仔', 'gua2 e5 e5 a2')
		
	def 加鞋仔的資料(self):
		self.加我的鞋仔的資料()
		self.鞋仔詞 = self.分析器.產生對齊詞('鞋仔', 'e5-a2')
		鞋集物件 = self.分析器.建立集物件('e5')
		仔集物件 = self.分析器.建立集物件('a2')
		self.鞋仔兩集句物件 = self.分析器.建立句物件('')
		self.鞋仔兩集句物件.內底集 = [鞋集物件, 仔集物件]
		self.孤詞鞋仔句 = self.分析器.產生對齊句('鞋仔', 'e5-a2')
		self.兩詞鞋仔句 = self.分析器.產生對齊句('鞋仔', 'e5 a2')
		
	def 試斷我的鞋仔(self, 答案):
		答案結果, 答案分數, 答案詞數 = self.斷詞.斷詞(self.字典, self.連詞, 答案)
		鞋的結果, 鞋的分數 , 鞋的詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.我_e5_e5_仔_鞋的)
		的鞋結果, 的鞋分數, 的鞋詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.我_e5_e5_仔_的鞋)
		e5_e5_結果, e5_e5_分數, e5_e5_詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.我_e5_e5_仔)
		self.assertEqual(答案結果, 答案,)
		self.assertEqual(鞋的結果, 答案,)
		self.assertEqual(的鞋結果, 答案,)
		self.assertEqual(e5_e5_結果, 答案,)
		self.assertLess(答案分數, 0.0,)
		self.assertLess(鞋的分數, 0.0,)
		self.assertLess(的鞋分數, 0.0,)
		self.assertLess(e5_e5_分數, 0.0,)
		self.assertEqual(答案詞數, 4,)
		self.assertEqual(鞋的詞數, 4,)
		self.assertEqual(的鞋詞數, 4,)
		self.assertEqual(e5_e5_詞數, 4,)

	def 加予伊出去耍的資料(self):
		self.予對齊詞 = self.分析器.產生對齊詞('予', 'hoo7')
		self.伊對齊詞 = self.分析器.產生對齊詞('伊', 'i1')
		self.雨衣對齊詞 = self.分析器.產生對齊詞('雨衣', 'hoo7-i1')
		self.出去對齊詞 = self.分析器.產生對齊詞('出去', 'tsut4-khi3')
		self.耍對齊詞 = self.分析器.產生對齊詞('耍', 'sng2')

		self.予伊出去耍全羅 = self.分析器.建立句物件('hoo7 i1 tsut4 khi3 sng2')
		self.予伊對齊句 = self.分析器.產生對齊句(
			'予伊出去耍', 'hoo7 i1 tsut4-khi3 sng2')
		self.雨衣對齊句 = self.分析器.產生對齊句(
			'雨衣出去耍', 'hoo7-i1 tsut4-khi3 sng2')
		self.予伊耍對齊句 = self.分析器.產生對齊句(
			'予伊耍雨衣', 'hoo7 i1 sng2 hoo7-i1')

	def 檢查分數詞數(self, 分數, 詞數, 分數上限, 詞數答案):
		self.assertLess(分數, 分數上限)
		self.assertEqual(詞數, 詞數答案)
