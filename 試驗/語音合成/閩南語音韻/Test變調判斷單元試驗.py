# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.語音合成.閩南語變調 import 閩南語變調
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.公用變數 import 標點符號
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 變調判斷單元試驗(TestCase):
    愛檢查的 = [
        ('句尾變調', '我愛媠媠 #', 'gua2 ai3 sui2-sui2 #'),
    ]

    def test_檢查本調(self):
        for 名, 漢字, 臺羅 in self.愛檢查的:
            輸入物件 = self.產生套用前物件(漢字.replace('#', ''), 臺羅.replace('#', ''))
            結果 = 變調判斷.判斷(輸入物件)
            答案字陣列 = self.產生套用前物件(漢字, 臺羅).篩出字陣列()

            這馬答案 = len(答案字陣列) - 1
            這馬結果 = len(結果) - 1
            while 這馬答案 >= 0:
                if 變調判斷.是井號(答案字陣列[這馬答案]):
                    self.assertEqual(結果[這馬結果], 維持本調)
                    這馬答案 -= 2
                else:
                    self.assertNotEqual(結果[這馬結果], 維持本調)
                    這馬答案 -= 1
                這馬結果 -= 1
            self.assertLess(這馬結果, 0)

    def test_句尾變調(self):
        章物件 = self.產生套用前物件('我愛媠媠', 'gua2 ai3 sui2-sui2')
        self.assertEqual(
            變調判斷.判斷(章物件),
            [實詞變調, 實詞變調, 實詞變調, 維持本調]
        )

    def test_仝詞攏輕聲(self):
        章物件 = self.產生套用前物件('我愛媠媠', 'gua2 ai3 0sui2-sui2')
        self.assertEqual(
            變調判斷.判斷(章物件),
            [實詞變調, 實詞變調, 實詞變調, 維持本調, '愛閣確定']
        )

    def test_的前無變調(self):
        章物件 = self.產生套用前物件(
            '我上愛媠媠的姑娘',
            'gua2 siong7 ai3 sui2-sui2 e5 koo1-niu5'
        )
        self.assertEqual(
            變調判斷.判斷(章物件),
            [實詞變調, 實詞變調, 實詞變調, 實詞變調, 維持本調, 實詞變調, 實詞變調, 維持本調]
        )

    def test_的前代名詞變調(self):
        章物件 = self.產生套用前物件(
            '我的媠媠',
            'gua2 e5 sui2-sui2'
        )
        self.assertEqual(
            變調判斷.判斷(章物件),
            [實詞變調, 實詞變調, 實詞變調, 維持本調]
        )

    def test_的前代名詞變調原本物件無變(self):
        原本 = 拆文分析器.建立句物件('我的媠媠')
        self._設定音值(原本,
                   [('g', 'ua', '2'), ('ʔ', 'e', '5'),
                    ('s', 'ui', '2'), ('s', 'ui', '2'), ])
        原本物件 = 句(原本.內底集)
        閩南語變調.變調(原本)
        self.assertEqual(原本, 原本物件)

    def test_井前無變調(self):
        章物件 = self.產生套用前物件('我#愛媠媠', 'gua2 # ai3 sui2-sui2')
        self.assertEqual(
            變調判斷.判斷(章物件),
            [維持本調, 愛提掉的, 實詞變調, 實詞變調, 維持本調]
        )

    def test_標點符號句尾變調(self):
        章物件 = self.產生套用前物件('我愛媠媠。', 'gua2 ai3 sui2-sui2 .')
        self.assertEqual(
            變調判斷.判斷(章物件),
            [維持本調, 實詞變調, 實詞變調, 維持本調, 標點符號]
        )

    def 產生套用前物件(self, 漢字, 臺羅):
        return (
            拆文分析器.對齊章物件(漢字, 臺羅)
            .轉音(臺灣閩南語羅馬字拼音)
            .轉音(臺灣閩南語羅馬字拼音, 函式='音值')
        )
