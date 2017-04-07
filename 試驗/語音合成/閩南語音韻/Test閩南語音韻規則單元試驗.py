# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 閩南語音韻規則單元試驗(TestCase):

    def test_一句(self):
        章物件 = self.產生套用前物件('我愛媠媠', 'gua2 ai3 sui2-sui2')
        答案 = [
            ('g', 'ua', '1'), ('ʔ', 'ai', '2'),
            ('s', 'ui', '1'), ('s', 'ui', '2')
        ]
        結果 = 閩南語音韻規則.套用(章物件)
        for 字物件, 音值 in zip(結果, 答案):
            self.assertEqual(字物件.音, 音值)

    def test_兩句(self):
        章物件 = self.產生套用前物件(
            '我愛媠媠。我愛媠媠。',
            'gua2 ai3 sui2-sui2 . gua2 ai3 sui2-sui2 .'
        )
        答案 = [
            ('g', 'ua', '1'), ('ʔ', 'ai', '2'),
            ('s', 'ui', '1'), ('s', 'ui', '2'), (None,),
            ('g', 'ua', '1'), ('ʔ', 'ai', '2'),
            ('s', 'ui', '1'), ('s', 'ui', '2'), (None,),
        ]
        結果 = 閩南語音韻規則.套用(章物件)
        for 字物件, 音值 in zip(結果, 答案):
            self.assertEqual(字物件.音, 音值)

    def test_井前無變調原本物件無變(self):
        章物件 = self.產生套用前物件('我#愛媠媠', 'gua2 # ai3 sui2-sui2')
        答案 = [
            ('g', 'ua', '2'), ('ʔ', 'ai', '2'),
            ('s', 'ui', '1'), ('s', 'ui', '2')
        ]
        結果 = 閩南語音韻規則.套用(章物件)
        for 字物件, 音值 in zip(結果, 答案):
            self.assertEqual(字物件.音, 音值)

    def 產生套用前物件(self, 漢字, 臺羅):
        return (
            拆文分析器.對齊章物件(漢字, 臺羅)
            .轉音(臺灣閩南語羅馬字拼音)
            .轉音(臺灣閩南語羅馬字拼音, 函式='音值')
        )
