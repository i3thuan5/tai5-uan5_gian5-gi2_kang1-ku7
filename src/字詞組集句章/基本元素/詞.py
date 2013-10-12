from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.基本元素.字 import 字

class 詞:
	內底字 = None
	def __init__(self, 字陣列 = []):
		if not isinstance(字陣列, list):
			raise 型態錯誤('傳入來的字陣列毋是陣列：{0}'.format(str(字陣列)))
		self.內底字 = []
		for 字物件 in 字陣列:
			if not isinstance(字物件, 字):
				raise 型態錯誤('字陣列內底有毋是字的：字陣列＝{0}，字物件＝{1}'.format(str(字陣列), str(字物件)))
			self.內底字.append(字(字物件.型, 字物件.音))
	def __eq__(self, 別个):
		return isinstance(別个, 詞) and self.內底字 == 別个.內底字
	def __str__(self):
		return '詞：{0}'.format(self.內底字)
	def __repr__(self):
		return self.__str__()
