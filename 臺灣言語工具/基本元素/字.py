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
from 臺灣言語工具.基本元素.公用變數 import 無音
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.基本元素.公用變數 import 標點符號

class 字:
	型 = None
	音 = None
	def __init__(self, 型, 音 = 無音):
		if not isinstance(型, str):
			raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		try:
			''.join(音)
		except:
			raise 型態錯誤('傳入來的音毋是字串佮字串對：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if 型 == '':
			raise 解析錯誤('傳入來的型是空的！')
		self.型 = 型
		self.音 = 音
	def 有音(self):
		return self.音!=無音 and self.音 not in 標點符號
	def __eq__(self, 別个):
		return isinstance(別个, 字) and self.型 == 別个.型 and self.音 == 別个.音
	def __hash__(self):
		return hash((self.型,self.音))
	def __str__(self):
		return '字：{0} {1}'.format(self.型, self.音)
	def __repr__(self):
		return self.__str__()
