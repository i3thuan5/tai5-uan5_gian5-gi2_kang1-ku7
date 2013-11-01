import unittest
from 字詞組集句章.音標系統.閩南語.臺灣客家話拼音 import 臺灣客家話拼音
from 字詞組集句章.音標系統.閩南語.臺灣客家話拼音 import 臺灣客家話拼音聲母表
from 字詞組集句章.音標系統.閩南語.臺灣客家話拼音 import 臺灣客家話拼音韻母表
from 字詞組集句章.音標系統.閩南語.臺灣客家話拼音 import 客話對通用聲對照表
from 字詞組集句章.音標系統.閩南語.臺灣客家話拼音 import 客話對通用韻對照表
from 字詞組集句章.音標系統.閩南語.通用拼音音標 import 通用拼音佮臺灣羅馬聲母對照表
from 字詞組集句章.音標系統.閩南語.通用拼音音標 import 通用拼音佮臺灣羅馬韻母對照表

class 臺灣客家話拼音測試(unittest.TestCase):
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
		客話音標 = 臺灣客家話拼音('ngiˋ')
		self.assertEqual(客話音標.音標, 'ngiˋ')
		self.assertEqual(客話音標.聲, '')
		self.assertEqual(客話音標.韻, 'ngi') 	
		self.assertEqual(客話音標.調, 'ˋ')

		客話音標 = 臺灣客家話拼音('mug') #目
		self.assertEqual(客話音標.音標, 'mug')
		self.assertEqual(客話音標.聲, '')
		self.assertEqual(客話音標.韻, 'mug')
		self.assertEqual(客話音標.調, '')
		
		客話音標 = 臺灣客家話拼音('ngiedˋ')#月
		self.assertEqual(客話音標.音標, 'ngiedˋ')
		self.assertEqual(客話音標.聲, '')
		self.assertEqual(客話音標.韻, 'ngied')
		self.assertEqual(客話音標.調, 'ˋ')
		
		客話音標 = 臺灣客家話拼音('ngin')#人
		self.assertEqual(客話音標.音標, 'ngin')
		self.assertEqual(客話音標.聲, '')
		self.assertEqual(客話音標.韻, 'ngin')
		self.assertEqual(客話音標.調, '')
#------------------------------------------
# 	def test_調值音標(self):
# 		self.assertEqual(臺灣客家話拼音('giog2').音標, 'giogˋ')

	def test_違法音標(self):
		self.assertEqual(臺灣客家話拼音('').音標, None)
		self.assertEqual(臺灣客家話拼音('@3@').音標, None)
		self.assertEqual(臺灣客家話拼音('gonkˊ').音標, None)
		self.assertEqual(臺灣客家話拼音('cn').音標, None)
		self.assertEqual(臺灣客家話拼音('tsé--á').音標, None)
		self.assertEqual(臺灣客家話拼音('óonn').音標, None)
		self.assertEqual(臺灣客家話拼音('giog+').音標, None)
		self.assertEqual(臺灣客家話拼音('giogˊ').音標, None)
		self.assertEqual(臺灣客家話拼音('ss').音標, None)
		self.assertEqual(臺灣客家話拼音('izrh').音標, None)
		
#--------------------------------------------------------

if __name__ == '__main__':
	unittest.main()
