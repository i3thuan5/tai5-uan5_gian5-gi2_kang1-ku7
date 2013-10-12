from 通用拼音音標 import 通用拼音音標
from 臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 毓哲語言辨識.第一步之揣出臺語通用 import 語法錯誤表
from 毓哲語言辨識.第一點一步之檢查通用臺音標對照表 import 對齊語料路徑

def 臺羅聲韻轉辨識合成型(聲,韻):
	if 聲=='m' or 聲=='n' or 聲=='ng':
		if 'm' not in 韻 and 'n' not in 韻:
			if 韻.endswith('h') or 韻.endswith('p') or 韻.endswith('t') or 韻.endswith('k'):
				韻=韻[:-1]+'nn'+韻[-1]
			else:
				韻+='nn'
			if 韻=='oonnh':
				韻='onnh'
	return (聲,韻)
	

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
				
				