# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡


class 物件譀鏡單元試驗(unittest.TestCase):

    def setUp(self):
        self.物件 = 拆文分析器.轉做句物件('頭-家｜thau5-ke1 員-工｜uan5-kang1')

    @patch('臺灣言語工具.基本元素.句.句.看型')
    def test_看型(self, 看型mock):
        物件譀鏡.看型(self.物件)
        看型mock.assert_called_once_with(
            物件分字符號='', 物件分詞符號='', 物件分句符號=''
        )

    @patch('臺灣言語工具.基本元素.句.句.看音')
    def test_看音(self, 看音mock):
        物件譀鏡.看音(self.物件)
        看音mock.assert_called_once_with(
            物件分字符號='-', 物件分詞符號=' ', 物件分句符號=' '
        )

    @patch('臺灣言語工具.基本元素.句.句.看音')
    def test_看音有參數(self, 看音mock):
        物件譀鏡.看音(self.物件, '_', '|', '^')
        看音mock.assert_called_once_with(
            物件分字符號='_', 物件分詞符號='|', 物件分句符號='^'
        )

    @patch('臺灣言語工具.基本元素.句.句.看分詞')
    def test_看分詞(self, 看分詞mock):
        物件譀鏡.看分詞(self.物件)
        看分詞mock.assert_called_once_with(
            物件分型音符號='｜', 物件分字符號='-', 物件分詞符號=' ', 物件分句符號=' ',
        )

    @patch('臺灣言語工具.基本元素.句.句.看分詞')
    def test_看分詞有參數(self, 看分詞mock):
        物件譀鏡.看分詞(self.物件, 物件分字符號='_', 物件分詞符號='|', 物件分句符號='^')
        看分詞mock.assert_called_once_with(
            物件分型音符號='｜', 物件分字符號='_', 物件分詞符號='|', 物件分句符號='^'
        )

    def test_參數烏白傳(self):
        self.assertRaises(AttributeError, 物件譀鏡.看型, 790830)
        self.assertRaises(AttributeError, 物件譀鏡.看音, None)
        self.assertRaises(AttributeError, 物件譀鏡.看分詞, '｜', '｜')
