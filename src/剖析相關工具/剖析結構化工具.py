from 剖析相關工具.剖析工具 import 剖析工具
from 資料庫工具.型體翻譯 import 型體翻譯
from 資料庫工具.型體翻譯 import 型體似義
from 資料庫工具.型體翻譯 import 揣型體
from 資料庫工具.型體翻譯 import 揣台華型體
from 資料庫工具.型體翻譯 import 揣詞六型體

class 剖析結構化工具:
	def 結構化剖析結果(self, 剖析結果字串):
# 		print(剖析結果字串.split('#'))
		空白, 語句資訊, 結束符號 = 剖析結果字串.split('#')
		if 空白 != '':
			print('有問題')
		逝資料, 語句 = 語句資訊.split(' ', 1)
# 		print(語句)
		結構化結果 = [逝資料.split(':')[0]]
		結構化結果.append(self.結構化語句(語句))


		結構化結果.append(結束符號)
		return 結構化結果
	def 結構化語句(self, 剖析語句):
# 		print(剖析語句			)
		括號位置 = 剖析語句.find('(')
		冒號位置 = 剖析語句.find(':')
# 		elif 冒號位置 >= 0 and (括號位置 < 0 or 括號位置 > 冒號位置):
		if 冒號位置 >= 0 and 括號位置 < 0:
			return tuple(剖析語句.split(':')[::-1])
# 		if 括號位置 >= 0 and (冒號位置 < 0 or 冒號位置 > 括號位置):
		elif 括號位置 >= 0:# and (冒號位置 < 0 or 冒號位置 > 括號位置):
			正括號位置 = 剖析語句.rfind(')')
			片語內容 = list(map(self.結構化語句, self.切片語(剖析語句[括號位置 + 1:正括號位置])))
			# #會切著中央的
			if 剖析語句[正括號位置 + 1:] != '':
				print('「' + 剖析語句 + '」後壁有加物件！！！')
			return [剖析語句[:括號位置]] + 片語內容
# 		print('「' + 剖析語句 + '」毋知按怎切！！！')
		return (剖析語句)
	def 切片語(self, 片語):
		切開結果 = []
		有問題 = False
		深度 = 0
		詞 = ''
		for 字 in 片語:
			if 字 == '|' and 深度 == 0:
				切開結果.append(詞)
				詞 = ''
			elif 字 == '(':
				深度 += 1
				詞 += 字
			elif 字 == ')':
				深度 -= 1
				詞 += 字
			else:
				詞 += 字
			if 深度 < 0:
				有問題 = True
		if 深度 != 0:
			有問題 = True
		切開結果.append(詞)
		if 有問題:
			print('「' + 片語 + '」括號有問題！！！')
		return 切開結果
# 	def 結構化片語(self, 片語):
# 		pass
# 	def 結構化詞(self, 詞):
# 		return
	def 處理結構化結果(self,剖析結果,處理函式):
		處理結果 = []
		for 一段剖析 in 剖析結果:
			if isinstance(一段剖析, list):
				處理結果.append(self.處理結構化結果(一段剖析,處理函式))
			elif isinstance(一段剖析, tuple):
				處理結果.append(處理函式(一段剖析))
			else:
				處理結果.append(一段剖析)
		return 處理結果



def	國閩單位翻譯(型體佮詞性語意):
# 		print(型體佮詞性語意)
	def 提翻譯(資料庫翻譯,型,音):
		return [(翻譯[型],翻譯[音]) for 翻譯 in 資料庫翻譯]
	翻譯集合=提翻譯(型體翻譯('漢語族官話方言北京官話臺灣腔', 型體佮詞性語意[0], '漢語族閩方言閩南語偏漳優勢音'),7,8)
	
	翻譯集合.extend(提翻譯(揣型體('漢語族閩方言閩南語偏漳優勢音', 型體佮詞性語意[0]),7,8))
	翻譯集合.extend(提翻譯(揣台華型體('漢語族閩方言閩南語偏漳優勢音', 型體佮詞性語意[0]),0,1))
	翻譯集合.extend(提翻譯(揣詞六型體('漢語族閩方言閩南語偏漳優勢音', 型體佮詞性語意[0]),0,1))
	
	if 翻譯集合==[]:
		翻譯=型體似義('漢語族官話方言北京官話臺灣腔', 型體佮詞性語意[0], '漢語族閩方言閩南語偏漳優勢音')
		if 翻譯!=[]:
			音=翻譯[0][8]
			翻譯=翻譯[0][7]
			return ('!'+翻譯+'@'+音+'!',)+tuple(型體佮詞性語意[1:])
	if 翻譯集合==[]:
		return 型體佮詞性語意
#	print(翻譯)
	return (翻譯集合,)+tuple(型體佮詞性語意[1:])

if __name__ == '__main__':
	工具 = 剖析工具()
# 	剖析結果字串集=工具.剖析('我想吃飯，，，我想吃很多飯。假如我也用這種方式旅行。再想到蝴蝶會生滿屋的毛蟲。')
	剖析結果字串集 = ['#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#，(COMMACATEGORY)',
			'#2:1.[0] %()#，(COMMACATEGORY)',
			'#3:1.[0] %()#，(COMMACATEGORY)',
			'#4:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)',
			'#5:1.[0] S(C:假如|NP(Head:N:我)|ADV:也|PP(Head:P:用|NP(DM:這種|Head:N:方式))|Head:Vi:旅行)#。(PERIODCATEGORY)',
			'#6:1.[0] VP(ADV:再|Head:Vt:想到|NP(S‧的(head:S(NP(Head:N:蝴蝶)|ADV:會|Head:Vt:生|NP(Head:N:滿屋))|Head:T:的)|Head:N:毛蟲))#。(PERIODCATEGORY)',
			'#1:1.[0] VP(evaluation:Dbb:再|Head:VE2:想到|goal:NP(predication:S‧的(head:S(agent:NP(Head:Nab:蝴蝶)|epistemics:Dbaa:會|Head:VC31:生|theme:NP(Head:Na:滿屋))|Head:DE:的)|Head:Nab:毛蟲))#。(PERIODCATEGORY)']
#  	print(剖析結果字串集)
	結構化工具 = 剖析結構化工具()
	印出=lambda 型體佮詞性語意:print(型體佮詞性語意[0], end=' ')
# 	print(國閩單位翻譯(('吃',)))
	for 剖析結果字串 in 剖析結果字串集:
		結構化結果 = 結構化工具.結構化剖析結果(剖析結果字串)
# 		print(結構化結果)
		結構化工具.處理結構化結果(結構化結果,印出)
		print()
		翻譯結果=結構化工具.處理結構化結果(結構化結果,國閩單位翻譯)
# 		print(翻譯結果)
		結構化工具.處理結構化結果(翻譯結果,印出)
		print()
