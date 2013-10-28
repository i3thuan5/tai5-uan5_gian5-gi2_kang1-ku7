from 斷詞標音.文字辭典 import 文字辭典
from 字詞組集句章.基本元素.公用變數 import 無音
from 斷詞標音.型音點 import 型音點
from 字詞組集句章.基本元素.詞 import 詞
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤

class 現掀辭典(文字辭典):
	大細 = None
	def __init__(self, 大細):
		self.大細 = 大細
		self.條目 = []
	def 加詞(self, 詞物件):
		if not isinstance(詞物件, 詞):
			raise 型態錯誤('傳入來的毋是詞物件：{0}'.format(str(詞物件)))
		if len(詞物件.內底字) <= self.大細:
			self.條目.append(詞物件)
		return

	def 查詞(self, 詞物件):
		if not isinstance(詞物件, 詞):
			raise 型態錯誤('傳入來的毋是詞物件：{0}'.format(str(詞物件)))
		結果=[]
		for 所在 in range(len(詞物件.內底字)):
			結果.append(set())
		for 辭典條 in self.條目:
			if self.查詞有仝無(詞物件, 辭典條):
				結果[len(辭典條.內底字)-1].add(辭典條)
		return 結果

	def 查詞有仝無(self, 詞物件, 辭典條):
		if len(詞物件.內底字) < len(辭典條.內底字):
			return False
		for 第幾字 in range(len(辭典條.內底字)):
			字物件 = 詞物件.內底字[第幾字]
			辭典條字物件 = 辭典條.內底字[第幾字]
			有著=False
			if 字物件.音 != 無音:
				if 字物件 == 辭典條字物件:
					有著 = True
			elif 字物件.型 == 辭典條字物件.型 or 字物件.型 == 辭典條字物件.音:
				有著 = True
			if not 有著:
				return False
		return True
