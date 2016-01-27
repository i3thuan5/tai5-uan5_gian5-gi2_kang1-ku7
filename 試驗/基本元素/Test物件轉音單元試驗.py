# -*- coding: utf-8 -*-
from unittest.case import TestCase
from unittest.mock import patch
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.基本元素.公用變數 import 分字符號
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤


class 物件轉音單元試驗(TestCase):

    @patch('臺灣言語工具.基本元素.句.句.看型')
    def test_轉音(self):
        self.物件.轉音()

    @patch('臺灣言語工具.基本元素.句.句.看型')
    def test_轉音有參數(self):
        self.物件.轉音()
