from 剖析相關工具.剖析結構化工具 import 剖析結構化工具
from 剖析相關工具.剖析工具 import 剖析工具
from 候選句.交叉二維揣候選句 import 詞相關評價
from 閩南資料.國閩字詞翻譯 import 字音結構化
from 候選句.交叉二維揣候選句 import 交叉二維揣候選句
from 候選句.建立候選句佮對應句關係 import 建立候選句佮對應句關係
from 候選句.建立候選句佮對應句關係 import 提出對照位置
from 候選句.建立候選句佮對應句關係 import 調整對照
from 候選句.建立候選句佮對應句關係 import 候選句佮對應句對照


if __name__ == '__main__':
# 	print(國閩單位翻譯('事'))
	工具=剖析工具()
	結構化工具 = 剖析結構化工具()
	揣候選句工具 = 交叉二維揣候選句()
	翻譯句 = '#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:回家))#，(COMMACATEGORY)'
	翻譯句 = '#1:1.[0] S(NP(Head:N:我)|Head:Vt:覺得|S(NP(Head:N:我)|Head:Vt:做|ASP:了|NP(DM:一個|V‧的(Vi:假|Head:T:的)|Head:N:作品)))#'
	## bug!!
	翻譯句 = '#1:1.[0] S(experiencer:NP(Head:Nhaa:我們)|quantity:Dab:都|Head:VK1:喜歡|goal:NP(Head:Nab:蝴蝶))#'
# 	翻譯句 = '#1:1.[0] S(theme:NP(Head:Nhaa:我)|Head:VA12:坐|location:Nab:火車|complement:VP(Head:VA11:來|location:Nca:台北))#'
# 	翻譯句 = '#1:1.[0] S(agent:NP(Head:Nhaa:你)|time:Ndabe:晚上|deontics:Dbab:要|Head:VC31:吃|theme:Nep:什麼)#'
# 	翻譯句 = '#1:1.[0] S(agent:NP(possessor:Nhaa:你|Head:Nab:晚餐)|deontics:Dbab:要|Head:VC31:吃|theme:Nep:什麼)#'
# 	翻譯句 = '#1:1.[0] S(NP(Head:N:我)|Head:Vi:坐|N:火車|VP(Head:Vi:來|N:台北))#'
#	翻譯句 = 工具.剖析('我今天要去台北')[0]
#	翻譯句 = 工具.剖析('明天會下雨')[0]
#	翻譯句 = 工具.剖析('山藥也是芳苑鄉重要農特產之一')[0]
#	翻譯句 = 工具.剖析('建仔要面對去年美聯霸主老虎')[0]
	print(翻譯句)
	翻譯句結構化結果 = 結構化工具.結構化剖析結果(翻譯句)
	印出 = lambda 型體佮詞性語意:print(型體佮詞性語意[0], end = ' ')

	挑出分數懸的=[]
	for 剖析結果字串 in 揣候選句工具.揣剖析資料:
# 		print(剖析結果字串)
		結構化結果 = 結構化工具.結構化剖析結果(剖析結果字串[3])
		分數 = 揣候選句工具.相似比較(翻譯句結構化結果[1], 結構化結果[1], 詞相關評價)
		挑出分數懸的.append((分數[0],分數,結構化結果,剖析結果字串))
	挑出分數懸的.sort(key=lambda 資料:資料[0],reverse=True)
	for i in range(3):
		if i<len(挑出分數懸的):
			剖析結果字串=挑出分數懸的[i][3]
			結構化結果=挑出分數懸的[i][2]
			分數=挑出分數懸的[i][1]
			print(分數)
			print(剖析結果字串)
			print(翻譯句結構化結果)
			print(結構化結果)
			結構化工具.處理結構化結果(翻譯句結構化結果, 印出)
			print()
			結構化工具.處理結構化結果(結構化結果, 印出)
			print()
			print(分數)
			對應句結構化 = 字音結構化([(剖析結果字串[4], 剖析結果字串[5])])
			print(對應句結構化)
			print(對應句結構化[0])
			print(對應句結構化[0].下跤)
			if 對應句結構化[0].下跤==None:
				continue
			候選句佮對應句 = 結構化工具.處理結構化結果(結構化結果, 候選句佮對應句對照(對應句結構化[0]))
			print(候選句佮對應句)
			建立關係 = 建立候選句佮對應句關係()
			提出位置工具 = 提出對照位置()
			結構化工具.處理結構化結果(候選句佮對應句, 提出位置工具.提出位置)
			關係所在 = 提出位置工具.對照位置
			print(關係所在)
			調整物件 = 調整對照((len(剖析結果字串[4]), 關係所在))
			調整後的對照關係 = 結構化工具.處理結構化結果(候選句佮對應句, 調整物件.調整)
			print("調整後的對照關係",end=" ")
			print(調整後的對照關係)
			# 替換結果 = 建立關係.相似換新(翻譯句結構化結果[1], 調整後的對照關係[1], 對應句結構化[0], 分數[1], 分數[2])
			對應句結構化 = 字音結構化([(剖析結果字串[4], 剖析結果字串[5])])
			print(對應句結構化[0].下跤)
			替換結果 = 建立關係.相似換新(翻譯句結構化結果[1], 調整後的對照關係[1], 對應句結構化[0], 分數[1], 分數[2])
#  			分數=揣候選句工具.相似(翻譯句結構化結果[1], 結構化結果[1], 詞相關評價)
# 			for 對應句 in 揣候選句工具.揣對應資料(剖析結果字串[0]):
# 				print(對應句[1])
# 				print(揣候選句工具.相似換新(翻譯句結構化結果, 結構化結果, 對應句[1], 詞相關評價))
			print(替換結果)
			替換陣列 = list(替換結果)
			替換陣列.sort()
			print(替換陣列)
			答案句 = []
			for 位置 in 替換陣列:
				print("替換結果[位置]")
				print(替換結果[位置])
				if 位置[0]<位置[1] or True:
					for 愛插入的詞 in 替換結果[位置]:
						print("愛插入的詞[0]")
						print(愛插入的詞[0])
						print(愛插入的詞[0][0])
						答案句.append(愛插入的詞[0][0])
	# 					for 詞選擇 in 愛插入的詞[0]:
	# 						print(詞選擇)
			for 答案 in 答案句:
				print(答案.型, end = "")
			print()
			for 答案 in 答案句:
				print(答案.音, end = " ")
			print()
			print()


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
# 	for 剖析結果字串 in 剖析結果字串集:
# # 		print(剖析結果字串)
# 		結構化結果 = 結構化工具.結構化剖析結果(剖析結果字串)
# 		print(翻譯句結構化結果)
# 		print(結構化結果)
# 		結構化工具.處理結構化結果(翻譯句結構化結果,印出)
# 		print()
# 		結構化工具.處理結構化結果(結構化結果,印出)
# 		print()
# 		print(揣候選句工具.相似比較(翻譯句結構化結果,結構化結果,None))
# 		print(揣候選句工具.相似換新(翻譯句結構化結果,結構化結果,'',None))
# # 		翻譯結果=結構化工具.處理結構化結果(結構化結果,國閩單位翻譯)
# # 		print(翻譯結果)
# # 		結構化工具.處理結構化結果(翻譯結果,印出)
# # 		print()
#
# ##
# # 	結構化結果 = 結構化工具.結構化剖析結果(剖析結果字串集[0])
# # 	結構化工具.處理結構化結果(翻譯句結構化結果,印出)
# # 	print()
# # 	結構化工具.處理結構化結果(結構化結果,印出)
# # 	print()
# # 	print(揣候選句工具.相似比較(翻譯句結構化結果,結構化結果,None))
# # 	print(揣候選句工具.相似換新(翻譯句結構化結果,結構化結果,'我想欲食飯',None))
# #
# # 	print(國閩單位翻譯(['回家']))
