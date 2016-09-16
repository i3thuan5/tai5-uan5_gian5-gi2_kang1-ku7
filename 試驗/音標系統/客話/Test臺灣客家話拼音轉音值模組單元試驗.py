# -*- coding: utf-8 -*-
import unittest
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音轉音值模組 import 臺灣客家話拼音對照音值聲母表
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音轉音值模組 import 臺灣客家話拼音對照音值韻母表
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音聲母對照表
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音韻母對照表


class 臺灣客家話拼音轉音值模組單元試驗(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_定看音標(self):
        self.assertEqual(臺灣客家話拼音('er').音值(), ('ʔ', 'ə', ''))
        self.assertEqual(臺灣客家話拼音('imˊ').音值(), ('ʔ', 'im', 'ˊ'))
        self.assertEqual(臺灣客家話拼音('iongˇ').音值(), ('ʔ', 'ioŋ', 'ˇ'))
        self.assertEqual(臺灣客家話拼音('giangˊ').音值(), ('k', 'iaŋ', 'ˊ'))
        self.assertEqual(臺灣客家話拼音('zauˊ').音值(), ('ts', 'au', 'ˊ'))
        self.assertEqual(臺灣客家話拼音('caˋ').音值(), ('tsʰ', 'a', 'ˋ'))
        self.assertEqual(臺灣客家話拼音('pon+').音值(), ('pʰ', 'on', '+'))
        self.assertEqual(臺灣客家話拼音('ng').音值(), ('ʔ', 'ŋ̩', ''))
        self.assertEqual(臺灣客家話拼音('ngiˋ').音值(), ('ȵ', 'i', 'ˋ'))
        self.assertEqual(臺灣客家話拼音('mug').音值(), ('m', 'uk', ''))
        self.assertEqual(臺灣客家話拼音('ngedˋ').音值(), ('ŋ', 'et', 'ˋ'))
        self.assertEqual(臺灣客家話拼音('ngin').音值(), ('ȵ', 'in', ''))
        self.assertEqual(臺灣客家話拼音('tongˋ').音值(), ('tʰ', 'oŋ', 'ˋ'))
        self.assertEqual(臺灣客家話拼音('bainnˋ').音值(), ('p', 'aⁿiⁿ', 'ˋ'))

    def test_大寫音標(self):
        self.assertEqual(臺灣客家話拼音('JIANGˊ').音值(), ('tɕ', 'iaŋ', 'ˊ'))
        self.assertEqual(臺灣客家話拼音('Jiangˊ').音值(), ('tɕ', 'iaŋ', 'ˊ'))

    def test_違法音標(self):
        self.assertEqual(臺灣客家話拼音('nged^').音值(), (None,))

    def test_其他違法音標(self):
        self.assertEqual(臺灣客家話拼音('@@').音值(), (None,))
        self.assertEqual(臺灣客家話拼音('pe̍m').音值(), (None,))
        self.assertEqual(臺灣客家話拼音('xxtsé--á').音值(), (None,))
        self.assertEqual(臺灣客家話拼音('óonn').音值(), (None,))
        self.assertEqual(臺灣客家話拼音('Jiumˊ').音值(), (None,))

    def test_全部攏會使產生方音物件(self):
        for 母 in 臺灣客家話拼音聲母對照表:
            self.assertIn(母, 臺灣客家話拼音對照音值聲母表)
        for 母 in 臺灣客家話拼音韻母對照表:
            self.assertIn(母, 臺灣客家話拼音對照音值韻母表)

    def test_鼻化韻逐个元音攏愛有鼻化(self):
        for 韻 in 臺灣客家話拼音對照音值韻母表.values():
            for 切 in 韻.split('ⁿ')[:-1]:
                self.assertEqual(len(切), 1, '{}有問題'.format(韻))
