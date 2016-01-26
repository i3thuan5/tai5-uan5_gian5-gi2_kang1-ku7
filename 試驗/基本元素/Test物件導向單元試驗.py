# -*- coding: utf-8 -*-
from unittest.case import TestCase
from unittest.mock import patch
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡


class 物件導向單元試驗(TestCase):

    def setUp(self):
        self.物件 = 拆文分析器.轉做句物件('頭-家｜thau5-ke1 員-工｜uan5-kang1')

    @patch('臺灣言語工具.解析整理.物件譀鏡.物件譀鏡.看型')
    def test_看型(self, 看型mock):
        self.物件.看型()
        看型mock.assert_called_once_with(self.物件)

    def test_看音(self):
        self.物件.看音()

    def test_看分詞(self):
        self.物件.看分詞()

    def test_看音有參數(self):
        self.物件.看音()

    def test_轉音(self):
        self.物件.轉音()

    def test_轉音有參數(self):
        self.物件.轉音()

    def test_篩出字物件(self):
        self.物件.篩出字物件()

    def test_網出詞物件(self):
        self.物件.網出詞物件()

    def test_辭典揣詞(self):
        self.物件.辭典揣詞()
# │   ├── 上長詞優先辭典揣詞.py
# │   ├── 拄好長度辭典揣詞.py
# │   ├── 尾字辭典揣詞.py

#
# ├── 辭典
# │   ├── __init__.py
# │   ├── 型音辭典.py
# │   ├── 型音點.py
# │   ├── 尾字辭典.py
# │   ├── 文字辭典.py
# │   └── 現掀辭典.py
    def test_斷詞(self):
        self.物件.斷詞()
# │   ├── 中研院   │   ├── 斷詞用戶端.py
# │   └── 辭典語言模型斷詞.py

    def test_翻譯(self):
        self.物件.翻譯()
# ├── 翻譯
# │   │   └── 斷詞斷字翻譯.cpython-34.pyc
# │   ├── 摩西工具
# │   │   ├── __init__.py
# │   │   ├── 安裝摩西翻譯佮相關程式.py
# │   │   ├── 摩西服務端.py
# │   │   ├── 摩西用戶端.py
# │   │   ├── 摩西翻譯模型訓練.py
# │   │   ├── 斷詞轉斷字的編碼器.py
# │   │   ├── 無編碼器.py
# │   │   └── 語句編碼器.py
# │   └── 斷詞斷字翻譯.py

    def test_集內組照排(self):
        self.物件.集內組照排()

    def test_號碼揀集內組(self):
        self.物件.座標揀集內組()

    def test_語言模型揀集內組(self):
        self.物件.語言模型揀集內組()

# ├── 語言模型
# │   ├── __init__.py
# │   ├── KenLM語言模型.py
# │   ├── KenLM語言模型訓練.py
# │   ├── 實際語言模型.py

    def test_綜合標音(self):
        self.物件.綜合標音(閩南語字綜合標音)
# │   ├── 句綜合標音.py
# │   ├── 字綜合標音.py
# │   ├── 詞組綜合標音.py
# │   └── 集綜合標音.py
