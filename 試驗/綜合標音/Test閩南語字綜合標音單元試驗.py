# -*- coding: utf-8 -*-
import unittest
from 臺灣言語工具.基本元素.字 import 字
from 臺灣言語工具.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 臺灣言語工具.基本元素.公用變數 import 無音
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
import json


class 閩南語字綜合標音單元試驗(unittest.TestCase):
    def setUp(self):
        self.我型, self.我音 = '我', 'gua2'

    def tearDown(self):
        pass

    def test_合法(self):
        綜合標音 = 閩南語字綜合標音(字(self.我型, self.我音))
        self.assertEqual(綜合標音.標音完整無(), True)
        綜合標音 = 閩南語字綜合標音(字(self.我型, self.我音), False)
        self.assertEqual(綜合標音.標音完整無(), True)
        綜合標音 = 閩南語字綜合標音(字(self.我型, self.我音), True)
        self.assertEqual(綜合標音.標音完整無(), True)

    def test_兩个字合法(self):
        我綜合標音 = 閩南語字綜合標音(字('我', 'gua2'))
        你綜合標音 = 閩南語字綜合標音(字('你', 'li2'))
        self.assertEqual(我綜合標音.標音完整無(), True)
        self.assertEqual(你綜合標音.標音完整無(), True)
        self.assertEqual(我綜合標音.型體, '我')
        self.assertEqual(你綜合標音.型體, '你')

    def test_轉json格式(self):
        綜合標音 = 閩南語字綜合標音(字('我', 'gua2'))
        self.assertEqual(綜合標音.標音完整無(), True)
        self.assertEqual(綜合標音.轉json格式(), json.loads(
                '{"型體":"我","臺羅數字調":"gua2","臺羅閏號調":"guá","通用數字調":"ghua4","吳守禮方音":"⿿⿿⿿ㆣㄨㄚˋ"}'))
        self.assertEqual(綜合標音.轉json格式(),
                         {"型體": "我", "臺羅數字調": "gua2", "臺羅閏號調": "guá", "通用數字調": "ghua4",
                          "吳守禮方音": "⿿⿿⿿ㆣㄨㄚˋ"})

    def test_標點合法(self):
        標點 = 閩南語字綜合標音(字('，', 無音))
        self.assertEqual(標點.標音完整無(), True)

    def test_標點轉json格式(self):
        標點 = 閩南語字綜合標音(字('，', 無音))
        self.assertEqual(標點.轉json格式(), {"型體": "，", "臺羅數字調": "", "臺羅閏號調": "", "通用數字調": "", "吳守禮方音": ""})

    def test_標點音無合法(self):
        綜合標音 = 閩南語字綜合標音(字('我', 'uo3'))
        self.assertEqual(綜合標音.標音完整無(), False)
        綜合標音 = 閩南語字綜合標音(字('我', 'uo3'), False)
        self.assertEqual(綜合標音.標音完整無(), False)
        self.assertRaises(解析錯誤, 閩南語字綜合標音, 字('我', 'uo3'), True)

    def test_烏白傳(self):
        self.assertRaises(型態錯誤, 閩南語字綜合標音, '我')
        self.assertRaises(型態錯誤, 閩南語字綜合標音, '我', False)
        self.assertRaises(型態錯誤, 閩南語字綜合標音, '我', True)
