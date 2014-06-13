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
from 臺灣言語工具.基本元素.字 import 字
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.基本元素.組 import 組
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.基本元素.章 import 章
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.程式掠漏 import 程式掠漏

class 詞物件網仔:
	_掠漏 = 程式掠漏()
	def 網字(self, 字物件):
		self._掠漏.毋是字物件就毋著(字物件)
		詞物件 = 詞()
		詞物件.內底字.append(字物件)
		return [詞物件]
	def 網詞(self, 詞物件):
		self._掠漏.毋是詞物件就毋著(詞物件)
		return [詞物件]
	def 網組(self, 組物件):
		self._掠漏.毋是組物件就毋著(組物件)
		return 組物件.內底詞
	def 網集(self, 集物件):
		self._掠漏.毋是集物件就毋著(集物件)
		if len(集物件.內底組) == 0:
			return []
		if len(集物件.內底組) > 1:
			raise 解析錯誤('內底組毋焦一个！！{0}'.format(str(集物件)))
		return self.網組(集物件.內底組[0])
	def 網句(self, 句物件):
		self._掠漏.毋是句物件就毋著(句物件)
		詞陣列 = []
		for 集物件 in 句物件.內底集:
			詞陣列.extend(self.網集(集物件))
		return 詞陣列
	def 網章(self, 章物件):
		self._掠漏.毋是章物件就毋著(章物件)
		詞陣列 = []
		for 句物件 in 章物件.內底句:
			詞陣列.extend(self.網句(句物件))
		return 詞陣列
	def 網出詞物件(self, 物件):
		if isinstance(物件, 字):
			return self.網字(物件)
		if isinstance(物件, 詞):
			return self.網詞(物件)
		if isinstance(物件, 組):
			return self.網組(物件)
		if isinstance(物件, 集):
			return self.網集(物件)
		if isinstance(物件, 句):
			return self.網句(物件)
		if isinstance(物件, 章):
			return self.網章(物件)
		self._掠漏.毋是字詞組集句章的毋著(物件)
