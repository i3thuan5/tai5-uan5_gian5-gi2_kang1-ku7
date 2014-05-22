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
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音聲母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音韻母表

教會羅馬字音標聲母表 = {'p', 'ph', 'm', 'b', 't', 'th', 'n', 'l',
		'k', 'kh', 'ng', 'g', 'h', 'ch', 'chh', 's', 'j', ''
		} | 臺灣閩南語羅馬字拼音聲母表
教會羅馬字音標韻母表 = {
	'a', 'ah', 'ap', 'at', 'ak', 'ann', 'annh',
	'am', 'an', 'ang',
	'e', 'eh', 'enn', 'ennh',
	'i', 'ih', 'ip', 'it', 'ek', 'inn', 'innh',
	'im', 'in', 'eng',
	'o', 'oh',
	'oo', 'ooh', 'op', 'ok', 'om', 'ong', 'onn', 'onnh',
	'ou', 'ouh',
	'oi', 'oih',  # 硩⿰落去
	'u', 'uh', 'ut', 'un',
	'ai', 'aih', 'ainn', 'ainnh',
	'au', 'auh', 'aunn', 'aunnh',
	'ia', 'iah', 'iap', 'iat', 'iak', 'iam', 'ian', 'iang', 'iann', 'iannh',
	'io', 'ioh',
	'iok', 'iong', 'ionn',
	'iu', 'iuh', 'iut', 'iunn', 'iunnh',
	'oa', 'oah', 'oat', 'oak', 'oan', 'oann', 'oannh',
	'oe', 'oeh', 'oenn', 'oennh',
	'ui', 'uih', 'uinn', 'uinnh',
	'iau', 'iauh', 'iaunn', 'iaunnh',
	'oai', 'oaih', 'oainn', 'oainnh',
	'm', 'mh', 'ng', 'ngh',
	'ioo', 'iooh',
	'iou', 'iouh',
	} | 臺灣閩南語羅馬字拼音韻母表
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
		self.分析聲韻調(音標.replace('hN', 'Nh').replace('ou', 'oo')
			.replace('ooN', 'onn').replace('oonn', 'onn'))
		if self.聲 == 'm' or self.聲 == 'n' or self.聲 == 'ng':
			if self.韻 == 'o':
				self.音標 = None

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
		elif self.韻[:2] == 'ou':
			韻母 = 'oo' + self.韻[2:]
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
