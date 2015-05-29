# -*- coding: utf-8 -*-
from sys import exit
import sys
import unittest
from unittest.suite import TestSuite


if __name__ == '__main__':
	'''預設做單元試驗佮整合試驗'
	PYTHONPATH=. python 試驗/走全部試驗.py # 試驗全做 
	PYTHONPATH=. python 試驗/走全部試驗.py 單元試驗 # 只做單元試驗 
	'''
	整合試驗 = '單元試驗' not in sys.argv

	試驗包 = TestSuite()
	試驗包.addTest(
			unittest.defaultTestLoader.discover('試驗',pattern='*單元試驗.py')
		)
	if 整合試驗:
		試驗包.addTest(
				unittest.defaultTestLoader.discover('試驗',pattern='*整合試驗.py')
			)
	print(試驗包.countTestCases)
	print((試驗包.countTestCases()))
	exit(0)
	試驗結果=unittest.TextTestRunner().run(試驗包)
	if 試驗結果. errors!=[] or 試驗結果.failures!=[]:
		exit(1)
	exit(0)
