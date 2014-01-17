"""
著作權所有 (C) 民國103年 意傳文化科技
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
from 資料庫.資料庫連線 import 資料庫連線
import os

class 匯入數位典藏文本段落:
	插入台語數位典藏文本資料庫 = 資料庫連線.prepare('INSERT INTO "台語文數位典藏"."原始段落資料" ' +
		'("檔案名","漢羅","全羅","漢羅逝","全羅逝") VALUES ($1,$2,$3,$4,$5)')
	插入修改數位典藏文本資料庫 = 資料庫連線.prepare('INSERT INTO "台語文數位典藏"."改過段落資料" ' +
		'("檔案名","漢羅","全羅","漢羅逝","全羅逝") VALUES ($1,$2,$3,$4,$5)')
	目錄='/dev/shm/re/'
	def __init__(self):
		for root, subFolders, files in os.walk(self.目錄):
# 			print(root, subFolders, files )
			if len(subFolders) == 0:
				for 檔案名 in files:
					if 檔案名.endswith('txt'):
						檔案路徑 = os.path.join(root, 檔案名)
	# 					print(檔案路徑)
# 						愛先find . -type f -iname *.tbk -exec iconv -f big5 {} -o {}.txt -c \;
						檔案 = open(檔案路徑)
# 						ks/K/1999/KS.1999.Tan5 Lui5.Ki3-liam7 chhai3-thau5 Chhoa3 Cheng3-liong5_hian3 hou7 Iap8 Beng5-ha5.tbk
# 						這檔案佇全羅有奇怪的編碼
# 						網頁面頂嘛是有問題
# 						http://xdcm.nmtl.gov.tw/dadwt/thak.asp?id=1439

						編碼錯誤 = {'  SeNnchit{hang7 ntai7-chi3, <BR>  bo5 iong7 peh8-choa2 sia2 cho3 ou-ji7. <BR>  u7 si7 moa2-pak e5 ng2-bang7 kiam chi3-khi3, <BR>  beh khoaN3 kou3-hiong e5 soaN-lun5 bi2-le7 pho7 hai2-chui2. '.strip():
							'  SeN chit-hang7 ntai7-chi3, <BR>  bo5 iong7 peh8-choa2 sia2 cho3 ou-ji7. <BR>  u7 si7 moa2-pak e5 ng2-bang7 kiam chi3-khi3, <BR>  beh khoaN3 kou3-hiong e5 soaN-lun5 bi2-le7 pho7 hai2-chui2. '.strip(),
							'  siong7-ai3 kap hak8-seng pheng7 khui3-lat8, <BR>  ma7 si7 chheng-chhun be7-lau7 e5 tong5-chi3, <BR>  ti7 Houston, ti7 Los Angelos, ti7 tai5-oan5,nti7npak-bi2. '.strip():
							'  siong7-ai3 kap hak8-seng pheng7 khui3-lat8, <BR>  ma7 si7 chheng-chhun be7-lau7 e5 tong5-chi3, <BR>  ti7 Houston, ti7 Los Angelos, ti7 tai5-oan5, ti7 pak-bi2. '.strip()}
						全羅字串=[]
						漢羅字串=[]
						這馬字串=全羅字串
						for 逝 in 檔案:
							逝 = 逝.strip()
							if 逝=='':
								continue
							if 逝 in ['<CL>','</CL>']:
								continue
							if 逝 in ['<HL>','</HL>',]:
								這馬字串=漢羅字串
								continue
							if 逝 in 編碼錯誤:
								逝 = 編碼錯誤[逝]
							這馬字串.append(逝)
# 						if (len(全羅字串)!=len(漢羅字串)):
# 							print(檔案路徑.split(self.目錄)[-1])
# 							print((全羅字串))
# 							print((漢羅字串))
# 							print()
						self.插入台語數位典藏文本資料庫(檔案路徑.split(self.目錄)[-1],
							'\n'.join(漢羅字串),'\n'.join(全羅字串),len(漢羅字串),len(全羅字串))
						self.插入修改數位典藏文本資料庫(檔案路徑.split(self.目錄)[-1],
							'\n'.join(漢羅字串),'\n'.join(全羅字串),len(漢羅字串),len(全羅字串))
						檔案.close()
						
if __name__ == '__main__':
	匯入數位典藏文本段落()
