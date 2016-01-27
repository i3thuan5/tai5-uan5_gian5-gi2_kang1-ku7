# -*- coding: utf-8 -*-
from unittest.case import TestCase
from unittest.mock import patch
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡


class 物件譀鏡單元試驗(TestCase):

    def setUp(self):
        self.物件 = 拆文分析器.轉做句物件('頭-家｜thau5-ke1 員-工｜uan5-kang1')

    @patch('臺灣言語工具.解析整理.物件譀鏡.物件譀鏡.看型')
    def test_看型(self, 看型mock):
        self.物件.看型()
        看型mock.assert_called_once_with(self.物件)

    def test_看音(self):
        self.物件.看音()

    def test_看分詞(self):
        self.物件.看分詞()

    def test_看音有參數(self):
        self.物件.看音()

    def test_轉音(self):
        self.物件.轉音()

    def test_轉音有參數(self):
        self.物件.轉音()
