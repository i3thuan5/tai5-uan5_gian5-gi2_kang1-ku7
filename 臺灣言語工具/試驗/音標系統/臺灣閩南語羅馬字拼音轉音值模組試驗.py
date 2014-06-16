# -*- coding: utf-8 -*-
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
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音聲母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音韻母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音轉音值模組 import 臺灣閩南語羅馬字拼音對照音值聲母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音轉音值模組 import 臺灣閩南語羅馬字拼音對照音值韻母表

class 臺灣閩南語羅馬字拼音轉音值模組試驗(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
		
	def test_定看音標(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('e').音值(), ('ʔ','e','1'))
		self.assertEqual(臺灣閩南語羅馬字拼音('e1').音值(),('ʔ','e','1'))
		self.assertEqual(臺灣閩南語羅馬字拼音('be2').音值(),('b','e','2'))
		self.assertEqual(臺灣閩南語羅馬字拼音('ang3').音值(),('ʔ','aŋ','3'))
		self.assertEqual(臺灣閩南語羅馬字拼音('mng5').音值(),('m','ŋ̩','5'))
		self.assertEqual(臺灣閩南語羅馬字拼音('ainn7').音值(), ('ʔ','aiⁿ','7'))
		self.assertEqual(臺灣閩南語羅馬字拼音('ang9').音值(), ('ʔ','aŋ','9'))

	def test_零聲母聲韻調輕(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('sih').音值(), ('s','iʔ','4'))
		self.assertEqual(臺灣閩南語羅馬字拼音('m5').音值(), ('ʔ','m̩','5'))
		self.assertEqual(臺灣閩南語羅馬字拼音('0e5').音值(), ('ʔ','e','0'))

	def test_蚵芋音(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('ho2').音值(),('h','ə','2'))
		self.assertEqual(臺灣閩南語羅馬字拼音('hoh').音值(), ('h','əh','4'))
		self.assertEqual(臺灣閩南語羅馬字拼音('hok').音值(),('h','ok','4'))
		self.assertEqual(臺灣閩南語羅馬字拼音('hio2').音值(), ('h','iə','2'))
		self.assertEqual(臺灣閩南語羅馬字拼音('hioh').音值(), ('h','iəh','4'))
		self.assertEqual(臺灣閩南語羅馬字拼音('hiok8').音值(), ('h','iok','8'))
		
	def test_舌尖顎化(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('tsia').音值(),('ts','ia','1'))
		self.assertEqual(臺灣閩南語羅馬字拼音('tsha').音值(),('tsh','a','1'))
		self.assertEqual(臺灣閩南語羅馬字拼音('sa').音值(),('s','s','1'))
		self.assertEqual(臺灣閩南語羅馬字拼音('jia').音值(), ('z','ia','1'))

	def test_輕聲(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('ta0').音值(),('t','a','0'))
		self.assertEqual(臺灣閩南語羅馬字拼音('pih0').音值(),('p','iʔ','0'))

	def test_語法輕聲(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('0a').音值(),('ʔ','a','0'))
		self.assertEqual(臺灣閩南語羅馬字拼音('0e5').音值(),('ʔ','e','0'))
		self.assertEqual(臺灣閩南語羅馬字拼音('0hannh').音值(),('t','aⁿ','0'))
		self.assertEqual(臺灣閩南語羅馬字拼音('0tsi̍t').音值(), ('ts','it','0'))

	def test_罕用音標(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('tor').音值(),('t','ə','1'))
		self.assertEqual(臺灣閩南語羅馬字拼音('kee5').音值(),('k','ɛ','5'))
		self.assertEqual(臺灣閩南語羅馬字拼音('ter5').音值(), ('t','ə','5'))
		self.assertEqual(臺灣閩南語羅馬字拼音('tere5').音值(), ('t','əe','5'))
		self.assertEqual(臺灣閩南語羅馬字拼音('tir5').音值(),('t','ɨ','5'))

	def test_違法音標(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('@@').音值(), None)
		self.assertEqual(臺灣閩南語羅馬字拼音('pe̍m').音值(), None)
		self.assertEqual(臺灣閩南語羅馬字拼音('xxtsé--á').音值(), None)
		self.assertEqual(臺灣閩南語羅馬字拼音('óonn').音值(), None)
		
	def test_全部攏會使產生方音物件(self):
		for 母 in 臺灣閩南語羅馬字拼音聲母表:
			self.assertIn(母,臺灣閩南語羅馬字拼音對照音值聲母表)
		for 母 in 臺灣閩南語羅馬字拼音韻母表:
			self.assertIn(母,臺灣閩南語羅馬字拼音對照音值韻母表)
