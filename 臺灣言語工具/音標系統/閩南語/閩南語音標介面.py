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
from abc import ABCMeta, abstractmethod

class 閩南語音標介面(metaclass=ABCMeta):
	#消警告用
	頂層=ABCMeta
	聲 = None
	韻 = None
	調 = 1
	音標 = None
	def 分析聲韻調(self, 音標):
		self.音標 = ''
		一開始 = True
		for 字元 in 音標:
			if 一開始:
				字元 = 字元.lower()
				一開始 = False
			if 字元 == '.':
				字元 = 'o'
			elif 字元 == 'N':
				字元 = 'nn'
			self.音標 += 字元
		無調號音標 = ''
		前一字元 = ''
		愛結束矣 = False
		音標是著的 = True
		for 字元 in self.音標 :
			if 字元.isnumeric():
				if self.調 == 1:
					self.調 = int(字元)
				else:
					音標是著的 = False
				愛結束矣 = True
			elif 愛結束矣:
				音標是著的 = False
			elif 字元 in self.聲調符號表:
				無調字元 , self.調 = self.聲調符號表[字元]
				無調號音標 += 前一字元 + 無調字元
				前一字元 = ''
			elif 前一字元 + 字元 in self.聲調符號表:
				無調字元 , self.調 = self.聲調符號表[前一字元 + 字元]
				無調號音標 += 無調字元
				前一字元 = ''				
			else:
				無調號音標 += 前一字元
				前一字元 = 字元
		無調號音標 += 前一字元
		聲韻符合 = False
		for 聲母 in self.聲母表:
			for 韻母 in self.韻母表:
				if 聲母 + 韻母 == 無調號音標:
					self.聲 = 聲母
					self.韻 = 韻母
					聲韻符合 = True
		if not 聲韻符合:
			音標是著的 = False
		elif self.韻.endswith('p') or self.韻.endswith('t') or self.韻.endswith('k') or self.韻.endswith('h'):
			if self.調 == 1:
				self.調 = 4
			elif self.調 != 4 and self.調 != 8:
				音標是著的 = False
		if 音標是著的:					
			print('聲母=' + self.聲 + ' 韻母=' + self.韻 + ' 調＝' + str(self.調))
			self.音標 = self.聲 + self.韻 + str(self.調)
		else:
			print('不合法 原音標＝' + 音標)
			self.音標 = None
		return self.音標
	def 標準音標(self):
		return self.轉換到臺灣閩南語羅馬字拼音()
	@abstractmethod
	def 轉換到臺灣閩南語羅馬字拼音(self):
		pass
