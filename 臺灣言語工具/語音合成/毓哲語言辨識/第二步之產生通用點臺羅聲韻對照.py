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
from 通用拼音音標 import 通用拼音音標
from 臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 毓哲語言辨識.第一步之揣出臺語通用 import 語法錯誤表
from 毓哲語言辨識.第一點一步之檢查通用臺音標對照表 import 對齊語料路徑

if __name__ == '__main__':
# 	字音對照 = 通用拼音音標('bai5')
# 	print(字音對照.音標)
# 	print(字音對照.轉換到臺灣閩南語羅馬字拼音())
# 	lines = [line.strip() for line in open('/home/Ihc/辨識/Syl2Monophone.dic.txt')]
	錯誤對照表={}
	for 原本,修正 in 語法錯誤表:
		錯誤對照表[原本]=修正
											
	lines = [line.strip() for line in open(對齊語料路徑+'臺語通用拼音.dic')]
	for line in lines:
		if line=='':
			continue
		通用,*音素=line.split()
		舊通用=通用
		if 通用 in 錯誤對照表:
			通用=錯誤對照表[通用]
		if 通用.endswith('h') or 通用.endswith('p') or 通用.endswith('t') or 通用.endswith('k'):
			通用+='7'
		else:
			通用+='1'
		字音對照 = 通用拼音音標(通用)
		if 通用=='sil1':
			print(' '.join(line.split()))
		else:
			臺羅拼音=臺灣閩南語羅馬字拼音(字音對照.轉換到臺灣閩南語羅馬字拼音())
			聲,韻=臺羅聲韻轉辨識合成型(臺羅拼音.聲,臺羅拼音.韻)
			if 聲=='':
				print(舊通用,end=' ')
				print(韻)
			else:
				print(舊通用,end=' ')
				print(聲,end=' ')
				print(韻)
				
				
