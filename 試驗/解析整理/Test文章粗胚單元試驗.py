# -*- coding: utf-8 -*-
import unittest
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 文章粗胚處理減號單元試驗(unittest.TestCase):

    def test_建立物件語句前處理減號連字號(self):
        原來語句 = '阮hak8-hau7佇大學路'
        處理好語句 = '阮hak8-hau7佇大學路'
        加空白後語句 = '阮hak8-hau7佇大學路'
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號濟輕聲(self):
        原來語句 = '儂莫走boo5--ki3。'
        處理好語句 = '儂莫走boo5 0ki3。'
        加空白後語句 = '儂莫走boo5 0ki3 。 '
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號住址(self):
        原來語句 = '大學路1001-1號，'
        處理好語句 = '大學路1001 - 1號，'
        加空白後語句 = '大學路1001 - 1號 ， '
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號算式(self):
        原來語句 = '因為5-2=3，所以3-5=-2'
        處理好語句 = '因為5 - 2=3，所以3 - 5= - 2'
        加空白後語句 = '因為5 - 2 = 3 ， 所以3 - 5 = - 2'
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號負數(self):
        原來語句 = '-20+5=-15'
        處理好語句 = ' - 20+5= - 15'
        加空白後語句 = ' - 20 + 5 = - 15'
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號做符號(self):
        原來語句 = '---- 媠 ----'
        處理好語句 = ' - - - - 媠 - - - - '
        加空白後語句 = ' - - - - 媠 - - - - '
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號連做伙做符號(self):
        原來語句 = '----媠----'
        處理好語句 = ' - - - - 媠 - - - - '
        加空白後語句 = ' - - - - 媠 - - - - '
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號連做伙做符號閣有正常符號(self):
        原來語句 = '---呵 li2-ho2'
        處理好語句 = ' - - - 呵 li2-ho2'
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )

    def test_建立物件語句前處理減號連字號前漢後羅(self):
        原來語句 = '食--tsit8-kua5才來'
        處理好語句 = '食 0tsit8-kua5才來'
        加空白後語句 = '食 0tsit8-kua5才來'
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號輕聲連字號前羅後漢(self):
        原來語句 = '儂莫走boo5--去。'
        處理好語句 = '儂莫走boo5 去。'
        加空白後語句 = '儂莫走boo5 去 。 '
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號連字號前羅後漢(self):
        原來語句 = '儂莫走boo5-來。'
        處理好語句 = '儂莫走boo5-來。'
        加空白後語句 = '儂莫走boo5-來 。 '
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號長連字符(self):
        原來語句 = '欲khuànn--tsit-ē--bô？'
        處理好語句 = '欲khuànn 0tsit-ē 0bô？'
        加空白後語句 = '欲khuànn 0tsit-ē 0bô ？ '
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號連字號音標輕聲開頭(self):
        原來語句 = '--ah'
        處理好語句 = '0ah'
        加空白後語句 = '0ah'
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號聲調輕聲開頭(self):
        原來語句 = '0ah'
        處理好語句 = '0ah'
        加空白後語句 = '0ah'
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號連字號漢字輕聲開頭(self):
        原來語句 = '--矣'
        處理好語句 = '矣'
        加空白後語句 = '矣'
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號連字號漢字句中輕聲開頭(self):
        原來語句 = '我 食 飯 --矣'
        處理好語句 = '我 食 飯 矣'
        加空白後語句 = '我 食 飯 矣'
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號輕聲接符號(self):
        原來語句 = '從中thang講，--破錢、用憨錢'
        處理好語句 = '從中thang講，破錢、用憨錢'
        加空白後語句 = '從中thang講 ， 破錢 、 用憨錢'
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號輕聲音標接符號(self):
        原來語句 = '從中thang講，--phuat4錢、用憨錢'
        處理好語句 = '從中thang講，0phuat4錢、用憨錢'
        加空白後語句 = '從中thang講 ， 0phuat4錢 、 用憨錢'
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號連字號漢字後(self):
        原來語句 = '轉-- 來'
        處理好語句 = '轉 - - 來'
        加空白後語句 = '轉 - - 來'
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理一个減號(self):
        原來音 = '-'
        處理好音 = ' - '
        加空白後音 = ' - '
        self.assertEqual(文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來音), 處理好音)
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好音), 加空白後音)

    def test_建立物件語句前處理減號輕聲開頭(self):
        原來語句 = '-重-看看'
        處理好語句 = ' - 重-看看'
        加空白後語句 = ' - 重-看看'
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號一个連字符(self):
        原來語句 = '-幕-'
        處理好語句 = ' - 幕 - '
        加空白後語句 = ' - 幕 - '
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號連字號前後漢字(self):
        # 這種測資嘛無法度
        原來語句 = '儂莫走無--去。'
        處理好語句 = '儂莫走無 去。'
        加空白後語句 = '儂莫走無 去 。 '
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號綜合(self):
        原來語句 = '食--tsit8-kua5才來，阮hak8-hau7佇大學路1001-1號，儂莫走boo5--ki3。'
        處理好語句 = '食 0tsit8-kua5才來，阮hak8-hau7佇大學路1001 - 1號，儂莫走boo5 0ki3。'
        加空白後語句 = '食 0tsit8-kua5才來 ， 阮hak8-hau7佇大學路1001 - 1號 ， 儂莫走boo5 0ki3 。 '
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號輕聲中央(self):
        原來語句 = 'tsio2 --e5 ia7 u7 tsit8-ban7 goo7-tshing tsiah.'
        處理好語句 = 'tsio2 0e5 ia7 u7 tsit8-ban7 goo7-tshing tsiah.'
        加空白後語句 = 'tsio2 0e5 ia7 u7 tsit8-ban7 goo7-tshing tsiah . '
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號組字式(self):
        原來語句 = '⿰---⿰---⿱--,⿰-,⿱⿰-,---⿱--'
        處理好語句 = '⿰---⿰---⿱--,⿰-,⿱⿰-,- ⿱--'
        加空白後語句 = '⿰---⿰---⿱-- , ⿰-,⿱⿰-,- ⿱--'
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理奇怪組合(self):
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1- niu5'), 'sui2 koo1 - niu5')
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1 -niu5'), 'sui2 koo1 - niu5')
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1-- niu5'), 'sui2 koo1 - - niu5')
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1--   niu5'), 'sui2 koo1 - - niu5')
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1--niu5'), 'sui2 koo1 0niu5')
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1 - -niu5'), 'sui2 koo1 - - niu5')
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1 --niu5'), 'sui2 koo1 0niu5')
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 'sui2 koo1  --niu5'), 'sui2 koo1 0niu5')

    def test_符號邊仔加空白(self):
        self.assertEqual(文章粗胚.符號邊仔加空白('腹肚枵'), '腹肚枵')
        self.assertEqual(文章粗胚.符號邊仔加空白('腹肚枵,'), '腹肚枵 , ')
        self.assertEqual(
            文章粗胚.符號邊仔加空白(':sui2,koo1,niu5...'), ' : sui2 , koo1 , niu5 . . . ')
        self.assertEqual(文章粗胚.符號邊仔加空白(
            ' :sui2,   koo1 ,niu5 .  .  .  '), ' : sui2 , koo1 , niu5 . . . ')
        self.assertEqual(
            文章粗胚.符號邊仔加空白(':sui2,koo1,niu5...'), ' : sui2 , koo1 , niu5 . . . ')
        self.assertEqual(
            文章粗胚.符號邊仔加空白(':sui2,koo1,niu5..a.'), ' : sui2 , koo1 , niu5 . . a . ')
        self.assertEqual(文章粗胚.符號邊仔加空白('我有100箍'), '我有100箍')
        self.assertEqual(文章粗胚.符號邊仔加空白('這馬時間12:20，'), '這馬時間12 : 20 ， ')

    def test_符號邊仔加空白分字符號問題(self):
        self.assertEqual(文章粗胚.符號邊仔加空白('sui2 koo1-niu5'), 'sui2 koo1-niu5')
        self.assertEqual(
            文章粗胚.符號邊仔加空白('sui2 koo1  -  niu5'), 'sui2 koo1 - niu5')
        self.assertEqual(文章粗胚.符號邊仔加空白('sui2 koo1-0niu5'), 'sui2 koo1-0niu5')
        self.assertEqual(文章粗胚.符號邊仔加空白('sui2 koo1-0niu5'), 'sui2 koo1-0niu5')
        self.assertEqual(文章粗胚.符號邊仔加空白('這馬分數12 - 20，'), '這馬分數12 - 20 ， ')
        self.assertEqual(
            文章粗胚.符號邊仔加空白('因為12  - 20= - 8，'), '因為12 - 20 = - 8 ， ')

    def test_符號邊仔加空白分字符號無應該處理著的(self):
        self.assertRaises(解析錯誤, 文章粗胚.符號邊仔加空白, 'sui2 koo1- niu5')
        self.assertRaises(解析錯誤, 文章粗胚.符號邊仔加空白, 'sui2 koo1 -niu5')
        self.assertRaises(解析錯誤, 文章粗胚.符號邊仔加空白, 'sui2 koo1-- niu5')
        self.assertRaises(解析錯誤, 文章粗胚.符號邊仔加空白, 'sui2 koo1--   niu5')
        self.assertRaises(解析錯誤, 文章粗胚.符號邊仔加空白, 'sui2 koo1--niu5')
        self.assertRaises(解析錯誤, 文章粗胚.符號邊仔加空白, 'sui2 koo1- -niu5')
        self.assertRaises(解析錯誤, 文章粗胚.符號邊仔加空白, 'sui2 koo1 --niu5')
        self.assertRaises(解析錯誤, 文章粗胚.符號邊仔加空白, 'sui2 koo1  --niu5')
        self.assertRaises(解析錯誤, 文章粗胚.符號邊仔加空白, '--niu5')
        self.assertRaises(解析錯誤, 文章粗胚.符號邊仔加空白, 'sui2--')

    def test_建立物件語句前減號當作標點符號(self):
        原來語句 = '阮hak8-hau7佇大學路'
        處理好語句 = '阮hak8 - hau7佇大學路'
        加空白後語句 = '阮hak8 - hau7佇大學路'
        self.assertEqual(文章粗胚.建立物件語句前減號變標點符號(原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
                         )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前前減號負數當作標點符號(self):
        原來語句 = '-20+5=-15'
        處理好語句 = ' - 20+5= - 15'
        加空白後語句 = ' - 20 + 5 = - 15'
        self.assertEqual(文章粗胚.建立物件語句前減號變標點符號(原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
                         )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_分字符號一大堆(self):
        原來語句 = 'lai5 tsing2-phoo7 khia7-kua3----tsit8 kua3 u7 sann-tsiah gu5, kiong7 tioh8 tsiann5-tsap8 kua3.'
        處理好語句 = 'lai5 tsing2-phoo7 khia7-kua3 - - - - tsit8 kua3 u7 sann-tsiah gu5, kiong7 tioh8 tsiann5-tsap8 kua3.'
        加空白後語句 = 'lai5 tsing2-phoo7 khia7-kua3 - - - - tsit8 kua3 u7 sann-tsiah gu5 , kiong7 tioh8 tsiann5-tsap8 kua3 . '
        self.assertEqual(
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句, 別的符號邊仔順紲加空白=False), 處理好語句
        )
        self.assertEqual(文章粗胚.符號邊仔加空白(處理好語句), 加空白後語句)

    def test_建立物件語句前處理減號順紲加空白(self):
        原來語句 = '阮ti1-tiau5佇大學路。'
        加空白後語句 = '阮ti1-tiau5佇大學路 。 '
        self.assertEqual(文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 加空白後語句)

    def test_建立物件語句前減號變標點符號順紲加空白(self):
        原來語句 = '阮ti1-tiau5佇大學路。'
        加空白後語句 = '阮ti1 - tiau5佇大學路 。 '
        self.assertEqual(文章粗胚.建立物件語句前減號變標點符號(原來語句), 加空白後語句)

    def test_南島的喉塞音(self):
        self.assertEqual(文章粗胚.符號邊仔加空白("Nga'ay ho?"), "Nga'ay ho ? ")
