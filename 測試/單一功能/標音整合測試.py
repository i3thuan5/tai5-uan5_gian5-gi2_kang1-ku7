import unittest
from 標音系統整合.標音整合 import 標音整合

class 標音整合測試(unittest.TestCase):
	def setUp(self):
		self.標音 = 標音整合('漢語族閩方言閩南語偏漳優勢音')
	def tearDown(self):
		pass
	def test_詞文讀(self):
		音 = self.標音.產生標音結果('台語字', self.標音.文讀層)
		self.assertEqual(str(音), '[[台 tai5], [語 gu2], [字 ji7]]')
	def test_詞白話(self):
		音 = self.標音.產生標音結果('台語字', self.標音.白話層)
		self.assertEqual(str(音), '[[台 tai5], [語 gi2], [字 ji7]]')
	def test_詞全部(self):
		音 = self.標音.產生標音結果('台語字', self.標音.全部)
		self.assertEqual(str(音), '[[台 tai5], [語 gi2, 語 gu2], [字 ji7]]')
	def test_規句文讀(self):
		音 = self.標音.產生標音結果('好好鱟刣甲屎那流。', self.標音.文讀層)
		self.assertEqual(str(音), '[[好好鱟刣甲屎那流。 ho2-ho2 hau7 thai5 kah4 sai2 na2 lau5.]]')
	def test_規句白話(self):
		音 = self.標音.產生標音結果('好好鱟刣甲屎那流。', self.標音.白話層)
		self.assertEqual(str(音), '[[好好鱟刣甲屎那流。 ho2-ho2 hau7 thai5 kah4 sai2 na2 lau5.]]')
	def test_規句全部(self):
		音 = self.標音.產生標音結果('好好鱟刣甲屎那流。', self.標音.全部)
		self.assertEqual(str(音), '[[好好鱟刣甲屎那流。 ho2-ho2 hau7 thai5 kah4 sai2 na2 lau5.]]')
	def test_句文讀(self):
		音 = self.標音.產生標音結果('好好鱟刣甲屎那流,', self.標音.文讀層)
		self.assertEqual(str(音), '[[好好 ho2-ho2], [鱟 hau7], [刣 thai5], [甲 kap4], [屎 su2], [那 na2], [流 liu5], [, ,]]')
	def test_句白話(self):
		音 = self.標音.產生標音結果('好好鱟刣甲屎那流,', self.標音.白話層)
		self.assertEqual(str(音), '[[好好 ho2-ho2], [鱟 hau7], [刣 thai5], [甲 kah4], [屎 sai2], [那 na2], [流 lau5], [, ,]]')
	def test_句全部(self):
		音 = self.標音.產生標音結果('好好鱟刣甲屎那流,', self.標音.全部)
		self.assertEqual(str(音), '[[好好 ho2-ho2], [鱟 hau7], [刣 thai5], [甲 kah4, 甲 kap4], [屎 sai2, 屎 su2], [那 na2], [流 lau5, 流 liu5], [, ,]]')
	def test_詩(self):
		音 = self.標音.產生標音結果('白日依山盡', self.標音.文讀層)
		self.assertEqual(str(音), '[[白 pik8], [日 jit8], [依 i1], [山 san1], [盡 tsin7]]')
	def test_謠(self):
		音 = self.標音.產生標音結果('點仔膠', self.標音.文讀層)
		self.assertEqual(str(音), '[[點 tiam2], [仔 a2, 仔 tsu2], [膠 ka1]]')

if __name__ == '__main__':
	unittest.main()