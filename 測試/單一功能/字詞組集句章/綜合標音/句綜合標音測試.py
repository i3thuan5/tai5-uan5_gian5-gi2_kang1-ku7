import unittest
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.綜合標音.句綜合標音 import 句綜合標音
from 字詞組集句章.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 字詞組集句章.綜合標音.集綜合標音 import 集綜合標音

class 句綜合標音測試(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.初胚工具 = 文章初胚工具()
	def tearDown(self):
		pass
	def test_基本測試(self):
		我 = self.分析器.產生對齊集('我', 'gua2')
		愛 = self.分析器.產生對齊集('愛', 'ai3')
		媠某 = self.分析器.產生對齊組('美女', 'sui2-boo2')
		美女 = self.分析器.產生對齊組('美女', 'mi2-lu2')
		莉=集([媠某, 美女])
		句物件 = 句([我, 愛, 莉])
		標音句 = 句綜合標音(閩南語字綜合標音, 句物件)
		self.assertEqual(len(標音句.綜合集), 3)
		self.assertEqual(len(標音句.綜合集[0].綜合詞組), 1)
		self.assertEqual(len(標音句.綜合集[1].綜合詞組), 1)
		self.assertEqual(len(標音句.綜合集[2].綜合詞組), 2)
		self.assertEqual(len(標音句.綜合集), 3)
		self.assertEqual(標音句.綜合集[0], 集綜合標音(閩南語字綜合標音,我))
		self.assertEqual(標音句.綜合集[1], 集綜合標音(閩南語字綜合標音,愛))
		self.assertEqual(標音句.綜合集[2], 集綜合標音(閩南語字綜合標音,莉))

if __name__ == '__main__':
	unittest.main()
