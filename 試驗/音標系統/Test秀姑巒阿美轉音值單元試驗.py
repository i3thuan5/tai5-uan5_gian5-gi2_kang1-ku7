# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.音標系統.Pangcah.原住民族語言書寫系統秀姑巒阿美語 import 原住民族語言書寫系統秀姑巒阿美語


class 原住民族語言書寫系統秀姑巒阿美語轉音值單元試驗(TestCase):

    def test_一般(self):
        self.assertEqual(
            原住民族語言書寫系統秀姑巒阿美語("cidal").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )

    def test_詞尾補塞音(self):
        self.assertEqual(
            原住民族語言書寫系統秀姑巒阿美語("kako").音值(),
            [['k', 'a'], ['k', 'o', 'ʔ']]
        )

    def test_詞頭詞尾攏愛補(self):
        self.assertEqual(
            原住民族語言書寫系統秀姑巒阿美語('ina').音值(),
            [['ʔ', 'i'], ['n', 'a', 'ʔ']]
        )

    def test_一个符號(self):
        self.assertEqual(
            原住民族語言書寫系統秀姑巒阿美語("o").音值(),
            [['ʔ', 'o', 'ʔ']]
        )

    def test_ng(self):
        self.assertEqual(
            原住民族語言書寫系統秀姑巒阿美語("nga'ay").音值(),
            [['ŋ', 'a'], ['ʡ', 'a', 'j']]
        )

    def test_VCCV(self):
        self.assertEqual(
            原住民族語言書寫系統秀姑巒阿美語("mimetmet").音值(),
            [['m', 'i'], ['m', 'ə', 't'], ['m', 'ə', 't']]
        )

    def test_VGGV(self):
        self.assertEqual(
            原住民族語言書寫系統秀姑巒阿美語("wayya").音值(),
            [['w', 'a', 'j'], ['j', 'a', 'ʔ']]
        )

    def test_大寫(self):
        self.assertEqual(
            原住民族語言書寫系統秀姑巒阿美語("O").音值(),
            [['ʔ', 'o', 'ʔ']]
        )

    def test_預設音標就是家己(self):
        self.assertEqual(原住民族語言書寫系統秀姑巒阿美語("O").預設音標(), 'O')

    def test_無合法(self):
        self.assertEqual(原住民族語言書寫系統秀姑巒阿美語("！").音標, None)
        self.assertEqual(原住民族語言書寫系統秀姑巒阿美語("！").音值(), [])
