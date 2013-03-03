from 教會系羅馬音標 import 教會系羅馬音標

臺灣閩南語羅馬字拼音聲母表 = {'p', 'ph', 'm', 'b', 't', 'th', 'n', 'l',
		'k', 'kh', 'ng', 'g', 'h', 'ts', 'tsh', 's', 'j', ''}
#臺灣閩南語羅馬字拼音方案使用手冊 + 臺灣語語音入門 + 教育部辭典的字
臺灣閩南語羅馬字拼音韻母表 = {'a', 'e', 'i', 'oo', 'o', 'u',
		'ai', 'au', 'ia', 'io', 'iu', 'ua', 'ue', 'ui', 'iau', 'uai',
		'ann', 'enn', 'inn', 'onn', 'm', 'ng', 'ainn', 'iann', 'iaunn', 'iunn', 'uann', 'uainn',
		'am', 'an', 'ang', 'im', 'in', 'ing', 'om', 'ong', 'iam', 'ian', 'iang', 'iong', 'un', 'uan',
		'ah', 'eh', 'ih', 'oh', 'uh', 'auh', 'iah', 'ioh', 'iuh', 'iauh', 'uah', 'ueh', 'ooh',
		'annh', 'ennh', 'innh', 'mh', 'iannh', 'ngh', 'ap', 'at', 'ak', 'op', 'ok', 'iok',
		'ip', 'it', 'ik', 'iap', 'iat', 'iak', 'ut', 'uat',
		'ioo', 'ir', 'ere', 'er', 'irinn', 'ee', 'uee', 'eeh', 'uinn', 'ionn', 'irm', 'irn', 'irng', 'eng', 'uang',
		'aih', 'ainnh', 'aunnh', 'erh', 'ereh', 'uih', 'irp', 'irt', 'irk', } | {
		'aunn', 'uenn','uaih', 'iunnh', 'iaunnh', 'uennh', 'uinnh', 'uainnh', 'iut', 'uak'} |{'onnh'}
臺灣閩南語羅馬字拼音聲調符號表 = dict(á = ('a', 2), à = ('a', 3), â = ('a', 5), ǎ = ('a', 6), ā = ('a', 7), a̍ = ('a', 8), a̋ = ('a', 9),
é = ('e', 2), è = ('e', 3), ê = ('e', 5), ě = ('e', 6), ē = ('e', 7), e̍ = ('e', 8), e̋ = ('e', 9),
í = ('i', 2), ì = ('i', 3), î = ('i', 5), ǐ = ('i', 6), ī = ('i', 7), i̍ = ('i', 8), i̋ = ('i', 9),
ó = ('o', 2), ò = ('o', 3), ô = ('o', 5), ǒ = ('o', 6), ō = ('o', 7), o̍ = ('o', 8), ő = ('o', 9),
ú = ('u', 2), ù = ('u', 3), û = ('u', 5), ǔ = ('u', 6), ū = ('u', 7), u̍ = ('u', 8), ű = ('u', 9),
ḿ = ('m', 2), m̀ = ('m', 3), m̂ = ('m', 5), m̌ = ('m', 6), m̄ = ('m', 7), m̍ = ('m', 8), m̋ = ('m', 9),
ń = ('n', 2), ǹ = ('n', 3), n̂ = ('n', 5), ň = ('n', 6), n̄ = ('n', 7), n̍ = ('n', 8), n̋ = ('n', 9),)

class 臺灣閩南語羅馬字拼音(教會系羅馬音標):
	聲母表 = 臺灣閩南語羅馬字拼音聲母表
	韻母表 = 臺灣閩南語羅馬字拼音韻母表
	聲調符號表 = None
	聲 = None
	韻 = None
	調 = 1
	輕 = False
	韻頭 = None
	韻腹 = None
	韻尾 = None
	音標 = None
	def __init__(self, 音標):
		self.分析聲韻調(音標)
#		if self.音標 != None:			
#			print('聲母=' + self.聲 + ' 韻母=' + self.韻 + ' 調＝' + str(self.調))
#		else:
#			print('不合法 原音標＝' + 音標)
	def 轉換到臺灣閩南語羅馬字拼音(self):
		return self.音標
# 聲 介 韻 調，韻含元音跟韻尾

if __name__ == '__main__':
	print (len(臺灣閩南語羅馬字拼音韻母表))
	print(臺灣閩南語羅馬字拼音('@@').音標)
	print(臺灣閩南語羅馬字拼音('pI̋m').音標)
	print(臺灣閩南語羅馬字拼音('pe̍m').音標)
	print(臺灣閩南語羅馬字拼音('pi̍m').音標)
	print(臺灣閩南語羅馬字拼音('pîm').音標)
	print(臺灣閩南語羅馬字拼音('pǐN').音標)
	print(臺灣閩南語羅馬字拼音('pih').音標)
	print(臺灣閩南語羅馬字拼音('cat8').音標)
	print(臺灣閩南語羅馬字拼音('Pih8').音標)

	print(臺灣閩南語羅馬字拼音('nňg').音標)
	print(臺灣閩南語羅馬字拼音('tor').音標)
	print(臺灣閩南語羅馬字拼音('tsőo').音標)
	print(臺灣閩南語羅馬字拼音('tsňg').音標)
	print(臺灣閩南語羅馬字拼音('xxtsé--á').音標)
	print(臺灣閩南語羅馬字拼音('pňg').音標)
	print(臺灣閩南語羅馬字拼音('óonn').音標)
	