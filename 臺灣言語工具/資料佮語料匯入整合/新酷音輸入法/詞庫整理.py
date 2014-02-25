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
'''
Created on 2013/7/31

@author: chhsueh
'''

def 整理詞庫():
	詞表 = []
	for 逝 in open('/home/ihc/桌面/1020801/新酷音詞庫/tsi'):
		if 逝.strip() == '':
			continue
#		print(逝.strip().split())
		字,頻率,*注音 = 逝.strip().split()
		頻率.split()
		if len(詞表)>0 and 字==詞表[-1][0] and ' '.join(注音)==詞表[-1][1]:
			pass
		elif len(詞表)>0 and 字==詞表[-1][0] and len(字)>1:
			if ('一' in 字 or '兒' in 字 or '刻' in 字 or '場' in 字 or
				'廈' in 字 or '帆' in 字 or '個' in 字):
				詞表.pop()
				詞表.append((字, ' '.join(注音)))
			elif '巫' in 字 or '兒' in 字 or '刻' in 字 or '場' in 字:
				pass
			else:
#				print(詞表[-1])
#				print(逝.strip())
				詞表.append((字, ' '.join(注音)))
		else:
			詞表.append((字, ' '.join(注音)))
#	for 字, 注音 in 詞表:
#		print(字, 注音)
	return 詞表
		
if __name__ == "__main__":
	整理詞庫()
	
