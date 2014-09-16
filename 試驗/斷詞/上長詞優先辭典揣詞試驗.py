# -*- coding: utf-8 -*-
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
from 試驗.斷詞.辭典揣詞試驗 import 辭典揣詞試驗
from 臺灣言語工具.斷詞.上長詞優先辭典揣詞 import 上長詞優先辭典揣詞
from 臺灣言語工具.基本元素.句 import 句

class 上長詞優先辭典揣詞試驗(辭典揣詞試驗):
	辭典揣詞 = 上長詞優先辭典揣詞

	def test_一四切比兩三切閣較好(self):
		self.test_基本揣詞()

		兩三分數 = []
		self.有一張對齊詞 = self.分析器.產生對齊詞('有一張', 'u7-tsit8-tiunn1')
		self.字典.加詞(self.有一張對齊詞)
		self.有一張集 = self.分析器.產生對齊集('有一張', 'u7-tsit8-tiunn1')
		新句物件 = 句([self.我對齊集, self.有一張集,
			self.椅仔對齊集, self.驚對齊集, self.驚對齊集])
		揣詞結果, 分數, 詞數 = self.揣詞.揣詞(self.字典, self.對齊句)
		self.assertEqual(揣詞結果, 新句物件)
		self.檢查分數詞數(分數, 詞數, 0, 5)
		兩三分數.append(分數)
		揣詞結果, 分數, 詞數 = self.揣詞.揣詞(self.字典, self.型句)
		self.assertEqual(揣詞結果, 新句物件)
		self.檢查分數詞數(分數, 詞數, 0, 5)
		兩三分數.append(分數)
		揣詞結果, 分數, 詞數 = self.揣詞.揣詞(self.字典, self.音句)
		self.assertEqual(揣詞結果, 新句物件)
		self.檢查分數詞數(分數, 詞數, 0, 5)
		兩三分數.append(分數)
		揣詞結果, 分數, 詞數 = self.揣詞.揣詞(self.字典, self.有詞漢羅)
		self.assertEqual(揣詞結果, 新句物件)
		self.檢查分數詞數(分數, 詞數, 0, 5)
		兩三分數.append(分數)
		揣詞結果, 分數, 詞數 = self.揣詞.揣詞(self.字典, self.無詞漢羅)
		self.assertEqual(揣詞結果, 新句物件)
		self.檢查分數詞數(分數, 詞數, 0, 5)
		兩三分數.append(分數)
		
		一四分數 = []
		self.一張椅仔對齊詞 = self.分析器.產生對齊詞('一張椅仔', 'tsit8-tiunn1-i2-a2')
		self.字典.加詞(self.一張椅仔對齊詞)
		self.一張椅仔集 = self.分析器.產生對齊集('一張椅仔', 'tsit8-tiunn1-i2-a2')
		新句物件 = 句([self.我對齊集, self.有對齊集,
			self.一張椅仔集, self.驚對齊集, self.驚對齊集])
		揣詞結果, 分數, 詞數 = self.揣詞.揣詞(self.字典, self.對齊句)
		self.assertEqual(揣詞結果, 新句物件)
		self.檢查分數詞數(分數, 詞數, 0, 5)
		一四分數.append(分數)
		揣詞結果, 分數, 詞數 = self.揣詞.揣詞(self.字典, self.型句)
		self.assertEqual(揣詞結果, 新句物件)
		self.檢查分數詞數(分數, 詞數, 0, 5)
		一四分數.append(分數)
		揣詞結果, 分數, 詞數 = self.揣詞.揣詞(self.字典, self.音句)
		self.assertEqual(揣詞結果, 新句物件)
		self.檢查分數詞數(分數, 詞數, 0, 5)
		一四分數.append(分數)
		揣詞結果, 分數, 詞數 = self.揣詞.揣詞(self.字典, self.有詞漢羅)
		self.assertEqual(揣詞結果, 新句物件)
		self.檢查分數詞數(分數, 詞數, 0, 5)
		一四分數.append(分數)
		揣詞結果, 分數, 詞數 = self.揣詞.揣詞(self.字典, self.無詞漢羅)
		self.assertEqual(揣詞結果, 新句物件)
		self.檢查分數詞數(分數, 詞數, 0, 5)
		一四分數.append(分數)
		
		for 分數 in 兩三分數[1:]:
			self.assertEqual(分數, 兩三分數[0])
		for 分數 in 一四分數[1:]:
			self.assertEqual(分數, 一四分數[0])
		self.assertLessEqual(兩三分數[0], 一四分數[0])
