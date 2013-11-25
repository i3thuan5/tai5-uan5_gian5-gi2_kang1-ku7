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
辨識路徑='/home/Ihc/意傳計劃/語音合成/辨識合成實作/一、辨識/'
# 語法錯誤表=[('niunn','niu'),('min','bin'),('ian','iam'),('ghian','giam'),('cian','tshiam'),
# 	('gian','kian'),('hiat','hiak'),('zian','ziam'),('ming','bing'),('mong','bong'),
# 	('puo','phoo'),('huo','hoo'),('s','si'),('z','tsi')]
語法錯誤表=[('niunn','niu'),('min','bin'),('miann','mia'),('mong','bong'),('ming','bing'),

	#拍無著的，有查過原來應該是按怎
	('pian','piann'),('ghian','ghia'),
	('hiat','hiah'),
	('ian','en'),('cian','ciam'),
	('hian','hiam'),('lian','liang'),('tian','tiann'),
	('puo','po'),('huo','hu'),
	('huei','hue'),('ton','to'),('nin','ni'),('ie','iap'),('loi','li'),('n','na'),('guk','gut'),
	('kuang','kang'),('men','me'),
	#有變iann，嘛有iam，iann較濟，予伊較袂汙染著
	('gian','giann'),('zian','zinn'),
	#z佮s後擺無一定是i，但是i較濟，予伊平均
	('s','si'),('z','zi')]

if __name__ == '__main__':
# 	字音對照 = 通用拼音音標('bai5')
# 	print(字音對照.音標)
# 	print(字音對照.轉換到臺灣閩南語羅馬字拼音())
	lines = [line.strip() for line in open(辨識路徑+'Syl2Monophone.dic.txt')]
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
	for 原本,修正 in 語法錯誤表:
		print(原本,end=' ')
		print(' '.join(對照表[修正]))
																		
