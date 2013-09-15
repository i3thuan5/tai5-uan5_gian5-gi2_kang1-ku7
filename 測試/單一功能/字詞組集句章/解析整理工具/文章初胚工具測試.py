import unittest
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.基本元素.詞 import 詞
from 字詞組集句章.基本元素.組 import 組
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.基本元素.章 import 章
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音

class 拆文初胚工具測試(unittest.TestCase):
	def setUp(self):
		self.初胚工具 = 文章初胚工具()
	def tearDown(self):
		pass

	def test_建立物件語句前處理減號連字號(self):
		原來語句 = '阮hak8-hau7佇大學路'
		處理好語句 = '阮hak8-hau7佇大學路'
		加空白後語句 = '阮hak8-hau7佇大學路'
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號濟輕聲(self):
		原來語句 = '儂莫走boo5--ki3。'
		處理好語句 = '儂莫走boo5-0ki3。'
		加空白後語句 = '儂莫走boo5-0ki3 。 '
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號住址(self):
		原來語句 = '大學路1001-1號，'
		處理好語句 = '大學路1001 - 1號，'
		加空白後語句 = '大學路1001 - 1號 ， '
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號算式(self):
		原來語句 = '因為5-2=3，所以3-5=-2'
		處理好語句 = '因為5 - 2=3，所以3 - 5= - 2'
		加空白後語句 = '因為5 - 2 = 3 ， 所以3 - 5 = - 2'
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號負數(self):
		原來語句 = '-20+5=-15'
		處理好語句 = ' - 20+5= - 15'
		加空白後語句 = ' - 20 + 5 = - 15'
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號做符號(self):
		原來語句 = '---- 媠 ----'
		處理好語句 = ' - - - - 媠 - - - - '
		加空白後語句 = ' - - - - 媠 - - - - '
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號連字號前漢後羅(self):
		原來語句 = '食--tsit8-kua5才來'
		處理好語句 = '食-0tsit8-kua5才來'
		加空白後語句 = '食-0tsit8-kua5才來'
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號連字號前羅後漢(self):
		原來語句 = '儂莫走boo5--去。'
		處理好語句 = '儂莫走boo5-去。'
		加空白後語句 = '儂莫走boo5-去 。 '
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)


	def test_建立物件語句前處理減號長連字符(self):
		原來語句 = '欲khuànn--tsit-ē--bô？'
		處理好語句 = '欲khuànn-0tsit-ē-0bô？'
		加空白後語句 = '欲khuànn-0tsit-ē-0bô ？ '
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)


	def test_建立物件語句前處理減號連字號音標輕聲開頭(self):
		原來語句 = '--ah'
		處理好語句 = '0ah'
		加空白後語句 = '0ah'
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號聲調輕聲開頭(self):
		原來語句 = '0ah'
		處理好語句 = '0ah'
		加空白後語句 = '0ah'
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號連字號漢字輕聲開頭(self):
		原來語句 = '--矣'
		處理好語句 = '矣'
		加空白後語句 = '矣'
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號輕聲開頭(self):
		原來語句 = '-重-看看'
		處理好語句 = ' - 重-看看'
		加空白後語句 = ' - 重-看看'
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號連字號前後漢字(self):
		# 這種測資嘛無法度
		原來語句 = '儂莫走無--去。'
		處理好語句 = '儂莫走無-去。'
		加空白後語句 = '儂莫走無-去 。 '
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號綜合(self):
		原來語句 = '食--tsit8-kua5才來，阮hak8-hau7佇大學路1001-1號，儂莫走boo5--ki3。'
		處理好語句 = '食-0tsit8-kua5才來，阮hak8-hau7佇大學路1001 - 1號，儂莫走boo5-0ki3。'
		加空白後語句 = '食-0tsit8-kua5才來 ， 阮hak8-hau7佇大學路1001 - 1號 ， 儂莫走boo5-0ki3 。 '
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理減號組字式(self):
		原來語句 = '⿰---⿰---⿱--,⿰-,⿱⿰-,---⿱--'
		處理好語句 = '⿰---⿰---⿱--,⿰-,⿱⿰-,--⿱--'
		加空白後語句 = '⿰---⿰---⿱-- , ⿰-,⿱⿰-,--⿱--'
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
		self.assertEqual(self.初胚工具.符號邊仔加空白(處理好語句), 加空白後語句)

	def test_建立物件語句前處理奇怪組合(self):
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1- niu5'), 'sui2 koo1 - niu5')
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1 -niu5'), 'sui2 koo1 - niu5')
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1-- niu5'), 'sui2 koo1 - - niu5')
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1--   niu5'), 'sui2 koo1 - - niu5')
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1--niu5'), 'sui2 koo1-0niu5')
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1 - -niu5'), 'sui2 koo1 - - niu5')
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1 --niu5'), 'sui2 koo1 -0niu5')
		self.assertEqual(self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1  --niu5'), 'sui2 koo1 -0niu5')

	def test_符號邊仔加空白(self):
		self.assertEqual(self.初胚工具.符號邊仔加空白('腹肚枵'), '腹肚枵')
		self.assertEqual(self.初胚工具.符號邊仔加空白('腹肚枵,'), '腹肚枵 , ')
		self.assertEqual(self.初胚工具.符號邊仔加空白(':sui2,koo1,niu5...'), ' : sui2 , koo1 , niu5 . . . ')
		self.assertEqual(self.初胚工具.符號邊仔加空白(' :sui2,   koo1 ,niu5 .  .  .  '), ' : sui2 , koo1 , niu5 . . . ')
		self.assertEqual(self.初胚工具.符號邊仔加空白(':sui2,koo1,niu5...'), ' : sui2 , koo1 , niu5 . . . ')
		self.assertEqual(self.初胚工具.符號邊仔加空白(':sui2,koo1,niu5..a.'), ' : sui2 , koo1 , niu5 . . a . ')
		self.assertEqual(self.初胚工具.符號邊仔加空白('我有100箍'), '我有100箍')
		self.assertEqual(self.初胚工具.符號邊仔加空白('這馬時間12:20，'), '這馬時間12 : 20 ， ')

	def test_符號邊仔加空白分字符號問題(self):
		self.assertEqual(self.初胚工具.符號邊仔加空白('sui2 koo1-niu5'), 'sui2 koo1-niu5')
		self.assertEqual(self.初胚工具.符號邊仔加空白('sui2 koo1  -  niu5'), 'sui2 koo1 - niu5')
		self.assertEqual(self.初胚工具.符號邊仔加空白('sui2 koo1-0niu5'), 'sui2 koo1-0niu5')
		self.assertEqual(self.初胚工具.符號邊仔加空白('sui2 koo1-0niu5'), 'sui2 koo1-0niu5')
		self.assertEqual(self.初胚工具.符號邊仔加空白('這馬分數12 - 20，'), '這馬分數12 - 20 ， ')
		self.assertEqual(self.初胚工具.符號邊仔加空白('因為12  - 20= - 8，'), '因為12 - 20 = - 8 ， ')

	def test_符號邊仔加空白分字符號無應該處理著的(self):
		self.assertRaises(解析錯誤, self.初胚工具.符號邊仔加空白, 'sui2 koo1- niu5')
		self.assertRaises(解析錯誤, self.初胚工具.符號邊仔加空白, 'sui2 koo1 -niu5')
		self.assertRaises(解析錯誤, self.初胚工具.符號邊仔加空白, 'sui2 koo1-- niu5')
		self.assertRaises(解析錯誤, self.初胚工具.符號邊仔加空白, 'sui2 koo1--   niu5')
		self.assertRaises(解析錯誤, self.初胚工具.符號邊仔加空白, 'sui2 koo1--niu5')
		self.assertRaises(解析錯誤, self.初胚工具.符號邊仔加空白, 'sui2 koo1- -niu5')
		self.assertRaises(解析錯誤, self.初胚工具.符號邊仔加空白, 'sui2 koo1 --niu5')
		self.assertRaises(解析錯誤, self.初胚工具.符號邊仔加空白, 'sui2 koo1  --niu5')
		self.assertRaises(解析錯誤, self.初胚工具.符號邊仔加空白, '--niu5')
		self.assertRaises(解析錯誤, self.初胚工具.符號邊仔加空白, 'sui2--')


if __name__ == '__main__':
	unittest.main()
# 	初胚工具 = 文章初胚工具(臺灣閩南語羅馬字拼音)
# 	print(初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音,'sui2 koo1- niu5'))
