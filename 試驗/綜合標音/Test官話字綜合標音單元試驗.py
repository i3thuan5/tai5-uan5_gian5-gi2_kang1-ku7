# -*- coding: utf-8 -*-
import unittest

from 臺灣言語工具.基本元素.公用變數 import 無音
from 臺灣言語工具.基本元素.字 import 字
from 臺灣言語工具.綜合標音.官話字綜合標音 import 官話字綜合標音
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


class 官話字綜合標音單元試驗(unittest.TestCase):
    def setUp(self):
        self.我型 = '我'
        self.我音 = 'ㄨㄛˇ'
        self.我標音 = '⿿⿿ㄨㄛˇ'
        self.你型 = '你'
        self.你音 = 'ㄋㄧˇ'

    def tearDown(self):
        pass

    def test_合法(self):
        綜合標音 = 官話字綜合標音(字(self.我型, self.我音))
        self.assertEqual(綜合標音.標音完整無(), True)
        綜合標音 = 官話字綜合標音(字(self.我型, self.我音), False)
        self.assertEqual(綜合標音.標音完整無(), True)
        綜合標音 = 官話字綜合標音(字(self.我型, self.我音), True)
        self.assertEqual(綜合標音.標音完整無(), True)

    def test_兩个字合法(self):
        我綜合標音 = 官話字綜合標音(字(self.我型, self.我音))
        你綜合標音 = 官話字綜合標音(字(self.你型, self.你音))
        self.assertEqual(我綜合標音.標音完整無(), True)
        self.assertEqual(你綜合標音.標音完整無(), True)
        self.assertEqual(我綜合標音.型體, self.我型)
        self.assertEqual(你綜合標音.型體, self.你型)

    def test_轉json格式(self):
        綜合標音 = 官話字綜合標音(字(self.我型, self.我音))
        self.assertEqual(綜合標音.轉json格式(),
                         {"型體": self.我型, "注音符號": self.我標音})
        self.assertEqual(綜合標音.標音完整無(), True)

    def test_標點合法(self):
        標點 = 官話字綜合標音(字('，', 無音))
        self.assertEqual(標點.標音完整無(), True)

    def test_標點轉json格式(self):
        標點 = 官話字綜合標音(字('，', 無音))
        self.assertEqual(標點.轉json格式(), {"型體": "，", "注音符號": ""})

    def test_標點音無合法(self):
        標音 = 官話字綜合標音(字('我', 'ㄆㄨㄧˋ'))
        self.assertEqual(標音.標音完整無(), False)
        標音 = 官話字綜合標音(字('我', 'ㄆㄨㄧˋ'), False)
        self.assertEqual(標音.標音完整無(), False)
        self.assertRaises(解析錯誤, 官話字綜合標音, 字('我', 'ㄆㄨㄧˋ'), True)

    def test_烏白傳(self):
        self.assertRaises(型態錯誤, 官話字綜合標音, '我')
        self.assertRaises(型態錯誤, 官話字綜合標音, '我', False)
        self.assertRaises(型態錯誤, 官話字綜合標音, '我', True)

    def test_輕聲轉json格式(self):
        型 = '的'
        音 = 'ㄉㄜ˙'
        綜合標音 = 官話字綜合標音(字(型, 音))
        self.assertEqual(綜合標音.標音完整無(), True)
        self.assertEqual(綜合標音.轉json格式(),
                         {"型體": 型, "注音符號": '⿿⿿˙ㄉㄜ'})
