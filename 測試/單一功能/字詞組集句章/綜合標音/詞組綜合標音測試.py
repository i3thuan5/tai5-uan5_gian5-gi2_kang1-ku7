import unittest
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.基本元素.詞 import 詞
from 字詞組集句章.基本元素.組 import 組
from 字詞組集句章.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 字詞組集句章.綜合標音.詞組綜合標音 import 詞組綜合標音
from 字詞組集句章.基本元素.公用變數 import 無音

class 詞組綜合標音測試(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.初胚工具 = 文章初胚工具()
	def tearDown(self):
		pass
	def test_基本測試(self):
		組物件 = self.分析器.產生對齊組('大美女', 'tua7 sui2-boo2')
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 組物件)
		self.assertEqual(len(標音詞組.綜合字), 3)
		self.assertEqual(標音詞組.綜合字[0], 閩南語字綜合標音(字('大', 'tua7')))
		self.assertEqual(標音詞組.綜合字[1], 閩南語字綜合標音(字('美', 'sui2')))
		self.assertEqual(標音詞組.綜合字[2], 閩南語字綜合標音(字('女', 'boo2')))
		self.assertEqual(標音詞組.連字音, 'tua7 sui2-boo2')

	def test_連字音檢查(self):
		組物件 = 組([self.分析器.產生對齊詞('大', 'tua7'),
			self.分析器.產生對齊詞('美女', 'sui2-boo2')])
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 組物件)
		self.assertEqual(len(標音詞組.綜合字), 3)
		self.assertEqual(標音詞組.綜合字[0], 閩南語字綜合標音(字('大', 'tua7')))
		self.assertEqual(標音詞組.綜合字[1], 閩南語字綜合標音(字('美', 'sui2')))
		self.assertEqual(標音詞組.綜合字[2], 閩南語字綜合標音(字('女', 'boo2')))
		self.assertEqual(標音詞組.連字音, 'tua7 sui2-boo2')

	def test_有標點符號(self):
		詞型 = '點仔膠，黏著跤，'
		詞音 = 'tiam2-a2-ka1 , liam5-tioh8 kha1 ,'
		組物件 = self.分析器.產生對齊組(詞型, 詞音)
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 組物件)
		self.assertEqual(len(標音詞組.綜合字), 8)
		self.assertEqual(標音詞組.綜合字[0], 閩南語字綜合標音(字('點', 'tiam2')))
		self.assertEqual(標音詞組.綜合字[1], 閩南語字綜合標音(字('仔', 'a2')))
		self.assertEqual(標音詞組.綜合字[2], 閩南語字綜合標音(字('膠', 'ka1')))
		self.assertEqual(標音詞組.綜合字[3], 閩南語字綜合標音(字('，', ',')))
		self.assertEqual(標音詞組.綜合字[4], 閩南語字綜合標音(字('黏', 'liam5')))
		self.assertEqual(標音詞組.綜合字[5], 閩南語字綜合標音(字('著', 'tioh8')))
		self.assertEqual(標音詞組.綜合字[6], 閩南語字綜合標音(字('跤', 'kha1')))
		self.assertEqual(標音詞組.綜合字[7], 閩南語字綜合標音(字('，', ',')))
		self.assertEqual(標音詞組.連字音, 'tiam2-a2-ka1 , liam5-tioh8 kha1 ,')

	def test_有無音字(self):
		組物件 = 組([self.分析器.產生對齊詞('點仔膠', 'tiam2-a2-ka1'),
				self.分析器.建立詞物件('，'),
				self.分析器.產生對齊詞('黏著', 'liam5-tioh8'),
				self.分析器.產生對齊詞('跤', 'kha1'),
				self.分析器.建立詞物件('，'),
				])
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 組物件)
		self.assertEqual(len(標音詞組.綜合字), 8)
		self.assertEqual(標音詞組.綜合字[0], 閩南語字綜合標音(字('點', 'tiam2')))
		self.assertEqual(標音詞組.綜合字[1], 閩南語字綜合標音(字('仔', 'a2')))
		self.assertEqual(標音詞組.綜合字[2], 閩南語字綜合標音(字('膠', 'ka1')))
		self.assertEqual(標音詞組.綜合字[3], 閩南語字綜合標音(字('，', 無音)))
		self.assertEqual(標音詞組.綜合字[4], 閩南語字綜合標音(字('黏', 'liam5')))
		self.assertEqual(標音詞組.綜合字[5], 閩南語字綜合標音(字('著', 'tioh8')))
		self.assertEqual(標音詞組.綜合字[6], 閩南語字綜合標音(字('跤', 'kha1')))
		self.assertEqual(標音詞組.綜合字[7], 閩南語字綜合標音(字('，', 無音)))
		self.assertEqual(標音詞組.連字音, 'tiam2-a2-ka1 liam5-tioh8 kha1')

	def test_詞中有無音字(self):
		組物件 = 組([
				詞([self.分析器.產生對齊字('點', 'tiam2'),
					self.分析器.建立字物件('仔'),
					self.分析器.產生對齊字('膠', 'ka1')]),
				self.分析器.建立詞物件('，'),
				self.分析器.產生對齊詞('黏著', 'liam5-tioh8'),
				self.分析器.產生對齊詞('跤', 'kha1'),
				self.分析器.建立詞物件('，'),
				])
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 組物件)
		self.assertEqual(len(標音詞組.綜合字), 8)
		self.assertEqual(標音詞組.綜合字[0], 閩南語字綜合標音(字('點', 'tiam2')))
		self.assertEqual(標音詞組.綜合字[1], 閩南語字綜合標音(字('仔')))
		self.assertEqual(標音詞組.綜合字[2], 閩南語字綜合標音(字('膠', 'ka1')))
		self.assertEqual(標音詞組.綜合字[3], 閩南語字綜合標音(字('，', 無音)))
		self.assertEqual(標音詞組.綜合字[4], 閩南語字綜合標音(字('黏', 'liam5')))
		self.assertEqual(標音詞組.綜合字[5], 閩南語字綜合標音(字('著', 'tioh8')))
		self.assertEqual(標音詞組.綜合字[6], 閩南語字綜合標音(字('跤', 'kha1')))
		self.assertEqual(標音詞組.綜合字[7], 閩南語字綜合標音(字('，', 無音)))
		self.assertEqual(標音詞組.連字音, 'tiam2-ka1 liam5-tioh8 kha1')

	def test_空組(self):
		組物件 = 組()
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 組物件)
		self.assertEqual(len(標音詞組.綜合字), 0)

	def test_傳詞檢查(self):
		詞物件 = self.分析器.產生對齊詞('大美女', 'tua7-sui2-boo2')
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 詞物件)
		self.assertEqual(len(標音詞組.綜合字), 3)
		self.assertEqual(標音詞組.綜合字[0], 閩南語字綜合標音(字('大', 'tua7')))
		self.assertEqual(標音詞組.綜合字[1], 閩南語字綜合標音(字('美', 'sui2')))
		self.assertEqual(標音詞組.綜合字[2], 閩南語字綜合標音(字('女', 'boo2')))
		self.assertEqual(標音詞組.連字音, 'tua7-sui2-boo2')

	def test_空詞檢查(self):
		詞物件 = self.分析器.建立詞物件('')
		標音詞組 = 詞組綜合標音(閩南語字綜合標音, 詞物件)
		self.assertEqual(標音詞組.綜合字, [])
		self.assertEqual(標音詞組.連字音, '')

if __name__ == '__main__':
	unittest.main()


# if __name__ == '__main__':
# 	標點處理工具 = 文章標點處理工具()
# 	標點處理工具.標點符號={}
# 	詞標音=[[詞('我','gua2',標點處理工具)],
# 		[詞('愛','ai3',標點處理工具)],
# 		[詞('大','tua7',標點處理工具)],
# 		[詞('美女','sui2-boo2',標點處理工具),詞('美女','mi2-lu2',標點處理工具)]]
# 	標音句=句綜合標音(詞標音,閩南語字綜合標音)
# 	print(標音句.綜合標音佮詞組陣列)
#
# 	標音 = 標音整合('漢語族閩方言閩南語偏漳優勢音')
# 	詞標音 = 標音.產生標音結果('台語字', 標音.全部)
# # 	print(詞標音)
# 	標音句=句綜合標音(詞標音,閩南語字綜合標音)
# 	print(標音句.綜合標音佮詞組陣列)
#
# 	標音 = 標音整合('漢語族閩方言閩南語偏漳優勢音')
# 	詞標音 = 標音.產生標音結果('我欲食飯，文莉足媠', 標音.全部)
# # 	print(詞標音)
# 	標音句=句綜合標音(詞標音,閩南語字綜合標音)
# 	print(標音句.綜合標音佮詞組陣列)
