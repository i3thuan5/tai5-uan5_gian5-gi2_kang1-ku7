from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.綜合標音.詞組綜合標音 import 詞組綜合標音
from 字詞組集句章.綜合標音.字綜合標音 import 字綜合標音

class 集綜合標音():
	綜合詞組 = []
	def __init__(self, 字綜合標音型態, 集物件):
		if not isinstance(字綜合標音型態, 字綜合標音):
			raise 型態錯誤('傳入來的毋是字綜合標音型態！{0}，{1}'.format(type(字綜合標音型態), str(字綜合標音型態)))
		if not isinstance(集物件, 集):
			raise 型態錯誤('傳入來的毋是集物件！{0}，{1}'.format(type(集物件), str(集物件)))
		for 組物件 in 集物件.內底組:
			self.綜合集.append(詞組綜合標音(字綜合標音型態, 組物件))
