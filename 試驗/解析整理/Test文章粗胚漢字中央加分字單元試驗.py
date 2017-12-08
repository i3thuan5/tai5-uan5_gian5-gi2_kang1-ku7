# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚


class 文章粗胚處理減號單元試驗(TestCase):

    def test_漢字中央加分字(self):
        原來語句 = '因為 你 足媠 的 ， 所以 我'
        處理好語句 = '因-為 你 足-媠 的 ， 所-以 我'
        self.assertEqual(
            文章粗胚.漢字中央加分字符號(原來語句),
            處理好語句
        )

    def test_注音中央莫加分字(self):
        原來語句 = '媠ㄙㄨㄧˋ ㄋㄧㄛ'
        處理好語句 = '媠-ㄙㄨㄧˋ ㄋㄧㄛ'
        self.assertEqual(
            文章粗胚.漢字中央加分字符號(原來語句),
            處理好語句
        )

    def test_hiragana(self):
        原來語句 = 'アルミ'
        處理好語句 = 'ア-ル-ミ'
        self.assertEqual(
            文章粗胚.漢字中央加分字符號(原來語句),
            處理好語句
        )

    def test_katakana(self):
        原來語句 = 'まんが'
        處理好語句 = 'ま-ん-が'
        self.assertEqual(
            文章粗胚.漢字中央加分字符號(原來語句),
            處理好語句
        )

    def test_hiragana佮漢字(self):
        原來語句 = 'じゃん拳'
        處理好語句 = 'じ-ゃ-ん-拳'
        self.assertEqual(
            文章粗胚.漢字中央加分字符號(原來語句),
            處理好語句
        )
