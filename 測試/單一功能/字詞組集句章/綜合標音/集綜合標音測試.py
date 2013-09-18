import unittest
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 字詞組集句章.綜合標音.集綜合標音 import 集綜合標音
from 字詞組集句章.綜合標音.詞組綜合標音 import 詞組綜合標音
from 字詞組集句章.基本元素.公用變數 import 無音

class 集綜合標音測試(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.初胚工具 = 文章初胚工具()
	def tearDown(self):
		pass
	def test_基本測試(self):
		媠某 = self.分析器.產生對齊組('美女', 'sui2-boo2')
		美女 = self.分析器.產生對齊組('美女', 'mi2-lu2')
		集物件 = 集([媠某, 美女])
		標音集 = 集綜合標音(閩南語字綜合標音, 集物件)
		self.assertEqual(len(標音集.綜合詞組), 2)
		self.assertEqual(標音集.綜合詞組[0], 詞組綜合標音(閩南語字綜合標音, 媠某))
		self.assertEqual(標音集.綜合詞組[1], 詞組綜合標音(閩南語字綜合標音, 美女))
	def test_有無音字(self):
		集物件 = 集([self.分析器.產生對齊組('點仔膠', 'tiam2-a2-ka1'),
				self.分析器.建立組物件('，'),
				self.分析器.產生對齊組('黏著跤', 'liam5-tioh8 kha1'),
				self.分析器.建立組物件('，'),
				])
		標音集 = 集綜合標音(閩南語字綜合標音, 集物件)
		self.assertEqual(len(標音集.綜合詞組), 4)
		self.assertEqual(len(標音集.綜合詞組[0].綜合字), 3)
		self.assertEqual(len(標音集.綜合詞組[1].綜合字), 1)
		self.assertEqual(len(標音集.綜合詞組[2].綜合字), 3)
		self.assertEqual(len(標音集.綜合詞組[3].綜合字), 1)
		self.assertEqual(標音集.綜合詞組[0].綜合字[0], 閩南語字綜合標音(字('點', 'tiam2')))
		self.assertEqual(標音集.綜合詞組[0].綜合字[1], 閩南語字綜合標音(字('仔', 'a2')))
		self.assertEqual(標音集.綜合詞組[0].綜合字[2], 閩南語字綜合標音(字('膠', 'ka1')))
		self.assertEqual(標音集.綜合詞組[1].綜合字[0], 閩南語字綜合標音(字('，', 無音)))
		self.assertEqual(標音集.綜合詞組[2].綜合字[0], 閩南語字綜合標音(字('黏', 'liam5')))
		self.assertEqual(標音集.綜合詞組[2].綜合字[1], 閩南語字綜合標音(字('著', 'tioh8')))
		self.assertEqual(標音集.綜合詞組[2].綜合字[2], 閩南語字綜合標音(字('跤', 'kha1')))
		self.assertEqual(標音集.綜合詞組[3].綜合字[0], 閩南語字綜合標音(字('，', 無音)))
		self.assertEqual(標音集.綜合詞組[0].連字音, 'tiam2-a2-ka1')
		self.assertEqual(標音集.綜合詞組[1].連字音, '')
		self.assertEqual(標音集.綜合詞組[2].連字音, 'liam5-tioh8 kha1')
		self.assertEqual(標音集.綜合詞組[3].連字音, '')

if __name__ == '__main__':
	unittest.main()
