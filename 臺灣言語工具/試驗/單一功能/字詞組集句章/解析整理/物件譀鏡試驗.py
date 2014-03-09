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
from 臺灣言語工具.字詞組集句章.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.字詞組集句章.基本元素.集 import 集
from 臺灣言語工具.字詞組集句章.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.字詞組集句章.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.字詞組集句章.基本元素.公用變數 import 分字符號

class 物件譀鏡試驗(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.譀鏡 = 物件譀鏡()
	def tearDown(self):
		pass

	def test_看字(self):
		型 = '我'
		音 = 'gua2'
		字物件 = self.分析器.產生對齊字(型, 音)
		self.assertEqual(self.譀鏡.看型(字物件), 型)
		self.assertEqual(self.譀鏡.看音(字物件), 音)
		斷詞 = 型 + '｜' + 音
		self.assertEqual(self.譀鏡.看斷詞(字物件, '｜'), 斷詞)

	def test_看詞(self):
		型 = '姑-娘'
		音 = 'koo1-niu5'
		詞物件 = self.分析器.產生對齊詞(型, 音)
		無分字型 = 型.replace(分字符號, '')
		self.assertEqual(self.譀鏡.看型(詞物件), 無分字型)
		self.assertEqual(self.譀鏡.看音(詞物件), 音)
		斷詞 = 型 + '｜' + 音
		self.assertEqual(self.譀鏡.看斷詞(詞物件, '｜'), 斷詞)

	def test_看組孤字(self):
		型 = '恁老母ti3佗位！'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7 !'
		組物件 = self.分析器.產生對齊組(型, 音)
		self.assertEqual(self.譀鏡.看型(組物件), 型)
		self.assertEqual(self.譀鏡.看音(組物件), 音)
		斷詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜!'
		self.assertEqual(self.譀鏡.看斷詞(組物件, '｜'), 斷詞)

	def test_看組連字(self):
		型 = '恁老母ti3佗位！'
		音 = 'lin1 lau3-bu2 ti3 to1-ui7 !'
		組物件 = self.分析器.產生對齊組(型, 音)
		self.assertEqual(self.譀鏡.看型(組物件), 型)
		self.assertEqual(self.譀鏡.看音(組物件), 音)
		斷詞 = '恁｜lin1 老-母｜lau3-bu2 ti3｜ti3 佗-位｜to1-ui7 ！｜!'
		self.assertEqual(self.譀鏡.看斷詞(組物件, '｜'), 斷詞)

	def test_看集(self):
		型 = '恁老母ti3佗位'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7'
		集物件 = self.分析器.產生對齊集(型, 音)
		self.assertEqual(self.譀鏡.看型(集物件), 型)
		self.assertEqual(self.譀鏡.看音(集物件), 音)
		斷詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7'
		self.assertEqual(self.譀鏡.看斷詞(集物件, '｜'), 斷詞)

	def test_看集內底有兩組以上(self):
		型 = '恁老母ti3佗位'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7'
		集物件 = 集([self.分析器.產生對齊組(型, 音), self.分析器.產生對齊組(型, 音)])
		self.assertRaises(解析錯誤, self.譀鏡.看型, 集物件)
		self.assertRaises(解析錯誤, self.譀鏡.看音, 集物件)
		self.assertRaises(解析錯誤, self.譀鏡.看斷詞, 集物件, '｜')

	def test_看句(self):
		型 = '恁老母ti3佗位'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7'
		句物件 = self.分析器.產生對齊句(型, 音)
		self.assertEqual(self.譀鏡.看型(句物件), 型)
		self.assertEqual(self.譀鏡.看音(句物件), 音)
		斷詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7'
		self.assertEqual(self.譀鏡.看斷詞(句物件, '｜'), 斷詞)

	def test_看章(self):
		型 = '恁老母ti3佗位！恁老母ti3佗位！'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7 ! lin1 lau3 bu2 ti3 to1 ui7 !'
		章物件 = self.分析器.產生對齊章(型, 音)
		self.assertEqual(self.譀鏡.看型(章物件), 型)
		self.assertEqual(self.譀鏡.看音(章物件), 音)
		斷詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜! 恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜!'
		self.assertEqual(self.譀鏡.看斷詞(章物件, '｜'), 斷詞)
		斷詞加 = '恁+lin1 老+lau3 母+bu2 ti3+ti3 佗+to1 位+ui7 ！+! 恁+lin1 老+lau3 母+bu2 ti3+ti3 佗+to1 位+ui7 ！+!'
		self.assertEqual(self.譀鏡.看斷詞(章物件, '+'), 斷詞加)

	def test_看章加連字符(self):
		型 = '恁老母ti3佗位！恁lau3-bu2-ti3佗位！'
		音 = 'lin1 lau3-bu2 ti3 to1 ui7 ! lin1 lau3-bu2-ti3 to1-ui7 !'
		章物件 = self.分析器.產生對齊章(型, 音)
		無分字型 = 型.replace(分字符號, '')
		self.assertEqual(self.譀鏡.看型(章物件), 無分字型)
		self.assertEqual(self.譀鏡.看音(章物件), 音)
		斷詞 = '恁｜lin1 老-母｜lau3-bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜! 恁｜lin1 lau3-bu2-ti3｜lau3-bu2-ti3 佗-位｜to1-ui7 ！｜!'
		self.assertEqual(self.譀鏡.看斷詞(章物件, '｜'), 斷詞)
		self.assertEqual(self.譀鏡.看斷詞(章物件, 分字音符號 = '｜'), 斷詞)

	def test_看章換連字符(self):
		型 = '恁老母ti3佗位！恁老母ti3佗位！'
		音 = 'lin1 lau3-bu2 ti3 to1 ui7 ! lin1 lau3-bu2-ti3 to1-ui7 !'
		答型 = '恁|老_母|ti3|佗|位|！|恁|老_母_ti3|佗_位|！'
		答音 = 'lin1|lau3_bu2|ti3|to1|ui7|!|lin1|lau3_bu2_ti3|to1_ui7|!'
		章物件 = self.分析器.產生對齊章(型, 音)
		self.assertEqual(self.譀鏡.看型(章物件, '_', '|'), 答型)
		self.assertEqual(self.譀鏡.看音(章物件, '_', '|'), 答音)
		self.assertEqual(self.譀鏡.看型(章物件, 物件分字符號 = '_', 物件分詞符號 = '|'), 答型)
		self.assertEqual(self.譀鏡.看音(章物件, 物件分字符號 = '_', 物件分詞符號 = '|'), 答音)
		斷詞 = '恁@lin1^老_母@lau3_bu2^ti3@ti3^佗@to1^位@ui7^！@!^恁@lin1^老_母_ti3@lau3_bu2_ti3^佗_位@to1_ui7^！@!'
		self.assertEqual(self.譀鏡.看斷詞(章物件, '@', '_', '^'), 斷詞)
		self.assertEqual(self.譀鏡.看斷詞(章物件, 分字音符號 = '@', 物件分字符號 = '_', 物件分詞符號 = '^'), 斷詞)

	def test_參數烏白傳(self):
		self.assertRaises(型態錯誤, self.譀鏡.看型, 790830)
		self.assertRaises(型態錯誤, self.譀鏡.看音, None)
		self.assertRaises(型態錯誤, self.譀鏡.看斷詞, '｜', '｜')
