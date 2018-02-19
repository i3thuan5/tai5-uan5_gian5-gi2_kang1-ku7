# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


class 拆文分析器連字符單元試驗(TestCase):
    def tearDown(self):
        if self.錯誤:
            with self.assertRaises(解析錯誤):
                拆文分析器.建立句物件(self.句)
        else:
            self.assertEqual(
                len(拆文分析器.建立句物件(self.句).篩出字物件()),
                self.字數
            )

    def test_一sui2(self):
        self.句 = '-sui2'
        self.錯誤 = True

    def test_sui2一(self):
        self.句 = 'sui2-'
        self.錯誤 = True

    def test_sui2一sui2(self):
        self.句 = 'sui2-sui2'
        self.錯誤 = False
        self.字數 = 2

    def test_sui2一_sui2(self):
        self.句 = 'sui2- sui2'
        self.錯誤 = True

    def test_sui2_一_sui2(self):
        self.句 = 'sui2 - sui2'
        self.錯誤 = False
        self.字數 = 1 + 1 + 1

    def test_sui2_一sui2(self):
        self.句 = 'sui2 -sui2'
        self.錯誤 = True

    def test_一一sui2(self):
        self.句 = '--sui2'
        self.錯誤 = False
        self.字數 = 1

    def test_一一_sui2(self):
        self.句 = '-- sui2'
        self.錯誤 = False
        self.字數 = 2 + 1
        self.fail()

    def test_一_一sui2(self):
        self.句 = '- -sui2'
        self.錯誤 = True

    def test_sui2一一(self):
        self.句 = 'sui2--'
        self.錯誤 = True

    def test_sui2一一sui2(self):
        self.句 = 'sui2--sui2'
        self.錯誤 = False
        self.字數 = 2

    def test_sui2一一_sui2(self):
        self.句 = 'sui2-- sui2'
        self.錯誤 = True

    def test_sui2_一一_sui2(self):
        self.句 = 'sui2 -- sui2'
        self.錯誤 = True

    def test_sui2_一一sui2(self):
        self.句 = 'sui2 --sui2'
        self.錯誤 = False
        self.字數 = 2

    def test_sui2一_一sui2(self):
        self.句 = 'sui2- -sui2'
        self.錯誤 = True

    def test_一一一_sui2(self):
        self.句 = '--- sui2'
        self.錯誤 = False
        self.字數 = 3 + 1

    def test_一一一sui2(self):
        self.句 = '---sui2'
        self.錯誤 = True

    def test_一_一一sui2(self):
        self.句 = '- --sui2'
        self.錯誤 = False
        self.字數 = 1 + 1

    def test_一一_一sui2(self):
        self.句 = '-- -sui2'
        self.錯誤 = True

    def test_sui2一一一sui2(self):
        self.句 = 'sui2---sui2'
        self.錯誤 = True

    def test_9_一_3_二_6(self):
        self.句 = '9 - 3 = 6'
        self.錯誤 = False
        self.字數 = 5

    def test_3_一_9_二_一6(self):
        self.句 = '3 - 9 = -6'
        self.錯誤 = False
        self.字數 = 6
