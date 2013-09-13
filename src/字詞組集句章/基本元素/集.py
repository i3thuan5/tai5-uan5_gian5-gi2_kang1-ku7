from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.基本元素.組 import 組

class 集:
	內底組 = None
	def __init__(self, 組陣列 = []):
		if not isinstance(組陣列, list):
			raise 型態錯誤('傳入來的組陣列毋是陣列：{0}'.format(str(組陣列)))
		self.內底組 = []
		for 組物件 in 組陣列:
			if not isinstance(組物件, 組):
				raise 型態錯誤('組陣列內底有毋是組的：組陣列＝{0}，組物件＝{1}'.format(str(組陣列), str(組物件)))
			self.內底組.append(組(組物件.內底詞))
	def __eq__(self, 別个):
		return 別个 != None and self.內底組 == 別个.內底組
	def __str__(self):
		return '集：{0}'.format(self.內底組)
	def __repr__(self):
		return self.__str__()
