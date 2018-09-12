# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺羅對通用聲對照表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺羅對通用韻對照表
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音佮臺灣羅馬聲母對照表
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音佮臺灣羅馬韻母對照表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音聲母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音韻母表


class 臺灣閩南語羅馬字拼音單元試驗(TestCase):

    def test_零聲母聲韻調輕(self):
        臺羅音標 = 臺灣閩南語羅馬字拼音('ainn7')
        self.assertEqual(臺羅音標.音標, 'ainn7')
        self.assertEqual(臺羅音標.聲, '')
        self.assertEqual(臺羅音標.韻, 'ainn')
        self.assertEqual(臺羅音標.調, '7')
        self.assertEqual(臺羅音標.輕, '')

    def test_完整聲韻調輕(self):
        臺羅音標 = 臺灣閩南語羅馬字拼音('sih')
        self.assertEqual(臺羅音標.音標, 'sih4')
        self.assertEqual(臺羅音標.聲, 's')
        self.assertEqual(臺羅音標.韻, 'ih')
        self.assertEqual(臺羅音標.調, '4')
        self.assertEqual(臺羅音標.輕, '')

    def test_韻化輔音聲韻調輕(self):
        臺羅音標 = 臺灣閩南語羅馬字拼音('ng5')
        self.assertEqual(臺羅音標.音標, 'ng5')
        self.assertEqual(臺羅音標.聲, '')
        self.assertEqual(臺羅音標.韻, 'ng')
        self.assertEqual(臺羅音標.調, '5')
        self.assertEqual(臺羅音標.輕, '')

    def test_語法輕聲聲韻調輕(self):
        臺羅音標 = 臺灣閩南語羅馬字拼音('0e5')
        self.assertEqual(臺羅音標.音標, '0e5')
        self.assertEqual(臺羅音標.聲, '')
        self.assertEqual(臺羅音標.韻, 'e')
        self.assertEqual(臺羅音標.調, '5')
        self.assertEqual(臺羅音標.輕, '0')

    def test_定看音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('ainn7').音標, 'ainn7')
        self.assertEqual(臺灣閩南語羅馬字拼音('ang3').音標, 'ang3')
        self.assertEqual(臺灣閩南語羅馬字拼音('ang9').音標, 'ang9')
        self.assertEqual(臺灣閩南語羅馬字拼音('e').音標, 'e1')
        self.assertEqual(臺灣閩南語羅馬字拼音('mng5').音標, 'mng5')
        self.assertEqual(臺灣閩南語羅馬字拼音('Pih8').音標, 'pih8')
        self.assertEqual(臺灣閩南語羅馬字拼音('Pih10').音標, 'pih10')
        self.assertEqual(臺灣閩南語羅馬字拼音('tı̍t').音標, 'tit8')

    def test_大寫開頭(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('Na5').音標, 'na5')
        self.assertEqual(臺灣閩南語羅馬字拼音('Phoo2').音標, 'phoo2')

    def test_輕聲(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('ta0').音標, 'ta0')
        self.assertEqual(臺灣閩南語羅馬字拼音('pih0').音標, 'pih0')

    def test_語法輕聲(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('0a').音標, '0a1')
        self.assertEqual(臺灣閩南語羅馬字拼音('0e5').音標, '0e5')
        self.assertEqual(臺灣閩南語羅馬字拼音('0ê').音標, '0e5')
        self.assertEqual(臺灣閩南語羅馬字拼音('0ê').音標, '0e5')
        self.assertEqual(臺灣閩南語羅馬字拼音('0hannh').音標, '0hannh4')
        self.assertEqual(臺灣閩南語羅馬字拼音('0tsi̍t').音標, '0tsit8')

    def test_臺灣日本話(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('1a').音標, '1a1')
        self.assertEqual(臺灣閩南語羅馬字拼音('1e5').音標, '1e5')
        self.assertEqual(臺灣閩南語羅馬字拼音('1ê').音標, '1e5')
        self.assertEqual(臺灣閩南語羅馬字拼音('1bai2').音標, '1bai2')
        self.assertEqual(臺灣閩南語羅馬字拼音('1hannh').音標, '1hannh4')
        self.assertEqual(臺灣閩南語羅馬字拼音('1tsi̍t').音標, '1tsit8')

    def test_綜合話(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('sui2').音標, 'sui2')
        self.assertEqual(臺灣閩南語羅馬字拼音('1sui2').音標, '1sui2')
        self.assertEqual(臺灣閩南語羅馬字拼音('sui2').音標, 'sui2')
        self.assertEqual(臺灣閩南語羅馬字拼音('0sui2').音標, '0sui2')
        self.assertEqual(臺灣閩南語羅馬字拼音('sui2').音標, 'sui2')
        self.assertEqual(臺灣閩南語羅馬字拼音('0sui2').音標, '0sui2')
        self.assertEqual(臺灣閩南語羅馬字拼音('1sui2').音標, '1sui2')

    def test_輕聲佮日本話無使做伙出現(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('01a').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音('10e5').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音('01ê').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音('10bai2').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音('01hannh').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音('10tsi̍t').音標, None)

    def test_輸入閏號音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('pI̋m').音標, 'pim9')
        self.assertEqual(臺灣閩南語羅馬字拼音('pi̍k').音標, 'pik8')
        self.assertEqual(臺灣閩南語羅馬字拼音('pîm').音標, 'pim5')
        self.assertEqual(臺灣閩南語羅馬字拼音('phǐN').音標, 'phinn6')
        self.assertEqual(臺灣閩南語羅馬字拼音('pih').音標, 'pih4')
        self.assertEqual(臺灣閩南語羅馬字拼音('nňg').音標, 'nng6')
        self.assertEqual(臺灣閩南語羅馬字拼音('tsőo').音標, 'tsoo9')
        self.assertEqual(臺灣閩南語羅馬字拼音('tsňg').音標, 'tsng6')
        self.assertEqual(臺灣閩南語羅馬字拼音('pňg').音標, 'png6')

    def test_鼻化ㆦ愛oo(self):
        self.assertIsNone(臺灣閩南語羅馬字拼音('ngo').音標)

    def test_次方言音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('tor').音標, 'tor1')
        self.assertEqual(臺灣閩南語羅馬字拼音('kee5').音標, 'kee5')
        self.assertEqual(臺灣閩南語羅馬字拼音('ter5').音標, 'ter5')
        self.assertEqual(臺灣閩南語羅馬字拼音('tere5').音標, 'tere5')
        self.assertEqual(臺灣閩南語羅馬字拼音('tir5').音標, 'tir5')

    def test_教羅傳統版音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('hiuⁿ').音標, 'hiunn1')
        self.assertEqual(臺灣閩南語羅馬字拼音('tsēⁿ').音標, 'tsenn7')
        self.assertEqual(臺灣閩南語羅馬字拼音('siⁿh').音標, 'sinnh4')
        self.assertEqual(臺灣閩南語羅馬字拼音('pháiⁿ').音標, 'phainn2')
        self.assertEqual(臺灣閩南語羅馬字拼音('ko͘').音標, 'koo1')
        self.assertEqual(臺灣閩南語羅馬字拼音('o͘h').音標, 'ooh4')
        self.assertEqual(臺灣閩南語羅馬字拼音('ô͘').音標, 'oo5')
        self.assertEqual(臺灣閩南語羅馬字拼音('hō͘').音標, 'hoo7')
        self.assertEqual(臺灣閩南語羅馬字拼音('hó͘ⁿ').音標, None)

    def test_附錄外來語先莫收_用另外的格式來(self):
        self.assertIsNone(臺灣閩南語羅馬字拼音('a33').音標)

    def test_無合法的調符愛擋咧(self):
        self.assertIsNone(臺灣閩南語羅馬字拼音('tsiòk').音標)

    def test_用著入聲調音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('ha8').音標, None)

    def test_入聲調用著其他調音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('hak7').音標, None)

    def test_違法音標_出現符號(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('@@').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音('a.').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音('.').音標, None)

    def test_違法音標_無em_m袂第八調(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('pe̍m').音標, None)

    def test_違法音標_無c(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('cat8').音標, None)

    def test_違法音標_超過一個音節(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('tsé--á').音標, None)

    def test_違法音標_無oonn(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('óonn').音標, None)

    def test_違法音標_無ot(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('ot').音標, None)

    def test_無存在的聲調(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('bo78').音標, None)

    def test_無正確_同母音袂出現兩擺(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('suii').音標, None)

    def test_無正確_鼻化音袂出現兩擺(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('ngan').音標, None)

    def test_無正確_干焦tkh會出現兩擺(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('sas').音標, None)

    def test_轉通用拼音(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('gio2').轉通用拼音(), 'ghior4')
        self.assertEqual(臺灣閩南語羅馬字拼音('hiunnh8').轉通用拼音(), 'hiunnh6')
        self.assertEqual(臺灣閩南語羅馬字拼音('suii').轉通用拼音(), None)

    def test_輕聲轉會過通用拼音(self):
        臺灣閩南語羅馬字拼音('bo0').轉通用拼音()

    def test_全部攏會轉通用拼音(self):
        for 臺, 通 in 臺羅對通用聲對照表.items():
            self.assertIn(臺, 臺灣閩南語羅馬字拼音聲母表)
            self.assertIn(通, 通用拼音佮臺灣羅馬聲母對照表)
        for 臺, 通 in 臺羅對通用韻對照表.items():
            self.assertIn(臺, 臺灣閩南語羅馬字拼音韻母表)
            self.assertIn(通, 通用拼音佮臺灣羅馬韻母對照表)
