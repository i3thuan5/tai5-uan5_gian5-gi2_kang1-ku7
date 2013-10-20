from unittest.case import TestCase
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 斷詞標音.型音辭典 import 型音辭典
from 斷詞標音.動態規劃斷詞標音 import 動態規劃斷詞標音
from 字詞組集句章.基本元素.組 import 組
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.基本元素.章 import 章
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤

class 動態規劃斷詞標音測試(TestCase):
	def setUp(self):
		self.字典 = 型音辭典(4)
		self.初胚工具 = 文章初胚工具()
		self.分析器 = 拆文分析器()
		self.斷詞標音 = 動態規劃斷詞標音()

		self.我對齊詞 = self.分析器.產生對齊詞('我', 'gua2')
		self.文我對齊詞 = self.分析器.產生對齊詞('我', 'ngoo2')
		self.有對齊詞 = self.分析器.產生對齊詞('有', 'u7')
		self.一張對齊詞 = self.分析器.產生對齊詞('一張', 'tsit8-tiunn1')
		self.椅仔對齊詞 = self.分析器.產生對齊詞('椅仔', 'i2-a2')
		self.驚對齊詞 = self.分析器.產生對齊詞('！', '!')

		self.我對齊組 = 組([self.我對齊詞])
		self.文我對齊組 = 組([self.文我對齊詞])
		self.有對齊組 = 組([self.有對齊詞])
		self.一張對齊組 = 組([self.一張對齊詞])
		self.椅仔對齊組 = 組([self.椅仔對齊詞])
		self.驚對齊組 = 組([self.驚對齊詞])

		self.我對齊集 = 集([self.我對齊組])
		self.文我對齊集 = 集([self.我對齊組, self.文我對齊組])
		self.有對齊集 = 集([self.有對齊組])
		self.一張對齊集 = 集([self.一張對齊組])
		self.椅仔對齊集 = 集([self.椅仔對齊組])
		self.驚對齊集 = 集([self.驚對齊組])

		self.句物件 = 句([self.我對齊集, self.有對齊集, self.一張對齊集,
			self.椅仔對齊集, self.驚對齊集])
		self.文我句物件 = 句([self.文我對齊集, self.有對齊集, self.一張對齊集,
			self.椅仔對齊集, self.驚對齊集])

		self.對齊句 = self.分析器.產生對齊句(
			'我有一張椅仔！！', 'gua2 u7 tsit8-tiunn1 i2-a2!!')
		self.型句 = self.分析器.建立句物件('我有一張椅仔！！')
		self.音句 = self.分析器.建立句物件('gua2 u7 tsit8-tiunn1 i2-a2!!')
		self.有詞漢羅 = self.分析器.建立句物件('我 u7 一張 i2-a2!!')
		self.無詞漢羅 = self.分析器.建立句物件('gua2 u7 一張 i2-a2!!')
	def tearDown(self):
		pass
	def test_基本斷詞標音(self):
		self.字典.加詞(self.我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.字典.加詞(self.驚對齊詞)
		self.assertEqual(self.斷詞標音.斷詞標音(self.對齊句),
			self.句物件)
		self.assertEqual(self.斷詞標音.斷詞標音(self.型句),
			self.句物件)
		self.assertEqual(self.斷詞標音.斷詞標音(self.音句),
			self.句物件)
		self.assertEqual(self.斷詞標音.斷詞標音(self.有詞漢羅),
			self.句物件)
		self.assertEqual(self.斷詞標音.斷詞標音(self.無詞漢羅),
			self.句物件)
	def test_多詞斷詞標音(self):
		self.字典.加詞(self.我對齊詞)
		self.字典.加詞(self.文我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.字典.加詞(self.驚對齊詞)
		self.assertEqual(self.斷詞標音.斷詞標音(self.對齊句),
			self.句物件)
		self.assertEqual(self.斷詞標音.斷詞標音(self.型句),
			self.文我句物件)
		self.assertEqual(self.斷詞標音.斷詞標音(self.音句),
			self.句物件)
		self.assertEqual(self.斷詞標音.斷詞標音(self.有詞漢羅),
			self.文我句物件)
		self.assertEqual(self.斷詞標音.斷詞標音(self.無詞漢羅),
			self.句物件)
	def test_集無使有多組(self):
		self.字典.加詞(self.我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.字典.加詞(self.驚對齊詞)
		self.assertRaises(解析錯誤,
			self.斷詞標音.斷詞標音, self.文我句物件)
	def test_章斷詞標音(self):
		self.字典.加詞(self.我對齊詞)
		self.字典.加詞(self.文我對齊詞)
		self.字典.加詞(self.有對齊詞)
		self.字典.加詞(self.一張對齊詞)
		self.字典.加詞(self.椅仔對齊詞)
		self.字典.加詞(self.驚對齊詞)
		章物件 = 章([self.對齊句, self.句物件])
		結果章 = 章([self.句物件, self.句物件])
		self.assertEqual(章物件, 結果章)

