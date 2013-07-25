from 通用拼音音標 import 通用拼音音標
from 臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 毓哲語言辨識.第二步之產生通用點臺羅聲韻對照 import 臺羅聲韻轉辨識合成型
from 毓哲語言辨識.第一步之揣出臺語通用 import 語法錯誤表

if __name__ == '__main__':
# 	字音對照 = 通用拼音音標('bai5')
# 	print(字音對照.音標)
# 	print(字音對照.轉換到臺灣閩南語羅馬字拼音())
# 	lines = [line.strip() for line in open('/home/Ihc/辨識/Syl2Monophone.dic.txt')]
	錯誤對照表={}
	for 原本,修正 in 語法錯誤表:
		錯誤對照表[原本]=修正
		
	lines = [line.strip() for line in open('/home/Ihc/處理愛對齊的語料/臺語通用拼音.dic')]
	對照表={}
	for line in lines:
		if line=='':
			continue
		通用,*音素=line.split()
		if 通用 in 錯誤對照表:
			通用=錯誤對照表[通用]
		if 通用.endswith('h') or 通用.endswith('p') or 通用.endswith('t') or 通用.endswith('k'):
			通用+='7'
		else:
			通用+='1'
		字音對照 = 通用拼音音標(通用)
		if 通用=='sil1':
				對照表['sil']='sil'
		else:
			臺羅拼音=臺灣閩南語羅馬字拼音(字音對照.轉換到臺灣閩南語羅馬字拼音())
			聲,韻=臺羅聲韻轉辨識合成型(臺羅拼音.聲,臺羅拼音.韻)
			if 聲=='':
				對照表[韻]=' '.join(音素)
			else:
				對照表[聲]=音素[0]
				對照表[韻]=' '.join(音素[1:])
	for 對照 in 對照表.items():
		print(' '.join(對照))
				