# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 物件轉字串整合試驗(TestCase):

    def tearDown(self):
        物件 = 拆文分析器.建立句物件(self.語句)
        self.assertEqual(物件.看語句(), self.語句)

    def test_漢羅(self):
        self.語句 = '欲lia̍h-ti!'

    def test_漢字輕聲(self):
        self.語句 = '--啊'

    def test_羅馬字輕聲(self):
        self.語句 = '--ah'

    def test_漢字濟字輕聲(self):
        self.語句 = '緊--出-來'

    def test_羅馬字濟字輕聲(self):
        self.語句 = 'Kín--tshut-lâi'
