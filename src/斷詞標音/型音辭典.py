from 斷詞標音.文字辭典 import 文字辭典
from 字詞組集句章.基本元素.公用變數 import 無音
from 斷詞標音.型音點 import 型音點

class 型音辭典(文字辭典):
	表 = None
	def __init__(self):
		self.表 = 型音點()
	def 加詞(self, 詞物件):
		self.加詞佇點(詞物件, 0, self.表)
		return
	
	def 查詞(self, 詞物件):
		self.加詞佇點(詞物件, 0, self.表)

	def 加詞佇點(self, 詞物件, 第幾字, 點):
		if 第幾字 == len(詞物件.內底字):
			點.條.append(詞物件)
		字物件 = 詞物件.內底字[第幾字]
		if 字物件.型 not in 點.表:
			點.表[字物件.型] = 型音點()
		self.加詞佇點(詞物件, 第幾字 + 1, 點.表[字物件.型])
		if 字物件.音 != 無音 and 字物件.音 not in 點.表:
			點.表[字物件.音] = []
		self.加詞佇點(詞物件, 第幾字 + 1, 點.表[字物件.型])
		return

	def 查詞佇點(self, 詞物件, 第幾字, 點):
		if 第幾字 == len(詞物件.內底字):
			return 點.條
		答案 = []
		字物件 = 詞物件.內底字[第幾字]
		if 字物件.型 in 點.表:
			答案.append(self.查詞佇點(詞物件, 第幾字 + 1, 點.表[字物件.型]))
		if 字物件.音 != 無音 and 字物件.音 in 點.表:
			答案.append(self.查詞佇點(詞物件, 第幾字 + 1, 點.表[字物件.型]))
		return 答案
