from 斷詞標音.文字辭典 import 文字辭典
from 字詞組集句章.基本元素.公用變數 import 無音
from 斷詞標音.型音點 import 型音點
from 字詞組集句章.基本元素.詞 import 詞

class 型音辭典(文字辭典):
	表 = None
	def __init__(self):
		self.表 = 型音點()
	def 加詞(self, 詞物件):
		self.加詞佇點(詞物件, 0, self.表)
		return

	def 查詞(self, 詞物件):
		結果 = self.查詞佇點(詞物件, 0, self.表)
		for 幾个 in range(len(結果), len(詞物件.內底字)):
			結果.append(set())
			幾个 = 幾个
		return 結果

	def 加詞佇點(self, 詞物件, 第幾字, 點):
		if 第幾字 == len(詞物件.內底字):
			點.條.add(詞(詞物件.內底字))
			return
		字物件 = 詞物件.內底字[第幾字]
		if 字物件.型 not in 點.表:
			點.表[字物件.型] = 型音點()
		self.加詞佇點(詞物件, 第幾字 + 1, 點.表[字物件.型])
		if 字物件.音 != 無音:
			if 字物件.音 not in 點.表:
				點.表[字物件.音] = 型音點()
			self.加詞佇點(詞物件, 第幾字 + 1, 點.表[字物件.音])
			if 字物件 not in 點.表:
				點.表[字物件] = 型音點()
			self.加詞佇點(詞物件, 第幾字 + 1, 點.表[字物件])
		return

	def 查詞佇點(self, 詞物件, 第幾字, 點):
		這馬答案 = []
# 		for 所在 in range(第幾字):
# 			這馬答案.append(set())
		if 第幾字 != 0:
			這馬答案.append(點.條)
# 		print(第幾字, '開始', 這馬答案)
		if 第幾字 == len(詞物件.內底字):
			return 這馬答案
# 		答案 = [這馬答案]
		字物件 = 詞物件.內底字[第幾字]
		if 字物件.音 != 無音:
			if 字物件 in 點.表:
				這馬答案.extend(self.查詞佇點(詞物件, 第幾字 + 1, 點.表[字物件]))
		elif 字物件.型 in 點.表:
			這馬答案.extend(self.查詞佇點(詞物件, 第幾字 + 1, 點.表[字物件.型]))

# 		print(第幾字, '結束', 這馬答案)
		return 這馬答案
# 		if 字物件.音 != 無音 and 字物件.音 in 點.表:
# 			答案.append(self.查詞佇點(詞物件, 第幾字 + 1, 點.表[字物件.型]))
# 		if len(答案)==0:
# 			return []
# 		上尾答案=答案[0]
# 		for 小答案 in 答案[1:]:
# 			for 所在 in range(len(上尾答案),len(小答案)):
# 				上尾答案.append(set())
# 			for 所在 in range(len(小答案)):
# 				上尾答案[所在].union(小答案[所在])
# 		return 上尾答案
