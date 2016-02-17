# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.音標系統.官話綜合標音 import 官話綜合標音
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤


class 官話綜合標音單元試驗(TestCase):

    def test_對齊物件(self):
        self.assertEqual(字('我', 'ㄨㄛˇ').綜合標音(官話綜合標音), {
            "漢字": '我', "注音符號": 'ㄨㄛˇ'
        })

    def test_無音綜合標音(self):
        self.assertEqual(字('我', 無音).綜合標音(官話綜合標音), {
            "漢字": '我', "注音符號": '我'
        })

    def test_標點綜合標音(self):
        self.assertEqual(字('，', 無音).綜合標音(官話綜合標音), {
            "漢字": '，', "注音符號": '，'
        })

    def test_對齊標點綜合標音(self):
        self.assertEqual(字('，', '.').綜合標音(官話綜合標音), {
            "漢字": '，', "注音符號": '.'
        })

    def test_標點音無合法的綜合標音(self):
        self.assertEqual(字('我', 'ㄉㄜ˙').綜合標音(官話綜合標音), {
            "漢字": '我', "注音符號": 'ㄆㄨㄧˋ'
        })

    def test_烏白傳(self):
        self.assertRaises(型態錯誤, 官話綜合標音, '我')
        self.assertRaises(型態錯誤, 官話綜合標音, '我', False)
        self.assertRaises(型態錯誤, 官話綜合標音, '我', True)

    def test_輕聲轉json格式(self):
        self.assertEqual(字('的', 'ㄉㄜ˙').綜合標音(官話綜合標音), {
            "漢字": '的', "注音符號": 'ㄉㄜ˙'
        })
