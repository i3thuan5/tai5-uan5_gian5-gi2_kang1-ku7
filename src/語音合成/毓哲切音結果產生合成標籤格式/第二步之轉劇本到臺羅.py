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
from 毓哲切音結果產生合成標籤格式.第一步之揣出愛處理的臺詞 import 合成標籤路徑
from 毓哲語言辨識.第一步之揣出臺語通用 import 語法錯誤表
# 有足濟所在會當閣改，入聲詞毋著濟

數字 = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
if __name__ == '__main__':
	# 來源="/home/Ihc/意傳計劃/語音合成/中研院/processed(teacher+student)/alltcp.tcp/"
	愛處理的標仔 = 合成標籤路徑 + '愛處理的標仔'
	標仔表 = set()
	for line in open(愛處理的標仔):
		標仔表.add(line.strip())
	來源 = 合成標籤路徑 + "alltcp.utf8"
	目標 = 合成標籤路徑 + "alltcp.tai5lo5"
	lines = [line.strip() for line in open(來源)]
	輸出 = open(目標, 'w')
	for line in lines:
		if line == '':
			continue
		if line.split()[0] not in 標仔表:
			continue
# 		if len(line.split())!=3:
# 			print(line)
# 			continue
		編號, *字音 = line.split()
		音標 = 字音[-1]
		# siap8_mih1 siann1_mi4
		更正表 = [('siap8_mih1', 'siann1_mi4'), ('di2_a_giann4', 'di2_a1_giann4'),
			('u_dierh2_lang5_e3_pe3_hu1', 'ut6_dierh2_lang5_e3_pe3_hu1')]
		詞更正表 = [('rip5', 'rip8'), ('huat5', 'huan5')]
		for 原來, 修改 in 更正表:
			if 原來 in 音標:
				音標 = 音標.replace(原來, 修改)
		臺羅 = []
		for 通用 in 音標.split('_'):
# 			if 通用.startswith('mih'):
# 				print(line)
			for 原本, 修正 in 語法錯誤表:
				if 通用 == 原本:
					通用 = 修正
				if ord(通用[-1]) >= 48 and ord(通用[-1]) <= 48 + 9 and 通用[:-1] == 原本:
					通用 = 修正 + 通用[-1]
			for 原本, 修正 in 詞更正表:
				if 通用 == 原本:
					通用 = 修正
			while len(通用) > 1 and 通用[-2] in 數字:
				if 通用[-1] == '0':
					通用 = 通用[:-1]
				else:
					通用 = 通用[:-2] + 通用[-1]
			if 通用[-1] not in 數字:
				if 通用.endswith('h') or 通用.endswith('p') or 通用.endswith('t') or 通用.endswith('k'):
					通用 += '7'
				else:
					通用 += '1'
			if len(通用) == 1:
				if 通用 == 'e':
					通用 = 'e2'
				elif 通用 == 'a':
					通用 = 'a4'
				elif 通用 == 'i':
					通用 = 'i1'
			if len(通用) > 1:
				if 通用[-2] == 'h' or 通用[-2] == 'p' or 通用[-2] == 't' or 通用[-2] == 'k':
# 					if 通用[-1] == '6' or 通用[-1] == '7' or  通用[-1] == '8':
# 						print(通用)
# 						print(line)
					if 通用[-1] == '1' or 通用[-1] == '2' or 通用[-1] == '3':
						通用 = 通用[:-1] + chr(ord(通用[-1]) + 5)
# 						print(通用)
# 						print(line)
						# 咧 閣 物
					if 通用[-1] == '4':
						通用 = 通用[:-2] + 通用[-1]
			臺羅音標 = 通用拼音音標(通用).轉換到臺灣閩南語羅馬字拼音()
			if 臺羅音標 != None:
				臺羅.append(臺羅音標)
			else:
				print("有問題！！")
				print(通用)
				print(line)
		print(編號, '-'.join(臺羅), sep = ' ', end = '\n', file = 輸出)
