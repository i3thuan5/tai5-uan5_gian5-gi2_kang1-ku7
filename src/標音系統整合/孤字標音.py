from 閩南資料.字 import 字
from 閩南資料.詞 import 詞
from 華語台語雙語語料庫系統.文章標點處理工具 import 文章標點處理工具
from 方音符號吳守禮改良式 import 方音符號吳守禮改良式
#愛整合入標音整合
#def 孤字標音(詞標音):
#	for 孤詞 in 詞標音:
#		for 
#		臺羅音陣列.append(詞標音.音)
#	臺羅音=
class 閩南語綜合標音():
	型體=None
	臺羅詞組=None
	臺羅數字調=None
	臺羅閏調=None
	通用數字調=None
	吳守禮方音=None
	def __init__(self,字資料):
		self.型體=字資料.型
#		self.臺羅詞組=字資料.音
#		if isinstance(字資料, 字):
		self.臺羅數字調=字資料.音
		self.吳守禮方音=方音符號吳守禮改良式(字資料.音).音標
	def 轉json格式(self):
		return ('{"型體":"'+self.型體+
			'","臺羅數字調":"'+self.臺羅數字調+
			'","吳守禮方音":"'+self.吳守禮方音+'"}')
	def __repr__(self):
		return self.轉json格式()
	def __str__(self):
		return self.轉json格式()

class 綜合標音佮詞組():
	綜合標音=None
	詞組=None
	def __init__(self,綜合標音,詞組):
		self.綜合標音=綜合標音
		self.詞組=詞組
	def 轉json格式(self):
		return ('{"綜合標音":['+
			','.join([標音.轉json格式() for 標音 in self.綜合標音])+
			'],"詞組":"'+self.詞組+'"}')
	def __repr__(self):
		return self.轉json格式()
	def __str__(self):
		return self.轉json格式()

class 綜合標音句():
	綜合標音佮詞組陣列=None
	def __init__(self,標音,綜合標音):
		self.綜合標音佮詞組陣列=[]
		for 規組字音 in 標音:
			self.綜合標音佮詞組陣列.append([])
			for 一組字音 in 規組字音: 
				綜合標音陣列=[]
				if isinstance(一組字音, 詞):
					綜合標音陣列=[綜合標音(一个字)
						for 一个字 in 一組字音.下跤]
				else:
					綜合標音陣列.append(綜合標音(一組字音))
				結果=綜合標音佮詞組(綜合標音陣列,一組字音.音)
				self.綜合標音佮詞組陣列[-1].append(結果)

if __name__ == '__main__':
	標點處理工具 = 文章標點處理工具()
	標點處理工具.標點符號={}
	詞標音=[[詞('我','gua2',標點處理工具)],
		[詞('愛','ai3',標點處理工具)],
		[詞('大','tua7',標點處理工具)],
		[詞('美女','sui2-boo2',標點處理工具),詞('美女','mi2-lu2',標點處理工具)]]
	print(詞標音)
	標音句=綜合標音句(詞標音,閩南語綜合標音)
	print(標音句.綜合標音佮詞組陣列)