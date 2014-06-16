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
from 臺灣言語工具.音標系統.閩南語.教會系羅馬音標 import 教會系羅馬音標
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組 import 臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音轉音值模組 import 臺灣閩南語羅馬字拼音轉音值模組

臺灣閩南語羅馬字拼音聲母表 = {
	'p', 'ph', 'm', 'b',
	't', 'th', 'n', 'l',
	'k', 'kh', 'ng', 'g',
	'ts', 'tsh', 's', 'j',
	'h', '', }
# 臺灣閩南語羅馬字拼音方案使用手冊 + 臺灣語語音入門 + 教育部辭典的字
# 歌仔戲：枝頭 ki1 thiou5， 土 thou。目前教羅共ou轉oo（因為台華辭典按呢處理）
臺灣閩南語羅馬字拼音韻母表 = {
	'a', 'ah', 'ap', 'at', 'ak', 'ann', 'annh',
	'am', 'an', 'ang',
	'e', 'eh', 'enn', 'ennh',
	'i', 'ih', 'ip', 'it', 'ik', 'inn', 'innh',
	'im', 'in', 'ing',
	'o', 'oh',
	'oo', 'ooh', 'op', 'ok', 'om', 'ong', 'onn', 'onnh',
	'oi', 'oih',  # 硩⿰落去
	'u', 'uh', 'ut', 'un',
	'ai', 'aih', 'ainn', 'ainnh',
	'au', 'auh', 'aunn', 'aunnh',
	'ia', 'iah', 'iap', 'iat', 'iak', 'iam', 'ian', 'iang', 'iann', 'iannh',
	'io', 'ioh',
	'iok', 'iong', 'ionn',
	'iu', 'iuh', 'iut', 'iunn', 'iunnh',
	'ua', 'uah', 'uat', 'uak', 'uan', 'uann', 'uannh',
	'ue', 'ueh', 'uenn', 'uennh',
	'ui', 'uih', 'uinn', 'uinnh',
	'iau', 'iauh', 'iaunn', 'iaunnh',
	'uai', 'uaih', 'uainn', 'uainnh',
	'm', 'mh', 'ng', 'ngh',
	'ioo', 'iooh',  # 諾 0hioo 0hiooh
	'er', 'erh', 'erm', 'ere', 'ereh',  # 泉　鍋
	'ee', 'eeh', 'eng', 'uee',  # 漳　家
	'ir', 'irh', 'irp', 'irt', 'irk', 'irm', 'irn', 'irng', 'irinn',
	'ie',  # 鹿港偏泉腔
	'or', 'orh', 'ior', 'iorh',  # 蚵
	'uang',  # 金門偏泉腔　　風　huang1
	}
臺灣閩南語羅馬字拼音聲調符號表 = dict(
	á = ('a', 2), à = ('a', 3), â = ('a', 5), ǎ = ('a', 6), ā = ('a', 7), a̍ = ('a', 8), a̋ = ('a', 9),
	é = ('e', 2), è = ('e', 3), ê = ('e', 5), ě = ('e', 6), ē = ('e', 7), e̍ = ('e', 8), e̋ = ('e', 9),
	í = ('i', 2), ì = ('i', 3), î = ('i', 5), ǐ = ('i', 6), ī = ('i', 7), i̍ = ('i', 8), i̋ = ('i', 9),
	ó = ('o', 2), ò = ('o', 3), ô = ('o', 5), ǒ = ('o', 6), ō = ('o', 7), o̍ = ('o', 8), ő = ('o', 9),
	ú = ('u', 2), ù = ('u', 3), û = ('u', 5), ǔ = ('u', 6), ū = ('u', 7), u̍ = ('u', 8), ű = ('u', 9),
	ḿ = ('m', 2), m̀ = ('m', 3), m̂ = ('m', 5), m̌ = ('m', 6), m̄ = ('m', 7), m̍ = ('m', 8), m̋ = ('m', 9),
	ń = ('n', 2), ǹ = ('n', 3), n̂ = ('n', 5), ň = ('n', 6), n̄ = ('n', 7), n̍ = ('n', 8), n̋ = ('n', 9),)

臺灣閩南語羅馬字拼音數字調轉閏號調表 = {
	('a', '2'):"á", ('a', '3'):"à", ('a', '5'):"â", ('a', '6'):"ǎ", ('a', '7'):"ā", ('a', '8'):"a̍", ('a', '9'):"a̋",
	('e', '2'):"é", ('e', '3'):"è", ('e', '5'):"ê", ('e', '6'):"ě", ('e', '7'):"ē", ('e', '8'):"e̍", ('e', '9'):"e̋",
	('ee', '2'):"ée", ('ee', '3'):"èe", ('ee', '5'):"êe", ('ee', '6'):"ěe", ('ee', '7'):"ēe", ('ee', '8'):"e̍e", ('ee', '9'):"e̋e",
	('ere', '2'):"eré", ('ere', '3'):"erè", ('ere', '5'):"erê", ('ere', '6'):"erě", ('ere', '7'):"erē", ('ere', '8'):"ere̍", ('ere', '9'):"ere̋",
	('i', '2'):"í", ('i', '3'):"ì", ('i', '5'):"î", ('i', '6'):"ǐ", ('i', '7'):"ī", ('i', '8'):"i̍", ('i', '9'):"i̋",
	('iri', '2'):"irí", ('iri', '3'):"irì", ('iri', '5'):"irî", ('iri', '6'):"irǐ", ('iri', '7'):"irī", ('iri', '8'):"iri̍", ('iri', '9'):"iri̋",
	('m', '2'):"ḿ", ('m', '3'):"m̀", ('m', '5'):"m̂", ('m', '6'):"m̌", ('m', '7'):"m̄", ('m', '8'):"m̍", ('m', '9'):"m̋",
	('ng', '2'):"ńg", ('ng', '3'):"ǹg", ('ng', '5'):"n̂g", ('ng', '6'):"ňg", ('ng', '7'):"n̄g", ('ng', '8'):"n̍g", ('ng', '9'):"n̋g",
	('o', '2'):"ó", ('o', '3'):"ò", ('o', '5'):"ô", ('o', '6'):"ǒ", ('o', '7'):"ō", ('o', '8'):"o̍", ('o', '9'):"ő",
	('oo', '2'):"óo", ('oo', '3'):"òo", ('oo', '5'):"ôo", ('oo', '6'):"ǒo", ('oo', '7'):"ōo", ('oo', '8'):"o̍o", ('oo', '9'):"őo",
	('u', '2'):"ú", ('u', '3'):"ù", ('u', '5'):"û", ('u', '6'):"ǔ", ('u', '7'):"ū", ('u', '8'):"u̍", ('u', '9'):"ű",
	('ui', '2'):"uí", ('ui', '3'):"uì", ('ui', '5'):"uî", ('ui', '6'):"uǐ", ('ui', '7'):"uī", ('ui', '8'):"ui̍", ('ui', '9'):"ui̋",
	('iu', '2'):"iú", ('iu', '3'):"iù", ('iu', '5'):"iû", ('iu', '6'):"iǔ", ('iu', '7'):"iū", ('iu', '8'):"iu̍", ('iu', '9'):"iű", }

臺羅對通用聲對照表 = {
	'p':'b', 'ph':'p', 'm':'m', 'b':'bh',
	't':'d', 'th':'t', 'n':'n', 'l':'l',
	'k':'g', 'kh':'k', 'ng':'ng', 'g':'gh',
	'ts':'z', 'tsh':'c', 's':'s', 'j':'r',
	'h':'h', '':'', }
臺羅對通用韻對照表 = {
	'a':'a', 'am':'am', 'an':'an', 'ang':'ang',
	'ah':'ah', 'ap':'ap', 'at':'at', 'ak':'ak',
	'ann':'ann', 'annh':'annh',
	'ai':'ai', 'aih':'aih', 'ainn':'ainn', 'ainnh':'ainnh',
	'au':'au', 'auh':'auh', 'aunn':'aunn', 'aunnh':'aunnh',
	'e':'e', 'eh':'eh', 'enn':'enn', 'ennh':'ennh',
	'ia':'ia', 'iah':'iah', 'iap':'iap', 'iat':'et', 'iak':'iak',
	'iam':'iam', 'ian':'en', 'iang':'iang',
	'iann':'iann', 'iannh':'iannh',
	'iau':'iau', 'iauh':'iauh', 'iaunn':'iaunn', 'iaunnh':'iaunnh',
	'i':'i', 'ih':'ih', 'ip':'ip', 'it':'it', 'ik':'ik',
	'im':'im', 'in':'in', 'ing':'ing',
	'inn':'inn', 'innh':'innh',
	'io':'ior', 'ioh':'iorh',
	'ioo':'io', 'iooh':'ioh', 'ionn':'ionn', 'iok':'iok', 'iong':'iong',
	'iu':'iu', 'iuh':'iuh', 'iut':'iut', 'iunn':'iunn', 'iunnh':'iunnh',
	'm':'m', 'mh':'mh', 'ng':'ng', 'ngh':'ngh',
	'o':'or', 'oh':'orh', 'op':'op',
	'om':'om', 'ong':'ong',
	'oo':'o', 'ooh':'oh', 'ok':'ok', 'onn':'onn', 'onnh':'onnh',
	'oi':'oi', 'oih':'oih',
	'ua':'ua', 'uah':'uah', 'uat':'uat', 'uak':'uak',
	'uann':'uann', 'uannh':'uannh', 'uan':'uan',
	'uai':'uai', 'uaih':'uaih', 'uainn':'uainn', 'uainnh':'uainnh',
	'ue':'ue', 'ueh':'ueh', 'uenn':'uenn', 'uennh':'uennh',
	'ui':'ui', 'uih':'uih', 'uinn':'uinn', 'uinnh':'uinnh',
	'u':'u', 'uh':'uh', 'ut':'ut',
	'un':'un',
	# 下跤是方音
	'or':'or', 'orh':'orh', 'ior':'ior', 'iorh':'iorh',
	'ee':'e', 'eeh':'eh', 'eng':'ing', 'uee':'ue',
	'ir':'i', 'irh':'ih', 'irp':'ip', 'irt':'it', 'irk':'ik',
	'irm':'im', 'irn':'in', 'irng':'ing', 'irinn':'inn',  # 無確定
	'er':'or', 'erh':'orh', 'erm':'orm', 'erm':'orm', 'ere':'er', 'ereh':'erh',
	'ie':'ie', 'uang':'uang',
}
臺羅對通用調對照表 = {'1':'1', '7':'2', '3':'3', '2':'4', '5':'5', '8':'6', '4':'7', '10':'8', '9':'9', '6':'7'}
class 臺灣閩南語羅馬字拼音(教會系羅馬音標):
	聲母表 = 臺灣閩南語羅馬字拼音聲母表
	韻母表 = 臺灣閩南語羅馬字拼音韻母表
	聲調符號表 = None
	聲 = None
	韻 = None
	調 = 1
	輕 = ''
	韻頭 = None
	韻腹 = None
	韻尾 = None
	音標 = None

	數字調轉閏號調表 = 臺灣閩南語羅馬字拼音數字調轉閏號調表

	對通用聲對照表 = 臺羅對通用聲對照表
	對通用韻對照表 = 臺羅對通用韻對照表
	對通用調對照表 = 臺羅對通用調對照表
	轉音值模組=臺灣閩南語羅馬字拼音轉音值模組()
	def __init__(self, 音標):
		self.分析聲韻調(音標)
		if self.聲 == 'm' or self.聲 == 'n' or self.聲 == 'ng':
			if self.韻 == 'o':
				self.韻 = 'oo'
				self.做音標()
	def 轉換到臺灣閩南語羅馬字拼音(self):
		return self.音標
	def 轉閏號調(self):
		if self.音標 == None:
			return None

		if (self.調 != '2' and self.調 != '3' and self.調 != '5' and self.調 != '6'
			and self.調 != '7' and self.調 != '8' and self.調 != '9'):  # or 調!=10:
			return self.聲 + self.韻

		for 符號 in ['a', 'oo', 'o', 'ee', 'ere', 'e', 'iri', 'ui', 'iu', 'u', 'i', 'ng', 'm']:
			if 符號 in self.音標:
				替代符號 = 符號
				break
		return self.輕 + self.日本話\
			+ self.聲 + self.韻.replace(替代符號, self.數字調轉閏號調表[(替代符號, self.調)])
# 	def 轉吳守禮方音(self):
# 		return 方音符號吳守禮改良式(self.音標).音標
# 	def 轉吳守禮方音組字式(self):
# 		return 方音符號吳守禮改良式(self.音標).產生音標組字式()
	def 轉通用拼音(self):
		if self.音標 == None:
			return None
		if self.聲 not in self.對通用聲對照表 or self.韻 not in self.對通用韻對照表 or self.調 not in self.對通用調對照表:
			raise RuntimeError(
				'轉通用拼音時對照表有問題！！{0}、{1}、{2}、{3}、{4}、{5}'
				.format(self.聲, self.韻, self.調,
				 self.韻 in self.對通用韻對照表, self.調 in self.對通用調對照表))
		return self.對通用聲對照表[self.聲] + self.對通用韻對照表[self.韻] + self.對通用調對照表[self.調]
	def 產生吳守禮方音物件(self):
		return 臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組(self.聲, self.韻, self.調, self.輕)
	def 音值(self):
		return self.轉音值模組.轉(self.聲, self.韻, self.調, self.輕)
