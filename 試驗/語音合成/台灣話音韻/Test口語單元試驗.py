# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.語音合成.閩南語音韻規則 import 閩南語音韻規則


class 口語單元試驗(TestCase):
    def tearDown(self):
        句物件 = (
            拆文分析器.對齊句物件(self.漢字, self.臺羅)
            .轉音(臺灣閩南語羅馬字拼音)
            .轉音(臺灣閩南語羅馬字拼音, 函式='音值')
        )
        self.assertEqual(台灣話口語規則.走(句物件).看語句(), self.答案)

    def test_一句(self):
        self.漢字 = '我愛媠媠'
        self.臺羅 = 'guá ài suí-suí'
        self.答案 = 'gua1 ʔai2 sui1-sui2'

    def test_標點(self):
        self.漢字 = '我愛媠媠。我愛媠媠。'
        self.臺羅 = 'guá ài suí-suí. guá ài suí-suí.'
        self.答案 = 'gua1 ʔai2 sui1-sui2. gua1 ʔai2 sui1-sui2.'

    def test_井前無變調原本物件無變(self):
        self.漢字 = '我#愛媠媠'
        self.臺羅 = 'guá # ài suí-suí'
        self.答案 = 'gua2 ʔai2 sui1-sui2'
