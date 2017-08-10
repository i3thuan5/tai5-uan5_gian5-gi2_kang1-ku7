# -*- coding: utf-8 -*-
from unittest.case import TestCase


from 臺灣言語工具.語音合成.決策樹仔問題.閩南語決策樹仔 import 閩南語決策樹仔
from 臺灣言語工具.語音合成.決策樹仔問題.客家話決策樹仔 import 客家話決策樹仔
from 臺灣言語工具.語音合成.決策樹仔問題.官話決策樹仔 import 官話決策樹仔
from 臺灣言語工具.語音合成.決策樹仔問題.秀姑巒阿美語決策樹仔 import 秀姑巒阿美語決策樹仔
from 臺灣言語工具.語音合成.決策樹仔問題.賽夏決策樹仔 import 賽夏決策樹仔
from 臺灣言語工具.音標系統.Bunun.Bubukun import Bubukun
from 臺灣言語工具.語音合成.決策樹仔問題.南島語決策樹仔 import 南島語決策樹仔


class 決策樹仔單元試驗(TestCase):

    def test_閩南語生決策樹仔問題(self):
        樹仔 = 閩南語決策樹仔()
        問題 = 樹仔.生()
        self.assertGreater(len(問題), 1000)

    def test_客家話生決策樹仔問題(self):
        樹仔 = 客家話決策樹仔()
        問題 = 樹仔.生()
        self.assertGreater(len(問題), 1000)

    def test_官話生決策樹仔問題(self):
        樹仔 = 官話決策樹仔()
        問題 = 樹仔.生()
        self.assertGreater(len(問題), 1000)

    def test_秀姑巒阿美生決策樹仔問題(self):
        self.assertGreater(len(秀姑巒阿美語決策樹仔.生()), 1000)

    def test_秀姑巒阿美有孤雙數問題(self):
        self.assertIn('孤數音節', '_Pangcah_'.join(秀姑巒阿美語決策樹仔.生()))

    def test_賽夏生決策樹仔問題(self):
        self.assertGreater(len(賽夏決策樹仔.生()), 1000)

    def test_南島語生決策樹仔問題(self):
        self.assertGreater(len(南島語決策樹仔(Bubukun).生()), 1000)
