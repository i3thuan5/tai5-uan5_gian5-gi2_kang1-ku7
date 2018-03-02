# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 拆文分析器斷詞單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.建立句物件(self.語句)
        self.assertEqual(len(句物件.網出詞物件()), self.詞數)

    def test_全羅看有黏做伙無決定斷詞(self):
        self.語句 = 'Guan2 tsit4-ma2'
        self.詞數 = 2

    def test_全羅輕聲看有黏做伙無決定斷詞(self):
        self.語句 = 'Mi̍h-kiānn phah-bô--khì --ah'
        self.詞數 = 3

    def test_漢字看有黏做伙無決定斷詞(self):
        self.語句 = '媠 姑娘'
        self.詞數 = 2

    def test_漢字輕聲就當作無仝詞(self):
        self.語句 = '好 --矣'
        self.詞數 = 2

    def test_漢字知影有輕聲猶原一個詞(self):
        self.語句 = '害--矣--啦'
        self.詞數 = 1

    def test_句中輕聲無連做伙嘛會使(self):
        self.語句 = '講會出--來'
        self.詞數 = 1

    def test_句中輕聲kah4後壁無連做伙嘛會使(self):
        self.語句 = '講--出-來'
        self.詞數 = 1

    def test_組字當作漢字(self):
        self.語句 = '癩⿸疒哥人'

        self.詞數 = 1

    def test_漢羅做伙(self):
        self.語句 = '台文通訊Bóng報'

        self.詞數 = 1

    def test_漢羅輕聲(self):
        self.語句 = '阿菊姨--a7'
        self.詞數 = 1

    def test_標點愛分開(self):
        self.語句 = '「白話字」'
        self.詞數 = 3

    def test_有連字符就認連字符(self):
        self.語句 = '無-？-bo5-?'
        self.詞數 = 1
