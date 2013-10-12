語料路徑='/home/Ihc/意傳計劃/語音合成/中研院/processed(teacher+student)/'

if __name__ == '__main__':
	import os
	來源="/home/Ihc/意傳計劃/語音合成/中研院/processed(teacher+student)/label/label/mid_score/"
	目標="/home/Ihc/意傳計劃/語音合成/中研院/processed(teacher+student)/label/newlabel/mid_score/"
	os.chdir(來源)
	for 檔名 in os.listdir("."):
		if 檔名.endswith(".lab"):
			lines = [line.strip() for line in open(來源+檔名)]
# 			print('\n'.join(lines[0].split()[0].split('-')))
			輸出 = open(目標+檔名, 'w')
			輸出.write('\n'.join(lines[0].split()[0].split('-')))
			輸出.write('\n')
			輸出.close()