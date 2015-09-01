# -*- coding: utf-8 -*-
import unittest

from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音聲母表, 臺灣閩南語羅馬字拼音韻母表
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音佮臺灣羅馬聲母對照表, 通用拼音佮臺灣羅馬韻母對照表, 通用拼音音標


class 通用拼音音標單元試驗(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_定看音標(self):
        表 = [('bai5', 'pai5'), ('ang3', 'ang3'),
             ('zin4', 'tsin2'), ('gior2', 'kio7'), ('gier1', 'kio1'),
             ('tang3', 'thang3'), ('kong9', 'khong9'), ('mng5', 'mng5')]
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

    @unittest.expectedFailure
    def test_輕聲(self):
        self.assertEqual(通用拼音音標('ta0').音標, 'ta0')
        self.assertEqual(通用拼音音標('pih0').音標, 'pih0')

    @unittest.expectedFailure
    def test_語法輕聲(self):
        self.assertEqual(通用拼音音標('0a').音標, '0a1')
        self.assertEqual(通用拼音音標('0e5').音標, '0e5')
        self.assertEqual(通用拼音音標('0ê').音標, '0e5')
        self.assertEqual(通用拼音音標('0ê').音標, '0e5')
        self.assertEqual(通用拼音音標('0hannh').音標, '0hannh4')
        self.assertEqual(通用拼音音標('0chi̍t').音標, '0chit8')
        self.assertEqual(通用拼音音標('0tsi̍t').音標, None)
        self.assertEqual(通用拼音音標('cat8').音標, 'cat8')

    @unittest.expectedFailure
    def test_輸入閏號音標(self):
        self.assertEqual(通用拼音音標('pI̋m').音標, 'pim9')
        self.assertEqual(通用拼音音標('pi̍m').音標, 'pim8')
        self.assertEqual(通用拼音音標('pîm').音標, 'pim5')
        self.assertEqual(通用拼音音標('phǐN').音標, 'phinn6')
        self.assertEqual(通用拼音音標('pih').音標, 'pih4')
        self.assertEqual(通用拼音音標('nňg').音標, 'nng6')
        self.assertEqual(通用拼音音標('chőo').音標, 'choo9')
        self.assertEqual(通用拼音音標('cňg').音標, 'cng6')
        self.assertEqual(通用拼音音標('pňg').音標, 'png6')

    @unittest.expectedFailure
    def test_鼻化ㆦ(self):
        self.assertEqual(通用拼音音標('mo5').音標, 'moo5')
        self.assertEqual(通用拼音音標('ngoo5').音標, 'ngoo5')

    @unittest.expectedFailure
    def test_罕用音標(self):
        self.assertEqual(通用拼音音標('tor').音標, 'tor1')
        self.assertEqual(通用拼音音標('kee5').音標, 'kee5')
        self.assertEqual(通用拼音音標('ter5').音標, 'ter5')
        self.assertEqual(通用拼音音標('tere5').音標, 'tere5')
        self.assertEqual(通用拼音音標('tir5').音標, 'tir5')

    def test_違法音標(self):
        self.assertEqual(通用拼音音標('@@').音標, None)
        self.assertEqual(通用拼音音標('pe̍m').音標, None)
        self.assertEqual(通用拼音音標('xxtsé--á').音標, None)
        self.assertEqual(通用拼音音標('óonn').音標, None)
        self.assertEqual(通用拼音音標('hir2').音標, None)
        self.assertEqual(通用拼音音標('e').音標, None)

    @unittest.expectedFailure
    def test_轉臺羅(self):
        self.assertEqual(通用拼音音標('cat8').轉換到臺灣閩南語羅馬字拼音(), 'tsat8')
        self.assertEqual(通用拼音音標('chuan5').轉換到臺灣閩南語羅馬字拼音(), 'tshuan5')
        self.assertEqual(通用拼音音標('tsang3').轉換到臺灣閩南語羅馬字拼音(), None)

    def test_全部攏會使產生方音物件(self):
        for _, 臺 in 通用拼音佮臺灣羅馬聲母對照表.items():
            self.assertIn(臺, 臺灣閩南語羅馬字拼音聲母表)
        for _, 臺 in 通用拼音佮臺灣羅馬韻母對照表.items():
            self.assertIn(臺, 臺灣閩南語羅馬字拼音韻母表)
