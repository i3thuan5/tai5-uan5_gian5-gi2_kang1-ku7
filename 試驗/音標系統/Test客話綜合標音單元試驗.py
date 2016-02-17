# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.音標系統.客話綜合標音 import 客話綜合標音
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤


class 客話綜合標音單元試驗(TestCase):

    def test_對齊物件(self):
        self.assertEqual(字('⿰厓', 'ngaiˇ').綜合標音(客話綜合標音), {
            "型體": '⿰厓',
            "臺灣客話": 'ngaiˇ'
        })

    def test_無音物件(self):
        self.assertEqual(字('⿰厓', 無音).綜合標音(客話綜合標音), {
            "型體": '⿰厓',
            "臺灣客話": '⿰厓'
        })

    def test_標點物件(self):
        self.assertEqual(字('，', 無音).綜合標音(客話綜合標音), {
            "型體": '，',
            "臺灣客話": '，'
        })

    def test_對齊標點物件(self):
        self.assertEqual(字('，', ',').綜合標音(客話綜合標音), {
            "型體": '，',
            "臺灣客話": ','
        })

    def test_標點音無合法(self):
        self.assertEqual(字('我', 'nggai').綜合標音(客話綜合標音), {
            "型體": '我',
            "臺灣客話": 'nggai'
        })

    def test_烏白傳(self):
        self.assertRaises(型態錯誤, 客話綜合標音, '我')
        self.assertRaises(型態錯誤, 客話綜合標音, '我', False)
        self.assertRaises(型態錯誤, 客話綜合標音, '我', True)
