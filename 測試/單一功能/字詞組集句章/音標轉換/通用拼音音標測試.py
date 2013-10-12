import unittest
from 字詞組集句章.音標系統.閩南語.通用拼音音標 import 通用拼音音標

class 通用拼音音標測試(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def atest_定看音標(self):
		self.assertEqual(通用拼音音標('ang3').音標, 'ang3')
		self.assertEqual(通用拼音音標('ang9').音標, 'ang9')
		self.assertEqual(通用拼音音標('e').音標, 'e1')
		self.assertEqual(通用拼音音標('mng5').音標, 'mng5')
		self.assertEqual(通用拼音音標('Pih8').音標, 'pih8')
		self.assertEqual(通用拼音音標('Pih10').音標, 'pih10')

	def atest_輕聲(self):
		self.assertEqual(通用拼音音標('ta0').音標, 'ta0')
		self.assertEqual(通用拼音音標('pih0').音標, 'pih0')

	def ateast_語法輕聲(self):
		self.assertEqual(通用拼音音標('0a').音標, '0a1')
		self.assertEqual(通用拼音音標('0e5').音標, '0e5')
		self.assertEqual(通用拼音音標('0ê').音標, '0e5')
		self.assertEqual(通用拼音音標('0ê').音標, '0e5')
		self.assertEqual(通用拼音音標('0hannh').音標, '0hannh4')
		self.assertEqual(通用拼音音標('0chi̍t').音標, '0chit8')
		self.assertEqual(通用拼音音標('0tsi̍t').音標, None)
		self.assertEqual(通用拼音音標('cat8').音標, 'cat8')

	def tdest_輸入閏號音標(self):
		self.assertEqual(通用拼音音標('pI̋m').音標, 'pim9')
		self.assertEqual(通用拼音音標('pi̍m').音標, 'pim8')
		self.assertEqual(通用拼音音標('pîm').音標, 'pim5')
		self.assertEqual(通用拼音音標('phǐN').音標, 'phinn6')
		self.assertEqual(通用拼音音標('pih').音標, 'pih4')
		self.assertEqual(通用拼音音標('nňg').音標, 'nng6')
		self.assertEqual(通用拼音音標('chőo').音標, 'choo9')
		self.assertEqual(通用拼音音標('cňg').音標, 'cng6')
		self.assertEqual(通用拼音音標('pňg').音標, 'png6')

	def stest_鼻化ㆦ(self):
		self.assertEqual(通用拼音音標('mo5').音標, 'moo5')
		self.assertEqual(通用拼音音標('ngoo5').音標, 'ngoo5')

	def stest_罕用音標(self):
		self.assertEqual(通用拼音音標('tor').音標, 'tor1')
		self.assertEqual(通用拼音音標('kee5').音標, 'kee5')
		self.assertEqual(通用拼音音標('ter5').音標, 'ter5')
		self.assertEqual(通用拼音音標('tere5').音標, 'tere5')
		self.assertEqual(通用拼音音標('tir5').音標, 'tir5')


	def test_違法音標(self):
		self.assertEqual(通用拼音音標('@@').音標, None)
		self.assertEqual(通用拼音音標('pe̍m').音標, None)
		self.assertEqual(通用拼音音標('xxtsé--á').音標, None)
		self.assertEqual(通用拼音音標('óonn').音標, None)
		self.assertEqual(通用拼音音標('hir2').音標, None)
		self.assertEqual(通用拼音音標('e').音標, None)

	def tesst_轉臺羅(self):
		self.assertEqual(通用拼音音標('cat8').轉換到臺灣閩南語羅馬字拼音(), 'tsat8')
		self.assertEqual(通用拼音音標('chuan5').轉換到臺灣閩南語羅馬字拼音(), 'tshuan5')
		self.assertEqual(通用拼音音標('tsang3').轉換到臺灣閩南語羅馬字拼音(), None)

	def test_全部攏會使產生方音物件(self):
		for 通,臺 in 通用轉臺羅聲母表:
			self.assertIn(臺,臺灣閩南語羅馬字拼音聲母表)
		for 通,臺 in 通用轉臺羅韻母表:
			self.assertIn(臺,臺灣閩南語羅馬字拼音韻母表)
		

if __name__ == '__main__':
	unittest.main()
