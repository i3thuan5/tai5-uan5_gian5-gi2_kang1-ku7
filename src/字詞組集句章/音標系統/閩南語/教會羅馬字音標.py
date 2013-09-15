from 字詞組集句章.音標系統.閩南語.教會系羅馬音標 import 教會系羅馬音標

教會羅馬字音標聲母表 = {'p', 'ph', 'm', 'b', 't', 'th', 'n', 'l',
		'k', 'kh', 'ng', 'g', 'h', 'ch', 'chh', 's', 'j', ''}
教會羅馬字音標韻母表 = {'a', 'e', 'i', 'oo', 'o', 'u', 'ai', 'au', 'ia', 'io', 'iu', 'oa', 'oe', 'ui', 'iau', 'oai',
		'ann', 'enn', 'inn', 'onn', 'm', 'ng', 'ainn', 'iann', 'iaunn', 'iunn', 'oann', 'oainn',
		'am', 'an', 'ang', 'im', 'in', 'eng', 'om', 'ong', 'iam', 'ian', 'iang', 'iong', 'un', 'oan',
		'ah', 'eh', 'ih', 'oh', 'uh', 'auh', 'iah', 'ioh', 'iuh', 'iauh', 'oah', 'oeh', 'ooh',
		'annh', 'ennh', 'innh', 'mh', 'iannh', 'ngh', 'ap', 'at', 'ak', 'op', 'ok', 'iok',
		'ip', 'it', 'ek', 'iap', 'iat', 'iak', 'ut', 'oat', }
教會羅馬字音標聲調符號表 = dict(
	á=('a', 2), à=('a', 3), â=('a', 5), ǎ=('a', 6), ā=('a', 7), a̍=('a', 8), a̋=('a', 9),
	é=('e', 2), è=('e', 3), ê=('e', 5), ě=('e', 6), ē=('e', 7), e̍=('e', 8), e̋=('e', 9),
	í=('i', 2), ì=('i', 3), î=('i', 5), ǐ=('i', 6), ī=('i', 7), i̍=('i', 8), i̋=('i', 9),
	ó=('o', 2), ò=('o', 3), ô=('o', 5), ǒ=('o', 6), ō=('o', 7), o̍=('o', 8), ő=('o', 9),
	ú=('u', 2), ù=('u', 3), û=('u', 5), ǔ=('u', 6), ū=('u', 7), u̍=('u', 8), ű=('u', 9),
	ḿ=('m', 2), m̀=('m', 3), m̂=('m', 5), m̌=('m', 6), m̄=('m', 7), m̍=('m', 8), m̋=('m', 9),
	ń=('n', 2), ǹ=('n', 3), n̂=('n', 5), ň=('n', 6), n̄=('n', 7), n̍=('n', 8), n̋=('n', 9),)
class 教會羅馬字音標(教會系羅馬音標):
	聲母表 = 教會羅馬字音標聲母表
	韻母表 = 教會羅馬字音標韻母表
	聲調符號表 = None
	聲 = None
	韻 = None
	調 = 1
	韻頭 = None
	韻腹 = None
	韻尾 = None
	音標 = None
	def __init__(self, 音標):
		self.分析聲韻調(音標)
			
	def 轉換到臺灣閩南語羅馬字拼音(self):
		if self.音標 == None:
			return None
		聲母 = None
		if self.聲 == 'ch':
			聲母 = 'ts'
		elif  self.聲 == 'chh':
			聲母 = 'tsh'
		else:
			聲母 = self.聲
		韻母 = None
		if self.韻[:2] == 'oa':
			韻母 = 'ua' + self.韻[2:]
		elif self.韻[:2] == 'oe':
			韻母 = 'ue' + self.韻[2:]
		elif self.韻 == 'ek':
			韻母 = 'ik'
		elif self.韻 == 'eng':
			韻母 = 'ing'
		else:
			韻母 = self.韻
		return 聲母 + 韻母 + str(self.調)
	# 聲 介 韻 調，韻含元音跟韻尾

if __name__ == '__main__':
	print(教會羅馬字音標('pI̋m').轉換到臺灣閩南語羅馬字拼音())
	print(教會羅馬字音標('pe̍m').轉換到臺灣閩南語羅馬字拼音())
	print(教會羅馬字音標('pi̍m').轉換到臺灣閩南語羅馬字拼音())
	print(教會羅馬字音標('pîm').轉換到臺灣閩南語羅馬字拼音())
	print(教會羅馬字音標('pǐm').轉換到臺灣閩南語羅馬字拼音())
	print(教會羅馬字音標('pih').轉換到臺灣閩南語羅馬字拼音())
	print(教會羅馬字音標('pih8').轉換到臺灣閩南語羅馬字拼音())
	print(教會羅馬字音標('cat8').轉換到臺灣閩南語羅馬字拼音())
