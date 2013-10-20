
from 字詞組集句章.基本元素.詞 import 詞

class 動態規劃斷詞標音:
	def 斷詞標音(self, 辭典, 組物件):
		字陣列 = []
		for 詞物件 in 組物件.內底詞:
			for 字物件 in 詞物件.內底字:
				字陣列.append(字物件)
		斷詞結果 = []
		for 所在 in range(len(字陣列)):
			斷詞結果.append(辭典.查詞(詞(字陣列[所在:所在 + 辭典.大細])))
		
