# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音附錄外來語 import 臺灣閩南語羅馬字拼音附錄外來語


class 臺灣閩南語羅馬字拼音附錄外來語單元試驗(TestCase):

    def test_一般拼音無接受(self):
        self.assertIsNone(臺灣閩南語羅馬字拼音附錄外來語('ainn7').音標)

    def test_完整聲韻調輕(self):
        臺羅音標 = 臺灣閩南語羅馬字拼音附錄外來語('han35')
        self.assertEqual(臺羅音標.音標, '1han9')
        self.assertEqual(臺羅音標.聲, 'h')
        self.assertEqual(臺羅音標.韻, 'an')
        self.assertEqual(臺羅音標.調, '9')
        self.assertEqual(臺羅音標.輕, '')
        self.assertEqual(臺羅音標.原本音標, 'han35')

    def test_外來語アルミ的ア(self):
        self.assertEqual(臺灣閩南語羅馬字拼音附錄外來語('a33').音標, '1a7')

    def test_外來語アルミ的ル(self):
        self.assertEqual(臺灣閩南語羅馬字拼音附錄外來語('lu55').音標, '1lu1')

    def test_外來語アルミ的ミ(self):
        self.assertEqual(臺灣閩南語羅馬字拼音附錄外來語('mih3').音標, '1mih4')

    def test_外來語拉鍊的拉(self):
        self.assertEqual(臺灣閩南語羅馬字拼音附錄外來語('la55').音標, '1la1')

    def test_外來語拉鍊的鍊(self):
        self.assertEqual(臺灣閩南語羅馬字拼音附錄外來語('lian51').音標, '1lian2')

    def test_無合法的調符愛擋咧(self):
        self.assertIsNone(臺灣閩南語羅馬字拼音附錄外來語('tsiòk').音標)
