# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 音標敢著單元試驗(TestCase):

    def test_著的音標(self):
        字物件 = 字('媠', 'sui2')
        self.assertTrue(字物件.音標敢著(臺灣閩南語羅馬字拼音))

    def test_毋著的音標(self):
        字物件 = 字('媠', 'sui4')
        self.assertFalse(字物件.音標敢著(臺灣閩南語羅馬字拼音))

    def test_無音(self):
        字物件 = 字('媠', '')
        self.assertTrue(字物件.音標敢著(臺灣閩南語羅馬字拼音))

    def test_注音符號(self):
        字物件 = 字('！', '!')
        self.assertTrue(字物件.音標敢著(臺灣閩南語羅馬字拼音))

    def test_句物件(self):
        句物件 = 拆文分析器.對齊句物件('點仔膠，黏著跤，', 'tiam2 a2 ka1, liam5 tioh8 kha1,')
        self.assertTrue(句物件.音標敢著(臺灣閩南語羅馬字拼音))

    def test_句物件有音毋著(self):
        句物件 = 拆文分析器.對齊句物件('點仔膠，黏著跤，', 'tiam2 a2 ka1, liam5 tioh8 kha4,')
        self.assertFalse(句物件.音標敢著(臺灣閩南語羅馬字拼音))
