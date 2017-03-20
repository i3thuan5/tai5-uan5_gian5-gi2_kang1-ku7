# -*- coding: utf-8 -*-
from sys import exit
import sys
import unittest
from unittest.suite import TestSuite


from 臺灣言語工具.翻譯.摩西工具.安裝摩西翻譯佮相關程式 import 安裝摩西翻譯佮相關程式
from 臺灣言語工具.語音辨識.HTK工具.安裝HTK語音辨識程式 import 安裝HTK語音辨識程式
from 臺灣言語工具.語音合成.HTS工具.安裝HTS語音辨識程式 import 安裝HTS語音辨識程式


'''
# 預設做單元試驗佮整合試驗
python 走全部試驗.py # 試驗全做
python 走全部試驗.py 單元試驗 # 只做單元試驗
python 走全部試驗.py 單元試驗 莫編譯程式 # 程式編譯過，需要快速走單元試驗
python -m unittest 試驗.斷詞.Test拄好長度辭典揣詞單元試驗 # 走單一試驗檔案
python 走全部試驗.py travis # travis無法度編了摩西程式，除了需要摩西檔案以外的試驗。會走中研院服務，毋過失敗袂影響程式結果
'''

if __name__ == '__main__':
    單元試驗 = '單元試驗' in sys.argv
    整合試驗 = '整合試驗' in sys.argv
    莫編譯程式 = '莫編譯程式' in sys.argv
    travis = 'travis' in sys.argv
    if not 單元試驗 and not 整合試驗:
        單元試驗 = True
        整合試驗 = True

    if not 莫編譯程式:
        安裝摩西翻譯佮相關程式.安裝gizapp()
        安裝摩西翻譯佮相關程式.安裝mgiza()  # 愛libboost
        安裝摩西翻譯佮相關程式.安裝moses(編譯CPU數=4)
        安裝HTK語音辨識程式.安裝htk()
        安裝HTS語音辨識程式.安裝sptk()
        安裝HTS語音辨識程式.安裝hts()
        安裝HTS語音辨識程式.掠htsDemoScript()

    試驗包 = TestSuite()
    if 單元試驗:
        試驗包.addTest(
            unittest.defaultTestLoader.discover(
                '.', pattern='Test*單元試驗.py'
            )
        )
    if 整合試驗:
        if not travis:
            試驗包.addTest(
                unittest.defaultTestLoader.discover(
                    '.', pattern='Test*整合試驗.py'
                )
            )
        else:
            # 中研院的服務嘛袂穩，莫影響試驗成功無成功
            # ./斷詞/Test中研院斷詞用戶端整合試驗.py
            # ./剖析/Test中研院剖析用戶端整合試驗.py
            試驗包.addTest(
                unittest.defaultTestLoader.discover(
                    '.', pattern='Test[!中]*整合試驗.py'
                )
            )
    試驗結果 = unittest.TextTestRunner().run(試驗包)
    if len(試驗結果.errors) > 0 or 試驗結果.failures != []:
        exit(1)
    if travis:
        中研院服務試驗包 = TestSuite()
        中研院服務試驗包.addTest(
            unittest.defaultTestLoader.discover(
                '.', pattern='Test中*整合試驗.py'
            )
        )
        unittest.TextTestRunner().run(中研院服務試驗包)
    exit(0)
