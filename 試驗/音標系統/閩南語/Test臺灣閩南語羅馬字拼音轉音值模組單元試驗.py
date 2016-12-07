# -*- coding: utf-8 -*-
import unittest
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音聲母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音韻母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音轉音值模組 import 臺灣閩南語羅馬字拼音對照音值聲母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音轉音值模組 import 臺灣閩南語羅馬字拼音對照音值韻母表


class 臺灣閩南語羅馬字拼音轉音值模組單元試驗(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_定看音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('e').音值(), ('ʔ', 'e', '1'))
        self.assertEqual(臺灣閩南語羅馬字拼音('e1').音值(), ('ʔ', 'e', '1'))
        self.assertEqual(臺灣閩南語羅馬字拼音('be2').音值(), ('b', 'e', '2'))
        self.assertEqual(臺灣閩南語羅馬字拼音('ang3').音值(), ('ʔ', 'aŋ', '3'))
        self.assertEqual(臺灣閩南語羅馬字拼音('mng5').音值(), ('m', 'ŋ̩', '5'))
        self.assertEqual(臺灣閩南語羅馬字拼音('ainn7').音值(), ('ʔ', 'aⁿiⁿ', '7'))
        self.assertEqual(臺灣閩南語羅馬字拼音('ang9').音值(), ('ʔ', 'aŋ', '9'))

    def test_零聲母聲韻調輕(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('sih').音值(), ('s', 'iʔ', '4'))
        self.assertEqual(臺灣閩南語羅馬字拼音('ah8').音值(), ('ʔ', 'aʔ', '8'))
        self.assertEqual(臺灣閩南語羅馬字拼音('m5').音值(), ('ʔ', 'm̩', '5'))
        self.assertEqual(臺灣閩南語羅馬字拼音('0e5').音值(), ('ʔ', 'e', '0'))

    def test_蚵芋音(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('ho2').音值(), ('h', 'ə', '2'))
        self.assertEqual(臺灣閩南語羅馬字拼音('hoh').音值(), ('h', 'əʔ', '4'))
        self.assertEqual(臺灣閩南語羅馬字拼音('hok').音值(), ('h', 'ok', '4'))
        self.assertEqual(臺灣閩南語羅馬字拼音('hio2').音值(), ('h', 'iə', '2'))
        self.assertEqual(臺灣閩南語羅馬字拼音('hioh').音值(), ('h', 'iəʔ', '4'))
        self.assertEqual(臺灣閩南語羅馬字拼音('hiok8').音值(), ('h', 'iok', '8'))

    def test_舌尖顎化(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('tsia').音值(), ('ts', 'ia', '1'))
        self.assertEqual(臺灣閩南語羅馬字拼音('tsha').音值(), ('tsʰ', 'a', '1'))
        self.assertEqual(臺灣閩南語羅馬字拼音('sa').音值(), ('s', 'a', '1'))
        self.assertEqual(臺灣閩南語羅馬字拼音('jia').音值(), ('dz', 'ia', '1'))

    def test_輕聲(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('ta0').音值(), ('t', 'a', '0'))
        self.assertEqual(臺灣閩南語羅馬字拼音('pih0').音值(), ('p', 'i', '0'))

    def test_語法輕聲(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('0a').音值(), ('ʔ', 'a', '0'))
        self.assertEqual(臺灣閩南語羅馬字拼音('0e5').音值(), ('ʔ', 'e', '0'))
        self.assertEqual(臺灣閩南語羅馬字拼音('0hannh').音值(), ('h', 'aⁿ', '0'))
        self.assertEqual(臺灣閩南語羅馬字拼音('0tsi̍t').音值(), ('ts', 'i', '0'))

    def test_罕用音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('tor').音值(), ('t', 'ə', '1'))
        self.assertEqual(臺灣閩南語羅馬字拼音('kee5').音值(), ('k', 'ɛ', '5'))
        self.assertEqual(臺灣閩南語羅馬字拼音('ter5').音值(), ('t', 'ə', '5'))
        self.assertEqual(臺灣閩南語羅馬字拼音('tere5').音值(), ('t', 'əe', '5'))
        self.assertEqual(臺灣閩南語羅馬字拼音('tir5').音值(), ('t', 'ɨ', '5'))

    def test_用著入聲調音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('ha8').音值(), (None,))

    def test_入聲調用著其他調音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('hak7').音值(), (None,))

    def test_其他違法音標(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('@@').音值(), (None,))
        self.assertEqual(臺灣閩南語羅馬字拼音('pe̍m').音值(), (None,))
        self.assertEqual(臺灣閩南語羅馬字拼音('xxtsé--á').音值(), (None,))
        self.assertEqual(臺灣閩南語羅馬字拼音('óonn').音值(), (None,))

    def test_全部攏會使產生方音物件(self):
        for 母 in 臺灣閩南語羅馬字拼音聲母表:
            self.assertIn(母, 臺灣閩南語羅馬字拼音對照音值聲母表)
        for 母 in 臺灣閩南語羅馬字拼音韻母表:
            self.assertIn(母, 臺灣閩南語羅馬字拼音對照音值韻母表)

    def test_鼻化韻逐个元音攏愛有鼻化(self):
        for 韻 in 臺灣閩南語羅馬字拼音對照音值韻母表.values():
            for 切 in 韻.split('ⁿ')[:-1]:
                self.assertEqual(len(切), 1, '{}有問題'.format(韻))
