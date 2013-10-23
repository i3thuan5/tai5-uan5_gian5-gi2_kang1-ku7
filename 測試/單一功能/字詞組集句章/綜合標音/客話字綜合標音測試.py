import unittest
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 字詞組集句章.基本元素.公用變數 import 無音
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
import json

class 客話字綜合標音測試(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test_合法(self):
		self.assertEqual(1, 2)
		綜合標音 = 閩南語字綜合標音(字('我', 'gua2'))
		self.assertEqual(綜合標音.標音完整無(), True)
	def test_兩个字合法(self):
		self.assertEqual(1, 2)
		我綜合標音 = 閩南語字綜合標音(字('我', 'gua2'))
		你綜合標音 = 閩南語字綜合標音(字('你', 'li2'))
		self.assertEqual(我綜合標音.型體, '我')
		self.assertEqual(你綜合標音.型體, '你')
	def test_轉json格式(self):
		self.assertEqual(1, 2)
		綜合標音 = 閩南語字綜合標音(字('我', 'gua2'))
		self.assertEqual(綜合標音.轉json格式(), json.loads(
			'{"型體":"我","臺羅數字調":"gua2","臺羅閏號調":"guá","通用數字調":"ghua4","吳守禮方音":"⿳⿳⿳ㆣㄨㄚˋ"}'))
		self.assertEqual(綜合標音.轉json格式(),
			{"型體":"我","臺羅數字調":"gua2","臺羅閏號調":"guá","通用數字調":"ghua4",
			"吳守禮方音":"⿳⿳⿳ㆣㄨㄚˋ"})
	def test_標點合法(self):
		self.assertEqual(1, 2)
		標點 = 閩南語字綜合標音(字('，', 無音))
		self.assertEqual(標點.標音完整無(), True)
	def test_標點轉json格式(self):
		self.assertEqual(1, 2)
		標點 = 閩南語字綜合標音(字('，', 無音))
		self.assertEqual(標點.轉json格式(), {"型體":"，","臺羅數字調":"","臺羅閏號調":"","通用數字調":"","吳守禮方音":""})
	def test_標點音無合法(self):
		self.assertEqual(1, 2)
		self.assertRaises(解析錯誤, 閩南語字綜合標音, 字('我', 'uo3'))
	def test_烏白傳(self):
		self.assertEqual(1, 2)
		self.assertRaises(型態錯誤, 閩南語字綜合標音, '我')

if __name__ == '__main__':
	unittest.main()
