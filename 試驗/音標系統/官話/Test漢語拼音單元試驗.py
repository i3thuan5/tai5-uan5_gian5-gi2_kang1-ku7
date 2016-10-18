# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.音標系統.官話.漢語拼音 import 漢語拼音


class 漢語拼音單元試驗(TestCase):

    def test_介音(self):
        self.assertEqual(漢語拼音('yi4').轉換到注音符號(), 'ㄧˋ')

    def test_完整音(self):
        self.assertEqual(漢語拼音('chuan2').轉換到注音符號(), 'ㄔㄨㄢˊ')

    def test_音位(self):
        self.assertEqual(漢語拼音('quan4').轉換到注音符號(), 'ㄑㄩㄢˋ')

    def test_一聲(self):
        self.assertEqual(漢語拼音('xue1').轉換到注音符號(), 'ㄒㄩㄝ')

    def test_零聲母(self):
        self.assertEqual(漢語拼音('wo3').轉換到注音符號(), 'ㄨㄛˇ')

    def test_ㄌㄩ(self):
        self.assertEqual(漢語拼音('lv4').轉換到注音符號(), 'ㄌㄩˋ')

    def test_輕聲(self):
        self.assertEqual(漢語拼音('zuo5').轉換到注音符號(), 'ㄗㄨㄛ˙')

    def test_空韻(self):
        self.assertEqual(漢語拼音('zi3').轉換到注音符號(), 'ㄗˇ')

    def test_無合法(self):
        self.assertEqual(漢語拼音('i4').轉換到注音符號(), None)

    def test_預設是注音符號(self):
        self.assertEqual(漢語拼音('duo3').預設音標(), 漢語拼音('duo3').轉換到注音符號())
