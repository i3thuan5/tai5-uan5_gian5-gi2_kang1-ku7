# -*- coding: utf-8 -*-
from 臺灣言語工具.基本元素.公用變數 import 無音
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.基本元素.字 import 字
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.綜合標音.字綜合標音 import 字綜合標音
from 臺灣言語工具.基本元素.公用變數 import 標點符號

class 閩南語字綜合標音(字綜合標音):
	型體 = None
	臺羅數字調 = None
	臺羅閏號調 = None
	通用數字調 = None
	吳守禮方音 = None
	def __init__(self, 字物件, 音標一定愛著=False):
		if not isinstance(字物件, 字):
			raise 型態錯誤('傳入來的毋是字物件！{0}，{1}'.format(type(字物件), str(字物件)))
		self.型體 = 字物件.型
		if 字物件.音 == 無音:
			self.臺羅數字調 = 無音
			self.吳守禮方音 = 無音
			self.臺羅閏號調 = 無音
			self.通用數字調 = 無音
		elif 字物件.音 in 標點符號:
			self.臺羅數字調 = 字物件.音
			self.臺羅閏號調 = 字物件.音
			self.通用數字調 = 字物件.音
			self.吳守禮方音 = 無音
		else:
			臺羅 = 臺灣閩南語羅馬字拼音(字物件.音)
			self.臺羅數字調 = 臺羅.音標
			self.吳守禮方音 = 臺羅.產生吳守禮方音物件().產生音標組字式()
			self.臺羅閏號調 = 臺羅.轉閏號調()
			self.通用數字調 = 臺羅.轉通用拼音()
			if 音標一定愛著 and not self.標音完整無():
				raise 解析錯誤('音標無合法：{0}，{1}，{2}，{3}，{4}，{5}'.
					format(字物件, self.型體, self.臺羅數字調, self.吳守禮方音,
					self.臺羅閏號調, self.通用數字調,))
	def 轉json格式(self):
		return {"型體":self.型體, "臺羅數字調":self.臺羅數字調,
			"臺羅閏號調":self.臺羅閏號調, "通用數字調":self.通用數字調,
			"吳守禮方音":self.吳守禮方音}
	def 標音完整無(self):
		return (self.型體 != None and self.臺羅數字調 != None
			and self.吳守禮方音 != None and self.臺羅閏號調 != None and self.通用數字調 != None)
	def __repr__(self):
		return self.轉json格式()
	def __str__(self):
		return self.轉json格式()
	def __eq__(self, 別个):
		return isinstance(別个, 閩南語字綜合標音) and self.型體 == 別个.型體 and \
			self.臺羅數字調 == 別个.臺羅數字調 and self.臺羅閏號調 == 別个.臺羅閏號調 and \
			self.通用數字調 == 別个.通用數字調 and self.吳守禮方音 == 別个.吳守禮方音
