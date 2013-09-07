import unittest
from 剖析相關工具.官方剖析工具 import 官方剖析工具
from 剖析相關工具.自設剖析工具 import 自設剖析工具

class 剖析工具測試(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass

	def test_官方剖析工具(self):
		工具 = 官方剖析工具()
		self.assertEqual(工具.剖析('我想吃飯。我想吃很多飯。'),
			['#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
			'#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)'
			])
	def test_自設剖析工具(self):
		工具 = 自設剖析工具()
		self.assertEqual(工具.剖析('我想吃飯。我想吃很多飯。'),
			['#1:1.[0] S(agent:NP(Head:Nhaa:我)|Head:VE2:想|goal:VP(Head:VA4:吃飯))#。(PERIODCATEGORY)',
			'#2:1.[0] S(agent:NP(Head:Nhaa:我)|Head:VE2:想|goal:VP(Head:VC31:吃|theme:NP(quantifier:Neqa:很多|Head:Nab:飯)))#。(PERIODCATEGORY)'
			])

if __name__ == '__main__':
	unittest.main()
