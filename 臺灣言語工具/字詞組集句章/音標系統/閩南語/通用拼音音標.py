# -*- coding: utf-8 -*-
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
from 臺灣言語工具.音標系統.閩南語.閩南語音標介面 import 閩南語音標介面
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音

通用拼音佮臺灣羅馬聲母對照表 = {
'b':'p',
'p':'ph',
'bh':'b',
'v':'b',
'm':'m',
'd':'t',
't':'th',
'n':'n',
'l':'l',
'g':'k',
'k':'kh',
'gh':'g',
'q':'g',
'ng':'ng',
'z':'ts',
'c':'tsh',
's':'s',
'r':'j',
'h':'h',
'':'',
}
通用拼音佮臺灣羅馬韻母對照表 = {
	'a':'a', 'ah':'ah', 'ap':'ap', 'at':'at', 'ak':'ak',
	'am':'am', 'an':'an', 'ang':'ang',
	'ann':'ann', 'annh':'annh',
	'ai':'ai', 'aih':'aih', 'ainn':'ainn', 'ainnh':'ainnh',
	'au':'au', 'auh':'auh', 'aunn':'aunn', 'aunnh':'aunnh',
	'e':'e', 'eh':'eh', 'en':'ian', 'et':'iat', 'enn':'enn', 'ennh':'ennh',
	'er':'o', 'erh':'oh', 'ernn':'onn',
	'ia':'ia', 'iah':'iah', 'iap':'iap', 'iak':'iak',
	'iam':'iam', 'iang':'iang',
	'iann':'iann', 'iannh':'iannh',
	'iau':'iau', 'iauh':'iauh', 'iaunn':'iaunn', 'iaunnh':'iaunnh',
	'ier':'io', 'ierh':'ioh',
	'i':'i', 'ih':'ih', 'ip':'ip', 'it':'it', 'ik':'ik',
	'im':'im', 'in':'in', 'ing':'ing',
	'inn':'inn', 'innh':'innh',
	'io':'ioo', 'ioh':'iooh', 'iok':'iok', 'iong':'iong', 'ionn':'ionn',
	'ior':'io', 'iorh':'ioh',
	'iu':'iu', 'iuh':'iuh', 'iut':'iut', 'iunn':'iunn', 'iunnh':'iunnh',
	'm':'m', 'mh':'mh', 'ng':'ng', 'ngh':'ngh',
	'o':'oo', 'oh':'ooh', 'op':'op', 'ok':'ok',
	'om':'om', 'ong':'ong',
	'onn':'onn', 'onnh':'onnh',
	'or':'o', 'orh':'oh', 'orm':'om', 'ornn':'onn',
	'oi':'oi', 'oih':'oih',
	'ua':'ua', 'uah':'uah', 'uat':'uat', 'uak':'uak', 'uainn':'uainn', 'uainnh':'uainnh',
	'uan':'uan', 'uann':'uann', 'uannh':'uannh',
	'uai':'uai', 'uaih':'uaih',
	'ue':'ue', 'ueh':'ueh', 'uenn':'uenn', 'uennh':'uennh',
	'ui':'ui',
	'uih':'uih', 'uinn':'uinn', 'uinnh':'uinnh',
	'u':'u', 'un':'un', 'uh':'uh', 'ut':'ut',
	'ie':'ie', 'uang':'uang',
	}
通用拼音佮臺灣羅馬調類對照表 = {
	'1':'1', '2':'7', '3':'3', '4':'2', '5':'5',
	'6':'8', '7':'4', '8':'10', '9':'9'}
class 通用拼音音標(閩南語音標介面):
	# 0 bh iaunnh 9 保險
	音標上長長度 = 1 + 2 + 6 + 1 + 1
	聲 = None
	韻 = None
	聲韻 = None
	調 = None
	音標 = None
	def __init__(self, 音標):
		self.聲母對照表 = 通用拼音佮臺灣羅馬聲母對照表
		self.韻母對照表 = 通用拼音佮臺灣羅馬韻母對照表
		self.調類對照表 = 通用拼音佮臺灣羅馬調類對照表
		self.音標 = None
		self.音標 = None
		if 音標[-1:] in self.調類對照表:
			for 所在 in range(len(音標) - 1):
				if 音標[:所在] in self.聲母對照表 and 音標[所在:-1] in self.韻母對照表:
					self.聲 = 音標[:所在]
					self.韻 = 音標[所在:-1]
					self.調 = 音標[-1:]
					if self.韻.endswith('h') or self.韻.endswith('p') or \
						self.韻.endswith('t') or self.韻.endswith('k'):
						if self.調 == '1':
							self.調 = '6'
						elif self.調 == '2':
							self.調 = '7'
						elif self.調 == '3':
							self.調 = '8'
					self.聲韻 = self.聲 + self.韻
					self.音標 = self.聲韻 + self.調
		if self.轉換到臺灣閩南語羅馬字拼音() == None:
			self.聲韻 = None
			self.音標 = None

	def 轉換到臺灣閩南語羅馬字拼音(self):
		if self.音標 == None:
			return None
		聲 = self.聲母對照表[self.聲]
		韻 = self.韻母對照表[self.韻]
		調 = self.調類對照表[self.調]
		臺羅 = 臺灣閩南語羅馬字拼音(聲 + 韻 + 調)
		return 臺羅.音標

# if __name__ == '__main__':
# 	for 通, 臺 in 通用拼音佮臺灣羅馬韻母對照表.items():
# 		print("'{0}':'{1}',".format(臺,通))
# 		臺羅 = 臺灣閩南語羅馬字拼音(臺)
# 		if 臺羅.聲 == '':
# # 	 			print("'{0}':'{1}',".format(通,臺))
# 			pass
# 		else:
# 			好通 = ''
# 			好韻 = ''
# 			for 通韻, 臺韻 in 通用拼音佮臺灣語言音標韻母對照表.items():
# 				if 通.endswith(通韻) and len(通韻) > len(好通):
# 					好通 = 通韻
# 					好韻 = 臺韻
# 			print(通[:-len(好通)], 臺[:-len(好韻)])
# 	字音對照 = 通用拼音音標('bai5')
# 	print(字音對照.音標)
# 	print(字音對照.轉換到臺灣閩南語羅馬字拼音())
# 	print(通用拼音音標('zit3').轉換到臺灣閩南語羅馬字拼音())
# 	print(通用拼音音標('zit3').轉換到臺灣閩南語羅馬字拼音())
# 	print('gior4')
# 	print(通用拼音音標('gior4').轉換到臺灣閩南語羅馬字拼音())
# 	print('gier3')
# 	print(通用拼音音標('gier3').轉換到臺灣閩南語羅馬字拼音())
# 	print(max([len (a) for a in 通用拼音佮臺灣語言音標聲韻對照表]))
