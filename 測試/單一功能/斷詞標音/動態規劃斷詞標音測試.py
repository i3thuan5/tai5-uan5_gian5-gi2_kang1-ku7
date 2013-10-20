from unittest.case import TestCase
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 斷詞標音.型音辭典 import 型音辭典

class 動態規劃斷詞標音測試(TestCase):
	def setUp(self):
		self.字典 = 型音辭典(4)
		self.初胚工具 = 文章初胚工具()
		self.分析器 = 拆文分析器()
		self.我對齊詞 = self.分析器.產生對齊詞('我', 'gua2')
		self.有對齊詞 = self.分析器.產生對齊詞('有', 'u7')
		self.一張對齊詞 = self.分析器.產生對齊詞('一張', 'tsit8-tiunn1')
		self.椅仔對齊詞 = self.分析器.產生對齊詞('椅仔', 'i2-a2')
		self.驚對齊詞 = self.分析器.產生對齊詞('！', '!')
		self.對齊句=self.分析器.產生對齊句(
			'我有一張椅仔！！','gua2 u7 tsit8-tiunn1 i2-a2!!')
		self.型句 = self.分析器.建立句物件('我有一張椅仔！！')
		self.音句 = self.分析器.建立詞物件('gua2 u7 tsit8-tiunn1 i2-a2!!')
	def tearDown(self):
		pass
	def test_漢字加詞成功無(self):
		self.字典.加詞(self.詞物件)
		self.assertEqual(self.字典.查詞(self.詞物件), [set(), set(), set(), {self.詞物件}])

