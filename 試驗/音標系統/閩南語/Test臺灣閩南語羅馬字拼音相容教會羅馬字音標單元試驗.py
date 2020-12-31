# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音相容教會羅馬字音標 import 臺灣閩南語羅馬字拼音相容教會羅馬字音標


class 臺灣閩南語羅馬字拼音相容臺灣閩南語羅馬字拼音相容教會羅馬字音標單元試驗(TestCase):

    def test_零聲母聲韻調輕(self):
        臺羅相容 = 臺灣閩南語羅馬字拼音相容教會羅馬字音標('ainn7')
        self.assertEqual(臺羅相容.音標, 'ainn7')
        self.assertEqual(臺羅相容.聲, '')
        self.assertEqual(臺羅相容.韻, 'ainn')
        self.assertEqual(臺羅相容.調, '7')
        self.assertEqual(臺羅相容.輕, '')

    def test_完整聲韻調輕(self):
        臺羅相容 = 臺灣閩南語羅馬字拼音相容教會羅馬字音標('sih')
        self.assertEqual(臺羅相容.音標, 'sih4')
        self.assertEqual(臺羅相容.聲, 's')
        self.assertEqual(臺羅相容.韻, 'ih')
        self.assertEqual(臺羅相容.調, '4')
        self.assertEqual(臺羅相容.輕, '')

    def test_韻化輔音聲韻調輕(self):
        臺羅相容 = 臺灣閩南語羅馬字拼音相容教會羅馬字音標('ng5')
        self.assertEqual(臺羅相容.音標, 'ng5')
        self.assertEqual(臺羅相容.聲, '')
        self.assertEqual(臺羅相容.韻, 'ng')
        self.assertEqual(臺羅相容.調, '5')
        self.assertEqual(臺羅相容.輕, '')

    def test_語法輕聲聲韻調輕(self):
        臺羅相容 = 臺灣閩南語羅馬字拼音相容教會羅馬字音標('0e5')
        self.assertEqual(臺羅相容.音標, '0e5')
        self.assertEqual(臺羅相容.聲, '')
        self.assertEqual(臺羅相容.韻, 'e')
        self.assertEqual(臺羅相容.調, '5')
        self.assertEqual(臺羅相容.輕, '0')

    def test_定看音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('ainn7').音標, 'ainn7')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('ang3').音標, 'ang3')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('ang9').音標, 'ang9')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('e').音標, 'e1')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('mng5').音標, 'mng5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('Pih8').音標, 'pih8')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('Pih10').音標, 'pih10')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('tı̍t').音標, 'tit8')

    def test_次方言音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('tor').音標, 'tor1')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('kee5').音標, 'kee5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('ter5').音標, 'ter5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('tere5').音標, 'tere5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('tir5').音標, 'tir5')

    def test_輕聲(self):
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('ta0').音標, 'ta0')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('pih0').音標, 'pih0')

    def test_大寫開頭(self):
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('Na5').音標, 'na5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('Phoo2').音標, 'phoo2')

    def test_語法輕聲(self):
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('0a').音標, '0a1')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('0e5').音標, '0e5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('0ê').音標, '0e5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('0ê').音標, '0e5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('0hannh').音標, '0hannh4')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('0chi̍t').音標, '0chit8')

    def test_臺灣日本話(self):
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('1a').音標, '1a1')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('1e5').音標, '1e5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('1ê').音標, '1e5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('1bai2').音標, '1bai2')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('1hannh').音標, '1hannh4')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('1chi̍t').音標, '1chit8')

    def test_輕聲佮日本話無使做伙出現(self):
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('01a').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('10e5').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('01ê').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('10bai2').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('01hannh').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('10chi̍t').音標, None)

    def test_輸入閏號音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('pI̋m').音標, 'pim9')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('pi̍k').音標, 'pik8')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('pîm').音標, 'pim5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('pih').音標, 'pih4')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('nňg').音標, 'nng6')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('chőo').音標, 'choo9')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('chňg').音標, 'chng6')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('pňg').音標, 'png6')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('phǐN').音標, 'phinn6')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('tioN5').音標, 'tionn5')

    def test_鼻化ㆦ(self):
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('mo5').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('ngo5').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('moo5').音標, 'moo5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('ngoo5').音標, 'ngoo5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('mou5').音標, 'moo5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('ngou5').音標, 'ngoo5')

    def test_教羅型音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('hiuⁿ').音標, 'hiunn1')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('chēⁿ').音標, 'chenn7')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('siⁿh').音標, 'sinnh4')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('pháiⁿ').音標, 'phainn2')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('ko͘').音標, 'koo1')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('o͘h').音標, 'ooh4')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('ô͘').音標, 'oo5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('hō͘').音標, 'hoo7')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('hó͘ⁿ').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('pō•').音標, 'poo7')

    def test_違法音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('@@').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('pe̍m').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('cat8').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('ché--á').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('óonn').音標, None)
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('ot').音標, None)

    def test_專用韻(self):
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('chhou1').音標, 'chhoo1')
        self.assertEqual(
            臺灣閩南語羅馬字拼音相容教會羅馬字音標('chhou1').轉換到臺灣閩南語羅馬字拼音(), 'tshoo1')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('houN3').音標, 'honn3')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('houN3').轉換到臺灣閩南語羅馬字拼音(), 'honn3')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('poah4').音標, 'poah4')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('poah4').轉換到臺灣閩南語羅馬字拼音(), 'puah4')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('koe1').音標, 'koe1')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('koe1').轉換到臺灣閩南語羅馬字拼音(), 'kue1')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('tek4').音標, 'tek4')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('tek4').轉換到臺灣閩南語羅馬字拼音(), 'tik4')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('eng5').音標, 'eng5')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('eng5').轉換到臺灣閩南語羅馬字拼音(), 'ing5')

    def test_相容臺羅的毋閣無是臺羅(self):
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('tsoe3').音標, 'tsoe3')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('tsoe3').轉換到臺灣閩南語羅馬字拼音(), 'tsue3')

    def test_支援臺羅(self):
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('tsing1').音標, 'tsing1')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('tsik4').音標, 'tsik4')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('uan2').音標, 'uan2')
        self.assertEqual(臺灣閩南語羅馬字拼音相容教會羅馬字音標('tshue1').音標, 'tshue1')
