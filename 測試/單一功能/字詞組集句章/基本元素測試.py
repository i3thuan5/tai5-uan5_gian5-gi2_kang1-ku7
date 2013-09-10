import unittest
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.基本元素.詞 import 詞

class 基本元素測試(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_字(self):
		型 = '媠'
		音 = 'ㄙㄨㄧˋ'
		字物件 = 字(型, 音)
		self.assertEqual(字物件.型, 型)
		self.assertEqual(字物件.音, 音)

	def test_詞(self):
		型 = '媠'
		音 = 'ㄙㄨㄧˋ'
		字物件 = 字(型, 音)
		字陣列 = [字物件, 字物件]
		詞物件 = 詞(字陣列)
		另外字陣列 = [字(型, 音), 字(型, 音)]
		self.assertEqual(詞物件.內底字, 另外字陣列)

	def tst_詞(self):
		型 = '媠媠姑娘'
		音 = 'ㄙㄨㄧˋ ㄙㄨㄧˋ ㄍㆦ ㄋㄧㄨˊ'
		字物件 = 字(型, 音)
		self.assertEqual(字物件.型, 型)
		self.assertEqual(字物件.音, 音)

if __name__ == '__main__':
	unittest.main()
