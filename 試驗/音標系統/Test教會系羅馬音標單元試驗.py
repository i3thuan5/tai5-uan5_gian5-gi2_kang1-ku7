# -*- coding: utf-8 -*-
import unittest
from 臺灣言語工具.音標系統.閩南語.教會系羅馬音標 import 教會系羅馬音標
from 臺灣言語工具.音標系統.閩南語.教會系羅馬音標 import 教會系羅馬音標聲調符號表


class 教會系羅馬音標單元試驗(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_教會系羅馬音標聲調符號表有正規無(self):
        正規法 = 教會系羅馬音標.正規法
        for 原本, _ in 教會系羅馬音標聲調符號表.items():
            self.assertEqual(原本, 正規法(None, 原本))
            self.assertLessEqual(len(原本), 3)
