# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.語音合成.閩南語音韻規則 import 閩南語音韻規則


class 音韻規則單元試驗(TestCase):
    def tearDown(self):
        章物件 = (
            拆文分析器.對齊章物件(self.漢字, self.臺羅)
            .轉音(臺灣閩南語羅馬字拼音)
            .轉音(臺灣閩南語羅馬字拼音, 函式='音值')
        )
        結果 = 閩南語音韻規則.套用(章物件)
        for 字物件, 音值 in zip(結果.篩出字物件(), self.答案):
            self.assertEqual(字物件.音, 音值)

    def test_一句(self):
        self.漢字 = '我愛媠媠'
        self.臺羅 = 'gua2 ai3 sui2-sui2'
        self.答案 = [
            ('g', 'ua', '1'), ('ʔ', 'ai', '2'),
            ('s', 'ui', '1'), ('s', 'ui', '2')
        ]

    def test_兩句(self):
        self.漢字 = '我愛媠媠。我愛媠媠。'
        self.臺羅 = 'gua2 ai3 sui2-sui2 . gua2 ai3 sui2-sui2 .'
        self.答案 = [
            ('g', 'ua', '1'), ('ʔ', 'ai', '2'),
            ('s', 'ui', '1'), ('s', 'ui', '2'), (None,),
            ('g', 'ua', '1'), ('ʔ', 'ai', '2'),
            ('s', 'ui', '1'), ('s', 'ui', '2'), (None,),
        ]

    def test_井前無變調原本物件無變(self):
        self.漢字 = '我#愛媠媠'
        self.臺羅 = 'gua2 # ai3 sui2-sui2'
        self.答案 = [
            ('g', 'ua', '2'), ('ʔ', 'ai', '2'),
            ('s', 'ui', '1'), ('s', 'ui', '2')
        ]

    def test_欲毋是再變調(self):
        self.漢字 = '欲望'
        self.臺羅 = 'iok8-bong7'
        self.答案 = [
            ('ʔ', 'iok', '10'),  ('b', 'oŋ', '7')
        ]

    def test_第9調仔前變調(self):
        self.漢字 = '小khua9仔'
        self.臺羅 = 'sio2-khua9-a2'
        self.答案 = [
            ('s', 'iə', '1'),  ('kʰ', 'ua', '9'), ('ʔ', 'a', '2'),
        ]


class 音韻規則其他單元試驗(TestCase):
    def test_句物件(self):
        章物件 = (
            拆文分析器.對齊句物件('我愛媠媠', 'gua2 ai3 sui2-sui2')
            .轉音(臺灣閩南語羅馬字拼音)
            .轉音(臺灣閩南語羅馬字拼音, 函式='音值')
        )
        答案 = [
            ('g', 'ua', '1'), ('ʔ', 'ai', '2'),
            ('s', 'ui', '1'), ('s', 'ui', '2')
        ]
        結果 = 閩南語音韻規則.套用(章物件)
        for 字物件, 音值 in zip(結果.篩出字物件(), 答案):
            self.assertEqual(字物件.音, 音值)

    def test_原本物件無變(self):
        self.漢字 = '我#愛媠媠'
        self.臺羅 = 'gua2 # ai3 sui2-sui2'
        章物件 = (
            拆文分析器.對齊章物件(self.漢字, self.臺羅)
            .轉音(臺灣閩南語羅馬字拼音)
            .轉音(臺灣閩南語羅馬字拼音, 函式='音值')
        )
        閩南語音韻規則.套用(章物件)
        self.答案 = [
            ('g', 'ua', '2'), (None,), ('ʔ', 'ai', '3'),
            ('s', 'ui', '2'), ('s', 'ui', '2')
        ]
        for 字物件, 音值 in zip(章物件.篩出字物件(), self.答案):
            self.assertEqual(字物件.音, 音值)
