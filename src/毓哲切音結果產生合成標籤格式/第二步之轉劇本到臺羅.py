from 通用拼音音標 import 通用拼音音標
from 毓哲切音結果產生合成標籤格式.第一步之揣出愛處理的臺詞 import 合成標籤路徑
from 毓哲語言辨識.第一步之揣出臺語通用 import 語法錯誤表
#有足濟所在會當閣改，入聲詞毋著濟
if __name__ == '__main__':
	# 來源="/home/Ihc/意傳計劃/語音合成/中研院/processed(teacher+student)/alltcp.tcp/"
	愛處理的標仔 = 合成標籤路徑 + '愛處理的標仔'
	標仔表 = set()
	for line in open(愛處理的標仔):
		標仔表.add(line.strip())
	來源 = 合成標籤路徑 + "alltcp.utf8"
	目標 = 合成標籤路徑 + "tai5lo5"
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
		#siap8_mih1 siann1_mi4
		for 通用 in 字音[-1].split('_'):
# 			if 通用.startswith('mih'):
# 				print(line)
			if len(通用) > 1:
				if 通用[-2] == 'h' or 通用[-2] == 'p' or 通用[-2] == 't' or 通用[-2] == 'k':
# 					if 通用[-1] == '6' or 通用[-1] == '7' or  通用[-1] == '8':
# 						print(通用)
# 						print(line)
					if 通用[-1] == '1' or 通用[-1] == '2' or 通用[-1] == '3':
						通用 = 通用[:-1] + chr(ord(通用[-1]) + 5)
# 						print(通用)
# 						print(line)
						#咧 閣 物
					if 通用[-1] == '4':
						通用 = 通用[:-2] + 通用[-1]
			for 原本, 修正 in 語法錯誤表:
				if 通用 == 原本:
					通用 = 修正
				if ord(通用[-1]) >= 48 and ord(通用[-1]) <= 48 + 9 and 通用[:-1] == 原本:
					通用 = 修正 + 通用[-1]
			臺羅音標 = 通用拼音音標(通用)
			if 臺羅音標.轉換到臺灣閩南語羅馬字拼音() == None or 通用 == 'sil':
				print(通用)
				print(line)
# 		print(編號,, sep=' ', end='\n', file=輸出)
