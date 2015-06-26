# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.音標系統.官話.官話注音符號 import 官話注音符號


class 官話注音符號單元試驗(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

# ---------------------------------------------

    def test_介音(self):
        注音 = 官話注音符號('ㄧˋ')
        self.assertEqual(注音.音標, 'ㄧˋ')
        self.assertEqual(注音.聲, '')
        self.assertEqual(注音.韻, 'ㄧ')
        self.assertEqual(注音.調, 'ˋ')
        self.assertEqual(注音.聲韻, 'ㄧ')

    def test_完整音(self):
        注音 = 官話注音符號('ㄔㄨㄢˊ')
        self.assertEqual(注音.音標, 'ㄔㄨㄢˊ')
        self.assertEqual(注音.聲, 'ㄔ')
        self.assertEqual(注音.韻, 'ㄨㄢ')
        self.assertEqual(注音.調, 'ˊ')
        self.assertEqual(注音.聲韻, 'ㄔㄨㄢ')

    def test_一聲(self):
        注音 = 官話注音符號('ㄒㄩㄝ')
        self.assertEqual(注音.音標, 'ㄒㄩㄝ')
        self.assertEqual(注音.聲, 'ㄒ')
        self.assertEqual(注音.韻, 'ㄩㄝ')
        self.assertEqual(注音.調, '')
        self.assertEqual(注音.聲韻, 'ㄒㄩㄝ')

    def test_零聲母(self):
        注音 = 官話注音符號('ㄨㄛˇ')
        self.assertEqual(注音.音標, 'ㄨㄛˇ')
        self.assertEqual(注音.聲, '')
        self.assertEqual(注音.韻, 'ㄨㄛ')
        self.assertEqual(注音.調, 'ˇ')
        self.assertEqual(注音.聲韻, 'ㄨㄛ')

    def test_輕聲(self):
        注音 = 官話注音符號('ㄉㄜ˙')
        self.assertEqual(注音.音標, 'ㄉㄜ˙')
        self.assertEqual(注音.聲, 'ㄉ')
        self.assertEqual(注音.韻, 'ㄜ')
        self.assertEqual(注音.調, '˙')
        self.assertEqual(注音.聲韻, 'ㄉㄜ')

    def test_輕聲頭前(self):
        注音 = 官話注音符號('˙ㄉㄜ')
        self.assertEqual(注音.音標, 'ㄉㄜ˙')
        self.assertEqual(注音.聲, 'ㄉ')
        self.assertEqual(注音.韻, 'ㄜ')
        self.assertEqual(注音.調, '˙')
        self.assertEqual(注音.聲韻, 'ㄉㄜ')

    def test_空韻(self):
        注音 = 官話注音符號('ㄗ')
        self.assertEqual(注音.音標, 'ㄗ')
        self.assertEqual(注音.聲, 'ㄗ')
        self.assertEqual(注音.韻, '')
        self.assertEqual(注音.調, '')
        self.assertEqual(注音.聲韻, 'ㄗ')

    def test_無合法(self):
        self.assertEqual(官話注音符號('ㄆㄢ').音標, 'ㄆㄢ')
        self.assertEqual(官話注音符號('ㄆㄢ+').音標, None)
        self.assertEqual(官話注音符號('ㄗㄧㄨ').音標, None)
        self.assertEqual(官話注音符號('ㄐ').音標, None)
        self.assertEqual(官話注音符號('').音標, None)
        self.assertEqual(官話注音符號('Ⅹㄛˇ').音標, None)  # 怪怪的「ㄨ」
