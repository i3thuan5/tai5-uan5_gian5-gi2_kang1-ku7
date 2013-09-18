
from 字詞組集句章.基本元素.詞 import 詞
from 字詞組集句章.基本元素.組 import 組
from 字詞組集句章.綜合標音.字綜合標音 import 字綜合標音
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.基本元素.公用變數 import 無音

class 詞組綜合標音():
	綜合字 = []
	連字音 = ''
	def __init__(self, 字綜合標音型態, 詞或組物件):
#		self.綜合字 = []
#		self.連字音 = ''
		if len(self.綜合字)!=0:
			self.綜合字.insert(0, '@@')
			raise RuntimeError('!!!!!! 綜合字＝{0}，{1}'.format(self.綜合字,self.連字音))
		if isinstance(詞或組物件, 詞):
			詞物件=詞或組物件
			self.連字音=self.提著詞的連字音(詞物件)
			for 一字 in 詞物件.內底字:
				self.綜合字.append(字綜合標音型態(一字))
				if not isinstance(self.綜合字[-1], 字綜合標音):
					raise 型態錯誤('傳入來的毋是字綜合標音型態！{0}，{1}'
						.format(type(self.綜合字[-1]), str(self.綜合字[-1])))
		elif isinstance(詞或組物件, 組):
			組物件=詞或組物件
			self.連字音=self.提著組的連字音(組物件)
			for 詞物件 in 組物件.內底詞:
				for 一字 in 詞物件.內底字:
					self.綜合字.append(字綜合標音型態(一字))
					if not isinstance(self.綜合字[-1], 字綜合標音):
						raise 型態錯誤('傳入來的毋是字綜合標音型態！{0}，{1}'
							.format(type(self.綜合字[-1]), str(self.綜合字[-1])))
		else:
			raise 型態錯誤('傳入來的毋是詞或組物件！{0}，{1}'.format(type(詞或組物件), str(詞或組物件)))
	def 轉json格式(self):
		return ('{"綜合標音":[' +
			','.join([標音.轉json格式() for 標音 in self.綜合標音 if 標音.標音完整無()]) +
			'],"詞組":"' + self.詞組 + '"}')
	def 標音完整無(self):
		return all([標音.標音完整無() for 標音 in self.綜合標音])
	def __repr__(self):
		return self.轉json格式()
	def __str__(self):
		return self.轉json格式()
	def __eq__(self, 別个):
		return 別个 != None and self.綜合字 == 別个.綜合字 and self.連字音 == 別个.連字音
	def 提著詞的連字音(self,詞物件):
		if not isinstance(詞物件, 詞):
			raise 型態錯誤('傳入來的毋是詞物件！{0}，{1}'.format(type(詞物件), str(詞物件)))
		音陣列=[]
		for 一字 in 詞物件.內底字:
			if 一字.音!=無音:
				音陣列.append(一字.音)
		return '-'.join(音陣列)	
	
	def 提著組的連字音(self,組物件):
		if not isinstance(組物件, 組):
			raise 型態錯誤('傳入來的毋是組物件！{0}，{1}'.format(type(組物件), str(組物件)))
		音陣列=[]
		for 詞物件 in 組物件.內底詞:
			音=self.提著詞的連字音(詞物件)
			if 音!=無音:
				音陣列.append(音)
		return ' '.join(音陣列)
		
		
