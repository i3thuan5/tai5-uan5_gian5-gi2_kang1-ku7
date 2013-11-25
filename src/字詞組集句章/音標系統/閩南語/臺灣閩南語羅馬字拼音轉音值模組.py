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
#臺灣閩南語羅馬字拼音對照音值韻母表 = {
#	'a', 'ah', 'ap', 'at', 'ak', 'ann', 'annh',
#	'am', 'an', 'ang',
#	'e', 'eh', 'enn', 'ennh',
#	'i', 'ih', 'ip', 'it', 'ik', 'inn', 'innh',
#	'im', 'in', 'ing',
#	'o', 'oh',
#	'oo', 'ooh', 'op', 'ok', 'om', 'ong', 'onn', 'onnh',
#	'oi', 'oih',  # 硩⿰落去
#	'u', 'uh', 'ut', 'un',
#	'ai', 'aih', 'ainn', 'ainnh',
#	'au', 'auh', 'aunn', 'aunnh',
#	'ia', 'iah', 'iap', 'iat', 'iak', 'iam', 'ian', 'iang', 'iann', 'iannh',
#	'io', 'ioh',
#	'iok', 'iong', 'ionn',
#	'iu', 'iuh', 'iut', 'iunn', 'iunnh',
#	'ua', 'uah', 'uat', 'uak', 'uan', 'uann', 'uannh',
#	'ue', 'ueh', 'uenn', 'uennh',
#	'ui', 'uih', 'uinn', 'uinnh',
#	'iau', 'iauh', 'iaunn', 'iaunnh',
#	'uai', 'uaih', 'uainn', 'uainnh',
#	'm', 'mh', 'ng', 'ngh',
#	'er', 'erh', 'erm', 'ere', 'ereh',  # 泉　鍋
#	'ee', 'eeh', 'eng', 'uee',  # 漳　家
#	'ir', 'irh', 'irp', 'irt', 'irk', 'irm', 'irn', 'irng', 'irinn',
#	'ioo', 'iooh',  # 諾 0hioo 0hiooh
#	'ie',  # 鹿港偏泉腔
#	'uang',
#	'or', 'orh', 'ior', 'iorh',  # 蚵
#		}
#
#class 臺灣閩南語羅馬字拼音轉音值模組():
#	韻母表 = 臺灣閩南語羅馬字拼音對照音值韻母表
#	聲 = None
#	韻 = None
#	調 = None
#	音標 = None
#	def __init__(self, 聲, 韻, 調, 輕):
#		if 聲 == None or 韻 == None or 調 == None or 輕 == None :
#			return
#		if 聲=='m' or 聲=='n' or 聲=='ng':
#			if 'm' not in 韻 and 'n' not in 韻:
#				if 韻.endswith('h') or 韻.endswith('p') or 韻.endswith('t') or 韻.endswith('k'):
#					韻=韻[:-1]+'nn'+韻[-1]
#				else:
#					韻+='nn'
#				if 韻=='oonnh':
#					韻='onnh'
#		return (聲,韻)
#		if 韻.startswith('i') and (聲 == 'ts' or 聲 == 'tsh' or 聲 == 's' or 聲 == 'j'):
#			聲 += 'i'
#		if 輕 == '0':
#			調 = '0'
#		self.聲 = self.聲母表[聲]
#		self.韻 = self.韻母表[韻]
#		self.調 = self.聲調符號表[調]
#		if 調 == '0':
#			self.音標 = self.調 + self.聲 + self.韻
#		elif 調 == '8':
#			self.音標 = self.聲 + self.韻[:-1] + self.調 + self.韻[-1:]
#		else:
#			self.音標 = self.聲 + self.韻 + self.調
