from 字詞組集句章.解析整理工具.集內組照排 import 集內組照排
from 斷詞標音.辭典條目 import 辭典條目

class 排標音結果:
	組照排 = 集內組照排()
	條目 = 辭典條目()
	文讀層 = None
	白話層 = None
	def __init__(self):
		self.文讀層 = self.條目.文讀層
		self.白話層 = self.條目.白話層

	def 照白文層排(self, 物件):
		return self.組照排.排好(self.白文照排, 物件)

	def 白文照排(self, 組物件):
		詞物件 = 組物件.內底詞[0]
		白 = 0
		文 = 0
		流水號=0
		if hasattr(詞物件, '屬性'):
			if self.白話層 in 詞物件.屬性:
				白 = -詞物件.屬性[self.白話層]
			if self.文讀層 in 詞物件.屬性:
				文 = 詞物件.屬性[self.文讀層]
			if '流水號' in 詞物件.屬性:
				流水號 = 詞物件.屬性['流水號']
		return (白, 文,流水號)
