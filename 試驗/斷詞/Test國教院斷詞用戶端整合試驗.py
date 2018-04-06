# -*- coding: utf-8 -*-
from unittest.case import TestCase


from 臺灣言語工具.斷詞.國教院斷詞用戶端 import 國教院斷詞用戶端


class 國教院斷詞用戶端整合試驗(TestCase):

    def test_語句斷一句話(self):
        斷詞結果 = 國教院斷詞用戶端.語句斷詞做陣列('市面上很少有「教科書設計」的專書')
        self.assertEqual(斷詞結果[0],  ["市面", "Nc"])
