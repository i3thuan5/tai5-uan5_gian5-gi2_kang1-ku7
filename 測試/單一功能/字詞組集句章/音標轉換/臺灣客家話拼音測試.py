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
from unittest.case import TestCase
from 字詞組集句章.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音

class 臺灣客家話拼音測試(TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass

#---------------------------------------------
	def test_零聲母聲韻調輕(self):
		客話音標 = 臺灣客家話拼音('er')
		self.assertEqual(客話音標.音標, 'er')
		self.assertEqual(客話音標.聲, '')
		self.assertEqual(客話音標.韻, 'er')
		self.assertEqual(客話音標.調, '')
		
		客話音標 = 臺灣客家話拼音('imˊ') #陰
		self.assertEqual(客話音標.音標, 'imˊ')
		self.assertEqual(客話音標.聲, '')
		self.assertEqual(客話音標.韻, 'im')
		self.assertEqual(客話音標.調, 'ˊ')
		
		客話音標 = 臺灣客家話拼音('iongˇ')##洋
		self.assertEqual(客話音標.音標, 'iongˇ')
		self.assertEqual(客話音標.聲, '')
		self.assertEqual(客話音標.韻, 'iong')
		self.assertEqual(客話音標.調, 'ˇ')
				
#-----------------------------------------------------		
	def test_完整聲韻調(self):
		客話音標 = 臺灣客家話拼音('giangˊ')
		self.assertEqual(客話音標.音標, 'giangˊ')
		self.assertEqual(客話音標.聲, 'g')
		self.assertEqual(客話音標.韻, 'iang')
		self.assertEqual(客話音標.調, 'ˊ')

		客話音標 = 臺灣客家話拼音('gauˊ')
		self.assertEqual(客話音標.音標, 'gauˊ')
		self.assertEqual(客話音標.聲, 'g')
		self.assertEqual(客話音標.韻, 'au')
		self.assertEqual(客話音標.調, 'ˊ')
		
		客話音標 = 臺灣客家話拼音('caˋ')
		self.assertEqual(客話音標.音標, 'caˋ')
		self.assertEqual(客話音標.聲, 'c')
		self.assertEqual(客話音標.韻, 'a')
		self.assertEqual(客話音標.調, 'ˋ')
	
		客話音標 = 臺灣客家話拼音('pon+') ##飯 /fan
		self.assertEqual(客話音標.音標, 'pon+')
		self.assertEqual(客話音標.聲, 'p')
		self.assertEqual(客話音標.韻, 'on')
		self.assertEqual(客話音標.調, '+')
#-----------------------------------------------------		

	def test_韻化輔音聲韻調輕(self):
		客話音標 = 臺灣客家話拼音('ng') 
		self.assertEqual(客話音標.音標, 'ng')
		self.assertEqual(客話音標.聲, '')
		self.assertEqual(客話音標.韻, 'ng') 	
		self.assertEqual(客話音標.調, '')

		客話音標 = 臺灣客家話拼音('ngiˋ') #ngia->ng ia, ngi->ng i
		self.assertEqual(客話音標.音標, 'ngiˋ')
		self.assertEqual(客話音標.聲, 'ng')
		self.assertEqual(客話音標.韻, 'i') 	
		self.assertEqual(客話音標.調, 'ˋ')

		客話音標 = 臺灣客家話拼音('mug') #目
		self.assertEqual(客話音標.音標, 'mug')
		self.assertEqual(客話音標.聲, 'm')
		self.assertEqual(客話音標.韻, 'ug')
		self.assertEqual(客話音標.調, '')
		
		客話音標 = 臺灣客家話拼音('ngiedˋ')#月
		self.assertEqual(客話音標.音標, 'ngiedˋ')
		self.assertEqual(客話音標.聲, 'ng')
		self.assertEqual(客話音標.韻, 'ied')
		self.assertEqual(客話音標.調, 'ˋ')
		
		客話音標 = 臺灣客家話拼音('ngin')#人
		self.assertEqual(客話音標.音標, 'ngin')
		self.assertEqual(客話音標.聲, 'ng')
		self.assertEqual(客話音標.韻, 'in')
		self.assertEqual(客話音標.調, '')
		
		客話音標 = 臺灣客家話拼音('tongˋ')#人
		self.assertEqual(客話音標.音標, 'tongˋ')
		self.assertEqual(客話音標.聲, 't')
		self.assertEqual(客話音標.韻, 'ong')
		self.assertEqual(客話音標.調, 'ˋ')
#------------------------------------------
# 	def test_調值音標(self):
# 		self.assertEqual(臺灣客家話拼音('giog2').音標, 'giogˋ')

	def test_違法音標(self):
		self.assertEqual(臺灣客家話拼音('').音標, None)
		self.assertEqual(臺灣客家話拼音('@3@').音標, None)
		self.assertEqual(臺灣客家話拼音('gonkˊ').音標, None)
		#self.assertEqual(臺灣客家話拼音('cn').音標, None)
		self.assertEqual(臺灣客家話拼音('tsé--á').音標, None)
		self.assertEqual(臺灣客家話拼音('óonn').音標, None)
		self.assertEqual(臺灣客家話拼音('giog+').音標, None)
		self.assertEqual(臺灣客家話拼音('giog').音標, 'giog')
		self.assertEqual(臺灣客家話拼音('giog^').音標, None)
		self.assertEqual(臺灣客家話拼音('ss').音標, None)
		self.assertEqual(臺灣客家話拼音('izrh').音標, None)
		
	def test_其他音標(self):
		#海陸rh-，六堆舌根音
		self.assertEqual(臺灣客家話拼音('ianˇ').音標, 'ianˇ')#圓
		self.assertEqual(臺灣客家話拼音('giadˋ').音標, 'giadˋ')#結
		self.assertEqual(臺灣客家話拼音('giai').音標, 'giai')#街
		 
		
		
	def test_大寫音標(self):
		self.assertEqual(臺灣客家話拼音('JIANGˊ').音標, 'jiangˊ')
		self.assertEqual(臺灣客家話拼音('Jiangˊ').音標, 'jiangˊ')
# #--------------------------------------------------------
# 
# if __name__ == '__main__':
# 	unittest.main()
