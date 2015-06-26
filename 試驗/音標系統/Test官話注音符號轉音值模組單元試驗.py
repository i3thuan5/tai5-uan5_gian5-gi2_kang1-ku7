# -*- coding: utf-8 -*-
import unittest
from 臺灣言語工具.音標系統.官話.官話注音符號 import 官話注音符號
from 臺灣言語工具.音標系統.官話.官話注音符號 import 官話注音符號聲
from 臺灣言語工具.音標系統.官話.官話注音符號 import 官話注音符號韻
from 臺灣言語工具.音標系統.官話.官話注音符號轉音值模組 import 官話注音符號對照音值聲母表
from 臺灣言語工具.音標系統.官話.官話注音符號轉音值模組 import 官話注音符號對照音值韻母表


class 官話注音符號轉音值模組單元試驗(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_單音(self):
        self.assertEqual(官話注音符號('ㄧˋ').音值(), ('ʔ', 'i', 'ˋ'))

    def test_三符號有調(self):
        self.assertEqual(官話注音符號('ㄔㄨㄢˊ').音值(), ('tʂʰ', 'uan', 'ˊ'))

    def test_三符號無調(self):
        self.assertEqual(官話注音符號('ㄒㄩㄝ').音值(), ('ɕ', 'ye', ''))

    def test_無聲(self):
        self.assertEqual(官話注音符號('ㄨㄟˇ').音值(), ('ʔ', 'uei', 'ˇ'))

    def test_輕聲(self):
        self.assertEqual(官話注音符號('ㄉㄜ˙').音值(), ('t', 'ɤ', '˙'))

    def test_空韻(self):
        self.assertEqual(官話注音符號('ㄗ').音值(), ('ts', 'ɿ', ''))
        self.assertEqual(官話注音符號('ㄓ').音值(), ('tʂ', 'ʅ', ''))
        self.assertEqual(官話注音符號('ㄖˋ').音值(), ('ʐ', 'ʅ', 'ˋ'))

    def test_喔我婆(self):
        self.assertEqual(官話注音符號('ㄛ').音值(), ('ʔ', 'o', ''))
        self.assertEqual(官話注音符號('ㄨㄛˇ').音值(), ('ʔ', 'uo', 'ˇ'))
        self.assertEqual(官話注音符號('ㄆㄛˊ').音值(), ('pʰ', 'uo', 'ˊ'))

    def test_翁東(self):
        self.assertEqual(官話注音符號('ㄨㄥ').音值(), ('ʔ', 'uŋ', ''))
        self.assertEqual(官話注音符號('ㄉㄨㄥ').音值(), ('t', 'oŋ', ''))

    def test_生風(self):
        self.assertEqual(官話注音符號('ㄕㄥ').音值(), ('ʂ', 'əŋ', ''))
        self.assertEqual(官話注音符號('ㄈㄥ').音值(), ('f', 'oŋ', ''))

    def test_無合法(self):
        self.assertEqual(官話注音符號('ㄗㄧㄨ').音值(), (None,))
        self.assertEqual(官話注音符號('').音值(), (None,))

    def test_全部攏會使產生方音物件(self):
        for 母 in 官話注音符號聲:
            self.assertIn(母, 官話注音符號對照音值聲母表)
        for 母 in 官話注音符號韻:
            self.assertIn(母, 官話注音符號對照音值韻母表)
