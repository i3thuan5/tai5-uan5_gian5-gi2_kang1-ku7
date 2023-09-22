# -*- coding: utf-8 -*-
from unittest.case import TestCase
from unittest.mock import patch
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.斷詞.語言模型揀集內組 import 語言模型揀集內組
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
from 臺灣言語工具.辭典.型音辭典 import 型音辭典
from 臺灣言語工具.斷詞.上長詞優先辭典揣詞 import 上長詞優先辭典揣詞
from 臺灣言語工具.辭典.現掀辭典 import 現掀辭典
from 臺灣言語工具.辭典.尾字辭典 import 尾字辭典
from 臺灣言語工具.斷詞.尾字辭典揣詞 import 尾字辭典揣詞
from 臺灣言語工具.斷詞.辭典語言模型斷詞 import 辭典語言模型斷詞
from 臺灣言語工具.解析整理.座標揀集內組 import 座標揀集內組
from 臺灣言語工具.語言模型.實際語言模型 import 實際語言模型
from 臺灣言語工具.解析整理.集內組照排 import 集內組照排


class 物件處理單元試驗(TestCase):

    def setUp(self):
        self.物件 = 拆文分析器.分詞句物件('頭-家｜thau5-ke1 員-工｜uan5-kang1')

    @patch('臺灣言語工具.解析整理.集內組照排.集內組照排.排')
    def test_集內組照排無名參數(self, 排mock):
        def 比字串(物件):
            return 物件
        # 這功能無定用，先用做的
        self.物件.做(集內組照排, '排', 比字串)
        排mock.assert_called_once_with(比字串, 物件=self.物件)

    @patch('臺灣言語工具.解析整理.集內組照排.集內組照排.排')
    def test_集內組照排有名參數(self, 排mock):
        def 比字串(物件):
            return 物件
        # 這功能無定用，先用做的
        self.物件.做(集內組照排, '排', 排法=比字串)
        排mock.assert_called_once_with(排法=比字串, 物件=self.物件)

    @patch('臺灣言語工具.解析整理.座標揀集內組.座標揀集內組.揀')
    def test_座標揀集內組(self, 揀mock):
        #         self.物件.揀(座標揀集內組)
        self.物件.揀(座標揀集內組, 集選擇=[0])
        揀mock.assert_called_once_with(集選擇=[0], 物件=self.物件)

    @patch('臺灣言語工具.斷詞.語言模型揀集內組.語言模型揀集內組.揀')
    def test_實際語言模型揀集內組(self, 揀mock):
        語言模型 = 實際語言模型(1)
        self.物件.揀(語言模型揀集內組, 語言模型=語言模型)
        揀mock.assert_called_once_with(語言模型=語言模型, 物件=self.物件)

    @patch('臺灣言語工具.斷詞.拄好長度辭典揣詞.拄好長度辭典揣詞.揣詞')
    def test_常用辭典揣詞(self, 揣詞mock):
        辭典 = 型音辭典(2)
        self.物件.揣詞(拄好長度辭典揣詞, 辭典)
        揣詞mock.assert_called_once_with(辭典, 物件=self.物件)

    @patch('臺灣言語工具.斷詞.上長詞優先辭典揣詞.上長詞優先辭典揣詞.揣詞')
    def test_其他辭典揣詞(self, 揣詞mock):
        辭典 = 現掀辭典(2)
        self.物件.揣詞(上長詞優先辭典揣詞, 辭典)
        揣詞mock.assert_called_once_with(辭典, 物件=self.物件)

    @patch('臺灣言語工具.斷詞.上長詞優先辭典揣詞.上長詞優先辭典揣詞.揣詞')
    def test_尾字辭典揣詞(self, 揣詞mock):
        辭典 = 尾字辭典(型音辭典)(2)
        self.物件.揣詞(尾字辭典揣詞(上長詞優先辭典揣詞), 辭典)
        揣詞mock.assert_called_once_with(辭典, 物件=self.物件)

    @patch('臺灣言語工具.斷詞.辭典語言模型斷詞.辭典語言模型斷詞.斷詞')
    def test_辭典語言模型斷詞(self, 斷詞mock):
        辭典 = 現掀辭典(2)
        語言模型 = 實際語言模型(1)
        self.物件.斷詞(辭典語言模型斷詞, 辭典, 語言模型)
        斷詞mock.assert_called_once_with(辭典, 語言模型, 物件=self.物件)
