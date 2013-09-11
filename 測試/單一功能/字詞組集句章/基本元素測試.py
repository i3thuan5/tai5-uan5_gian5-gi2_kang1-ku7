import unittest
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.基本元素.詞 import 詞
from 字詞組集句章.基本元素.組 import 組
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.基本元素.章 import 章
from 字詞組集句章.基本元素.公用變數 import 無音
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤

class 基本元素測試(unittest.TestCase):
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

if __name__ == '__main__':
	unittest.main()
