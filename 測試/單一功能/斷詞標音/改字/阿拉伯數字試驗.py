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
from unittest.case import TestCase
from 斷詞標音.改字.阿拉伯數字 import 阿拉伯數字

class 阿拉伯數字試驗(TestCase):
	def setUp(self):
		self.數字 = 阿拉伯數字()
		pass

	def tearDown(self):
		pass

	def test_判斷是數字無(self):
		self.assertEqual(self.數字.是數字無(''), False)
		self.assertEqual(self.數字.是數字無('0'), True)
		self.assertEqual(self.數字.是數字無('12312'), True)
		self.assertEqual(self.數字.是數字無('13３2312'), True)
		self.assertEqual(self.數字.是數字無('6'), True)
		self.assertEqual(self.數字.是數字無('013３2312三'), False)
		self.assertEqual(self.數字.是數字無('００13３27890'), True)
		self.assertEqual(self.數字.是數字無('000'), True)
		# 小數本來就會使拆開唸，予別的模組合起來
		self.assertEqual(self.數字.是數字無('00.30'), False)
		self.assertEqual(self.數字.是數字無('197.080'), False)
		self.assertEqual(self.數字.是數字無('197.08.0'), False)

	def test_轉號碼(self):
		問答 = [
			('2', '二'),
			('10', '一空'),
			('23', '二三'),
			('15', '一五'),
			('120', '一二空'),
			('230', '二三空'),
			('602', '六百空二'),
			('1001', '一空空一'),
			('1020', '一空二空'),
			('1300', '一三空空'),
			('4512', '四五一二'),
			('5004', '五空空四'),
			('6070', '六空七空'),
			('9800', '九八空'),  # 九干八百
			('10800', '一萬空八百'),
			('400000800', '四空空空空空八空空'),
			('1230567890980654', '一二三空五六七八九空九八空六五四'),
			('1300130013', '一三空空一三空空一三')
			('2000000022222', '兩空空空空空空空二二二二二'),
			('10000000000000000', '一空空空空空空空空空空空空空空空空'),
			('0830', '空八三空'),
			]
		for 問, 答 in 問答:
			if 答 == None:
				self.assertEqual(self.數字.是號碼無(問), False)
				self.assertEqual(self.數字.轉號碼('空', 問), 問)
			else:
				self.assertEqual(self.數字.是號碼無(問), True)
				self.assertEqual(self.數字.轉號碼('空', 問), 答)
				self.assertEqual(self.數字.轉號碼('零', 問),
						答.replace('空', '零'))
	def test_轉數量(self):
		問答 = [
			('2', '二'),
			('10', '十'),
			('23', '二十一'),
			('15', '十一'),
			('120', '百二'),  # 一百二十 一百二
			('230', '兩百三'),  # 兩百三十
			('602', '六百空二'),
			('1001', '一千空一'),
			('1020', '一千空二十'),
			('1300', '千三'),  # 一千三百 一千三
			('4512', '四千五百一十二'),
			('5004', '五千空四'),
			('6070', '六千空七十'),
			('9800', '九千八'),  # 九干八百
			('10800', '一萬空八百'),
			('400000800', '四億空八百'),
			('1230567890980654', '一千兩百三十兆五千六百七十八億九千空九十八萬空六百五十四'),
			('1300130013', '十三億空一十三萬空一十三')
			('2000000022222', '兩兆空二萬兩千兩百二十二'),
			('10000000000000000', None),
			('0830', None),
			]
		for 問, 答 in 問答:
			if 答 == None:
				self.assertEqual(self.數字.是數量無(問), False)
				self.assertEqual(self.數字.轉數量('空', 問), 問)
			else:
				self.assertEqual(self.數字.是數量無(問), True)
				self.assertEqual(self.數字.轉數量('空', 問), 答)
				self.assertEqual(self.數字.轉數量('零', 問),
						答.replace('空', '零'))
	def test_轉閩南語數量省一佮單位(self):
		問答 = [
			('一百二十', '百二'),
			('兩百三十', '兩百三'),
			('六百空二', None),
			('一千空一', None),
			('一千空一十', '一千空十'),
			('一千空二十', None),
			('一千一百一十', '一千一百十'),
			('一千三百', '千三'),
			('一千三百一十三', '一千三百十三'),
			('四千五百一十二', '四千五百十二'),
			('五千空四', None),
			('六千空七十', None),
			('九干八百', '九千八'),
			('十三萬空一十三', '十三萬空十三'),
			]
		for 問, 答 in 問答:
			if 答 == None:
				self.assertEqual(self.數字.轉閩南語數量無(問), False)
				self.assertEqual(self.數字.轉閩南語數量(問), 問)
			else:
				self.assertEqual(self.數字.轉閩南語數量無(問), True)
				self.assertEqual(self.數字.轉閩南語數量(問), 答)
	def test_轉客家話數量省單位(self):
		問答 = [
			('一百二十', '百二'),
			('兩百三十', '兩百三'),
			('六百零二', None),
			('一千零一', None),
			('一千零一十', None),
			('一千零二十', None),
			('一千一百一十', None),
			('一千三百', '千三'),
			('一千三百一十三', None),
			('四千五百一十二', None),
			('五千零四', None),
			('六千零七十', None),
			('九干八百', '九千八'),
			('十三億零一十三萬零一十三', None),
			]
		for 問, 答 in 問答:
			if 答 == None:
				self.assertEqual(self.數字.轉客家話數量無(問), False)
				self.assertEqual(self.數字.轉客家話數量(問), 問)
			else:
				self.assertEqual(self.數字.轉客家話數量無(問), True)
				self.assertEqual(self.數字.轉客家話數量(問), 答)
	def test_轉國語數量省上尾單位(self):
		問答 = [
			('一百二十', '一百二'),
			('兩百三十', '兩百三'),
			('六百零二', None),
			('一千零一', None),
			('一千零一十', None),
			('一千零二十', None),
			('一千一百一十', None),
			('一千三百', '一千三'),
			('一千三百一十三', None),
			('四千五百一十二', None),
			('五千零四', None),
			('六千零七十', None),
			('九干八百', '九千八'),
			('十三億零一十三萬零一十三', None),
			]
		for 問, 答 in 問答:
			if 答 == None:
				self.assertEqual(self.數字.轉國語數量無(問), False)
				self.assertEqual(self.數字.轉國語數量(問), 問)
			else:
				self.assertEqual(self.數字.轉國語數量無(問), True)
				self.assertEqual(self.數字.轉國語數量(問), 答)
