from 閩南資料.字 import 字

class 詞(字):
	下跤 = None
	def __init__(self, 型, 音, 文章標點處理工具):
# 		super(字, self).__init__(型, 音)
		super().__init__(型, 音)
		self.標點處理工具 = 文章標點處理工具
		self.結構化()
	def 結構化(self):
		漢字數量 = self.標點處理工具.計算漢字語句漢字數量(self.型)
		音標數量 = self.標點處理工具.計算音標語句音標數量(self.音)
		if 漢字數量 != 音標數量:
			return
		漢字陣列 = self.標點處理工具.分離漢字(self.型)
		音標陣列 = self.標點處理工具.分離漢字(self.音)
		if len(漢字陣列) != len(音標陣列):
			return
		self.下跤 = []
		for i in range(len(漢字陣列)):
			self.下跤.append(字(漢字陣列[i], 音標陣列[i]))


