from 字詞組集句章.基本元素.公用變數 import 無音
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.綜合標音.字綜合標音 import 字綜合標音
from 字詞組集句章.基本元素.公用變數 import 標點符號

class 國語字綜合標音(字綜合標音):
	型體 = None
	注音符號 = None
	def __init__(self, 字物件):
		if not isinstance(字物件, 字):
			raise 型態錯誤('傳入來的毋是字物件！{0}，{1}'.format(type(字物件), str(字物件)))
		self.型體 = 字物件.型
		if 字物件.音 == 無音:
			self.注音符號 = 無音
		elif 字物件.音 in 標點符號:
			self.注音符號 = 無音
		else:
			if len(字物件.音) == 1:
				self.注音符號 = '⿳' + 字物件.音 + ' '
			else:
				self.注音符號 = '⿳' * (len(字物件.音) - 1) + 字物件.音
			if not self.標音完整無():
				raise 解析錯誤('音標無合法：{0}，{1}，{2}'.
					format(字物件, self.型體, self.注音符號))
	def 轉json格式(self):
		return {"型體":self.型體, "注音符號":self.注音符號}
	def 標音完整無(self):
		return (self.型體 != None and self.注音符號 != None)
	def __repr__(self):
		return self.轉json格式()
	def __str__(self):
		return self.轉json格式()
	def __eq__(self, 別个):
		return isinstance(別个, 國語字綜合標音) and self.型體 == 別个.型體 and \
			self.注音符號 == 別个.注音符號
