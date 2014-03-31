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
from 剖析相關工具.剖析結構化工具 import 剖析結構化工具
from 閩南資料.國閩字詞翻譯 import 國閩單位翻譯
from 剖析相關工具.剖析工具 import 剖析工具
from 言語資料庫.公用資料 import 資料庫連線

class 揣候選句:
	def __init__(self):
# 		self.揣剖析資料 = 資料庫連線.prepare('SELECT ' +
# 			'"甲"."流水號","丁"."流水號","甲"."型體","甲"."音標","乙"."型體","丁"."型體","丁"."音標"' +
# 			'FROM "言語"."文字" AS "甲","言語"."斷詞暫時表" AS "乙","言語"."關係" AS "丙",' +
# 			'"言語"."文字" AS "丁" ' +
# 			'WHERE "甲"."流水號"="乙"."斷詞目標流水號" AND' +
# 			'"甲"."流水號"="丙"."乙流水號" AND "丙"."關係性質"=\'會當替換\' AND ' +
# 			'"丁"."流水號"="丙"."甲流水號" ' +
# 			'ORDER BY "甲"."流水號" DESC ' +
# 			'LIMIT 10000')()
# 		self.揣剖析資料 = 資料庫連線.prepare('SELECT DISTINCT ' +
# 			'"甲"."流水號","甲"."型體","甲"."音標","乙"."型體","丁"."型體","丁"."音標"' +
# 			'FROM "言語"."文字" AS "甲","言語"."斷詞暫時表" AS "乙","言語"."關係" AS "丙",' +
# 			'"言語"."文字" AS "丁" ' +
# 			'WHERE "甲"."流水號"="乙"."斷詞目標流水號" AND' +
# 			'"甲"."流水號"="丙"."乙流水號" AND "丙"."關係性質"=\'會當替換\' AND ' +
# 			'"丁"."流水號"="丙"."甲流水號" ' +
# 			'ORDER BY "甲"."流水號" DESC ' +
# 			'LIMIT 100000')()
		self.揣剖析資料 =[(1099398, '你這乳臭未乾的小子，自以為長大了就不肯聽話，我看你是皮癢的樣子。', None, '#3:1.[0] S(NP(Head:N:我)|Head:Vt:看|S(NP(Head:N:你)|Head:Vt:是|NP(V‧的(Vi:皮癢|Head:T:的)|Head:N:樣子)))#。(PERIODCATEGORY)', '囡仔疕爾爾就生毛閣發角，我看你是皮咧癢的款。', 'gin2-a2-phi2 nia7-nia7 to7 senn1-mng5 koh4 huat4-kak4, gua2 khuann3 li2 si7 phue5 teh4 tsiunn7 e5 khuan2. '),(988032, '我很討厭別人干預我的事。', None, '#1:1.[0] S(NP(Head:N:我)|ADV:很|Head:Vt:討厭|S(NP(Head:N:別人)|Head:Vt:干預|NP(N‧的(N:我|Head:T:的)|Head:N:事)))#。(PERIODCATEGORY)', '我真討厭別人干涉我的代誌。', 'gua2 tsin1 tho2-ia3 pat8-lang5 kan1-siap8 gua2 e5 tai7-tsi3. ')]
		self.揣對應資料 =lambda 流水號: 資料庫連線.prepare('SELECT DISTINCT ' +
			'"丁"."流水號","丁"."型體","丁"."音標" ' +
			'FROM "言語"."關係" AS "丙",' +
			'"言語"."文字" AS "丁" ' +
			'WHERE ' +
			'"丙"."乙流水號"=$1 AND "丙"."關係性質"=\'會當替換\' AND ' +
			'"丁"."流水號"="丙"."甲流水號" ' +
			'ORDER BY "丁"."流水號" DESC ' +
			'LIMIT 100000')(流水號)
# 		print(self.揣剖析資料)
	def 相似比較(self, 翻譯句, 候選句, 評分函式):
		候選句長度 = len(候選句)
		候選句位置 = 0
		攏總分數 = 1
		無法度直接換 = False
		for 一段剖析 in 翻譯句:
			無相仝 = True
			while 無相仝 and 候選句位置 < 候選句長度:
				if isinstance(一段剖析, list) and isinstance(候選句[候選句位置], list) and 一段剖析[0] == 候選句[候選句位置][0]:
					攏總分數 += self.相似比較(一段剖析, 候選句[候選句位置], 評分函式)
					無相仝 = False
				elif isinstance(一段剖析, tuple) and isinstance(候選句[候選句位置], tuple) and 一段剖析[1] == 候選句[候選句位置][1]:
					攏總分數 += 100
					if 一段剖析[0] == 候選句[候選句位置][0]:
						攏總分數 += 100
						if len(一段剖析) >= 3 and len(候選句[候選句位置]) >= 3 and 一段剖析[2] == 候選句[候選句位置][2]:
							攏總分數 += 100
					無相仝 = False
				elif isinstance(一段剖析, str):
					無相仝 = False

				候選句位置 += 1
# 				print(攏總分數)
# 			print(無相仝)
			if 無相仝:
				無法度直接換 = True
		if 無法度直接換:
			攏總分數 = -1
# 				print(一段剖析)
# 				print(候選句位置)
		return 攏總分數
	def 相似換新(self, 翻譯句, 候選句, 對應句, 評分函式):
		候選句長度 = len(候選句)
		候選句位置 = 0
		攏總分數 = 1
		無法度直接換 = False
		結果句 = []
		for 一段剖析 in 翻譯句:
			無相仝 = True
			while 無相仝 and 候選句位置 < 候選句長度:
# 				print(一段剖析)
# 				print(type(一段剖析))
				if isinstance(一段剖析, list) and isinstance(候選句[候選句位置], list) and 一段剖析[0] == 候選句[候選句位置][0]:
					結果句.append(self.相似換新(一段剖析, 候選句[候選句位置], 對應句, 評分函式))
					無相仝 = False
				elif isinstance(一段剖析, tuple) and isinstance(候選句[候選句位置], tuple) and 一段剖析[1] == 候選句[候選句位置][1]:
					攏總分數 += 100
					結果詞 = 國閩單位翻譯(一段剖析)
					對照詞 = 國閩單位翻譯(候選句[候選句位置])
					結果句.append((結果詞, 一段剖析, 對照詞, 候選句[候選句位置],))
					if 一段剖析[0] == 候選句[候選句位置][0]:
						攏總分數 += 100
						print(對照詞, end = '')
						print(" 免變")
						if len(一段剖析) >= 3 and len(候選句[候選句位置]) >= 3 and 一段剖析[2] == 候選句[候選句位置][2]:
							攏總分數 += 100
					else:
						for 對照 in 對照詞[0]:#結果=(字,音）
							if 對照[0] in 對應句:
								print(對照,end=",")
# 							else:
# 								賰的.append(結果)
# 						print(對照詞, end = '')
						print(" ----> ", end = '')
# 						賰的=[]
						print(結果詞)
# 						for 結果 in 結果詞[0]:#結果=(字,音）
# 							if 結果[0] in 對應句:
# 								print(結果,end=",")
# 							else:
# 								賰的.append(結果)
# 						print('|',end='')
# 						print(賰的)
							
					無相仝 = False
				elif isinstance(一段剖析, str):
					結果句.append(一段剖析)
					無相仝 = False
				else:
					print(候選句[候選句位置], end = '')
					print('擲掉')
				候選句位置 += 1
# 				print(攏總分數)
# 			print(無相仝)
			if 無相仝:
				無法度直接換 = True
		if 無法度直接換:
			攏總分數 = -1
			print(候選句, end = '')
			print('規句愛換')
# 				print(一段剖析)
# 				print(候選句位置)
		return 結果句
if __name__ == '__main__':
#  	print(剖析結果字串集)
	結構化工具 = 剖析結構化工具()
	揣候選句工具 = 揣候選句()
	翻譯句 = '#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:回家))#，(COMMACATEGORY)'
	翻譯句='#1:1.[0] S(NP(Head:N:我)|Head:Vt:覺得|S(NP(Head:N:我)|Head:Vt:做|ASP:了|NP(DM:一個|V‧的(Vi:假|Head:T:的)|Head:N:作品)))#'
	
	翻譯句結構化結果 = 結構化工具.結構化剖析結果(翻譯句)
	印出 = lambda 型體佮詞性語意:print(型體佮詞性語意[0], end = ' ')
# 	print(國閩單位翻譯(('吃',)))

	for 剖析結果字串 in 揣候選句工具.揣剖析資料:
# 		print(剖析結果字串)
		結構化結果 = 結構化工具.結構化剖析結果(剖析結果字串[3])
		分數=揣候選句工具.相似比較(翻譯句結構化結果, 結構化結果, None)
		if 分數>300:
			print(翻譯句結構化結果)
			print(結構化結果)
			結構化工具.處理結構化結果(翻譯句結構化結果, 印出)
			print()
			結構化工具.處理結構化結果(結構化結果, 印出)
			print()
			print(分數)
			for 對應句 in 揣候選句工具.揣對應資料(剖析結果字串[0]):
				print(對應句[1])
				print(揣候選句工具.相似換新(翻譯句結構化結果, 結構化結果, 對應句[1], None))


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
#
# # 	結構化結果 = 結構化工具.結構化剖析結果(剖析結果字串集[0])
# # 	結構化工具.處理結構化結果(翻譯句結構化結果,印出)
# # 	print()
# # 	結構化工具.處理結構化結果(結構化結果,印出)
# # 	print()
# # 	print(揣候選句工具.相似比較(翻譯句結構化結果,結構化結果,None))
# # 	print(揣候選句工具.相似換新(翻譯句結構化結果,結構化結果,'我想欲食飯',None))
# #
# # 	print(國閩單位翻譯(['回家']))
