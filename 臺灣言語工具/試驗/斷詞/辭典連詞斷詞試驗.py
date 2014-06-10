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

		self.我對齊詞 = self.分析器.產生對齊詞('我', 'gua2')
		self.文我對齊詞 = self.分析器.產生對齊詞('我', 'ngoo2')
		self.有對齊詞 = self.分析器.產生對齊詞('有', 'u7')
		self.一張對齊詞 = self.分析器.產生對齊詞('一張', 'tsit8-tiunn1')
		self.椅仔對齊詞 = self.分析器.產生對齊詞('椅仔', 'i2-a2')
		self.驚對齊詞 = self.分析器.產生對齊詞('！', '!')

		self.對齊句 = self.分析器.產生對齊句(
			'我有一張椅仔！！', 'gua2 u7 tsit8-tiunn1 i2-a2!!')
		self.型句 = self.分析器.建立句物件('我有一張椅仔！！')
		self.音句 = self.分析器.建立句物件('gua2 u7 tsit8-tiunn1 i2-a2!!')
		self.有詞漢羅 = self.分析器.建立句物件('我 u7 一張 i2-a2!!')
		self.無詞漢羅 = self.分析器.建立句物件('gua2 u7 一張 i2-a2!!')

		self.予對齊詞 = self.分析器.產生對齊詞('予', 'hoo7')
		self.伊對齊詞 = self.分析器.產生對齊詞('伊', 'i1')
		self.雨衣對齊詞 = self.分析器.產生對齊詞('雨衣', 'hoo7-i1')
		self.出去對齊詞 = self.分析器.產生對齊詞('出去', 'tsut4-khi2')
		self.耍對齊詞 = self.分析器.產生對齊詞('耍', 'sng2')

		self.予伊出去耍全羅 = self.分析器.建立句物件('hoo7 i1 tsut4 khi2 sng2')
		self.予伊對齊句 = self.分析器.產生對齊句(
			'予伊出去耍', 'hoo7 i1 tsut4-khi3 sng2')
		self.雨衣對齊句 = self.分析器.產生對齊句(
			'雨衣出去耍', 'hoo7-i1 tsut4-khi3 sng2')
		self.予伊耍對齊句 = self.分析器.產生對齊句(
			'予伊耍雨衣', 'hoo7 i1 sng2 hoo7-i1')



	def tearDown(self):
		pass

	def test_句無連詞(self):
		self.字典.加詞(self.我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.字典.加詞(self.驚對齊詞)
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.對齊句)
		self.assertEqual(斷詞結果, self.句物件)
		self.檢查分數詞數(分數, 詞數, 0, 6)
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.型句)
		self.assertEqual(斷詞結果, self.句物件)
		self.檢查分數詞數(分數, 詞數, 0, 6)
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.音句)
		self.assertEqual(斷詞結果, self.句物件)
		self.檢查分數詞數(分數, 詞數, 0, 6)
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.有詞漢羅)
		self.assertEqual(斷詞結果, self.句物件)
		self.檢查分數詞數(分數, 詞數, 0, 6)
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.無詞漢羅)
		self.assertEqual(斷詞結果, self.句物件)
		self.檢查分數詞數(分數, 詞數, 0, 6)

	def test_句毋是愈長愈好(self):
		self.予對齊詞 = self.分析器.產生對齊詞('予', 'hoo7')
		self.伊對齊詞 = self.分析器.產生對齊詞('伊', 'i1')
		self.雨衣對齊詞 = self.分析器.產生對齊詞('雨衣', 'hoo7-i1')
		self.出去對齊詞 = self.分析器.產生對齊詞('出去', 'tsut4-khi2')
		self.耍對齊詞 = self.分析器.產生對齊詞('耍', 'sng2')
		self.字典.加詞(self.予對齊詞)
		self.字典.加詞(self.伊對齊詞)
		self.字典.加詞(self.出去對齊詞)
		self.字典.加詞(self.耍對齊詞)
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.對齊句)
		self.assertEqual(斷詞結果, self.予伊對齊句)
		self.檢查分數詞數(分數, 詞數, 0, 4)

		self.字典.加詞(self.雨衣對齊詞)
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.型句)
		self.assertEqual(斷詞結果, self.雨衣對齊句)
		self.檢查分數詞數(分數, 詞數, 0, 3)

		self.連詞.看(self.self.予伊耍對齊句)
		斷詞結果, 分數, 詞數 = self.斷詞.斷詞(self.字典, self.連詞, self.音句)
		self.assertEqual(斷詞結果, self.句物件)
		self.檢查分數詞數(分數, 詞數, 0, 4)

	def test_試驗好矣未(self):
		raise NotImplementedError
