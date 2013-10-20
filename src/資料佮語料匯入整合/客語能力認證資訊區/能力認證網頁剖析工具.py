'''
Created on 2013/7/31

@author: chhsueh
'''

from html.parser import HTMLParser
造字組字表 = {
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
class 能力認證網頁剖析工具(HTMLParser):
	剖析結果 = []
	字體內量 = 0
	表格內 = 0
	def 剖析客話辭典檔案(self, 檔名):
		檔案 = open(檔名)
		資料 = 檔案.read()
		檔案.close()
		return self.剖析客話辭典網頁(資料)
	def 剖析客話辭典網頁(self, 資料):
		self.初始化剖析結果()
		self.feed(資料)
		return self.目前剖析結果()
	def 初始化剖析結果(self):
		self.剖析結果 = []
		self.表格內 = 0
		self.開始 = False
	def 目前剖析結果(self):
		return self.剖析結果
	def handle_starttag(self, tag, attrs):
		屬性表 = dict(attrs)
		if tag == 'div' and 'style' in 屬性表 and 屬性表['style'] == 'height:3px':
			self.開始 = True
		if self.開始:
			if self.表格內 >= 3:
				if tag == "td":
					self.剖析結果.append('')
				if tag == "input":
					if "checked" in 屬性表:
						self.剖析結果[-1] += 'sui2'
# 				elif tag == 'img':
# 					src = dict(attrs)['src']
# 					if src.startswith('koupng'):
# 						tsoo2zi7too5 = src.split('/')[-1].split('.')[0]
# 	# 					print(tsoo2zi7too5)
# 						if tsoo2zi7too5 not in 造字組字表:
# 							print(tsoo2zi7too5, '無佇組字表')
# 							self.剖析結果[-1] += tsoo2zi7too5
# 						else:
# 							self.剖析結果[-1] += 造字組字表[tsoo2zi7too5]
			if tag == "table":
				self.表格內 += 1
	def handle_endtag(self, tag):
		if self.開始:
			if tag == "table":
				self.表格內 -= 1
				if self.表格內 == 0:
					self.開始 = False
	def handle_data(self, data):
		if self.開始:
			if self.表格內 >= 3:
				if len(self.剖析結果) > 0:
					self.剖析結果[-1] += data.strip()
# 				 print('', data.strip(),'',end='',sep='')

if __name__ == "__main__":
	網頁剖析工具 = 能力認證網頁剖析工具(strict = False)
	a = 網頁剖析工具.剖析客話辭典檔案('/home/Ihc/tmpfs/words.aspx?param=100003')
	print(a)
