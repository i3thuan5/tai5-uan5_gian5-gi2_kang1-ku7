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
from 字詞組集句章.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音聲母對照表
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音聲母表
from 字詞組集句章.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音韻母對照表
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音韻母表
from 字詞組集句章.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音調類對照表
import itertools
import hashlib

class 產生部份問題集:
	元音 = ['a', 'i', 'u', 'e', 'o']
	韻尾 = ['m', 'n', 'ng', 'h', 'p', 't', 'k']
	鼻化韻 = ['nn', 'nnh']
	def __init__(self):
	# 	音表 = [line.strip().split()
	# 		for line in open(對齊語料路徑 + '臺羅聲韻查通用音素.dic')]
		音表 = []
		for i in 臺灣客家話拼音聲母對照表:
			if i not in 臺灣閩南語羅馬字拼音聲母表:
				音表.append(i)
		for i in 臺灣客家話拼音韻母對照表:
			if i not in 臺灣閩南語羅馬字拼音韻母表:
				音表.append(i)
		
		聲韻問題版 = [('QS "Si7_{0}_MD5" {{ {1} }}', '*-{0}+*'),
			('QS "Si7_Tau5_{0}_MD5" {{ {1} }}', '{0}-*'),
			('QS "Si7_Bue2_{0}_MD5" {{ {1} }}', '*+{0}/*')]
		for 主問題,小問題 in 聲韻問題版:
			for 音 in 音表[:]:
				結果=self.輸出問題(主問題.format(音,小問題.format(音)))
				print(結果)
				
		聲韻問題版 = [('QS "Si7_Tshu2_Tiau3_{0}_MD5" {{ {1} }}', '*<{0}>*'),
			('QS "Si7_Tau5_Tiau3_{0}_MD5" {{ {1} }}', '*tiau3:{0}<*'),
			('QS "Si7_Bue2_Tiau3_{0}_MD5" {{ {1} }}', '*>{0}/*')]
			
		for 主問題,小問題 in 聲韻問題版:
			for 長度 in range(1, len(臺灣客家話拼音調類對照表) + 1):
				for 組合 in itertools.combinations(臺灣客家話拼音調類對照表, 長度):
					名=str(組合).replace(' ','')
					結果=self.輸出問題(主問題.format(名,','.join(map(小問題.format,組合))))
					print(結果)
			結果=self.輸出問題(主問題.format('x',小問題.format('x')))
			print(結果)
	def 輸出問題(self,欲好的問題):
		雜湊=hashlib.md5()
		雜湊.update(欲好的問題.encode(encoding='utf_8', errors='strict'))
		雜湊值=雜湊.hexdigest()
		return 欲好的問題.replace('MD5',雜湊值)
		
if __name__ == '__main__':
	產生部份問題集()
