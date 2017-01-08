# -*- coding: utf-8 -*-
import unittest
from unittest.case import TestCase
from 臺灣言語工具.音標系統.客話.秀姑巒阿美 import 秀姑巒阿美
from 臺灣言語工具.音標系統.客話.秀姑巒阿美轉音值模組 import 秀姑巒阿美對照音值聲母表
from 臺灣言語工具.音標系統.客話.秀姑巒阿美轉音值模組 import 秀姑巒阿美對照音值韻母表
from 臺灣言語工具.音標系統.客話.秀姑巒阿美 import 秀姑巒阿美聲母對照表
from 臺灣言語工具.音標系統.客話.秀姑巒阿美 import 秀姑巒阿美韻母對照表


class 秀姑巒阿美轉音值單元試驗(TestCase):

    def test_一般(self):
        self.assertEqual(秀姑巒阿美("kako").音值(), ('k', 'a', 'k', 'u',))

    def test_一个符號(self):
        self.assertEqual(秀姑巒阿美("o").音值(), ('o'))

    def test_ng(self):
        self.assertEqual(秀姑巒阿美("nga'ay").音值(), ('ŋ', 'a', 'ʔ', 'a', 'y'))

    def test_大寫(self):
        self.assertEqual(秀姑巒阿美("O").音值(), ('o'))
