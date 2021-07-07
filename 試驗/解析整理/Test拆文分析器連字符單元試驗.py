# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 拆文分析器連字符單元試驗(TestCase):
    def tearDown(self):
        self.assertEqual(
            len(拆文分析器.建立句物件(self.句).篩出字物件()),
            self.字數,
            self.句
        )

    def test_一(self):
        self.句 = '-'
        self.字數 = 1

    def test_一_(self):
        self.句 = '- '
        self.字數 = 1

    def test__一(self):
        self.句 = ' -'
        self.字數 = 1

    def test__一_(self):
        self.句 = ' - '
        self.字數 = 1

    def test_一sui2(self):
        self.句 = '-sui2'
        self.字數 = 2

    def test_sui2一(self):
        self.句 = 'sui2-'
        self.字數 = 2

    def test_一_sui2(self):
        self.句 = '- sui2'
        self.字數 = 2

    def test_sui2_一(self):
        self.句 = 'sui2 -'
        self.字數 = 2

    def test_sui2一sui2(self):
        self.句 = 'sui2-sui2'
        self.字數 = 2

    def test_sui2一_sui2(self):
        self.句 = 'sui2- sui2'
        self.字數 = 1 + 1 + 1

    def test_sui2_一_sui2(self):
        self.句 = 'sui2 - sui2'
        self.字數 = 1 + 1 + 1

    def test_sui2_一sui2(self):
        self.句 = 'sui2 -sui2'
        self.字數 = 1 + 1 + 1

    def test_一一sui2(self):
        self.句 = '--sui2'
        self.字數 = 1

    def test_一一_sui2(self):
        self.句 = '-- sui2'
        self.字數 = 2 + 1

    def test_一_一sui2(self):
        self.句 = '- -sui2'
        self.字數 = 1 + 1 + 1

    def test_sui2一一(self):
        self.句 = 'sui2--'
        self.字數 = 1 + 2

    def test_sui2一一sui2(self):
        self.句 = 'sui2--sui2'
        self.字數 = 2

    def test_sui2一一_sui2(self):
        self.句 = 'sui2-- sui2'
        self.字數 = 1 + 2 + 1

    def test_sui2_一一_sui2(self):
        self.句 = 'sui2 -- sui2'
        self.字數 = 1 + 2 + 1

    def test_sui2_一一sui2(self):
        self.句 = 'sui2 --sui2'
        self.字數 = 2

    def test_sui2一_一sui2(self):
        self.句 = 'sui2- -sui2'
        self.字數 = 1 + 1 + 1 + 1

    def test_一一一_sui2(self):
        self.句 = '--- sui2'
        self.字數 = 3 + 1

    def test_一一一sui2(self):
        self.句 = '---sui2'
        self.字數 = 3 + 1

    def test_一_一一sui2(self):
        self.句 = '- --sui2'
        self.字數 = 1 + 1

    def test_一一_一sui2(self):
        self.句 = '-- -sui2'
        self.字數 = 2 + 1 + 1

    def test_sui2一一一sui2(self):
        self.句 = 'sui2---sui2'
        self.字數 = 1 + 3 + 1

    def test_1一pái(self):
        self.句 = '1-pái'
        self.字數 = 2

    def test_3_一_9_二_一6(self):
        self.句 = '3 - 9 = -6'
        self.字數 = 6
