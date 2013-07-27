from 毓哲語言辨識.第零步之處理標籤格式 import 語料路徑

合成標籤路徑='/home/Ihc/意傳計劃/語音合成/辨識合成實作/三、切音標籤到合成/'
if __name__ == '__main__':
	import os
	懸來源 = 語料路徑 + "label/newlabel/high_score/"
	中來源 = 語料路徑 + "label/newlabel/mid_score/"
	
	目標=合成標籤路徑+'愛處理的標仔'
	輸出=open(目標,'w')
	檔案表 = set()
	os.chdir(懸來源)
	for files in os.listdir("."):
		if files.endswith(".lab"):
			切割 = files.split('_')
			if len(切割) == 2:
				檔案表.add(切割[0])
			else:
				print(files)
	os.chdir(中來源)
	for files in os.listdir("."):
		if files.endswith(".lab"):
			切割 = files.split('_')
			if len(切割) == 2:
				檔案表.add(切割[0])
			else:
				print(files)
	for 檔案 in 檔案表:
		print(檔案,file=輸出)
