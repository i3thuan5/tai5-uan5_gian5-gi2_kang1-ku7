from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.基本元素.公用變數 import 無音
from 字詞組集句章.基本元素.公用變數 import 本調符號
from 字詞組集句章.解析整理工具.字物件篩仔 import 字物件篩仔
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤


class 臺羅變調暫時處理:
	分析器=拆文分析器()
	本調記號=分析器.產生對齊字(本調符號, 無音)
	篩仔=字物件篩仔()
	
	變調規則={'1':'7','2':'1','3':'2','5':'7','7':'3',}
	def 變調(self,句物件):
		字陣列=self.篩仔.篩出字物件(句物件)
		尾本調=[]
		for 所在 in range(len(字陣列)):
			if 所在+1<len(字陣列):
				if 字陣列[所在+1]==self.本調記號:
					尾本調.append(True)
				else:
					尾本調.append(False)
			else:
				尾本調.append(True)
		for 所在 in range(len(字陣列)):
			if not 尾本調[所在]:
				if 字陣列[所在].音!='':
					臺羅=self.轉臺羅韻調(臺灣閩南語羅馬字拼音(字陣列[所在].音))
					字陣列[所在].音=臺羅.音標
		return 字陣列

	def 轉臺羅韻調(self,臺羅):
		if 臺羅.韻.endswith('h'):
			if 臺羅.調=='4':
				臺羅.調='2'
			elif 臺羅.調=='8':
				臺羅.調='3'
			else:
				raise 解析錯誤('喉塞尾調錯誤！！')
			臺羅.韻=臺羅.韻[:-1]
		elif 臺羅.韻.endswith('p') or 臺羅.韻.endswith('t') or 臺羅.韻.endswith('k'):
			if 臺羅.調=='4':
				臺羅.調='8'
			elif 臺羅.調=='8':
				臺羅.調='10'
			else:
				raise 解析錯誤('入尾調錯誤！！')
		else:
			if 臺羅.調 in self.變調規則:
				臺羅.調=self.變調規則[臺羅.調]
			else:
				raise 解析錯誤('非入調錯誤！！')
		臺羅.做音標()
		return 臺羅
			
		
				
			
				
				