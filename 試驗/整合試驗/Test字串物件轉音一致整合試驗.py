# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 字串物件轉音一致整合試驗(TestCase):

    def tearDown(self):
        ku = 拆文分析器.建立句物件(self.語句)
        物件 = ku.轉音(臺灣閩南語羅馬字拼音, '轉調符')
        self.assertEqual(物件.看語句(), self.答案)

    def test_羅馬字(self):
        self.語句 = 'kin2--tshut4-lai5'
        self.答案 = 'kín--tshut-lâi'

    def test_大寫羅馬字(self):
        self.語句 = 'Kin2--tshut4-lai5'
        self.答案 = 'Kín--tshut-lâi'
