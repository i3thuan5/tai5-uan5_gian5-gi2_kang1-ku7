對齊語料路徑='/home/Ihc/意傳計劃/語音合成/辨識合成實作/二、處理愛對齊的語料/'
if __name__ == '__main__':
	對照表=set()
	lines = [line.strip() for line in open(對齊語料路徑+'臺語通用拼音.dic')]
	for line in lines:
		if line=='':
			continue
		通用,*音素=line.split()
		對照表.add(通用)
	來源="/home/Ihc/tmpfs/mid_syl_list"
	lines = [line.strip() for line in open(來源)]
	for line in lines:
		通用,*音素=line.split()
		if 通用 in 對照表:
# 			print(line)
			pass
		else:
			print(通用)
# 			print(字音對照.音標)
# 			print(字音對照.轉換到臺灣閩南語羅馬字拼音())
#			grep -v er xx| grep -v eu | grep -v y | grep -v ei | grep -v ou | grep -v ii | grep -v uo | grep -v ung | grep -v ch | grep -v zh | grep -v sh | grep -v oi | grep -v em | grep -v ep | grep -v r | grep -v uang
			pass