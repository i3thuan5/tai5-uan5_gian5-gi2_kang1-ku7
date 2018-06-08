# -*- coding: utf-8 -*-
from os import makedirs
from os.path import join
from tempfile import TemporaryDirectory
from unittest.case import TestCase
from unittest.mock import patch, call


from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.翻譯.摩西工具.摩西服務端 import 摩西服務端


class 摩西服務端單元試驗(TestCase):

    def test_moses_git(self):
        with TemporaryDirectory() as 資料夾:
            self.做模型檔(資料夾)

            makedirs(join(資料夾, 'mosesdecoder', 'bin'))
            with open(join(資料夾, 'mosesdecoder', 'bin', 'mosesserver'), 'wb'):
                pass

            摩西服務端(資料夾, moses安裝路徑=資料夾)

    def test_moses一个執行(self):
        with TemporaryDirectory() as 資料夾:
            self.做模型檔(資料夾)

            with open(join(資料夾, 'mosesserver'), 'wb'):
                pass

            摩西服務端(資料夾, moses安裝路徑=資料夾)

    def 做模型檔(self, 資料夾):
        makedirs(join(資料夾, 'model'))
        with open(join(資料夾, 'model', 'moses.ini'), 'wt'):
            pass
