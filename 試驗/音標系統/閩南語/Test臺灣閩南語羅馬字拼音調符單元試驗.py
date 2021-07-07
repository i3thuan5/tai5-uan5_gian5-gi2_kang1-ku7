# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 臺灣閩南語羅馬字拼音調符單元試驗(TestCase):

    def test_大寫數字調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('Sui2')
        self.assertEqual(拼音物件.轉調符(), 'Suí')

    def test_大寫傳統調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('Suí')
        self.assertEqual(拼音物件.轉調符(), 'Suí')

    def test_大寫輕聲(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('0Suí')
        self.assertEqual(拼音物件.轉調符(), '0Suí')

    def test_小寫數字調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('sui2')
        self.assertEqual(拼音物件.轉調符(), 'suí')

    def test_小寫傳統調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('suí')
        self.assertEqual(拼音物件.轉調符(), 'suí')

    def test_小寫輕聲(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('0suí')
        self.assertEqual(拼音物件.轉調符(), '0suí')

    def test_無正確(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('suii')
        self.assertEqual(拼音物件.轉調符(), None)

    def test_優勢腔(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('ainn7').轉調符(), 'āinn')
        self.assertEqual(臺灣閩南語羅馬字拼音('ang3').轉調符(), 'àng')
        self.assertEqual(臺灣閩南語羅馬字拼音('au3').轉調符(), 'àu')
        self.assertEqual(臺灣閩南語羅馬字拼音('mng5').轉調符(), 'mn̂g')
        self.assertEqual(臺灣閩南語羅馬字拼音('gio2').轉調符(), 'gió')
        self.assertEqual(臺灣閩南語羅馬字拼音('hiunnh8').轉調符(), 'hiu̍nnh')
        self.assertEqual(臺灣閩南語羅馬字拼音('moo5').轉調符(), 'môo')

    def test_方言韻(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('tere5').轉調符(), 'terê')
        self.assertEqual(臺灣閩南語羅馬字拼音('tir5').轉調符(), 'tîr')

    def test_外來語佮輕聲(self):
        # 符號予別的工具處理
        self.assertEqual(臺灣閩南語羅馬字拼音('0tir5').轉調符(), '0tîr')
