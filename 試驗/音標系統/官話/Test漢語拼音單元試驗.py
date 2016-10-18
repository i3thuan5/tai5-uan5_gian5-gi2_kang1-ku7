# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.音標系統.官話.官話注音符號 import 官話注音符號
from 臺灣言語工具.音標系統.官話.漢語拼音 import 漢語拼音


class 漢語拼音單元試驗(TestCase):

    def test_介音(self):
        注音 = 官話注音符號(漢語拼音('yi4').轉換到注音符號())
        self.assertEqual(注音.音標, 'ㄧˋ')
        self.assertEqual(注音.聲, '')
        self.assertEqual(注音.韻, 'ㄧ')
        self.assertEqual(注音.調, 'ˋ')
        self.assertEqual(注音.聲韻, 'ㄧ')

    def test_完整音(self):
        注音 = 官話注音符號(漢語拼音('chuan2').轉換到注音符號())
        self.assertEqual(注音.音標, 'ㄔㄨㄢˊ')
        self.assertEqual(注音.聲, 'ㄔ')
        self.assertEqual(注音.韻, 'ㄨㄢ')
        self.assertEqual(注音.調, 'ˊ')
        self.assertEqual(注音.聲韻, 'ㄔㄨㄢ')

    def test_一聲(self):
        注音 = 官話注音符號(漢語拼音('xue1').轉換到注音符號())
        self.assertEqual(注音.音標, 'ㄒㄩㄝ')
        self.assertEqual(注音.聲, 'ㄒ')
        self.assertEqual(注音.韻, 'ㄩㄝ')
        self.assertEqual(注音.調, '')
        self.assertEqual(注音.聲韻, 'ㄒㄩㄝ')

    def test_零聲母(self):
        注音 = 官話注音符號(漢語拼音('wo3').轉換到注音符號())
        self.assertEqual(注音.音標, 'ㄨㄛˇ')
        self.assertEqual(注音.聲, '')
        self.assertEqual(注音.韻, 'ㄨㄛ')
        self.assertEqual(注音.調, 'ˇ')
        self.assertEqual(注音.聲韻, 'ㄨㄛ')

    def test_ㄌㄩ(self):
        注音 = 官話注音符號(漢語拼音('lv4').轉換到注音符號())
        self.assertEqual(注音.音標, 'ㄌㄩˋ')
        self.assertEqual(注音.聲, 'ㄌ')
        self.assertEqual(注音.韻, 'ㄩ')
        self.assertEqual(注音.調, 'ˋ')
        self.assertEqual(注音.聲韻, 'ㄌㄩ')

    def test_輕聲(self):
        注音 = 官話注音符號(漢語拼音('ㄉㄜ˙').轉換到注音符號())
        self.assertEqual(注音.音標, 'ㄉㄜ˙')
        self.assertEqual(注音.聲, 'ㄉ')
        self.assertEqual(注音.韻, 'ㄜ')
        self.assertEqual(注音.調, '˙')
        self.assertEqual(注音.聲韻, 'ㄉㄜ')

    def test_空韻(self):
        注音 = 官話注音符號(漢語拼音('zi4').轉換到注音符號())
        self.assertEqual(注音.音標, 'ㄗ')
        self.assertEqual(注音.聲, 'ㄗ')
        self.assertEqual(注音.韻, '')
        self.assertEqual(注音.調, '')
        self.assertEqual(注音.聲韻, 'ㄗ')

    def test_無合法(self):
        self.assertEqual(漢語拼音('i4').轉換到注音符號(), None)

    def test_預設是注音符號(self):
        self.assertEqual(漢語拼音('duo3').預設音標(), 漢語拼音('duo3').轉換到注音符號())
