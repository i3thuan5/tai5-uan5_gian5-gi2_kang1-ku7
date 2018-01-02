# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音音標
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音佮臺灣羅馬聲母對照表
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音佮臺灣羅馬韻母對照表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音聲母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音韻母表


class 通用拼音音標單元試驗(TestCase):

    def test_定看音標(self):
        表 = [('bai5', 'pai5'), ('ang3', 'ang3'),
             ('zin4', 'tsin2'), ('gior2', 'kio7'), ('gier1', 'kio1'),
             ('tang3', 'thang3'), ('kong9', 'khong9'), ('mng5', 'mng5'),
             ('cat8', 'tshat10'), ('zang5', 'tsang5'),
             ('mo5', 'moo5'), ('ngo5', 'ngoo5'),
             ]
        for 通, 臺 in 表:
            字音對照 = 通用拼音音標(通)
            self.assertEqual(字音對照.音標, 通)
            self.assertEqual(字音對照.轉換到臺灣閩南語羅馬字拼音(), 臺)

    def test_入聲(self):
        表 = [('zit4', None, None),
             ('pih8', 'pih8', 'phih10'),
             ('bah2', 'bah7', 'pah4',),
             ('zierk1', None, None),
             ('ziok1', 'ziok6', 'tsiok8'), ]
        for 原, 通, 臺 in 表:
            字音對照 = 通用拼音音標(原)
            self.assertEqual(字音對照.音標, 通)
            self.assertEqual(字音對照.轉換到臺灣閩南語羅馬字拼音(), 臺)

    def test_轉forpa(self):
        通 = 'iorh6'
        forpa = 'ierh6'
        self.assertEqual(通用拼音音標(通).轉ForPA(), forpa)

    def test_違法音標(self):
        self.assertEqual(通用拼音音標('@@').音標, None)
        self.assertEqual(通用拼音音標('pe̍m').音標, None)
        self.assertEqual(通用拼音音標('xxtsé--á').音標, None)
        self.assertEqual(通用拼音音標('óonn').音標, None)
        self.assertEqual(通用拼音音標('hir2').音標, None)
        self.assertEqual(通用拼音音標('e').音標, None)
        self.assertEqual(通用拼音音標('tsang3').轉換到臺灣閩南語羅馬字拼音(), None)

    def test_全部攏會使產生方音物件(self):
        for _, 臺 in 通用拼音佮臺灣羅馬聲母對照表.items():
            self.assertIn(臺, 臺灣閩南語羅馬字拼音聲母表)
        for _, 臺 in 通用拼音佮臺灣羅馬韻母對照表.items():
            self.assertIn(臺, 臺灣閩南語羅馬字拼音韻母表)
