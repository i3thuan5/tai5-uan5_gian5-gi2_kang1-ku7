# -*- coding: utf-8 -*-
from sys import exit, stderr
import sys
import unittest
from unittest.suite import TestSuite


from 臺灣言語工具.翻譯.摩西工具.安裝摩西翻譯佮相關程式 import 安裝摩西翻譯佮相關程式


'''預設做單元試驗佮整合試驗'
python 走全部試驗.py # 試驗全做
python 走全部試驗.py 編譯摩西程式 # 試驗全做，而且編譯摩西程式
python 走全部試驗.py 單元試驗 # 只做單元試驗
python -m unittest 試驗.整合試驗.Test摩西模型訓練佮翻譯整合試驗 # 走單一試驗
'''

if __name__ == '__main__':
    整合試驗 = '單元試驗' not in sys.argv
    編譯摩西程式 = '編譯摩西程式' in sys.argv

    錯誤狀況 = 0
    試驗包 = TestSuite()
    試驗包.addTest(
        unittest.defaultTestLoader.discover('試驗', pattern='Test*單元試驗.py')
    )
    if 整合試驗:
        if 編譯摩西程式:
            安裝程式 = 安裝摩西翻譯佮相關程式()
            安裝程式.安裝moses(編譯CPU數=4)
            安裝程式.安裝gizapp()
            安裝程式.安裝mgiza()
        else:
            錯誤狀況 = 5  # 無編譯摩西會出現5个錯誤
        試驗包.addTest(
            unittest.defaultTestLoader.discover('試驗', pattern='Test*整合試驗.py')
        )
    試驗結果 = unittest.TextTestRunner().run(試驗包)
    if len(試驗結果.errors) > 錯誤狀況 or 試驗結果.failures != []:
        exit(1)
    if len(試驗結果.errors) != []:
        print('因為無編譯摩西程式試驗，有{}个試驗發生錯誤，的。程式猶原回傳0'.format(錯誤狀況), file=stderr)
    exit(0)
