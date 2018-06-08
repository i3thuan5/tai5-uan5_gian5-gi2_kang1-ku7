from unittest.case import TestCase


from 臺灣言語工具.翻譯.摩西工具.安裝摩西翻譯佮相關程式 import 安裝摩西翻譯佮相關程式


class 摩西模型編譯整合試驗(TestCase):
    def test_編譯較濟擺嘛無問題(self):
        安裝摩西翻譯佮相關程式.安裝moses(編譯CPU數=4, 清掉=True)
        安裝摩西翻譯佮相關程式.安裝moses(編譯CPU數=4, 清掉=False)
        安裝摩西翻譯佮相關程式.安裝moses(編譯CPU數=4, 清掉=True)
