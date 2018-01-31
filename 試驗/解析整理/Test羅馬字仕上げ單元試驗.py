# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.羅馬字仕上げ import 羅馬字仕上げ
from unittest.case import TestCase

# 仕上げ
# しあげ
# ㄒㄧ˫ ㄚ ㆣㆤㆷ
# 1si7_1a1_1geh4


class 羅馬字仕上げ單元試驗(TestCase):

    def tearDown(self):
        self.assertEqual(
            羅馬字仕上げ.しあげ(self.原來語句), self.處理好語句, self.原來語句
        )

    def test_轉大寫字(self):
        self.原來語句 = 'gua2 ai2 sui2 koo1-niu5!'
        self.處理好語句 = 'Gua2 ai2 sui2 koo1-niu5!'

    def test_轉外來語(self):
        self.原來語句 = '1ōo-1too-1bái-tiam3'
        self.處理好語句 = '*ōo-*too-*bái-tiam3'

    def test_轉輕聲(self):
        self.原來語句 = 'Aih! bo5-0ki3 0ah4.'
        self.處理好語句 = 'Aih! Bo5--ki3--ah4.'

    def test_綜合(self):
        self.原來語句 = 'āu-piah ê 1ōo-1too-1bái-tiàm bô-khì-0ah!'
        self.處理好語句 = 'Āu-piah ê *ōo-*too-*bái-tiàm bô-khì--ah!'

    def test_一佮空開頭(self):
        self.原來語句 = '100 ê 000!'
        self.處理好語句 = '100 ê 000!'

    def test_孤一佮孤空(self):
        self.原來語句 = '1 ê 0'
        self.處理好語句 = '1 ê 0'

    def test_句首語助詞(self):
        self.原來語句 = '0ah!'
        self.處理好語句 = 'Ah!'

    def test_句頭攏愛大寫(self):
        self.原來語句 = 'sī . sī .'
        self.處理好語句 = 'Sī. Sī.'

    def test_標點符號頭前免空白(self):
        self.原來語句 = 'Hannh ? Sī--ooh .'
        self.處理好語句 = 'Hannh? Sī--ooh.'

    def test_第二句頭前愛閬格(self):
        self.原來語句 = 'Tsi̍t-tshing . 0hannh ?'
        self.處理好語句 = 'Tsi̍t-tshing. Hannh?'

    def test_攏是減號(self):
        self.原來語句 = '------'
        self.處理好語句 = '------'
