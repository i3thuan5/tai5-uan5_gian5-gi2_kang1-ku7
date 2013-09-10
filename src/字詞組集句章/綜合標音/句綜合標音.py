from 閩南資料.詞 import 詞
from 字詞集句章.綜合標音.詞組綜合標音 import 詞組綜合標音
class 句綜合標音():
	綜合標音佮詞組陣列=None
	def __init__(self,標音,綜合標音):
		self.綜合標音佮詞組陣列=[]
		for 規組字音 in 標音:
			self.綜合標音佮詞組陣列.append([])
			for 一組字音 in 規組字音: 
				綜合標音陣列=[]
				if isinstance(一組字音, 詞) and 一組字音.下跤!=None:#標點符號會當作是詞，但是下跤無物件
					綜合標音陣列=[綜合標音(一个字)
						for 一个字 in 一組字音.下跤]
				else:
					綜合標音陣列.append(綜合標音(一組字音))
				結果=詞組綜合標音(綜合標音陣列,一組字音.音)
				if 結果.標音完整無():
					self.綜合標音佮詞組陣列[-1].append(結果)