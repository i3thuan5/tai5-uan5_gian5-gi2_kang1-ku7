"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
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
