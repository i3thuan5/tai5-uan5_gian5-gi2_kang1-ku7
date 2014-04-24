# -*- coding: utf-8 -*-

class 語句編碼器:
	def 編碼(self,語句):
		return 語句.encode('unicode_escape').decode('ascii')
	def 解碼(self,語句):
		return 語句.encode('ascii').decode('unicode_escape')

if __name__=='__main__':
	編碼器=語句編碼器()
	print(編碼器.編碼('𪜶飼pig'))
	print(編碼器.解碼('\\U0002a736\\u98fcpig'))
	print(編碼器.解碼(編碼器.編碼('𪜶飼pig')))
	print(編碼器.編碼(編碼器.解碼('\\U0002a736\\u98fcpig')))
		