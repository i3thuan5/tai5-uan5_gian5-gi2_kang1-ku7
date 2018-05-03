'''
Created on 2018年4月12日

@author: pigu
'''
import unittest
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from unittest.case import skip


@skip('暫時取消該功能')
class 臺羅轉白話字數字調單元試驗(unittest.TestCase):

    # 一律輸出小寫

    def test_大寫數字調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('Tsui2')
        self.assertEqual(拼音物件.轉白話字數字調(), 'chui2')

    def test_大寫傳統調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('Tsuí')
        self.assertEqual(拼音物件.轉白話字數字調(), 'chui2')

    @skip('TODO 待討論')
    def test_大寫輕聲(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('--Tsuí')
        self.assertEqual(拼音物件.轉白話字數字調(), '0chui2')

    def test_小寫數字調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('tsui2')
        self.assertEqual(拼音物件.轉白話字數字調(), 'chui2')

    def test_小寫傳統調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('tshuí')
        self.assertEqual(拼音物件.轉白話字數字調(), 'chhui2')

    @skip('TODO 待討論')
    def test_小寫輕聲(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('--tsuí')
        self.assertEqual(拼音物件.轉白話字數字調(), '0chui2')

    @skip('TODO 待討論')
    def test_小寫輕聲數字調(self):
        拼音物件 = 臺灣閩南語羅馬字拼音('0tsui2')
        self.assertEqual(拼音物件.轉白話字數字調(), '0chui2')

    def test_雙母音oa(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('ua5').轉白話字數字調(), 'oa5')
        self.assertEqual(臺灣閩南語羅馬字拼音('uan5').轉白話字數字調(), 'oan5')

    def test_三母音oai(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('kuai3').轉白話字數字調(), 'koai3')

    def test_三母音iau(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('iau7').轉白話字數字調(), 'iau7')

    def test_鼻化音nn(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('ainn1').轉白話字數字調(), 'aiⁿ1')

    def test_鼻化音nnh(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('ainnh4').轉白話字數字調(), 'aihⁿ4')

    def test_oo(self):
        # ó͘, ō͘,
        self.assertEqual(臺灣閩南語羅馬字拼音('hoo7').轉白話字數字調(), 'ho͘7')

    def test_優勢腔(self):
        self.assertEqual(臺灣閩南語羅馬字拼音('gio2').轉白話字數字調(), 'gio2')
        self.assertEqual(臺灣閩南語羅馬字拼音('au3').轉白話字數字調(), 'au3')
        self.assertEqual(臺灣閩南語羅馬字拼音('ainn7').轉白話字數字調(), 'aiⁿ7')
        self.assertEqual(臺灣閩南語羅馬字拼音('hah8').轉白話字數字調(), 'hah8')

#     def test_方言韻(self):
#         self.assertEqual(臺灣閩南語羅馬字拼音('tere5').轉白話字數字調(), 'terê')
#         self.assertEqual(臺灣閩南語羅馬字拼音('tir5').轉白話字數字調(), 'tîr')
#
#     def test_外來語佮輕聲(self):
#         # 符號予別的工具處理
#         self.assertEqual(臺灣閩南語羅馬字拼音('0tir5').轉白話字數字調(), '0tîr')
#         self.assertEqual(臺灣閩南語羅馬字拼音('1tir5').轉白話字數字調(), '1tîr')
