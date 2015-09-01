# -*- coding: utf-8 -*-
import unittest

from 臺灣言語工具.解析整理.羅馬音仕上げ import 羅馬音仕上げ


# 仕上げ
# しあげ
# ㄒㄧ˫ ㄚ ㆣㆤㆷ
# 1si7_1a1_1geh4


class 羅馬音仕上げ單元試驗(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        self.羅馬音仕上げ = 羅馬音仕上げ()
        self.assertEqual(
            self.羅馬音仕上げ.しあげ(self.原來語句), self.處理好語句)

    def test_轉大寫字(self):
        self.原來語句 = 'gua2 ai2 sui2 koo1-niu5!'
        self.處理好語句 = 'Gua2 ai2 sui2 koo1-niu5!'

    def test_轉外來語(self):
        self.原來語句 = '1ōo-1too-1bái-tiam3'
        self.處理好語句 = '*ōo-*too-*bái-tiam3'

    def test_轉輕聲(self):
        self.原來語句 = '0aih! bo5-0ki3 0ah4.'
        self.處理好語句 = '--aih! bo5--ki3--ah4.'

    def test_綜合(self):
        self.原來語句 = 'āu-piah ê 1ōo-1too-1bái-tiàm bô-khì-0ah!'
        self.處理好語句 = 'Āu-piah ê *ōo-*too-*bái-tiàm bô-khì--ah!'
