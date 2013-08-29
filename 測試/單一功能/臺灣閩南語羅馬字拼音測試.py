from 臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
import unittest

class 臺灣閩南語羅馬字拼音測試(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test_基本分析音標(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('@@').音標, None)
		self.assertEqual(臺灣閩南語羅馬字拼音('pI̋m').音標, 'pim9')
		self.assertEqual(臺灣閩南語羅馬字拼音('pe̍m').音標, None)
		self.assertEqual(臺灣閩南語羅馬字拼音('pi̍m').音標, 'pim8')
		self.assertEqual(臺灣閩南語羅馬字拼音('pîm').音標, 'pim5')
		self.assertEqual(臺灣閩南語羅馬字拼音('pǐN').音標, 'pinn6')
		self.assertEqual(臺灣閩南語羅馬字拼音('pih').音標, 'pih4')
		self.assertEqual(臺灣閩南語羅馬字拼音('cat8').音標, None)
		self.assertEqual(臺灣閩南語羅馬字拼音('Pih8').音標, 'pih8')	
		self.assertEqual(臺灣閩南語羅馬字拼音('nňg').音標, 'nng6')
		self.assertEqual(臺灣閩南語羅馬字拼音('tor').音標, 'tor1')
		self.assertEqual(臺灣閩南語羅馬字拼音('tsőo').音標, 'tsoo9')
		self.assertEqual(臺灣閩南語羅馬字拼音('tsňg').音標, 'tsng6')
		self.assertEqual(臺灣閩南語羅馬字拼音('xxtsé--á').音標, None)
		self.assertEqual(臺灣閩南語羅馬字拼音('pňg').音標, 'png6')
		self.assertEqual(臺灣閩南語羅馬字拼音('óonn').音標, None)	
		self.assertEqual(臺灣閩南語羅馬字拼音('ainn7').音標, 'ainn7')
		self.assertEqual(臺灣閩南語羅馬字拼音('ang3').音標, 'ang3')
		self.assertEqual(臺灣閩南語羅馬字拼音('au3').音標, 'au3')
		self.assertEqual(臺灣閩南語羅馬字拼音('mng5').音標, 'mng5')
	def test_轉閏號調(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('ainn7').轉閏號調(),'āinn')
		self.assertEqual(臺灣閩南語羅馬字拼音('ang3').轉閏號調(),'àng')
		self.assertEqual(臺灣閩南語羅馬字拼音('au3').轉閏號調(),'àu')
		self.assertEqual(臺灣閩南語羅馬字拼音('mng5').轉閏號調(),'mn̂g')
		self.assertEqual(臺灣閩南語羅馬字拼音('gio2').轉閏號調(),'gió')
		self.assertEqual(臺灣閩南語羅馬字拼音('hiunnh8').轉閏號調(),'hiu̍nnh')
	def test_轉通用拼音(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('gio2').轉通用拼音(),'ghior4')
		self.assertEqual(臺灣閩南語羅馬字拼音('hiunnh8').轉通用拼音(),'hiunnh6')


if __name__ == '__main__':
	unittest.main()
