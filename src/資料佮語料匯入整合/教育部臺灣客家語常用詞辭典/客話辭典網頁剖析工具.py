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
'''
Created on 2013/7/31

@author: chhsueh
'''

from html.parser import HTMLParser
造字組字表={
'2430':'⿰火',
'2A61':'⿰齒含',
'35F1':'⿰口集',
'3614':'⿰口賽',
'39FE':'⿰忽',
'3F13':'⿰瓜兼',
'3F8A':'⿴疒朿',
'F305':'⿰厓',
'F307':'⿰恩',
'F30E':'⿰各攴',
'F315':'⿰百',
'F31B':'⿰目巠',
'F349':'⿰虫憲',
'F34E':'⿰亥',
'F34F':'⿰丁',
'F350':'⿰口束',
'F354':'⿴走支',
'F357':'⿰爭',
'F35A':'⿰送',
'F35F':'⿰石剝',
'F360':'⿰黑乇',
'F369':'⿰虫另',
'F36A':'⿰卒欠',
'F36B':'⿰火剌',
'F36C':'⿱拜',
'F36D':'⿰⿱⿱⿰人人一韭',
'F36E':'⿰言',
'F36F':'⿰',
'F372':'⿰目聶',
'F374':'⿰⿱巾',
'F377':'⿰戾攴',
'F379':'⿰巴',
'F37B':'⿰米呈',
'F37C':'⿰雀',
'F37D':'⿰木盛',
'F37E':'⿴辶甲',
'F382':'⿰口虐',
'F383':'⿰火',
'F384':'⿰虫奇',
'F385':'⿴疒彖',
'F390':'⿰敖',
'F392':'⿴辶方',
'F394':'⿰目翕',
'F397':'⿱臿',
'F39A':'⿰亢',
'F39B':'⿴冖同',
'F39C':'⿴囗又',
'F3A5':'⿴疒盍',
'F3B4':'⿰目甫',
'F3B5':'⿰鼻乚',
'F3B9':'⿰目荅',
'F3BF':'⿱難',
'F3C9':'⿰卑',
'F401':'⿰牙子',
'F40E':'⿰發',
'F40F':'⿰蔑',
'F414':'⿰亞',
'F416':'⿰壴',
'F426':'⿰它',
'F433':'⿰火巢',
'F434':'⿰兼',
'F436':'⿰貝',
'F437':'⿰堅',
'F438':'⿰金贏',
'F442':'⿰虫念',
'F444':'⿴辶丁',
'F446':'⿰口尢',
'F448':'⿰骨犮',
'F44F':'⿰⿱夭韭',
'F463':'⿰口尃',
'F488':'⿰歷',
'F545':'⿰皮卜',
'F4BC':'㑁',
'F457':'⿰⿰⿰Ｆ４５７',
}
class 客話辭典網頁剖析工具(HTMLParser):
	剖析結果=[]
	字體內量=0
	表格內=0
	def 剖析客話辭典檔案(self,檔名):
		檔案=open(檔名)
		資料=檔案.read()
		檔案.close()
		return self.剖析客話辭典網頁(資料)
	def 剖析客話辭典網頁(self,資料):
		self.初始化剖析結果()
		self.feed(資料)
		return self.目前剖析結果()
	def 初始化剖析結果(self):
		self.剖析結果=[]
		self.字體內量=0
		self.表格內=0
	def 目前剖析結果(self):
		return self.剖析結果
	def handle_starttag(self, tag, attrs):
		if self.字體內量>0 and self.表格內>0:
			if tag=="td":
				self.剖析結果.append('')
			elif tag=='img':
				src=dict(attrs)['src']
				if src.startswith('koupng'):
					tsoo2zi7too5=src.split('/')[-1].split('.')[0]
# 					print(tsoo2zi7too5)
					if tsoo2zi7too5 not in 造字組字表:
						print(tsoo2zi7too5,'無佇組字表')
						self.剖析結果[-1]+=tsoo2zi7too5
					else:
						self.剖析結果[-1]+=造字組字表[tsoo2zi7too5]
		if tag=="font":
			self.字體內量+=1
		elif tag=="table":
			self.表格內+=1
	def handle_endtag(self, tag):
#		 if self.字體內量>0 and self.表格內>0:
#			 if tag=="td":
#				 print()
		if tag=="font":
			self.字體內量-=1
		elif tag=="table":
			self.表格內-=1
	def handle_data(self, data):
		if self.字體內量>0 and self.表格內>0:
			if len(self.剖析結果)>0:
				self.剖析結果[-1]+=data.strip()
#				 print('', data.strip(),'',end='',sep='')

if __name__ == "__main__":
	網頁剖析工具 = 客話辭典網頁剖析工具(strict=False)
	網頁剖析工具.feed('<html><head><title>Test</title></head>'
				'<body><h1>  Parse me!  </h1></body></html>')
	網頁剖析工具.feed('<html><head><title>Test</title></head>'
				'<body><h1>  Parse me!  </h1></body></html>')
	su=open('/home/chhsueh/su.html').read()
#	 print(su)
	a=網頁剖析工具.剖析客話辭典網頁(su)
	print(a)
	word=open('/home/chhsueh/word.html').read()
#	 print(word)
	a=網頁剖析工具.剖析客話辭典網頁(word)
	print(a)
	
