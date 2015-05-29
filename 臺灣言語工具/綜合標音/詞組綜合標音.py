# -*- coding: utf-8 -*-
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.基本元素.組 import 組
from 臺灣言語工具.綜合標音.字綜合標音 import 字綜合標音
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡

class 詞組綜合標音():
	綜合字 = []
	連字音 = ''
	譀鏡 = 物件譀鏡()
	def __init__(self, 字綜合標音型態, 詞或組物件):
		self.綜合字 = []
		self.連字音 = ''
		if not isinstance(字綜合標音型態, type) or \
			not issubclass(字綜合標音型態, 字綜合標音):
			raise 型態錯誤('傳入來的字綜合標音有問題！{0}，{1}'.format(type(字綜合標音型態), str(字綜合標音型態)))
		if isinstance(詞或組物件, 詞):
			詞物件 = 詞或組物件
			for 一字 in 詞物件.內底字:
				self.綜合字.append(字綜合標音型態(一字))
				if not isinstance(self.綜合字[-1], 字綜合標音):
					raise 型態錯誤('傳入來的毋是字綜合標音型態！{0}，{1}'
						.format(type(self.綜合字[-1]), str(self.綜合字[-1])))
			self.連字音 = self.譀鏡.看音(詞物件)
		elif isinstance(詞或組物件, 組):
			組物件 = 詞或組物件
			for 詞物件 in 組物件.內底詞:
				for 一字 in 詞物件.內底字:
					self.綜合字.append(字綜合標音型態(一字))
					if not isinstance(self.綜合字[-1], 字綜合標音):
						raise 型態錯誤('傳入來的毋是字綜合標音型態！{0}，{1}'
							.format(type(self.綜合字[-1]), str(self.綜合字[-1])))
			self.連字音 = self.譀鏡.看音(組物件)
		else:
			raise 型態錯誤('傳入來的毋是詞或組物件！{0}，{1}'.format(type(詞或組物件), str(詞或組物件)))
	def 轉json格式(self):
		return {"詞組綜合標音":[
			標音.轉json格式() for 標音 in self.綜合字
			], "連字音": self.連字音}
	def 標音完整無(self):
		return all([標音.標音完整無() for 標音 in self.綜合標音])
	def __repr__(self):
		return self.轉json格式()
	def __str__(self):
		return self.轉json格式()
	def __eq__(self, 別个):
		return isinstance(別个, 詞組綜合標音) and \
			self.綜合字 == 別个.綜合字 and self.連字音 == 別个.連字音
