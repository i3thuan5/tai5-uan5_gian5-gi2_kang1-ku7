from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.基本元素.句 import 句

class 章:
	內底句 = None
	def __init__(self, 句陣列 = []):
		if not isinstance(句陣列, list):
			raise 型態錯誤('傳入來的句陣列毋是陣列：{0}'.format(str(句陣列)))
		self.內底句 = []
		for 句物件 in 句陣列:
			if not isinstance(句物件, 句):
				raise 型態錯誤('句陣列內底有毋是句的：句陣列＝{0}，句物件＝{1}'.format(str(句陣列), str(句物件)))
			self.內底句.append(句(句物件.內底集))
	def __eq__(self, 別个):
		return 別个 != None and self.內底句 == 別个.內底句
	def __str__(self):
		return '章：{0}'.format(self.內底句)
	def __repr__(self):
		return self.__str__()
