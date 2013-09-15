
from 字詞組集句章.基本元素.詞 import 詞
from 字詞組集句章.基本元素.組 import 組
from 字詞組集句章.綜合標音.字綜合標音 import 字綜合標音
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤

class 詞組綜合標音():
	綜合字 = []
	連字音 = ''
	def __init__(self, 字綜合標音型態, 詞或組物件):
		if not isinstance(字綜合標音型態, 字綜合標音):
			raise 型態錯誤('傳入來的毋是字綜合標音型態！{0}，{1}'.format(type(字綜合標音型態), str(字綜合標音型態)))
		if isinstance(詞或組物件, 詞):
			詞物件=詞或組物件
#			連字音=''.join([逐字.音 for 逐字 in 詞物件.內底字])
		elif isinstance(詞或組物件, 組):
			組物件=詞或組物件
		else:
			raise 型態錯誤('傳入來的毋是集物件！{0}，{1}'.format(type(集物件), str(集物件)))
		for 組物件 in 集物件.內底組:
			self.綜合集.append(詞組綜合標音(字綜合標音型態, 組物件))
	def 轉json格式(self):
		return ('{"綜合標音":[' +
			','.join([標音.轉json格式() for 標音 in self.綜合標音 if 標音.標音完整無()]) +
			'],"詞組":"' + self.詞組 + '"}')
	def 標音完整無(self):
		return all([標音.標音完整無() for 標音 in self.綜合標音])
	def __repr__(self):
		return self.轉json格式()
	def __str__(self):
		return self.轉json格式()
