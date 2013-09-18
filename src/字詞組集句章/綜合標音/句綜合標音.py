from 字詞組集句章.綜合標音.集綜合標音 import 集綜合標音
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.基本元素.句 import 句

class 句綜合標音():
	綜合集 = []
	def __init__(self, 字綜合標音型態, 句物件):
		self.綜合集 = []
		if not isinstance(句物件, 句):
			raise 型態錯誤('傳入來的毋是句物件！{0}，{1}'.format(type(句物件), str(句物件)))
		for 集物件 in 句物件.內底集:
			self.綜合集.append(集綜合標音(字綜合標音型態, 集物件))
	def __eq__(self, 別个):
		return isinstance(別个, 句綜合標音) and self.綜合集 == 別个.綜合集
