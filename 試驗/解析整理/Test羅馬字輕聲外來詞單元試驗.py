# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.羅馬字仕上げ import 羅馬字仕上げ

# 仕上げ
# しあげ
# ㄒㄧ˫-ㄚ-ㆣㆤㆷ
# 1si7_1a1_1geh4
# *sī-*a-*geh
# sī-a-geh


class 羅馬字仕上げ單元試驗(TestCase):

    def tearDown(self):
        self.assertEqual(
            羅馬字仕上げ.輕聲佮外來語(self.原來語句), self.處理好語句, self.原來語句
        )

    def test_一般語句(self):
        self.原來語句 = 'gua2 ai2 sui2 koo1-niu5!'
        self.處理好語句 = 'gua2 ai2 sui2 koo1-niu5!'

    def test_轉外來語(self):
        self.原來語句 = '1ōo-1too-1bái-tiam3'
        self.處理好語句 = '*ōo-*too-*bái-tiam3'

    def test_轉輕聲(self):
        self.原來語句 = '0aih! bo5-0ki3 0ah4.'
        self.處理好語句 = '--aih! bo5--ki3 --ah4.'

    def test_綜合(self):
        self.原來語句 = 'āu-piah ê 1ōo-1too-1bái-tiàm bô-khì-0ah!'
        self.處理好語句 = 'āu-piah ê *ōo-*too-*bái-tiàm bô-khì--ah!'

    def test_一佮空開頭(self):
        self.原來語句 = '100 ê 000!'
        self.處理好語句 = '100 ê 000!'

    def test_孤一佮孤空(self):
        self.原來語句 = '1 ê 0 !'
        self.處理好語句 = '1 ê 0 !'
