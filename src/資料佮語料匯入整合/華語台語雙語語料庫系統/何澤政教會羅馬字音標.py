from 字詞組集句章.音標系統.閩南語.教會系羅馬音標 import 教會系羅馬音標
from 字詞組集句章.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標韻母表
from 字詞組集句章.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標聲母表
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音韻母表

何澤政教會羅馬字音標韻母表 = 教會羅馬字音標韻母表 | {'ou', 'ouh', } | 臺灣閩南語羅馬字拼音韻母表

class 何澤政教會羅馬字音標(教會系羅馬音標):
	聲母表 = 教會羅馬字音標聲母表
	韻母表 = 何澤政教會羅馬字音標韻母表
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
		elif self.韻 == 'ou':
			韻母 = 'oo'
		elif self.韻 == 'ouh':
			韻母 = 'ooh'
		else:
			韻母 = self.韻
		return 聲母 + 韻母 + str(self.調)
	# 聲 介 韻 調，韻含元音跟韻尾

if __name__ == '__main__':
	print(何澤政教會羅馬字音標('pI̋m').轉換到臺灣閩南語羅馬字拼音())
	print(何澤政教會羅馬字音標('pe̍m').轉換到臺灣閩南語羅馬字拼音())
	print(何澤政教會羅馬字音標('pi̍m').轉換到臺灣閩南語羅馬字拼音())
	print(何澤政教會羅馬字音標('pîm').轉換到臺灣閩南語羅馬字拼音())
	print(何澤政教會羅馬字音標('pǐm').轉換到臺灣閩南語羅馬字拼音())
	print(何澤政教會羅馬字音標('pih').轉換到臺灣閩南語羅馬字拼音())
	print(何澤政教會羅馬字音標('pih8').轉換到臺灣閩南語羅馬字拼音())
	print(何澤政教會羅馬字音標('cat8').轉換到臺灣閩南語羅馬字拼音())
	print(何澤政教會羅馬字音標('mou').轉換到臺灣閩南語羅馬字拼音())
