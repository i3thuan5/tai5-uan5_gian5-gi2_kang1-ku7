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
from html.parser import HTMLParser
'''
Created on 2013/7/31

@author: chhsueh
'''


class 剖析信望愛語料庫表格(HTMLParser):
	剖析結果 = []
	字體內量 = 0
	表格內 = 0
	def 剖析信望愛語料庫檔案(self, 檔名):
		檔案 = open(檔名)
		資料 = 檔案.read()
		檔案.close()
		return self.剖析信望愛語料庫網頁(資料)
	def 剖析信望愛語料庫網頁(self, 資料):
		self.初始化剖析結果()
		self.feed(資料)
		return self.目前剖析結果()
	def 初始化剖析結果(self):
		self.剖析結果 = []
		self.表格內 = 0
		self.詞型內 = 0
		self.開始 = False
	def 目前剖析結果(self):
		return self.剖析結果
	def handle_starttag(self, tag, attrs):
		屬性表 = dict(attrs)
		if tag=='form' and 'lang' in 屬性表 and 屬性表['lang']=='nan':
			self.表格內=1
		elif tag=='lexical-unit':
			self.詞型內+=1
	def handle_endtag(self, tag):
		if tag=='form':
			self.表格內=0
		elif tag=='lexical-unit':
			self.詞型內-=1
	def handle_data(self, data):
		data=data.strip()
		if data!='':
			if self.詞型內>0 and self.表格內>0:
				self.剖析結果.append(data)

if __name__ == "__main__":
	網頁剖析工具 = 剖析信望愛語料庫表格(strict = False)
	a = 網頁剖析工具.剖析信望愛語料庫檔案('/home/Ihc/tmpfs/nan/nan.lift')
	print(a)
