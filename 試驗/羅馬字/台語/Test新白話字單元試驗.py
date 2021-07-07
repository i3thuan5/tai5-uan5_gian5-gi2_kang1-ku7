# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.羅馬字.台語 import 新白話字


class 新白話字單元試驗(TestCase):

    def test_白話字(self):
        self.assertIsNotNone(新白話字('chhō͘').音標)

    def test_臺羅(self):
        self.assertIsNotNone(新白話字('tshō͘').音標)

    def test_違法(self):
        self.assertIsNone(新白話字('cō͘').音標)

    def test_鼻聲母袂使配陽韻(self):
        self.assertIsNone(新白話字('nong').音標)

    def test_鼻聲母袂使配入聲(self):
        self.assertIsNone(新白話字('mit').音標)

    def test_鼻聲母免寫鼻化韻(self):
        self.assertIsNone(新白話字('nuann').音標)

    def test_鼻聲母會當韻化輔音(self):
        self.assertIsNotNone(新白話字('mn̂g').音標)

    def test_濁聲母韻袂使配鼻化韻(self):
        self.assertIsNone(新白話字('buann').音標)
