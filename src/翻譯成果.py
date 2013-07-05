from 剖析相關工具.剖析工具 import 剖析工具
from 系統整合.翻譯整合 import 翻譯整合


if __name__ == '__main__':
# 	print(國閩單位翻譯('事'))
	翻譯句 = '#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:回家))#，(COMMACATEGORY)'
	翻譯句 = '#1:1.[0] S(NP(Head:N:我)|Head:Vt:覺得|S(NP(Head:N:我)|Head:Vt:做|ASP:了|NP(DM:一個|V‧的(Vi:假|Head:T:的)|Head:N:作品)))#'
	## bug!!
	翻譯句 = '#1:1.[0] S(experiencer:NP(Head:Nhaa:我們)|quantity:Dab:都|Head:VK1:喜歡|goal:NP(Head:Nab:蝴蝶))#'
	翻譯句 = '#1:1.[0] S(theme:NP(Head:Nhaa:我)|Head:VA12:坐|location:Nab:火車|complement:VP(Head:VA11:來|location:Nca:台北))#'
# 	翻譯句 = '#1:1.[0] S(agent:NP(Head:Nhaa:你)|time:Ndabe:晚上|deontics:Dbab:要|Head:VC31:吃|theme:Nep:什麼)#'
# 	翻譯句 = '#1:1.[0] S(agent:NP(possessor:Nhaa:你|Head:Nab:晚餐)|deontics:Dbab:要|Head:VC31:吃|theme:Nep:什麼)#'
# 	翻譯句 = '#1:1.[0] S(NP(Head:N:我)|Head:Vi:坐|N:火車|VP(Head:Vi:來|N:台北))#'
#	翻譯句 = 工具.剖析('我今天要去台北')[0]
#	翻譯句 = 工具.剖析('明天會下雨')[0]
#	翻譯句 = 工具.剖析('山藥也是芳苑鄉重要農特產之一')[0]
#	翻譯句 = 工具.剖析('建仔要面對去年美聯霸主老虎')[0]
	print(翻譯句)
	
	工具 = 剖析工具()
# 	剖析結果字串集=工具.剖析('我想吃飯，，，我想吃很多飯。假如我也用這種方式旅行。再想到蝴蝶會生滿屋的毛蟲。')
	剖析結果字串集 = ['#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#，(COMMACATEGORY)',
			'#2:1.[0] %()#，(COMMACATEGORY)',
			'#3:1.[0] %()#，(COMMACATEGORY)',
			'#4:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)',
			'#5:1.[0] S(C:假如|NP(Head:N:我)|ADV:也|PP(Head:P:用|NP(DM:這種|Head:N:方式))|Head:Vi:旅行)#。(PERIODCATEGORY)',
			'#6:1.[0] VP(ADV:再|Head:Vt:想到|NP(S‧的(head:S(NP(Head:N:蝴蝶)|ADV:會|Head:Vt:生|NP(Head:N:滿屋))|Head:T:的)|Head:N:毛蟲))#。(PERIODCATEGORY)',
			'#1:1.[0] VP(evaluation:Dbb:再|Head:VE2:想到|goal:NP(predication:S‧的(head:S(agent:NP(Head:Nab:蝴蝶)|epistemics:Dbaa:會|Head:VC31:生|theme:NP(Head:Na:滿屋))|Head:DE:的)|Head:Nab:毛蟲))#。(PERIODCATEGORY)',
			'#1:1.[0] S(NP(Head:N:我們)|ADV:要|Head:Vi:下班)#，(COMMACATEGORY)',
			'#2:1.[0] S(NP(Head:N:我)|PP(Head:P:和|NP(Head:N:他))|Head:Vt:想|VP(Head:Vi:回家))#，(COMMACATEGORY)',
			'#3:1.[0] S(NP(Head:N:你們)|DM:兩個|Head:Vt:想|VP(Head:Vi:睡覺))#。(PERIODCATEGORY)']
	整合工具=翻譯整合()
	整合工具.國閩翻譯(剖析結果字串集)
