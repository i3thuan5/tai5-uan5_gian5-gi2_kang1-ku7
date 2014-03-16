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
from 臺灣言語工具.字詞組集句章.基本元素.字 import 字
from 臺灣言語工具.字詞組集句章.基本元素.詞 import 詞
from 臺灣言語工具.字詞組集句章.基本元素.組 import 組
from 臺灣言語工具.字詞組集句章.基本元素.集 import 集
from 臺灣言語工具.字詞組集句章.基本元素.句 import 句
from 臺灣言語工具.字詞組集句章.基本元素.章 import 章
from 臺灣言語工具.字詞組集句章.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.字詞組集句章.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.字詞組集句章.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音

class 文章粗胚試驗(unittest.TestCase):
	def setUp(self):
		self.粗胚 = 文章粗胚()
	def tearDown(self):
		pass

	def test_建立物件語句前處理減號連字號(self):
		原來語句 = '阮hak8-hau7佇大學路'
		處理好語句 = '阮hak8-hau7佇大學路'
		加空白後語句 = '阮hak8-hau7佇大學路'
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號濟輕聲(self):
		原來語句 = '儂莫走boo5--ki3。'
		處理好語句 = '儂莫走boo5-0ki3。'
		加空白後語句 = '儂莫走boo5-0ki3 。 '
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號住址(self):
		原來語句 = '大學路1001-1號，'
		處理好語句 = '大學路1001 - 1號，'
		加空白後語句 = '大學路1001 - 1號 ， '
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號算式(self):
		原來語句 = '因為5-2=3，所以3-5=-2'
		處理好語句 = '因為5 - 2=3，所以3 - 5= - 2'
		加空白後語句 = '因為5 - 2 = 3 ， 所以3 - 5 = - 2'
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號負數(self):
		原來語句 = '-20+5=-15'
		處理好語句 = ' - 20+5= - 15'
		加空白後語句 = ' - 20 + 5 = - 15'
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號做符號(self):
		原來語句 = '---- 媠 ----'
		處理好語句 = ' - - - - 媠 - - - - '
		加空白後語句 = ' - - - - 媠 - - - - '
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號連字號前漢後羅(self):
		原來語句 = '食--tsit8-kua5才來'
		處理好語句 = '食-0tsit8-kua5才來'
		加空白後語句 = '食-0tsit8-kua5才來'
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號連字號前羅後漢(self):
		原來語句 = '儂莫走boo5--去。'
		處理好語句 = '儂莫走boo5-去。'
		加空白後語句 = '儂莫走boo5-去 。 '
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)


	def test_建立物件語句前處理減號長連字符(self):
		原來語句 = '欲khuànn--tsit-ē--bô？'
		處理好語句 = '欲khuànn-0tsit-ē-0bô？'
		加空白後語句 = '欲khuànn-0tsit-ē-0bô ？ '
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)


	def test_建立物件語句前處理減號連字號音標輕聲開頭(self):
		原來語句 = '--ah'
		處理好語句 = '0ah'
		加空白後語句 = '0ah'
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號聲調輕聲開頭(self):
		原來語句 = '0ah'
		處理好語句 = '0ah'
		加空白後語句 = '0ah'
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號連字號漢字輕聲開頭(self):
		原來語句 = '--矣'
		處理好語句 = '矣'
		加空白後語句 = '矣'
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)
		
	def test_建立物件語句前處理一个減號(self):
		原來音 = '-'
		處理好音 = ' - '
		加空白後音 = ' - '
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來音), 處理好音)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好音), 加空白後音)

	def test_建立物件語句前處理減號輕聲開頭(self):
		原來語句 = '-重-看看'
		處理好語句 = ' - 重-看看'
		加空白後語句 = ' - 重-看看'
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號連字號前後漢字(self):
		# 這種測資嘛無法度
		原來語句 = '儂莫走無--去。'
		處理好語句 = '儂莫走無-去。'
		加空白後語句 = '儂莫走無-去 。 '
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號綜合(self):
		原來語句 = '食--tsit8-kua5才來，阮hak8-hau7佇大學路1001-1號，儂莫走boo5--ki3。'
		處理好語句 = '食-0tsit8-kua5才來，阮hak8-hau7佇大學路1001 - 1號，儂莫走boo5-0ki3。'
		加空白後語句 = '食-0tsit8-kua5才來 ， 阮hak8-hau7佇大學路1001 - 1號 ， 儂莫走boo5-0ki3 。 '
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號組字式(self):
		原來語句 = '⿰---⿰---⿱--,⿰-,⿱⿰-,---⿱--'
		處理好語句 = '⿰---⿰---⿱--,⿰-,⿱⿰-,--⿱--'
		加空白後語句 = '⿰---⿰---⿱-- , ⿰-,⿱⿰-,--⿱--'
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理奇怪組合(self):
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1- niu5'), 'sui2 koo1 - niu5')
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1 -niu5'), 'sui2 koo1 - niu5')
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1-- niu5'), 'sui2 koo1 - - niu5')
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1--   niu5'), 'sui2 koo1 - - niu5')
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1--niu5'), 'sui2 koo1-0niu5')
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1 - -niu5'), 'sui2 koo1 - - niu5')
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1 --niu5'), 'sui2 koo1 -0niu5')
		self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1  --niu5'), 'sui2 koo1 -0niu5')

	def test_符號邊仔加空白(self):
		self.assertEqual(self.粗胚.符號邊仔加空白('腹肚枵'), '腹肚枵')
		self.assertEqual(self.粗胚.符號邊仔加空白('腹肚枵,'), '腹肚枵 , ')
		self.assertEqual(self.粗胚.符號邊仔加空白(':sui2,koo1,niu5...'), ' : sui2 , koo1 , niu5 . . . ')
		self.assertEqual(self.粗胚.符號邊仔加空白(' :sui2,   koo1 ,niu5 .  .  .  '), ' : sui2 , koo1 , niu5 . . . ')
		self.assertEqual(self.粗胚.符號邊仔加空白(':sui2,koo1,niu5...'), ' : sui2 , koo1 , niu5 . . . ')
		self.assertEqual(self.粗胚.符號邊仔加空白(':sui2,koo1,niu5..a.'), ' : sui2 , koo1 , niu5 . . a . ')
		self.assertEqual(self.粗胚.符號邊仔加空白('我有100箍'), '我有100箍')
		self.assertEqual(self.粗胚.符號邊仔加空白('這馬時間12:20，'), '這馬時間12 : 20 ， ')

	def test_符號邊仔加空白分字符號問題(self):
		self.assertEqual(self.粗胚.符號邊仔加空白('sui2 koo1-niu5'), 'sui2 koo1-niu5')
		self.assertEqual(self.粗胚.符號邊仔加空白('sui2 koo1  -  niu5'), 'sui2 koo1 - niu5')
		self.assertEqual(self.粗胚.符號邊仔加空白('sui2 koo1-0niu5'), 'sui2 koo1-0niu5')
		self.assertEqual(self.粗胚.符號邊仔加空白('sui2 koo1-0niu5'), 'sui2 koo1-0niu5')
		self.assertEqual(self.粗胚.符號邊仔加空白('這馬分數12 - 20，'), '這馬分數12 - 20 ， ')
		self.assertEqual(self.粗胚.符號邊仔加空白('因為12  - 20= - 8，'), '因為12 - 20 = - 8 ， ')

	def test_符號邊仔加空白分字符號無應該處理著的(self):
		self.assertRaises(解析錯誤, self.粗胚.符號邊仔加空白, 'sui2 koo1- niu5')
		self.assertRaises(解析錯誤, self.粗胚.符號邊仔加空白, 'sui2 koo1 -niu5')
		self.assertRaises(解析錯誤, self.粗胚.符號邊仔加空白, 'sui2 koo1-- niu5')
		self.assertRaises(解析錯誤, self.粗胚.符號邊仔加空白, 'sui2 koo1--   niu5')
		self.assertRaises(解析錯誤, self.粗胚.符號邊仔加空白, 'sui2 koo1--niu5')
		self.assertRaises(解析錯誤, self.粗胚.符號邊仔加空白, 'sui2 koo1- -niu5')
		self.assertRaises(解析錯誤, self.粗胚.符號邊仔加空白, 'sui2 koo1 --niu5')
		self.assertRaises(解析錯誤, self.粗胚.符號邊仔加空白, 'sui2 koo1  --niu5')
		self.assertRaises(解析錯誤, self.粗胚.符號邊仔加空白, '--niu5')
		self.assertRaises(解析錯誤, self.粗胚.符號邊仔加空白, 'sui2--')
		
	def test_建立物件語句前減號當作標點符號(self):
		原來語句 = '阮hak8-hau7佇大學路'
		處理好語句 = '阮hak8 - hau7佇大學路'
		加空白後語句 = '阮hak8 - hau7佇大學路'
		self.assertEqual(self.粗胚.建立物件語句前減號變標點符號(原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)
		
	def test_建立物件語句前前減號負數當作標點符號(self):
		原來語句 = '-20+5=-15'
		處理好語句 = ' - 20+5= - 15'
		加空白後語句 = ' - 20 + 5 = - 15'
		self.assertEqual(self.粗胚.建立物件語句前減號變標點符號(原來語句), 處理好語句)
		self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_數字調英文中央加分字符號(self):
		原語句 = 'mi2-kiann7 boo5-0ki3 ah4ah!'
		結果語句 = 'mi2-kiann7 boo5-0ki3 ah4-ah!'
		self.assertEqual(self.粗胚.數字調英文中央加分字符號(原語句), 結果語句)

if __name__ == '__main__':
	unittest.main()
# 	粗胚 = 文章粗胚(臺灣閩南語羅馬字拼音)
# 	print(粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音,'sui2 koo1- niu5'))
