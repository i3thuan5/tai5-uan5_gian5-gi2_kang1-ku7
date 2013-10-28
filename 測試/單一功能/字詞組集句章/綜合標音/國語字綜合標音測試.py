import unittest
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.綜合標音.國語字綜合標音 import 國語字綜合標音
from 字詞組集句章.基本元素.公用變數 import 無音
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤

class 國語字綜合標音測試(unittest.TestCase):
	def setUp(self):
		self.我型 = '我'
		self.我音 = 'ㄨㄛˇ'
		self.我標音 = '⿰⿰ㄨㄛˇ'
		self.你型 = '你'
		self.你音 = 'ㄋㄧˇ'
	def tearDown(self):
		pass
	def test_合法(self):
		綜合標音 = 國語字綜合標音(字(self.我型, self.我音))
		self.assertEqual(綜合標音.標音完整無(), True)
	def test_兩个字合法(self):
		我綜合標音 = 國語字綜合標音(字(self.我型, self.我音))
		你綜合標音 = 國語字綜合標音(字(self.你型, self.你音))
		self.assertEqual(我綜合標音.型體, self.我型)
		self.assertEqual(你綜合標音.型體, self.你型)
	def test_轉json格式(self):
		綜合標音 = 國語字綜合標音(字(self.我型, self.我音))
		self.assertEqual(綜合標音.轉json格式(),
			{"型體":self.我型, "注音符號":self.我標音})
	def test_標點合法(self):
		標點 = 國語字綜合標音(字('，', 無音))
		self.assertEqual(標點.標音完整無(), True)
	def test_標點轉json格式(self):
		標點 = 國語字綜合標音(字('，', 無音))
		self.assertEqual(標點.轉json格式(), {"型體":"，", "注音符號":""})
	def test_標點音無合法(self):
		self.assertRaises(解析錯誤, 國語字綜合標音, 字('我', 'nggai'))
	def test_烏白傳(self):
		self.assertRaises(型態錯誤, 國語字綜合標音, '我')

if __name__ == '__main__':
	unittest.main()
