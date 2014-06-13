# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國103年 意傳文化科技
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
from unittest.case import TestCase
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔
from 臺灣言語工具.基本元素.章 import 章
from 臺灣言語工具.解析整理.參數錯誤 import 參數錯誤
from math import log10
from math import pow

class 語句連詞(TestCase):
	# 無看過的詞的出現機率，佮srilm仝款當做負的無限
	無看過 = -99
	_網仔 = 詞物件網仔()
	def __init__(self, 上濟詞數):
		if 上濟詞數 <= 0:
			raise 參數錯誤('詞數愛是正整數，傳入來的是{0}'.format(上濟詞數))
		self.上濟詞數 = 上濟詞數
		self.總數表 = [0] * self.上濟詞數
		self.連詞表 = {}
	def 總數(self):
		return self.總數表
	def 數量(self, 連詞):
		數量表 = []
		for 長度 in range(min(self.上濟詞數, len(連詞))):
			組合 = tuple(連詞[-1 - 長度:])
			if 組合 in self.連詞表:
				數量表.append(self.連詞表[組合])
			else:
				數量表.append(0)
		return 數量表
	def 機率(self, 連詞):
		數量表 = self.數量(連詞)
		機率表 = []
		for 數, 總 in zip(數量表, self.總數表):
			if 數 == 0:
				機率表.append(self.無看過)
			else:
				機率表.append(self.對數(數 / 總))
		return 機率表
	def 條件(self, 連詞):
		'''條件機率'''
		數量表 = self.數量(連詞)
		前數量表 = self.數量(連詞[:-1])
		條件表 = []
# 		print('數量表', 數量表)
# 		print('前數量表', 前數量表, self.總數表[:1],)
		for 數, 前 in zip(數量表, self.總數表[:1] + 前數量表):
			if 數 == 0:
				條件表.append(self.無看過)
			else:
				條件表.append(self.對數(數 / 前))
# 		print('條件表',條件表)
		return 條件表
	def 看(self, 物件):
		if isinstance(物件, 章):
			self.看章物件(物件)
			return
		詞陣列 = [None] + self._網仔.網出詞物件(物件) + [None]
		for 長度 in range(1, self.上濟詞數 + 1):
			for 所在 in range(len(詞陣列) - 長度 + 1):
				self.總數表[長度 - 1] += 1
				組合 = tuple(詞陣列[所在:所在 + 長度])
				if 組合 not in self.連詞表:
					self.連詞表[組合] = 1
				else:
					self.連詞表[組合] += 1
		self.連詞表[(None,)] -= 1
		return
	def 看章物件(self, 章物件):
		for 句物件 in 章物件.內底句:
			self.看(句物件)
		return
	def 對數(self, 數字):
		return log10(數字)
	def 指數(self, 數字):
		return pow(10.0, 數字)
