# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 臺灣閩南語羅馬字拼音閏號單元試驗(TestCase):

    def test_大寫數字調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('Sui2')
        self.assertEqual(拼音物件.轉閏號調(), 'Suí')

    def test_大寫傳統調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('Suí')
        self.assertEqual(拼音物件.轉閏號調(), 'Suí')

    def test_大寫輕聲(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('0Suí')
        self.assertEqual(拼音物件.轉閏號調(), '0Suí')

    def test_小寫數字調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('sui2')
        self.assertEqual(拼音物件.轉閏號調(), 'suí')

    def test_小寫傳統調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('suí')
        self.assertEqual(拼音物件.轉閏號調(), 'suí')

    def test_小寫輕聲(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('0suí')
        self.assertEqual(拼音物件.轉閏號調(), '0suí')
