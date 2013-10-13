from 字詞組集句章.音標系統.閩南語.教會系羅馬音標 import 教會系羅馬音標
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組 import 臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組

臺灣閩南語羅馬字拼音聲母表 = {'p', 'ph', 'm', 'b', 't', 'th', 'n', 'l',
		'k', 'kh', 'ng', 'g', 'h', 'ts', 'tsh', 's', 'j', ''}
# 臺灣閩南語羅馬字拼音方案使用手冊 + 臺灣語語音入門 + 教育部辭典的字
臺灣閩南語羅馬字拼音韻母表 = {'a', 'e', 'i', 'oo', 'o', 'u',
		'ai', 'au', 'ia', 'io', 'iu', 'ua', 'ue', 'ui', 'iau', 'uai',
		'ann', 'enn', 'inn', 'onn', 'm', 'ng', 'ainn', 'iann', 'iaunn', 'iunn', 'uann', 'uainn',
		'am', 'an', 'ang', 'im', 'in', 'ing', 'om', 'ong', 'iam', 'ian', 'iang', 'iong', 'un', 'uan',
		'ah', 'eh', 'ih', 'oh', 'uh', 'auh', 'iah', 'ioh', 'iuh', 'iauh', 'uah', 'ueh', 'ooh',
		'annh', 'ennh', 'innh', 'mh', 'iannh', 'ngh', 'ap', 'at', 'ak', 'op', 'ok', 'iok',
		'ip', 'it', 'ik', 'iap', 'iat', 'iak', 'ut', 'uat',
		'er', 'ere', 'erh', 'ereh', 'erm', 'ee', 'uee', 'eeh',
		'ir', 'irinn', 'irm', 'irn', 'irng',
		'uinn', 'ionn', 'eng', 'uang', 'irh', 'irp', 'irt', 'irk',
		'ioo','iooh', # 諾 0hioo 0hiooh
		'ie', #	鹿港偏泉腔
		'aih', 'ainnh', 'aunnh', 'uih', } | {
		'aunn', 'uenn', 'uaih', 'iunnh', 'iaunnh', 'uennh', 'uinnh', 'uainnh', 'iut', 'uak'} | {'onnh'} | {
		'or', 'orh', 'ior', 'iorh', }
臺灣閩南語羅馬字拼音聲調符號表 = dict(
	á=('a', 2), à=('a', 3), â=('a', 5), ǎ=('a', 6), ā=('a', 7), a̍=('a', 8), a̋=('a', 9),
	é=('e', 2), è=('e', 3), ê=('e', 5), ě=('e', 6), ē=('e', 7), e̍=('e', 8), e̋=('e', 9),
	í=('i', 2), ì=('i', 3), î=('i', 5), ǐ=('i', 6), ī=('i', 7), i̍=('i', 8), i̋=('i', 9),
	ó=('o', 2), ò=('o', 3), ô=('o', 5), ǒ=('o', 6), ō=('o', 7), o̍=('o', 8), ő=('o', 9),
	ú=('u', 2), ù=('u', 3), û=('u', 5), ǔ=('u', 6), ū=('u', 7), u̍=('u', 8), ű=('u', 9),
	ḿ=('m', 2), m̀=('m', 3), m̂=('m', 5), m̌=('m', 6), m̄=('m', 7), m̍=('m', 8), m̋=('m', 9),
	ń=('n', 2), ǹ=('n', 3), n̂=('n', 5), ň=('n', 6), n̄=('n', 7), n̍=('n', 8), n̋=('n', 9),)

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

臺羅對通用聲對照表={
	'p':'b','ph':'p','m':'m','b':'bh',
	't':'d','th':'t','n':'n','l':'l',
	'k':'g','kh':'k','ng':'ng','g':'gh',
	'ts':'z','tsh':'c','s':'s','j':'r',
	'h':'h','':'',}
臺羅對通用韻對照表={
		
'a':'a',
'ah':'ah',
'ai':'ai',
'ainn':'ainn',
'ak':'ak',
'am':'am',
'an':'an',
'ang':'ang',
'ann':'ann',
'ap':'ap',
'at':'at',
'au':'au',
'aunn':'aunn',
'e':'e',
'eh':'eh',
'enn':'enn',
'iah':'iah',
'ia':'ia',
'iak':'iak',
'iam':'iam',
'ian':'en',
'iang':'iang',
'iannh':'iannh',
'iann':'iann',
'iap':'iap',
'iat':'et',
'iau':'iau',
'iaunn':'iaunn',
'ih':'ih',
'i':'i',
'ik':'ik',
'im':'im',
'ing':'ing',
'in':'in',
'innh':'innh',
'inn':'inn',
'ioh':'iorh',
'io':'io',
'io':'ior',
'iok':'iok',
'iong':'iong',
'ionn':'ionn',
'ip':'ip',
'it':'it',
'iu':'iu',
'iunn':'iunn',
'm':'m',
'ng':'ng',
'o':'er',
'oh':'erh',
'oh':'orh',
'ok':'ok',
'om':'om',
'ong':'ong',
'onn':'onn',
'ooh':'oh',
'oo':'o',
'o':'or',
'uah':'uah',
'uainnh':'uainnh',
'uainn':'uainn',
'uai':'uai',
'uann':'uann',
'uan':'uan',
'uat':'uat',
'ua':'ua',
'ueh':'ueh',
'ue':'ue',
'uh':'uh',
'uih':'uih',
'uinn':'uinn',
'ui':'ui',
'un':'un',
'ut':'ut',
'u':'u',
		}
臺羅對通用調對照表={'1':'1', '7':'2', '3':'3', '2':'4', '5':'5', '8':'6', '4':'7', '10':'8', '9':'9',}
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

		return self.聲 + self.韻.replace(替代符號, self.數字調轉閏號調表[(替代符號, self.調)])
# 	def 轉吳守禮方音(self):
# 		return 方音符號吳守禮改良式(self.音標).音標
# 	def 轉吳守禮方音組字式(self):
# 		return 方音符號吳守禮改良式(self.音標).產生音標組字式()
	def 轉通用拼音(self):
		if self.音標 == None:
			return None
		if self.聲 not in self.對通用聲對照表 or self.韻 not in self.對通用韻對照表 or self.調 not in self.對通用調對照表:
			raise RuntimeError('轉通用拼音時對照表有問題！！')
		return self.對通用聲對照表[self.聲] +self.對通用韻對照表[self.韻] + self.對通用調對照表[self.調]
	def 產生吳守禮方音物件(self):
		return 臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組(self.聲, self.韻, self.調, self.輕)
