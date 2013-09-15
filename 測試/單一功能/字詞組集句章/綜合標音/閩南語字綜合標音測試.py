import unittest
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 字詞組集句章.基本元素.公用變數 import 無音
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤

class 閩南語字綜合標音測試(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test_合法(self):
		綜合標音 = 閩南語字綜合標音(字('我', 'gua2'))
		self.assertEqual(綜合標音.標音完整無(), True)
	def test_轉json格式(self):
		綜合標音 = 閩南語字綜合標音(字('我', 'gua2'))
		self.assertEqual(綜合標音.轉json格式(), '{"型體":"我","臺羅數字調":"gua2","臺羅閏號調":"guá","通用數字調":"ghua4","吳守禮方音":"⿳⿳⿳ㆣㄨㄚˋ"}')
	def test_標點合法(self):
		標點 = 閩南語字綜合標音(字('，', 無音))
		self.assertEqual(標點.標音完整無(), True)
	def test_標點轉json格式(self):
		標點 = 閩南語字綜合標音(字('，', 無音))
		self.assertEqual(標點.轉json格式(), '{"型體":"，","臺羅數字調":"' + 無音 + '","臺羅閏號調":"' + 無音 + '","通用數字調":"' + 無音 + '","吳守禮方音":"' + 無音 + '"}')
	def test_標點音無合法(self):
		self.assertRaises(解析錯誤, 閩南語字綜合標音, 字('我', 'uo3'))
	def test_烏白傳(self):
		self.assertRaises(解析錯誤, 閩南語字綜合標音, '我')

if __name__ == '__main__':
	unittest.main()
