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
from 臺灣言語工具.字詞組集句章.基本元素.詞 import 詞
from 臺灣言語工具.字詞組集句章.基本元素.組 import 組
from 臺灣言語工具.字詞組集句章.基本元素.集 import 集
from 臺灣言語工具.字詞組集句章.基本元素.句 import 句
from 臺灣言語工具.字詞組集句章.基本元素.章 import 章
from 臺灣言語工具.字詞組集句章.基本元素.公用變數 import 無音
from 臺灣言語工具.字詞組集句章.解析整理.型態錯誤 import 型態錯誤

class 基本元素試驗(unittest.TestCase):
	def setUp(self):
		self.型 = '媠'
		self.音 = 'ㄙㄨㄧˋ'
		self.字物件 = 字(self.型, self.音)
		self.字陣列 = [self.字物件, self.字物件]
		self.詞物件 = 詞(self.字陣列)
		self.詞陣列 = [self.詞物件, self.詞物件, self.詞物件]
		self.組物件 = 組(self.詞陣列)
		self.組陣列 = [self.組物件, self.組物件, self.組物件, self.組物件]
		self.集物件 = 集(self.組陣列)
		self.集陣列 = [self.集物件, self.集物件]
		self.句物件 = 句(self.集陣列)
		self.句陣列 = [self.句物件, self.句物件, self.句物件]
		self.章物件 = 章(self.句陣列)


	def tearDown(self):
		pass

	def test_字(self):
		型 = '媠'
		音 = 'ㄙㄨㄧˋ'
		字物件 = 字(型, 音)
		self.assertEqual(字物件.型, 型)
		self.assertEqual(字物件.音, 音)

	def test_字無音(self):
		型 = '媠'
		字物件 = 字(型)
		self.assertEqual(字物件.型, 型)
		self.assertEqual(字物件.音, 無音)

	def test_詞(self):
		型 = '媠'
		音 = 'ㄙㄨㄧˋ'
		字物件 = 字(型, 音)
		字陣列 = [字物件, 字物件]
		詞物件 = 詞(字陣列)
		另外字陣列 = [字(型, 音), 字(型, 音)]
		self.assertEqual(詞物件.內底字, 另外字陣列)
	def test_組(self):
		self.assertEqual(self.組物件.內底詞, self.詞陣列)
	def test_集(self):
		self.assertEqual(self.集物件.內底組, self.組陣列)
	def test_句(self):
		self.assertEqual(self.句物件.內底集, self.集陣列)
	def test_章(self):
		self.assertEqual(self.章物件.內底句, self.句陣列)

	def test_字烏白傳(self):
		型 = '媠'
		音 = 'ㄙㄨㄧˋ'
		字物件 = 字(型)
		self.assertRaises(型態錯誤, 字, 4)
		self.assertRaises(型態錯誤, 字, (音,))
		self.assertRaises(型態錯誤, 字, 型, None)
		self.assertRaises(型態錯誤, 字, 型, 20)

	def test_詞組集章句烏白傳(self):
		self.assertRaises(型態錯誤, 詞, None)
		self.assertRaises(型態錯誤, 詞, [None])
		self.assertRaises(型態錯誤, 詞, ['sui2'])
		self.assertRaises(型態錯誤, 組, None)
		self.assertRaises(型態錯誤, 組, [None])
		self.assertRaises(型態錯誤, 組, ['sui2'])
		self.assertRaises(型態錯誤, 集, None)
		self.assertRaises(型態錯誤, 集, [None])
		self.assertRaises(型態錯誤, 集, ['sui2'])
		self.assertRaises(型態錯誤, 章, None)
		self.assertRaises(型態錯誤, 章, [None])
		self.assertRaises(型態錯誤, 章, ['sui2'])
		self.assertRaises(型態錯誤, 句, None)
		self.assertRaises(型態錯誤, 句, [None])
		self.assertRaises(型態錯誤, 句, ['sui2'])

	def test_句獨立檢查(self):
		self.assertEqual(len(self.句物件.內底集), 2)
		self.assertEqual(len(self.章物件.內底句[0].內底集), 2)
		self.集陣列.append(集(self.組陣列))
		self.assertEqual(len(self.句物件.內底集), 2)
		self.assertEqual(len(self.章物件.內底句[0].內底集), 2)

	def test_句結構檢查(self):
		self.assertEqual(len(self.句物件.內底集), 2)
		self.assertEqual(len(self.章物件.內底句[0].內底集), 2)
		self.句物件.內底集.append(集(self.組陣列))
		self.assertEqual(len(self.句物件.內底集), 3)
		self.assertEqual(len(self.章物件.內底句[0].內底集), 2)

	def test_集獨立檢查(self):
		self.assertEqual(len(self.集物件.內底組), 4)
		self.assertEqual(len(self.句物件.內底集[0].內底組), 4)
		self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組), 4)
		self.組陣列.append(組(self.詞陣列))
		self.assertEqual(len(self.集物件.內底組), 4)
		self.assertEqual(len(self.句物件.內底集[0].內底組), 4)
		self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組), 4)

	def test_集結構檢查(self):
		self.assertEqual(len(self.集物件.內底組), 4)
		self.assertEqual(len(self.句物件.內底集[0].內底組), 4)
		self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組), 4)
		self.集物件.內底組.append(組(self.詞陣列))
		self.assertEqual(len(self.集物件.內底組), 5)
		self.assertEqual(len(self.句物件.內底集[0].內底組), 4)
		self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組), 4)

	def test_組獨立檢查(self):
		self.assertEqual(len(self.組物件.內底詞), 3)
		self.assertEqual(len(self.集物件.內底組[0].內底詞), 3)
		self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞), 3)
		self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞), 3)
		self.詞陣列.append(詞(self.字陣列))
		self.assertEqual(len(self.組物件.內底詞), 3)
		self.assertEqual(len(self.集物件.內底組[0].內底詞), 3)
		self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞), 3)
		self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞), 3)

	def test_組結構檢查(self):
		self.assertEqual(len(self.組物件.內底詞), 3)
		self.assertEqual(len(self.集物件.內底組[0].內底詞), 3)
		self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞), 3)
		self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞), 3)
		self.組物件.內底詞.append(詞(self.字陣列))
		self.assertEqual(len(self.組物件.內底詞), 4)
		self.assertEqual(len(self.集物件.內底組[0].內底詞), 3)
		self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞), 3)
		self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞), 3)

	def test_詞獨立檢查(self):
		新型 = '文'
		新音 = 'ㆠㄨㄣˊ'
		新字物件 = 字(新型, 新音)
		self.assertEqual(len(self.詞物件.內底字), 2)
		self.assertEqual(len(self.組物件.內底詞[0].內底字), 2)
		self.assertEqual(len(self.集物件.內底組[0].內底詞[0].內底字), 2)
		self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞[0].內底字), 2)
		self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字), 2)
		self.字陣列.append(新字物件)
		self.assertEqual(len(self.詞物件.內底字), 2)
		self.assertEqual(len(self.組物件.內底詞[0].內底字), 2)
		self.assertEqual(len(self.集物件.內底組[0].內底詞[0].內底字), 2)
		self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞[0].內底字), 2)
		self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字), 2)

	def test_詞結構檢查(self):
		新型 = '文'
		新音 = 'ㆠㄨㄣˊ'
		新字物件 = 字(新型, 新音)
		self.assertEqual(len(self.詞物件.內底字), 2)
		self.assertEqual(len(self.組物件.內底詞[0].內底字), 2)
		self.assertEqual(len(self.集物件.內底組[0].內底詞[0].內底字), 2)
		self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞[0].內底字), 2)
		self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字), 2)
		self.詞物件.內底字.append(新字物件)
		self.assertEqual(len(self.詞物件.內底字), 3)
		self.assertEqual(len(self.組物件.內底詞[0].內底字), 2)
		self.assertEqual(len(self.集物件.內底組[0].內底詞[0].內底字), 2)
		self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞[0].內底字), 2)
		self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字), 2)

	def test_字獨立檢查(self):
		新型 = '文'
		新音 = 'ㆠㄨㄣˊ'
		新字物件 = 字(self.型, self.音)
		self.assertEqual(self.詞物件.內底字[0], 字(self.型, self.音))
		self.assertEqual(self.組物件.內底詞[0].內底字[0], 字(self.型, self.音))
		self.assertEqual(self.集物件.內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
		self.assertEqual(self.句物件.內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
		self.assertEqual(self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
		self.字物件.型 = 新型
		self.字物件.音 = 新音
		self.assertEqual(self.詞物件.內底字[0], 字(self.型, self.音))
		self.assertEqual(self.組物件.內底詞[0].內底字[0], 字(self.型, self.音))
		self.assertEqual(self.集物件.內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
		self.assertEqual(self.句物件.內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
		self.assertEqual(self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))

	def test_字結構檢查(self):
		新型 = '文'
		新音 = 'ㆠㄨㄣˊ'
		新字物件 = 字(self.型, self.音)
		self.assertEqual(self.詞物件.內底字[0], 字(self.型, self.音))
		self.assertEqual(self.組物件.內底詞[0].內底字[0], 字(self.型, self.音))
		self.assertEqual(self.集物件.內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
		self.assertEqual(self.句物件.內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
		self.assertEqual(self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
		self.詞物件.內底字[0] = 新字物件
		self.assertEqual(self.詞物件.內底字[0], 字(self.型, self.音))
		self.assertEqual(self.組物件.內底詞[0].內底字[0], 字(self.型, self.音))
		self.assertEqual(self.集物件.內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
		self.assertEqual(self.句物件.內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
		self.assertEqual(self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))

	def test_詞獨立缺失(self):
		新型 = '文'
		新音 = 'ㆠㄨㄣˊ'
		新組物件 = 組(self.詞陣列)
		self.assertEqual(新組物件, self.組物件)
		新組物件.內底詞[0].內底字[0].型 = 新型
		新組物件.內底詞[0].內底字[0].音 = 新音
# 		self.assertRaises(AssertionError, self.assertNotEqual, 新組物件, self.組物件,)
		self.assertNotEqual(新組物件, self.組物件)

if __name__ == '__main__':
	unittest.main()
