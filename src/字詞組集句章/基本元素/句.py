from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.基本元素.集 import 集

class 句:
	內底集 = None
	def __init__(self, 集陣列 = []):
		if not isinstance(集陣列, list):
			raise 型態錯誤('傳入來的集陣列毋是陣列：{0}'.format(str(集陣列)))
		for 集物件 in 集陣列:
			if not isinstance(集物件, 集):
				raise 型態錯誤('集陣列內底有毋是集的：集陣列＝{0}，集物件＝{1}'.format(str(集陣列),str(集物件)))
		self.內底集 = 集陣列
	def __eq__(self, 別个):
		return 別个 != None and self.內底集 == 別个.內底集
	def __str__(self):
		return '句：{0}'.format(self.內底集)
	def __repr__(self):
		return self.__str__()
