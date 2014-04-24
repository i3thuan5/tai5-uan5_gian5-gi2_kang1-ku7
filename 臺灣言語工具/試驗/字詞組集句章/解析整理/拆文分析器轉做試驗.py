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
import unittest
from 臺灣言語工具.字詞組集句章.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.字詞組集句章.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.字詞組集句章.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.字詞組集句章.解析整理.文章粗胚 import 文章粗胚

class 拆文分析器轉做試驗(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.粗胚 = 文章粗胚()
	def tearDown(self):
		pass

	def test_轉做字孤字(self):
		分詞 = '𪜶｜in1'
		型 = '𪜶'
		音 = 'in1'
		字物件 = self.分析器.轉做字物件(分詞)
		self.assertEqual(字物件.型, 型)
		self.assertEqual(字物件.音, 音)

	# 轉做字無檢查有對齊無，這應該是轉物件音的空課
	def test_轉做字無對齊(self):
		分詞 = '美-麗｜sui2'
		型 = '美-麗'
		音 = 'sui2'
		字物件 = self.分析器.轉做字物件(分詞)
		self.assertEqual(字物件.型, 型)
		self.assertEqual(字物件.音, 音)

	def test_轉做字有兩字(self):
		分詞 = '兩｜nng7 个｜e5'
		self.assertRaises(解析錯誤, self.分析器.轉做字物件, 分詞)
	def test_轉做字無半字(self):
		分詞 = ''
		self.assertRaises(解析錯誤, self.分析器.轉做字物件, 分詞)
	def test_轉做字無分型音(self):
		分詞 = '無'
		self.assertRaises(解析錯誤, self.分析器.轉做字物件, 分詞)
	def test_轉做字連字(self):
		分詞 = '-｜-'
		型 = '-'
		音 = '-'
		字物件 = self.分析器.轉做字物件(分詞)
		self.assertEqual(字物件.型, 型)
		self.assertEqual(字物件.音, 音)

	def test_轉做詞孤字(self):
		分詞 = '𪜶｜in1'
		型 = '𪜶'
		音 = 'in1'
		詞物件 = self.分析器.轉做詞物件(分詞)
		self.assertEqual(len(詞物件.內底字), 1)
		self.assertEqual(詞物件.內底字[0].型, 型)
		self.assertEqual(詞物件.內底字[0].音, 音)

	def test_轉做詞濟字(self):
		分詞 = '美-麗｜bi2-le7'
		型甲 = '美'
		音甲 = 'bi2'
		型乙 = '麗'
		音乙 = 'le7'
		詞物件 = self.分析器.轉做詞物件(分詞)
		self.assertEqual(len(詞物件.內底字), 2)
		self.assertEqual(詞物件.內底字[0].型, 型甲)
		self.assertEqual(詞物件.內底字[0].音, 音甲)
		self.assertEqual(詞物件.內底字[1].型, 型乙)
		self.assertEqual(詞物件.內底字[1].音, 音乙)

	def test_轉做詞漢字無連字(self):
		分詞 = '美麗｜bi2-le7'
		型甲 = '美'
		音甲 = 'bi2'
		型乙 = '麗'
		音乙 = 'le7'
		詞物件 = self.分析器.轉做詞物件(分詞)
		self.assertEqual(len(詞物件.內底字), 2)
		self.assertEqual(詞物件.內底字[0].型, 型甲)
		self.assertEqual(詞物件.內底字[0].音, 音甲)
		self.assertEqual(詞物件.內底字[1].型, 型乙)
		self.assertEqual(詞物件.內底字[1].音, 音乙)

	def test_轉做詞無對齊(self):
		分詞 = '美-麗｜sui2'
		self.assertRaises(解析錯誤, self.分析器.轉做詞物件, 分詞)

	def test_轉做詞有兩字(self):
		分詞 = '兩｜nng7 个｜e5'
		self.assertRaises(解析錯誤, self.分析器.轉做詞物件, 分詞)

	def test_轉做詞無半字(self):
		分詞 = ''
		詞物件 = self.分析器.轉做詞物件(分詞)
		self.assertEqual(len(詞物件.內底字), 0)

	def test_轉做詞無分型音(self):
		分詞 = '無'
		self.assertRaises(解析錯誤, self.分析器.轉做字物件, 分詞)

	def test_轉做組集句章孤字(self):
		分詞 = '𪜶｜in1'
		組物件 = self.分析器.轉做組物件(分詞)
		self.assertEqual(len(組物件.內底詞), 1)
		self.assertEqual(組物件.內底詞[0], self.分析器.轉做詞物件('𪜶｜in1'))
		集物件 = self.分析器.轉做集物件(分詞)
		self.assertEqual(len(集物件.內底組), 1)
		self.assertEqual(集物件.內底組[0], 組物件)
		句物件 = self.分析器.轉做句物件(分詞)
		self.assertEqual(len(句物件.內底集), 1)
		self.assertEqual(句物件.內底集[0], 集物件)
		章物件 = self.分析器.轉做章物件(分詞)
		self.assertEqual(len(章物件.內底句), 1)
		self.assertEqual(章物件.內底句[0], 句物件)

	def test_轉做組集句章濟字(self):
		分詞 = '𪜶｜in1 兩｜nng7 个｜e5 生-做｜senn1-tso3 一-模-一-樣｜it4-boo5-it4-iunn7 。｜.'
		組物件 = self.分析器.轉做組物件(分詞)
		self.assertEqual(len(組物件.內底詞), 6)
		self.assertEqual(組物件.內底詞[0], self.分析器.轉做詞物件('𪜶｜in1'))
		self.assertEqual(組物件.內底詞[1], self.分析器.轉做詞物件('兩｜nng7'))
		self.assertEqual(組物件.內底詞[2], self.分析器.轉做詞物件('个｜e5'))
		self.assertEqual(組物件.內底詞[3], self.分析器.轉做詞物件('生-做｜senn1-tso3'))
		self.assertEqual(組物件.內底詞[4], self.分析器.轉做詞物件('一-模-一-樣｜it4-boo5-it4-iunn7'))
		self.assertEqual(組物件.內底詞[5], self.分析器.轉做詞物件('。｜.'))
		集物件 = self.分析器.轉做集物件(分詞)
		self.assertEqual(len(集物件.內底組), 1)
		self.assertEqual(集物件.內底組[0], 組物件)
		句物件 = self.分析器.轉做句物件(分詞)
		self.assertEqual(len(句物件.內底集), 1)
		self.assertEqual(句物件.內底集[0], 集物件)
		章物件 = self.分析器.轉做章物件(分詞)
		self.assertEqual(len(章物件.內底句), 1)
		self.assertEqual(章物件.內底句[0], 句物件)

	def test_轉做組集句章濟字佮有連字(self):
		分詞 = '兩｜nng7 个｜e5 -｜- -｜- 一-模-一-樣｜it4-boo5-it4-iunn7 。｜.'
		組物件 = self.分析器.轉做組物件(分詞)
		self.assertEqual(len(組物件.內底詞), 6)
		self.assertEqual(組物件.內底詞[0], self.分析器.轉做詞物件('兩｜nng7'))
		self.assertEqual(組物件.內底詞[1], self.分析器.轉做詞物件('个｜e5'))
		self.assertEqual(組物件.內底詞[2], self.分析器.轉做詞物件('-｜-'))
		self.assertEqual(組物件.內底詞[3], self.分析器.轉做詞物件('-｜-'))
		self.assertEqual(組物件.內底詞[4], self.分析器.轉做詞物件('一-模-一-樣｜it4-boo5-it4-iunn7'))
		self.assertEqual(組物件.內底詞[5], self.分析器.轉做詞物件('。｜.'))
		集物件 = self.分析器.轉做集物件(分詞)
		self.assertEqual(len(集物件.內底組), 1)
		self.assertEqual(集物件.內底組[0], 組物件)
		句物件 = self.分析器.轉做句物件(分詞)
		self.assertEqual(len(句物件.內底集), 1)
		self.assertEqual(句物件.內底集[0], 集物件)
		章物件 = self.分析器.轉做章物件(分詞)
		self.assertEqual(len(章物件.內底句), 1)
		self.assertEqual(章物件.內底句[0], 句物件)

	def test_轉做組集句章濟字有加的空白(self):
		分詞 = '  𪜶｜in1    兩｜nng7     个｜e5 \n'\
			'  生-做｜senn1-tso3 一-模-一-樣｜it4-boo5-it4-iunn7 。｜.    '
		組物件 = self.分析器.轉做組物件(分詞)
		self.assertEqual(len(組物件.內底詞), 6)
		self.assertEqual(組物件.內底詞[0], self.分析器.轉做詞物件('𪜶｜in1'))
		self.assertEqual(組物件.內底詞[1], self.分析器.轉做詞物件('兩｜nng7'))
		self.assertEqual(組物件.內底詞[2], self.分析器.轉做詞物件('个｜e5'))
		self.assertEqual(組物件.內底詞[3], self.分析器.轉做詞物件('生-做｜senn1-tso3'))
		self.assertEqual(組物件.內底詞[4], self.分析器.轉做詞物件('一-模-一-樣｜it4-boo5-it4-iunn7'))
		self.assertEqual(組物件.內底詞[5], self.分析器.轉做詞物件('。｜.'))
		集物件 = self.分析器.轉做集物件(分詞)
		self.assertEqual(len(集物件.內底組), 1)
		self.assertEqual(集物件.內底組[0], 組物件)
		句物件 = self.分析器.轉做句物件(分詞)
		self.assertEqual(len(句物件.內底集), 1)
		self.assertEqual(句物件.內底集[0], 集物件)
		章物件 = self.分析器.轉做章物件(分詞)
		self.assertEqual(len(章物件.內底句), 1)
		self.assertEqual(章物件.內底句[0], 句物件)

	def test_轉做組集句章無半字(self):
		分詞 = ''
		組物件 = self.分析器.轉做組物件(分詞)
		self.assertEqual(len(組物件.內底詞), 0)
		集物件 = self.分析器.轉做集物件(分詞)
		self.assertEqual(len(集物件.內底組), 0)
		句物件 = self.分析器.轉做句物件(分詞)
		self.assertEqual(len(句物件.內底集), 0)
		章物件 = self.分析器.轉做章物件(分詞)
		self.assertEqual(len(章物件.內底句), 0)

	def test_轉做章濟句(self):
		分詞一 = '𪜶｜in1 兩｜nng7 个｜e5 兄-弟-仔｜hiann1-ti7-a2 '\
			'為-著｜ui7-tioh8 拚｜piann3 生-理｜sing1-li2 ，｜, '
		分詞二 = '就｜to7 按-呢｜an2-ne1 一-刀-兩-斷｜it4-to1-liong2-tuan7 '\
			'無｜bo5 來-去｜lai5-khi3 。｜.'
		分詞 = 分詞一 + 分詞二
		章物件 = self.分析器.轉做章物件(分詞)
		self.assertEqual(len(章物件.內底句), 2)
		self.assertEqual(章物件.內底句[0], self.分析器.轉做句物件(分詞一))
		self.assertEqual(章物件.內底句[1], self.分析器.轉做句物件(分詞二))
		
	def test_轉做章濟標點句(self):
		分詞零= '。｜. 。｜. '
		分詞一 = '𪜶｜in1 兩｜nng7 个｜e5 兄-弟-仔｜hiann1-ti7-a2 '\
			'為-著｜ui7-tioh8 拚｜piann3 生-理｜sing1-li2 ，｜, 。｜. '
		分詞二 ='就｜to7 。｜. 。｜. '
		分詞三= '就｜to7 按｜an2 。｜. '
		分詞四 = '就｜to7 按-呢｜an2-ne1 。｜. '
		分詞五  = '就｜to7 按-呢｜an2-ne1 一-刀-兩-斷｜it4-to1-liong2-tuan7 '\
			'無｜bo5 來-去｜lai5-khi3 。｜. 。｜. ！｜! '
		分詞陣列 = [分詞零,分詞一,分詞二,分詞三,分詞四,分詞五]
		分詞 = ''.join(分詞陣列)
		章物件 = self.分析器.轉做章物件(分詞)
		句陣列=[]
		for 分 in 分詞陣列:
			 句陣列.append(self.分析器.轉做句物件(分))
		self.assertEqual(len(章物件.內底句), 6)
		self.assertEqual(章物件.內底句, 句陣列)
		
	def test_烏白傳參數(self):
		self.assertRaises(型態錯誤, self.分析器.轉做字物件, None)
		self.assertRaises(型態錯誤, self.分析器.轉做詞物件, 333)
		self.assertRaises(型態錯誤, self.分析器.轉做組物件, [])
		self.assertRaises(型態錯誤, self.分析器.轉做集物件, None)
		self.assertRaises(型態錯誤, self.分析器.轉做句物件, 14325)
		self.assertRaises(型態錯誤, self.分析器.轉做章物件, ('None',))
