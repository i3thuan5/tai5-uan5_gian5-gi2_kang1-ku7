# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from os.path import join, dirname
from csv import DictReader
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 臺灣閩南語羅馬字拼音調符整合試驗(TestCase):

    def test_檢查佮教典有仝款無(self):
        詞條檔名 = join(dirname(__file__), '語料', '詞目總檔.csv')
        with open(詞條檔名) as 檔案:
            for 一逝 in DictReader(檔案):
                組物件 = 拆文分析器.建立組物件(一逝['音讀'])
                for 字物件 in 組物件.篩出字物件():
                    拼音物件 = 臺灣閩南語羅馬字拼音(字物件.型)
                    if 拼音物件.音標 is not None:
                        self.assertEqual(拼音物件.轉調符(), 字物件.型, 一逝['音讀'])
