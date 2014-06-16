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
from 臺灣言語工具.語音合成.生決策樹仔問題 import 生決策樹仔問題
class 閩南語決策樹仔:
	生問題=生決策樹仔問題()
	def 生(self):
		pass
	def 詞句長度(self):
		'''長度
		詞句 頭前中 長度 <=
		詞
			3*10*2
		句
			3*20*2
		'''
	def 孤聲韻(self):
		'''
	孤聲韻
		QS "Si7_xm" {*-xm+*}
		QS "Si7_xng" {*-xng+*}
		'''
	def 元音(self):
		'''
		元音
			QS "Si7_Sun5_Uan5_Im1"           {*-a+*,*-i+*,*-u+*,*-e+*,*-o+*}
			QS "Si7_Uan5_Im1"           {*-*a*+*,*-*i*+*,*-*u*+*,*-*e*+*,*-*o*+*}
			QS "Si7_Ki2_Uan5_Im1"      {*-*i*+*,*-*e*+*,*-*a*+*}
			QS "Si7_Kin1_Uan5_Im1"    {*-*o*+*,*-*u*+*}
			QS "Si7_Ting2_Uan5_Im1"      {*-*?i*+*,*-*?u*+*}
			QS "Si7_Tiong1_Uan5_Im1"    {*-*e*+*,*-*o*+*}
			QS "Si7_Ke1_Uan5_Im1"      {*-*a*+*}
		'''
	def 韻尾類(self):
		'''
			QS "Si7_Tsiap4_Tshun5_Im1" {*-*?p+*,*-*?m+*}
			QS "Si7_Tsiap4_Ki2_Im1" {*-*?t+*,*-*?n+*}
			QS "Si7_Tsiap4_Kin1_Im1" {*-*?k+*,*-*?ng+*}
			QS "Si7_Tsiap4_Phinn5_Im1"    {*-*?m+*,*-*?n+*,*-*?ng+*}
			QS "Si7_Un7_Hua3_Phinn5_Im1"    {*-xm+*,*-xng+*}
			QS "Si7_Tsu2_Im1_Phinn5_Im1"    {*-m+*,*-ng+*,*-*am+*,*-*em+*,*-*um+*,*-*em+*,*-*om+*,*-*ang+*,*-*eng+*,*-*ung+*,*-*eng+*,*-*ong+*}
		'''
	def 介音類(self):
		'''i*-,u*-'''
	def 鼻化音類(self):
		'''ⁿ'''
	def 子音類(self):
		'''
		QS "Si7_Tsing1_Im1"   {*-p+*,*-t+*,*-k+*,*-ts+*}
		QS "Si7_Song2_Ki3_Im1"      {*-ph+*,*-th+*,*-kh+*,*-tsh+*}
		QS "Si7_Lo5_Im1"    {*-b+*,*-l+*,*-g+*,*-j+*}
		QS "Si7_Lo5_Sail3_Im1"    {*-b+*,*-g+*,*-j+*}
		QS "Si7_Phinn5_Im1"    {*-m+*,*-n+*,*-ng+*}
		QS "Si7_Sun5_Sai3_Im1"      {*-p+*,*-ph+*,*-b+*,*-t+*,*-th+*,*-k+*,*-kh+*,*-g+*}
		QS "Si7_Sai3_Im1"           {*-p+*,*-ph+*,*-b+*,*-t+*,*-th+*,*-k+*,*-kh+*,*-g+*,*-ts+*,*-tsh+*,*-j+*}
		QS "Si7_Sai3_Tshat4_Im1"    {*-ts+*,*-tsh+*,*-j+*}
		QS "Si7_Tshat4_Im1"         {*-s+*,*-h+*,*-ts+*,*-tsh+*,*-j+*}
		QS "Si7_Sun5_Tshat4_Im1"    {*-s+*,*-h+*}
		QS "Si7_Tshun5_Tsu2_Im1"   {*-p+*,*-ph+*,*-b+*,*-m+*}
		QS "Si7_Ki2_Tsu2_Im1"      {*-t+*,*-th+*,*-n+*,*-l+*,*-ts+*,*-tsh+*,*-j+*,*-s+*}
		QS "Si7_Kin1_Tsu2_Im1"    {*-k+*,*-kh+*,*-g+*,*-ng+*,*-h+*}
		'''
	def 聲韻公家(self):
		'''
		QS "Si7_U7_Phinn5_Im1"    {*-*m*+*,*-*ng*+*}
		'''
	def 調(self):
		'''孤，組合'''		

元音 = ['a', 'i', 'u', 'e', 'o']
韻尾 = ['m', 'n', 'ŋ', 'h', 'p', 't', 'k']
鼻化韻 = ['nn', 'nnh']