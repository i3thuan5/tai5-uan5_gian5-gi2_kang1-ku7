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
from math import log10
from math import pow
from abc import ABCMeta
from abc import abstractmethod
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔

class 語句連詞(metaclass=ABCMeta):
	# 無看過的詞的出現機率，佮srilm仝款當做負的無限
	無看過 = -99
	_分析器 = 拆文分析器()
	_開始 = 詞([_分析器.建立字物件('<s>')])
	_結束 = 詞([_分析器.建立字物件('</s>')])
	_網仔 = 詞物件網仔()
	def 開始(self):
		return self._開始
	def 結束(self):
		return self._結束 
	def 對數(self, 數字):
		return log10(數字)
	def 指數(self, 數字):
		return pow(10.0, 數字)
	@abstractmethod
	def 上濟詞數(self):
		pass
	def 評分(self, 物件):
		詞陣列 = [self.開始()] + self._網仔.網出詞物件(物件) + [self.結束()]
		return self.評詞陣列分(詞陣列, 開始的所在=1)
	@abstractmethod
	def 評詞陣列分(self, 詞陣列, 開始的所在=0):
		pass
