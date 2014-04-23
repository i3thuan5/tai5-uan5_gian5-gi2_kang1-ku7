# -*- coding: utf-8 -*-
from urllib.parse import quote
from urllib.parse import unquote

class 語句編碼器:
	def 編碼(self,語句):
		'''會當配合jdk的native2ascii'''
		return 語句.encode('unicode_escape').decode('ascii')
	def 解碼(self,語句):
		'''會當配合jdk的native2ascii -reverse'''
		return 語句.encode('ascii').decode('unicode_escape')

if __name__=='__main__':
	來='/home/Ihc/mt/編碼/翻.臺語斷詞.txt'
	去='/home/Ihc/mt/編碼/翻2.臺語斷詞.txt'
	編碼器=語句編碼器()
	檔案=open(去,'w')
	for 一逝 in open(來):
		print(編碼器.編碼(一逝.strip()),file=檔案)
	檔案.close()
		