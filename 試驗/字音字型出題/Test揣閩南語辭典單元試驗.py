# -*- coding: utf-8 -*-
import unittest


@unittest.skip('無維護')
class 揣閩南語題目單元試驗(unittest.TestCase):
	def setUp(self):
		self.閩南語題目 = 揣閩南語題目()
		self._分析器 = 拆文分析器()

	def tearDown(self):
		pass
	
	def test_三字(self):
		self.閩南語題目.資料.append((self._分析器.產生對齊組('媠噹噹', 'sui2-tang1-tang1'), 3))
		答案 = [[('「媠」噹噹', '「sui2」-tang1-tang1')],
			[('媠「噹」噹', 'sui2-「tang1」-tang1')], [('媠噹「噹」', 'sui2-tang1-「tang1」')],
			]
		for 擺 in range(10):
			self.assertIn(self.閩南語題目.出題(1), 答案) 

	def test_四字(self):
		self.閩南語題目.資料.append((self._分析器.產生對齊組('一心一意', 'it4-sim1-it4-i3'), 4))
		答案 = [[('「一」心一意', '「it4」-sim1-it4-i3')], [('一「心」一意', 'it4-「sim1」-it4-i3')],
			[('一心「一」意', 'it4-sim1-「it4」-i3')], [('一心一「意」', 'it4-sim1-it4-「i3」')],
			]
		for 擺 in range(10):
			self.assertIn(self.閩南語題目.出題(1), 答案)

	def test_輕聲(self):
		self.閩南語題目.資料.append((self._分析器.產生對齊組('一來', 'it-0lâi'), 2))
		答案 = [[('「一」來', '「it」--lâi')], [('一「來」', 'it-「--lâi」')]]
		for 擺 in range(10):
			self.assertIn(self.閩南語題目.出題(1), 答案)
