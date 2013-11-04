from 字詞組集句章.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音聲母對照表
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音聲母表
from 字詞組集句章.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音韻母對照表
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音韻母表
from 字詞組集句章.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音調類對照表
import itertools

元音 = ['a', 'i', 'u', 'e', 'o']
韻尾 = ['m', 'n', 'ng', 'h', 'p', 't', 'k']
鼻化韻 = ['nn', 'nnh']
if __name__ == '__main__':
# 	音表 = [line.strip().split()
# 		for line in open(對齊語料路徑 + '臺羅聲韻查通用音素.dic')]
	音表 = []
	for i in 臺灣客家話拼音聲母對照表:
		if i not in 臺灣閩南語羅馬字拼音聲母表:
			音表.append(i)
	for i in 臺灣客家話拼音韻母對照表:
		if i not in 臺灣閩南語羅馬字拼音韻母表:
			音表.append(i)
	
	聲韻問題版 = [('QS "Si7_{0}" {{ {1} }}', '*-{0}+*'),
		('QS "Si7_Tau5_{0}" {{ {1} }}', '{0}-*'),
		('QS "Si7_Bue2_{0}" {{ {1} }}', '*+{0}/*')]
	for 主問題,小問題 in 聲韻問題版:
		for 音 in 音表[:]:
			print(主問題.format(音,小問題.format(音)))
			
	聲韻問題版 = [('QS "Si7_Tshu2_Tiau3_{0}" {{ {1} }}', '*<{0}>*'),
		('QS "Si7_Tau5_Tiau3_{0}" {{ {1} }}', '*tiau3:{0}<*'),
		('QS "Si7_Bue2_Tiau3_{0}" {{ {1} }}', '*>{0}/*')]
		
	for 主問題,小問題 in 聲韻問題版:
		for 長度 in range(1, len(臺灣客家話拼音調類對照表) + 1):
			for 組合 in itertools.combinations(臺灣客家話拼音調類對照表, 長度):
				名=str(組合).replace(' ','')
				print(主問題.format(名,','.join(map(小問題.format,組合))))
		print(主問題.format('x',小問題.format('x')))
