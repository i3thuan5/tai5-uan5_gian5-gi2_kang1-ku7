# -*- coding: utf-8 -*-
import os

class 外部程式工具:
	def 專案目錄(self):
		程式所在 = os.path.abspath(__file__)
		程式所在, 資料夾 = 程式所在.rsplit('/', 1)
		while 資料夾 != '臺灣言語工具':
			程式所在, 資料夾 = 程式所在.rsplit('/', 1)
		return 程式所在
