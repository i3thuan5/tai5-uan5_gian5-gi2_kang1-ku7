from 通用拼音音標 import 通用拼音音標


if __name__ == '__main__':
# 	字音對照 = 通用拼音音標('bai5')
# 	print(字音對照.音標)
# 	print(字音對照.轉換到臺灣閩南語羅馬字拼音())
	lines = [line.strip() for line in open('/home/Ihc/辨識/Syl2Monophone.dic.txt')]
# 	lines = [line.strip() for line in open('/home/Ihc/處理愛對齊的語料/臺語通用拼音.dic')]
	對照表={}
	for line in lines:
		通用,*音素=line.split()
		if 通用.endswith('h') or 通用.endswith('p') or 通用.endswith('t') or 通用.endswith('k'):
			通用+='7'
		else:
			通用+='1'
		字音對照 = 通用拼音音標(通用)
		if 字音對照.轉換到臺灣閩南語羅馬字拼音()!=None or 通用=='sil1':
			print(line)
			對照表[通用[:-1]]=音素
			pass
		else:
# 			print(通用[:-1])
# 			print(字音對照.音標)
# 			print(字音對照.轉換到臺灣閩南語羅馬字拼音())
#			grep -v er xx| grep -v eu | grep -v y | grep -v ei | grep -v ou | grep -v ii | grep -v uo | grep -v ung | grep -v ch | grep -v zh | grep -v sh | grep -v oi | grep -v em | grep -v ep | grep -v r | grep -v uang
			pass
# 	語法錯誤表=[('niunn','niu'),('min','bin'),('ian','iam'),('ghian','giam'),('cian','tshiam'),
# 		('gian','kian'),('hiat','hiak'),('zian','ziam'),('ming','bing'),('mong','bong'),
# 		('puo','phoo'),('huo','hoo'),('s','si'),('z','tsi')]
	語法錯誤表=[('niunn','niu'),('min','bin'),('ian','iam'),('ghian','ghiam'),('cian','ciam'),
		('gian','giam'),('hiat','hiah'),('zian','ziam'),('ming','bing'),('mong','bong'),
		('puo','po'),('huo','ho'),('s','si'),('z','zi')]
	for 原本,修正 in 語法錯誤表:
		print(原本,end=' ')
		print(' '.join(對照表[修正]))
																		
