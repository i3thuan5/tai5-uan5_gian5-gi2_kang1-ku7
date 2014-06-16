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

臺灣閩南語羅馬字拼音對照音值聲母表 = {
	'p':'p', 'ph':'ph','m':'m','b':'b', 
	't':'t', 'th':'th','n':'n', 'l':'l', 
	'k':'k', 'kh':'kh', 'ng':'ng', 'g':'g', 
	'ts':'ts', 'tsh':'tsh', 's':'s', 'j':'j', 
	'h':'h', '':'',
	}

臺灣閩南語羅馬字拼音對照音值韻母表 = {'a':'a', 
'ah':'ah', 'ap':'ap', 'at':'at', 'ak':'ak', 
'ann':'aⁿ', 'annh':'aⁿh', 
'am':'am', 'an':'an', 'ang':'ang', 'e':'e', 
'eh':'eh', 'enn':'eⁿ', 'ennh':'eⁿh', 
'i':'i', 'ih':'ih', 'ip':'ip', 'it':'it', 'ik':'ik', 
'inn':'iⁿ', 'innh':'iⁿh', 
'im':'im', 'in':'in', 'ing':'ing', 
'o':'o', 'oh':'oh',
'oo':'oo', 'ooh':'ooh', 'op':'op','ok':'ok', 
'om':'om', 'ong':'ong',
'onn':'oⁿ', 'onnh':'oⁿh', 
'oi':'oi', 'oih':'oih', 
'u':'u', 'uh':'uh', 'ut':'ut', 'un':'un', 
'ai':'ai', 'aih':'aih', 'ainn':'aiⁿ', 'ainnh':'aiⁿh', 
'au':'au', 'auh':'auh', 'aunn':'auⁿ', 'aunnh':'auⁿh', 
'ia':'ia', 'iah':'iah', 'iap':'iap', 'iat':'iat', 'iak':'iak', 
'iam':'iam', 'ian':'ian', 'iang':'iang', 
'iann':'iaⁿ', 'iannh':'iaⁿh', 
'io':'io', 'ioh':'ioh', 'iok':'iok', 
'iong':'iong', 'ionn':'ioⁿ', 
'iu':'iu', 'iuh':'iuh', 'iut':'iut', 
'iunn':'iuⁿ', 'iunnh':'iuⁿh', 
'ua':'ua', 'uah':'uah', 'uat':'uat', 'uak':'uak', 
'uan':'uan', 'uann':'uaⁿ', 'uannh':'uaⁿh', 
'ue':'ue', 'ueh':'ueh', 
'uenn':'ueⁿ', 'uennh':'ueⁿh', 
'ui':'ui', 'uih':'uih', 
'uinn':'uiⁿ', 'uinnh':'uiⁿh', 
'iau':'iau', 'iauh':'iauh', 
'iaunn':'iauⁿ', 'iaunnh':'iauⁿh', 
'uai':'uai', 'uaih':'uaih', 
'uainn':'uaiⁿ', 'uainnh':'uaiⁿh', 
'm':'m','mh':'mh', 
'ng':'ng', 'ngh':'ngh', 
'ioo':'ioo', 'iooh':'iooh', 
'er':'er', 'erh':'erh', 
'erm':'erm', 'ere':'ere', 'ereh':'ereh', 
'ee':'ee', 'eeh':'eeh', 'eng':'eng', 'uee':'uee', 
'ir':'ir', 'irh':'irh', 'irp':'irp', 'irt':'irt', 'irk':'irk', 
'irm':'irm', 'irn':'irn', 'irng':'irng', 
'irinn':'iriⁿ', 
'ie':'ie', 
'or':'or', 'orh':'orh', 'ior':'ior', 'iorh':'iorh', 
'uang':'uang', 
				}
for a in 臺灣閩南語羅馬字拼音韻母表:
	print("'{0}':'{0}', ".format(a))
class 臺灣閩南語羅馬字拼音轉音值模組():
	韻母表 = 臺灣閩南語羅馬字拼音對照音值韻母表
	聲 = None
	韻 = None
	調 = None
	音標 = None
	def __init__(self, 聲, 韻, 調, 輕):
		if 聲 == None or 韻 == None or 調 == None or 輕 == None :
			return
		if 聲=='m' or 聲=='n' or 聲=='ng':
			if 'm' not in 韻 and 'n' not in 韻:
				if 韻.endswith('h') or 韻.endswith('p') or 韻.endswith('t') or 韻.endswith('k'):
					韻=韻[:-1]+'nn'+韻[-1]
				else:
					韻+='nn'
				if 韻=='oonnh':
					韻='onnh'
		return (聲,韻)
		if 韻.startswith('i') and (聲 == 'ts' or 聲 == 'tsh' or 聲 == 's' or 聲 == 'j'):
			聲 += 'i'
		if 輕 == '0':
			調 = '0'
		self.聲 = self.聲母表[聲]
		self.韻 = self.韻母表[韻]
		self.調 = self.聲調符號表[調]
		if 調 == '0':
			self.音標 = self.調 + self.聲 + self.韻
		elif 調 == '8':
			self.音標 = self.聲 + self.韻[:-1] + self.調 + self.韻[-1:]
		else:
			self.音標 = self.聲 + self.韻 + self.調
