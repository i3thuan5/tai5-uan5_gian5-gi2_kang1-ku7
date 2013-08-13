from 方音符號吳守禮改良式 import 方音符號吳守禮改良式
from 言語資料庫.公用資料 import 標點符號

class 閩南語字詞綜合標音():
	型體 = None
	臺羅詞組 = None
	臺羅數字調 = None
	臺羅閏調 = None
	通用數字調 = None
	吳守禮方音 = None
	def __init__(self, 字資料):
		self.型體 = 字資料.型
# 		self.臺羅詞組=字資料.音
# 		if isinstance(字資料, 字):
		if 字資料.型 in 標點符號 or 字資料.型==字資料.音:
			self.臺羅數字調 = ''
			self.吳守禮方音 = ''
		else:
			self.臺羅數字調 = 字資料.音
			self.吳守禮方音 = 方音符號吳守禮改良式(字資料.音).產生音標組字式()
	def 轉json格式(self):
		return ('{"型體":"' + self.型體 +
			'","臺羅數字調":"' + self.臺羅數字調 +
			'","吳守禮方音":"' + self.吳守禮方音 + '"}')
	def 標音完整無(self):
		return self.型體 != None and self.臺羅數字調 != None and self.吳守禮方音 != None
	def __repr__(self):
		return self.轉json格式()
	def __str__(self):
		return self.轉json格式()
