# -*- coding: utf-8 -*-
from unittest.case import TestCase
from unittest.mock import patch
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡


class 物件綜合標音單元試驗(TestCase):

    def setUp(self):
        self.物件 = 拆文分析器.轉做句物件('頭-家｜thau5-ke1 員-工｜uan5-kang1')

    def test_綜合標音(self):
        self.物件.綜合標音(閩南語字綜合標音)
# │   ├── 句綜合標音.py
# │   ├── 字綜合標音.py
# │   ├── 詞組綜合標音.py
# │   └── 集綜合標音.py
