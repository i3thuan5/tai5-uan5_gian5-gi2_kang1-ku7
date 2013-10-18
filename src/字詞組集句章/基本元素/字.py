from 字詞組集句章.基本元素.公用變數 import 無音
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤

class 字:
	型 = None
	音 = None
	def __init__(self, 型, 音 = 無音):
		if not isinstance(型, str):
			raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if not isinstance(音, str):
			raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if 型 == '':
			raise 解析錯誤('傳入來的型是空的！')
		self.型 = 型
		self.音 = 音
	def __eq__(self, 別个):
		return isinstance(別个, 字) and self.型 == 別个.型 and self.音 == 別个.音
	def __hash__(self):
		return hash((self.型,self.音))
	def __str__(self):
		return '字：{0} {1}'.format(self.型, self.音)
	def __repr__(self):
		return self.__str__()
