
from 資料庫.查資料庫 import 查資料庫
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.基本元素.章 import 章
from 字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡
import Pyro4

class 國語翻譯():
	查資料 = 查資料庫()
	標音工具 = Pyro4.Proxy("PYRONAME:內部自動標音")
	# 台華詞典用
	譀鏡 = 物件譀鏡()
	def 翻譯章物件(self, 原來腔口, 欲揣腔口, 章物件):
		句陣列 = []
		for 句物件 in 章物件.內底句:
			集陣列 = []
			for 集物件 in 句物件.內底集:
				組陣列 = []
				for 組物件 in 集物件.內底組:
# 						詞陣列=[]
					for 詞物件 in 組物件.內底詞:
						組陣列.extend(
							self.查資料.型體翻譯著(原來腔口,
							self.譀鏡.看型(詞物件), 欲揣腔口))
# 						組陣列.append(組(詞陣列))
				if len(組陣列)==0:
					self.標音工具.語句標音(欲揣腔口, self.譀鏡.看型(詞物件))
				else:
					集陣列.append(集(組陣列))
			句陣列.append(句(集陣列))
		翻譯了章物件 = 章(句陣列)
		return 翻譯了章物件
