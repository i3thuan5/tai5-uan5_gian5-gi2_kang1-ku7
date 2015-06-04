# -*- coding: utf-8 -*-
from sys import exit
import sys
import unittest
from unittest.suite import TestSuite
from 臺灣言語工具.翻譯.摩西工具.安裝摩西翻譯佮相關程式 import 安裝摩西翻譯佮相關程式


'''預設做單元試驗佮整合試驗'
PYTHONPATH=. python 試驗/走全部試驗.py # 試驗全做 
PYTHONPATH=. python 試驗/走全部試驗.py 單元試驗 # 只做單元試驗 
PYTHONPATH=. python -m unittest 試驗.整合試驗.Test摩西模型訓練佮翻譯整合試驗 # 走單一試驗
'''
if __name__ == '__main__':
	整合試驗 = '單元試驗' not in sys.argv

	試驗包 = TestSuite()
	試驗包.addTest(
			unittest.defaultTestLoader.discover('試驗', pattern='Test*單元試驗.py')
		)
	if 整合試驗:
		試驗包.addTest(
				unittest.defaultTestLoader.discover('試驗', pattern='Test*整合試驗.py')
			)
		安裝程式 = 安裝摩西翻譯佮相關程式()
		安裝程式.安裝moses(編譯CPU數=1)
		安裝程式.安裝mgiza()
	試驗結果 = unittest.TextTestRunner().run(試驗包)
	if 試驗結果. errors != [] or 試驗結果.failures != []:
		exit(1)
	exit(0)
