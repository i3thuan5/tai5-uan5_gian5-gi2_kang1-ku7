# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.參數錯誤 import 參數錯誤
from os import remove
from unittest.mock import patch, call


class 辭典單元試驗:
    辭典型態 = None

    def setUp(self):
        self.字典 = self.辭典型態(4)
        self.孤詞物 = 拆文分析器.建立詞物件('你')
        self.孤詞音 = 拆文分析器.建立詞物件('li2')
        self.二詞物 = 拆文分析器.建立詞物件('好')
        self.二詞音 = 拆文分析器.建立詞物件('ho2')
        self.短詞物 = 拆文分析器.建立詞物件('你好')
        self.短詞音 = 拆文分析器.建立詞物件('li2-ho2')
        self.詞物件 = 拆文分析器.建立詞物件('你好無-？')
        self.詞音標 = 拆文分析器.建立詞物件('li2-ho2-bo5-?')
        self.對齊詞 = 拆文分析器.對齊詞物件('你好無？', 'li2-ho2-bo5-?')
        self.偏泉詞 = 拆文分析器.對齊詞物件('你好無？', 'lu2-ho2-bo5-?')
        self.無仝詞 = 拆文分析器.對齊詞物件('你有無？', 'li2-u7-bo5-?')
        self.傷長詞 = 拆文分析器.對齊詞物件('你有好無？', 'li2-u7-ho2-bo5-?')

    def tearDown(self):
        pass

    def test_漢字加詞成功無(self):
        self.字典.加詞(self.詞物件)
        self.assertEqual(
            self.字典.查詞(self.詞物件), [set(), set(), set(), {self.詞物件}])

    def test_多對齊加詞成功無(self):
        self.字典.加詞(self.對齊詞)
        self.字典.加詞(self.對齊詞)
        self.assertEqual(
            self.字典.查詞(self.對齊詞), [set(), set(), set(), {self.對齊詞}])

    def test_查對齊詞成功無(self):
        self.字典.加詞(self.對齊詞)
        self.assertEqual(
            self.字典.查詞(self.詞物件), [set(), set(), set(), {self.對齊詞}])
        self.assertEqual(
            self.字典.查詞(self.詞音標), [set(), set(), set(), {self.對齊詞}])
        self.assertEqual(
            self.字典.查詞(self.對齊詞), [set(), set(), set(), {self.對齊詞}])
        self.assertEqual(self.字典.查詞(self.無仝詞), [set(), set(), set(), set()])

    def test_相近詞無使查著(self):
        self.字典.加詞(self.無仝詞)
        self.assertEqual(self.字典.查詞(self.詞物件), [set(), set(), set(), set()])
        self.assertEqual(len(self.詞音標.內底字), 4)
        self.assertEqual(self.字典.查詞(self.詞音標), [set(), set(), set(), set()])
        self.assertEqual(self.字典.查詞(self.對齊詞), [set(), set(), set(), set()])
        self.assertEqual(
            self.字典.查詞(self.無仝詞), [set(), set(), set(), {self.無仝詞}])

    def test_傷長詞無使查著(self):
        self.字典.加詞(self.對齊詞)
        self.字典.加詞(self.傷長詞)
        self.assertEqual(
            self.字典.查詞(self.詞物件), [set(), set(), set(), {self.對齊詞}])
        self.assertEqual(
            self.字典.查詞(self.詞音標), [set(), set(), set(), {self.對齊詞}])
        self.assertEqual(
            self.字典.查詞(self.對齊詞), [set(), set(), set(), {self.對齊詞}])
        self.assertEqual(
            self.字典.查詞(self.傷長詞), [set(), set(), set(), set(), set()])

    def test_長短詞攏愛揣出來(self):
        self.字典.加詞(self.孤詞物)
        self.字典.加詞(self.二詞物)
        self.字典.加詞(self.短詞物)
        self.字典.加詞(self.詞物件)
        self.字典.加詞(self.孤詞音)
        self.字典.加詞(self.二詞音)
        self.字典.加詞(self.短詞音)
        self.字典.加詞(self.詞音標)
        self.assertEqual(self.字典.查詞(self.詞物件),
                         [{self.孤詞物}, {self.短詞物}, set(), {self.詞物件}])
        self.assertEqual(self.字典.查詞(self.詞音標),
                         [{self.孤詞音}, {self.短詞音}, set(), {self.詞音標}])

    def test_仝款長度有兩个以上(self):
        self.字典.加詞(self.詞物件)
        self.字典.加詞(self.對齊詞)
        self.字典.加詞(self.偏泉詞)
        self.assertEqual(self.字典.查詞(self.詞物件),
                         [set(), set(), set(), {self.詞物件, self.對齊詞, self.偏泉詞}])
        self.assertEqual(self.字典.查詞(self.詞音標),
                         [set(), set(), set(), {self.對齊詞}])

    def test_長度零的詞愛錯誤(self):
        self.assertRaises(解析錯誤, self.字典.加詞, 詞())

    def test_上限長度零(self):
        self.assertRaises(參數錯誤, self.辭典型態, 0)
        self.assertRaises(參數錯誤, self.辭典型態, -10)

    def test_字數(self):
        for 長度 in range(1, 100):
            self.assertEqual(self.辭典型態(長度).上濟字數(), 長度)

    def test_加檔案的詞(self):
        檔名 = '暫存檔'
        詞陣列 = [self.對齊詞, self.詞音標]
        with open(檔名, 'w') as 檔案:
            for 詞物件 in 詞陣列:
                print(詞物件.看分詞(), file=檔案)
        with patch('臺灣言語工具.辭典.{0}.{0}.加詞'.format(self.辭典型態.__name__)) as 加詞mock:
            self.字典.加檔案的詞(檔名)
            call陣列 = []
            for 詞物件 in 詞陣列:
                call陣列.append(call(詞物件))
            加詞mock.assert_has_calls(call陣列)
        remove(檔名)

    def test_輕聲就揣著輕聲(self):
        輕聲 = 拆文分析器.建立詞物件('--啊', '--ah')
        self.字典.加詞(輕聲)
        self.assertEqual(self.字典.查詞(輕聲), [{輕聲}])

    def test_輕聲揣無重音(self):
        輕聲 = 拆文分析器.建立詞物件('--啊', '--ah')
        重音 = 拆文分析器.建立詞物件('啊', 'ah')
        self.字典.加詞(重音)
        self.assertEqual(self.字典.查詞(輕聲), [set()])

    def test_漢字輕聲揣無重音(self):
        輕聲 = 拆文分析器.建立詞物件('--啊')
        重音 = 拆文分析器.建立詞物件('啊', 'ah')
        self.字典.加詞(重音)
        self.assertEqual(self.字典.查詞(輕聲), [set()])

    def test_重音揣無輕聲(self):
        輕聲 = 拆文分析器.建立詞物件('--啊', '--ah')
        重音 = 拆文分析器.建立詞物件('啊', 'ah')
        self.字典.加詞(輕聲)
        self.assertEqual(self.字典.查詞(重音), [set()])
