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
	'p':'p', 'ph':'ph', 'm':'m', 'b':'b',
	't':'t', 'th':'th', 'n':'n', 'l':'l',
	'k':'k', 'kh':'kh', 'ng':'ŋ', 'g':'g',
	'ts':'ts', 'tsh':'tsh', 's':'s', 'j':'z',
	'h':'h', '':'ʔ',
	}

臺灣閩南語羅馬字拼音對照音值韻母表 = {
	'a':'a', 'ah':'aʔ', 'ap':'ap', 'at':'at', 'ak':'ak',
	'am':'am', 'an':'an', 'ang':'aŋ',
	'ann':'aⁿ', 'annh':'aⁿʔ',
	'e':'e', 'eh':'eʔ', 'enn':'eⁿ', 'ennh':'eⁿʔ',
	'i':'i', 'ih':'iʔ', 'ip':'ip', 'it':'it', 'ik':'ik',
	'inn':'iⁿ', 'innh':'iⁿʔ',
	'im':'im', 'in':'in', 'ing':'iŋ',
	'o':'ə', 'oh':'əʔ',
	'oo':'o', 'ooh':'oʔ', 'op':'op', 'ok':'ok',
	'om':'om', 'ong':'oŋ',
	'onn':'oⁿ', 'onnh':'oⁿʔ',
	'oi':'əi', 'oih':'əiʔ',  # ##
	'u':'u', 'uh':'uʔ', 'ut':'ut', 'un':'un',
	'ai':'ai', 'aih':'aiʔ', 'ainn':'aiⁿ', 'ainnh':'aiⁿʔ',
	'au':'au', 'auh':'auʔ', 'aunn':'auⁿ', 'aunnh':'auⁿʔ',
	'ia':'ia', 'iah':'iaʔ', 'iap':'iap', 'iat':'iet', 'iak':'iak',
	'iam':'iam', 'ian':'ien', 'iang':'iaŋ',
	'iann':'iaⁿ', 'iannh':'iaⁿʔ',
	'iə':'iə', 'iəh':'iəʔ', 'iok':'iok',
	'iong':'ioŋ', 'ionn':'ioⁿ',
	'iu':'iu', 'iuh':'iuʔ', 'iut':'iut',
	'iunn':'iuⁿ', 'iunnh':'iuⁿʔ',
	'ua':'ua', 'uah':'uaʔ', 'uat':'uat', 'uak':'uak',
	'uan':'uan', 'uann':'uaⁿ', 'uannh':'uaⁿʔ',
	'ue':'ue', 'ueh':'ueʔ',
	'uenn':'ueⁿ', 'uennh':'ueⁿʔ',
	'ui':'ui', 'uih':'uiʔ',
	'uinn':'uiⁿ', 'uinnh':'uiⁿʔ',
	'iau':'iau', 'iauh':'iauʔ',
	'iaunn':'iauⁿ', 'iaunnh':'iauⁿʔ',
	'uai':'uai', 'uaih':'uaiʔ',
	'uainn':'uaiⁿ', 'uainnh':'uaiⁿʔ',
	'm':'m̩', 'mh':'m̩ʔ',
	'ng':'ŋ̩', 'ngh':'ŋ̩ʔ',
	'ioo':'io', 'iooh':'ioʔ',
	'er':'ə', 'erh':'əʔ',
	'erm':'əm', 'ere':'əe', 'ereh':'əeʔ',
	'ee':'ɛ', 'eeh':'ɛʔ', 'eng':'eŋ', 'uee':'uee',
	'ir':'ɨ', 'irh':'ɨʔ', 'irp':'ɨp', 'irt':'ɨt', 'irk':'ɨk',
	'irm':'ɨm', 'irn':'ɨn', 'irng':'ɨŋ',
	'irinn':'ɨiⁿ',
	'ie':'ie',
	'or':'ə', 'orh':'əʔ', 'ior':'iə', 'iorh':'iəʔ',
	'uang':'uaŋ',
	}

class 臺灣閩南語羅馬字拼音轉音值模組():
	聲母表 = 臺灣閩南語羅馬字拼音對照音值聲母表
	韻母表 = 臺灣閩南語羅馬字拼音對照音值韻母表
	聲 = None
	韻 = None
	調 = None
	音標 = None
	def __init__(self, 聲, 韻, 調, 輕):
		if 聲 == None or 韻 == None or 調 == None or 輕 == None :
			return
		self.聲 = self.聲母表[聲]
		self.韻 = self.韻母表[韻]
		self.調 = 調
		if 調 == '0' or 輕 == '0':
			調 = 3
			if self.韻.endswith('ʔ') or self.韻.endswith('p')\
					or self.韻.endswith('t') or self.韻.endswith('k'):
				self.韻 = self.韻[:-1]
		return (self.聲, self.韻, self.調)
