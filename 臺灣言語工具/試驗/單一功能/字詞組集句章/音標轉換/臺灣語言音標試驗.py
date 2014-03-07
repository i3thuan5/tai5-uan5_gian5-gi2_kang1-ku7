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
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.臺灣語言音標 import 臺灣語言音標

class 臺灣語言音標試驗(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test_定看音標(self):
		self.assertEqual(臺灣語言音標('ainn7').音標, 'ainn7')
		self.assertEqual(臺灣語言音標('ang3').音標, 'ang3')
		self.assertEqual(臺灣語言音標('ang9').音標, 'ang9')
		self.assertEqual(臺灣語言音標('e').音標, 'e1')
		self.assertEqual(臺灣語言音標('mng5').音標, 'mng5')
		self.assertEqual(臺灣語言音標('Pih8').音標, 'pih8')
		self.assertEqual(臺灣語言音標('Pih10').音標, 'pih10')
		
	def test_大寫開頭(self):
		self.assertEqual(臺灣語言音標('Na5').音標, 'na5')
		self.assertEqual(臺灣語言音標('Phoo2').音標, 'phoo2')

	def test_輕聲(self):
		self.assertEqual(臺灣語言音標('ta0').音標, 'ta0')
		self.assertEqual(臺灣語言音標('pih0').音標, 'pih0')

	def test_語法輕聲(self):
		self.assertEqual(臺灣語言音標('0a').音標, '0a1')
		self.assertEqual(臺灣語言音標('0e5').音標, '0e5')
		self.assertEqual(臺灣語言音標('0ê').音標, '0e5')
		self.assertEqual(臺灣語言音標('0ê').音標, '0e5')
		self.assertEqual(臺灣語言音標('0hannh').音標, '0hannh4')
		self.assertEqual(臺灣語言音標('0chi̍t').音標, '0chit8')
		self.assertEqual(臺灣語言音標('0tsi̍t').音標, None)
		self.assertEqual(臺灣語言音標('cat8').音標, 'cat8')

	def test_輸入閏號音標(self):
		self.assertEqual(臺灣語言音標('pI̋m').音標, 'pim9')
		self.assertEqual(臺灣語言音標('pi̍m').音標, 'pim8')
		self.assertEqual(臺灣語言音標('pîm').音標, 'pim5')
		self.assertEqual(臺灣語言音標('phǐN').音標, 'phinn6')
		self.assertEqual(臺灣語言音標('pih').音標, 'pih4')
		self.assertEqual(臺灣語言音標('nňg').音標, 'nng6')
		self.assertEqual(臺灣語言音標('chőo').音標, 'choo9')
		self.assertEqual(臺灣語言音標('cňg').音標, 'cng6')
		self.assertEqual(臺灣語言音標('pňg').音標, 'png6')

	def test_鼻化ㆦ(self):
		self.assertEqual(臺灣語言音標('mo5').音標, 'moo5')
		self.assertEqual(臺灣語言音標('ngoo5').音標, 'ngoo5')

	def test_罕用音標(self):
		self.assertEqual(臺灣語言音標('tor').音標, 'tor1')
		self.assertEqual(臺灣語言音標('kee5').音標, 'kee5')
		self.assertEqual(臺灣語言音標('ter5').音標, 'ter5')
		self.assertEqual(臺灣語言音標('tere5').音標, 'tere5')
		self.assertEqual(臺灣語言音標('tir5').音標, 'tir5')


	def test_違法音標(self):
		self.assertEqual(臺灣語言音標('@@').音標, None)
		self.assertEqual(臺灣語言音標('pe̍m').音標, None)
		self.assertEqual(臺灣語言音標('xxtsé--á').音標, None)
		self.assertEqual(臺灣語言音標('óonn').音標, None)

	def test_轉臺羅(self):
		self.assertEqual(臺灣語言音標('cat8').轉換到臺灣閩南語羅馬字拼音(), 'tsat8')
		self.assertEqual(臺灣語言音標('chuan5').轉換到臺灣閩南語羅馬字拼音(), 'tshuan5')
		self.assertEqual(臺灣語言音標('tsang3').轉換到臺灣閩南語羅馬字拼音(), None)


if __name__ == '__main__':
	unittest.main()
