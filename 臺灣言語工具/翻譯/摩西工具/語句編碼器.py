# -*- coding: utf-8 -*-

class 語句編碼器:
	def 編碼(self,語句):
		return 語句.encode('unicode_escape').decode('ascii')
	def 解碼(self,語句):
		return 語句.encode('ascii').decode('unicode_escape')
