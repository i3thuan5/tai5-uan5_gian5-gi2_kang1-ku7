from 閩南資料.字 import 字

class 詞(字):
	下跤 = None
	字佇詞排名=None
	字佇詞賰幾字=None
	def __init__(self, 型, 音, 文章標點處理工具):
# 		super(字, self).__init__(型, 音)
		if 音==None:
			音=''
		super().__init__(型, 音)
		self.標點處理工具 = 文章標點處理工具
		if 文章標點處理工具!=None:
			self.結構化()
	def 結構化(self):
# 		漢字數量 = self.標點處理工具.計算漢字語句漢字數量(self.型)
# 		音標數量 = self.標點處理工具.計算音標語句音標數量(self.音)
# 		print(str(漢字數量 )+" "+ str(音標數量))
# 		if 漢字數量 != 音標數量:
# 			return
		漢字陣列 = self.標點處理工具.分離漢字(self.型)
		遏袂整理音標陣列 = self.標點處理工具.切開語句(self.音)
		音標陣列 = []
		self.字佇詞排名=[]
		self.字佇詞賰幾字=[]
		for 遏袂整理音標 in 遏袂整理音標陣列:
			if 遏袂整理音標 != ' ' and 遏袂整理音標 != '':
				單獨音標=遏袂整理音標.replace('--','-').split('-')
				排名=0
				顛倒排名=len(單獨音標)
				for 音標 in 單獨音標:
					音標陣列.append(音標)
					self.字佇詞排名.append(排名)
					self.字佇詞賰幾字.append(顛倒排名)
					排名+=1
					顛倒排名-=1
# 		print(音標陣列)
# 		print(str(len(漢字陣列)) + " " + str(len(音標陣列)))
		if len(漢字陣列) != len(音標陣列):
			self.字佇詞排名=None
			self.字佇詞賰幾字=None
			return
		self.下跤 = []
		for i in range(len(漢字陣列)):
			self.下跤.append(字(漢字陣列[i], 音標陣列[i]))
	def 揣出上適合的詞(self, 欲揣的詞,已經使用):
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
				if 已經使用[i + j]:
					仝款 = False
				if not 仝款:
					break
			if 仝款:
				for j in range(len(欲揣的詞.下跤)):
					已經使用[i + j] = True
				return (i, i + len(欲揣的詞.下跤))
		return (0, 0)
# 	def __eq__(self,other):
# 		print("hi")
# 		return self.型==other.型 and self.音==other.音
def 用字產生詞(字陣列):
	型=''
	音=''
	for 字 in 字陣列:
		型+=字.型
		音+='-'+字.音
	上尾詞=詞(型, 音[1:], None)
	上尾詞.下跤=字陣列
	return 上尾詞
		
	

