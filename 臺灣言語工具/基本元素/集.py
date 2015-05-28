# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本元素.組 import 組

class 集:
	內底組 = None
	def __init__(self, 組陣列 = []):
		try:
			self.內底組 = []
			for 組物件 in 組陣列:
				if not isinstance(組物件, 組):
					raise 型態錯誤('組陣列內底有毋是組的：組陣列＝{0}，組物件＝{1}'.format(str(組陣列), str(組物件)))
				self.內底組.append(組(組物件.內底詞))
		except TypeError as 問題:
			raise 型態錯誤('傳入來的組陣列毋法度疊代：{0}，問題：{1}'
					.format(str(組陣列),問題))
	def __eq__(self, 別个):
		return isinstance(別个, 集) and self.內底組 == 別个.內底組
	def __str__(self):
		return '集：{0}'.format(self.內底組)
	def __repr__(self):
		return self.__str__()
