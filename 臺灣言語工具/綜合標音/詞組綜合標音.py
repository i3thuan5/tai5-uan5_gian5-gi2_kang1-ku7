# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.基本元素.組 import 組
from 臺灣言語工具.綜合標音.字綜合標音 import 字綜合標音
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡

class 詞組綜合標音():
	綜合字 = []
	連字音 = ''
	譀鏡 = 物件譀鏡()
	def __init__(self, 字綜合標音型態, 詞或組物件):
		self.綜合字 = []
		self.連字音 = ''
		if not isinstance(字綜合標音型態, type) or \
			not issubclass(字綜合標音型態, 字綜合標音):
			raise 型態錯誤('傳入來的字綜合標音有問題！{0}，{1}'.format(type(字綜合標音型態), str(字綜合標音型態)))
		if isinstance(詞或組物件, 詞):
			詞物件 = 詞或組物件
			for 一字 in 詞物件.內底字:
				self.綜合字.append(字綜合標音型態(一字))
				if not isinstance(self.綜合字[-1], 字綜合標音):
					raise 型態錯誤('傳入來的毋是字綜合標音型態！{0}，{1}'
						.format(type(self.綜合字[-1]), str(self.綜合字[-1])))
			self.連字音 = self.譀鏡.看詞物件音(詞物件)
		elif isinstance(詞或組物件, 組):
			組物件 = 詞或組物件
			for 詞物件 in 組物件.內底詞:
				for 一字 in 詞物件.內底字:
					self.綜合字.append(字綜合標音型態(一字))
					if not isinstance(self.綜合字[-1], 字綜合標音):
						raise 型態錯誤('傳入來的毋是字綜合標音型態！{0}，{1}'
							.format(type(self.綜合字[-1]), str(self.綜合字[-1])))
			self.連字音 = self.譀鏡.看組物件音(組物件)
		else:
			raise 型態錯誤('傳入來的毋是詞或組物件！{0}，{1}'.format(type(詞或組物件), str(詞或組物件)))
	def 轉json格式(self):
		return {"詞組綜合標音":[
			標音.轉json格式() for 標音 in self.綜合字
			], "連字音": self.連字音}
	def 標音完整無(self):
		return all([標音.標音完整無() for 標音 in self.綜合標音])
	def __repr__(self):
		return self.轉json格式()
	def __str__(self):
		return self.轉json格式()
	def __eq__(self, 別个):
		return isinstance(別个, 詞組綜合標音) and \
			self.綜合字 == 別个.綜合字 and self.連字音 == 別个.連字音
