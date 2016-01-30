# -*- coding: utf-8 -*-
import itertools
from unittest.case import TestCase
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.基本物件.組 import 組
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.章 import 章


class 建立產生新物件單元試驗(TestCase):

    def setUp(self):
        self.型 = '媠'
        self.音 = 'ㄙㄨㄧˋ'
        self.字物件 = 字(self.型, self.音)
        self.字陣列 = [self.字物件, self.字物件]
        self.詞物件 = 詞(self.字陣列)
        self.詞陣列 = [self.詞物件, self.詞物件, self.詞物件]
        self.組物件 = 組(self.詞陣列)
        self.組陣列 = [self.組物件, self.組物件, self.組物件, self.組物件]
        self.集物件 = 集(self.組陣列)
        self.集陣列 = [self.集物件, self.集物件]
        self.句物件 = 句(self.集陣列)
        self.句陣列 = [self.句物件, self.句物件, self.句物件]
        self.章物件 = 章(self.句陣列)

    def test_詞組集章句傳其他疊代(self):
        self.assertEqual(self.詞物件, 詞(tuple(self.詞物件.內底字)))
        self.assertEqual(self.組物件, 組(tuple(self.組物件.內底詞)))
        self.assertEqual(self.集物件, 集(itertools.chain(self.集物件.內底組)))
        self.assertEqual(self.句物件, 句(tuple(self.句物件.內底集)))
        self.assertEqual(self.章物件, 章(tuple(self.章物件.內底句)))

    def test_詞內底檢查(self):
        self.assertEqual(self.詞物件.內底字, self.字陣列)

    def test_組內底檢查(self):
        self.assertEqual(self.組物件.內底詞, self.詞陣列)

    def test_集內底檢查(self):
        self.assertEqual(self.集物件.內底組, self.組陣列)

    def test_句內底檢查(self):
        self.assertEqual(self.句物件.內底集, self.集陣列)

    def test_章內底檢查(self):
        self.assertEqual(self.章物件.內底句, self.句陣列)

    def test_句獨立檢查_改舊陣列無影響新的(self):
        self.assertEqual(len(self.句物件.內底集), 2)
        self.assertEqual(len(self.章物件.內底句[0].內底集), 2)
        self.集陣列.append(集(self.組陣列))
        self.assertEqual(len(self.句物件.內底集), 2)
        self.assertEqual(len(self.章物件.內底句[0].內底集), 2)

    def test_句結構檢查(self):
        self.assertEqual(len(self.句物件.內底集), 2)
        self.assertEqual(len(self.章物件.內底句[0].內底集), 2)
        self.句物件.內底集.append(集(self.組陣列))
        self.assertEqual(len(self.句物件.內底集), 3)
        self.assertEqual(len(self.章物件.內底句[0].內底集), 2)

    def test_集獨立檢查_改舊陣列無影響新的(self):
        self.assertEqual(len(self.集物件.內底組), 4)
        self.assertEqual(len(self.句物件.內底集[0].內底組), 4)
        self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組), 4)
        self.組陣列.append(組(self.詞陣列))
        self.assertEqual(len(self.集物件.內底組), 4)
        self.assertEqual(len(self.句物件.內底集[0].內底組), 4)
        self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組), 4)

    def test_集結構檢查(self):
        self.assertEqual(len(self.集物件.內底組), 4)
        self.assertEqual(len(self.句物件.內底集[0].內底組), 4)
        self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組), 4)
        self.集物件.內底組.append(組(self.詞陣列))
        self.assertEqual(len(self.集物件.內底組), 5)
        self.assertEqual(len(self.句物件.內底集[0].內底組), 4)
        self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組), 4)

    def test_組獨立檢查_改舊陣列無影響新的(self):
        self.assertEqual(len(self.組物件.內底詞), 3)
        self.assertEqual(len(self.集物件.內底組[0].內底詞), 3)
        self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞), 3)
        self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞), 3)
        self.詞陣列.append(詞(self.字陣列))
        self.assertEqual(len(self.組物件.內底詞), 3)
        self.assertEqual(len(self.集物件.內底組[0].內底詞), 3)
        self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞), 3)
        self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞), 3)

    def test_組結構檢查(self):
        self.assertEqual(len(self.組物件.內底詞), 3)
        self.assertEqual(len(self.集物件.內底組[0].內底詞), 3)
        self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞), 3)
        self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞), 3)
        self.組物件.內底詞.append(詞(self.字陣列))
        self.assertEqual(len(self.組物件.內底詞), 4)
        self.assertEqual(len(self.集物件.內底組[0].內底詞), 3)
        self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞), 3)
        self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞), 3)

    def test_詞獨立檢查_改舊陣列無影響新詞(self):
        新型 = '文'
        新音 = 'ㆠㄨㄣˊ'
        新字物件 = 字(新型, 新音)
        self.assertEqual(len(self.詞物件.內底字), 2)
        self.assertEqual(len(self.組物件.內底詞[0].內底字), 2)
        self.assertEqual(len(self.集物件.內底組[0].內底詞[0].內底字), 2)
        self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞[0].內底字), 2)
        self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字), 2)
        self.字陣列.append(新字物件)
        self.assertEqual(len(self.詞物件.內底字), 2)
        self.assertEqual(len(self.組物件.內底詞[0].內底字), 2)
        self.assertEqual(len(self.集物件.內底組[0].內底詞[0].內底字), 2)
        self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞[0].內底字), 2)
        self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字), 2)

    def test_詞結構檢查(self):
        新型 = '文'
        新音 = 'ㆠㄨㄣˊ'
        新字物件 = 字(新型, 新音)
        self.assertEqual(len(self.詞物件.內底字), 2)
        self.assertEqual(len(self.組物件.內底詞[0].內底字), 2)
        self.assertEqual(len(self.集物件.內底組[0].內底詞[0].內底字), 2)
        self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞[0].內底字), 2)
        self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字), 2)
        self.詞物件.內底字.append(新字物件)
        self.assertEqual(len(self.詞物件.內底字), 3)
        self.assertEqual(len(self.組物件.內底詞[0].內底字), 2)
        self.assertEqual(len(self.集物件.內底組[0].內底詞[0].內底字), 2)
        self.assertEqual(len(self.句物件.內底集[0].內底組[0].內底詞[0].內底字), 2)
        self.assertEqual(len(self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字), 2)

    def test_字獨立檢查_改舊物件無影響新的(self):
        新型 = '文'
        新音 = 'ㆠㄨㄣˊ'
        self.assertEqual(self.詞物件.內底字[0], 字(self.型, self.音))
        self.assertEqual(self.組物件.內底詞[0].內底字[0], 字(self.型, self.音))
        self.assertEqual(self.集物件.內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
        self.assertEqual(
            self.句物件.內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
        self.assertEqual(
            self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
        self.字物件.型 = 新型
        self.字物件.音 = 新音
        self.assertEqual(self.詞物件.內底字[0], 字(self.型, self.音))
        self.assertEqual(self.組物件.內底詞[0].內底字[0], 字(self.型, self.音))
        self.assertEqual(self.集物件.內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
        self.assertEqual(
            self.句物件.內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
        self.assertEqual(
            self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))

    def test_字結構檢查(self):
        新字物件 = 字(self.型, self.音)
        self.assertEqual(self.詞物件.內底字[0], 字(self.型, self.音))
        self.assertEqual(self.組物件.內底詞[0].內底字[0], 字(self.型, self.音))
        self.assertEqual(self.集物件.內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
        self.assertEqual(
            self.句物件.內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
        self.assertEqual(
            self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
        self.詞物件.內底字[0] = 新字物件
        self.assertEqual(self.詞物件.內底字[0], 字(self.型, self.音))
        self.assertEqual(self.組物件.內底詞[0].內底字[0], 字(self.型, self.音))
        self.assertEqual(self.集物件.內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
        self.assertEqual(
            self.句物件.內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))
        self.assertEqual(
            self.章物件.內底句[0].內底集[0].內底組[0].內底詞[0].內底字[0], 字(self.型, self.音))

    def test_組獨立檢查_改新組無影響舊的(self):
        新型 = '文'
        新音 = 'ㆠㄨㄣˊ'
        新組物件 = 組(self.詞陣列)
        self.assertEqual(新組物件, self.組物件)
        新組物件.內底詞[0].內底字[0].型 = 新型
        新組物件.內底詞[0].內底字[0].音 = 新音
# 		self.assertRaises(AssertionError, self.assertNotEqual, 新組物件, self.組物件,)
        self.assertNotEqual(新組物件, self.組物件)
