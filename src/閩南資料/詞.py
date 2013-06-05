from 閩南資料.字 import 字

class 詞(字):
	下跤 = None
	def __init__(self, 型, 音, 文章標點處理工具):
# 		super(字, self).__init__(型, 音)
		super().__init__(型, 音)
		self.標點處理工具 = 文章標點處理工具
		self.結構化()
	def 結構化(self):
# 		漢字數量 = self.標點處理工具.計算漢字語句漢字數量(self.型)
# 		音標數量 = self.標點處理工具.計算音標語句音標數量(self.音)
# 		print(str(漢字數量 )+" "+ str(音標數量))
# 		if 漢字數量 != 音標數量:
# 			return
		漢字陣列 = self.標點處理工具.分離漢字(self.型)
		遏袂整理音標陣列 = self.標點處理工具.切開語句(self.音.replace('-', ' '))
		音標陣列 = []
		for 遏袂整理音標 in 遏袂整理音標陣列:
			if 遏袂整理音標 != ' ' and 遏袂整理音標 != '':
				音標陣列.append(遏袂整理音標)
# 		print(音標陣列)
# 		print(str(len(漢字陣列)) + " " + str(len(音標陣列)))
		if len(漢字陣列) != len(音標陣列):
			return
		self.下跤 = []
		for i in range(len(漢字陣列)):
			self.下跤.append(字(漢字陣列[i], 音標陣列[i]))
	def 揣出上適合的詞(self, 欲揣的詞):
# 		print( 欲揣的詞 ,end=' ')
		if 欲揣的詞.下跤==None:
			return (0,0)
		for i in range(len(self.下跤) - len(欲揣的詞.下跤)):
			仝款 = True
			for j in range(len(欲揣的詞.下跤)):
# 				print(i,end=' ')
# 				print(j)
# 				if not self.下跤[i + j] == 欲揣的詞.下跤[j]:
				if not (self.下跤[i + j].型 == 欲揣的詞.下跤[j].型 and 
					self.下跤[i + j].音 == 欲揣的詞.下跤[j].音):
					仝款 = False
				if not 仝款:
					break
			if 仝款:
				空字 = 字(None, None)
				for j in range(len(欲揣的詞.下跤)):
					self.下跤[i + j] = 空字
				return (i, i + len(欲揣的詞.下跤))
		return (0, 0)
# 	def __eq__(self,other):
# 		print("hi")
# 		return self.型==other.型 and self.音==other.音


