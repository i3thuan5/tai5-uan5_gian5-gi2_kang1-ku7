# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國103年 意傳文化科技
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

臺灣客家話拼音對照音值聲母表 = {
	'b':'p', 'p':'pʰ', 'bb':'b', 'm':'m', 'f':'f', 'v':'v',
	'd':'t', 't':'tʰ', 'l':'l', 'n':'n', 'r':'j',
	'z':'ts', 'c':'tsʰ', 's':'s',
	'j':'tɕ', 'q':'tɕʰ', 'x':'ɕ',
	'zh':'tʃ', 'ch':'tʃʰ', 'sh':'ʃ', 'rh':'ʒ',
	'g':'k', 'k':'kʰ', 'ng':'ŋ',
	'h':'h', '':'ʔ',
}

臺灣客家話拼音對照音值韻母表 = {
	'ii':'ï', 'i':'i', 'e':'e', 'a':'a', 'o':'o', 'u':'u',
	'ie':'ie', 'eu':'eu', 'ieu':'ieu', 'ia':'ia', 'ua':'ua', 'ai':'ai',
	'iai':'iai', 'uai':'uai', 'au':'au', 'iau':'iau', 'io':'io', 'oi':'oi',
	'ioi':'ioi', 'iu':'iu', 'ui':'ui', 'iui':'iui',
	'ue':'ue',
	'iim':'ïm', 'im':'im', 'em':'em', 'iem':'iem', 'am':'am', 'iam':'iam',
	'iin':'ïn', 'in':'in', 'en':'en', 'ien':'ien', 'uen':'uen', 'an':'an',
	'ian':'ian', 'uan':'uan', 'on':'on', 'ion':'ion', 'un':'un', 'iun':'iun',
	'ang':'aŋ', 'iang':'iaŋ', 'uang':'uaŋ',
	'ong':'oŋ', 'iong':'ioŋ', 'ung':'uŋ', 'iung':'iuŋ',
	'iib':'ïp', 'ib':'ip', 'eb':'ep', 'ieb':'iep', 'ab':'ap', 'iab':'iap',
	'iid':'ït', 'id':'it', 'ed':'et', 'ied':'iet', 'ued':'uet',
	'ad':'at', 'iad':'iat', 'uad':'uat', 'od':'ot', 'iod':'iot', 'ud':'ut', 'iud':'iut',
	'ag':'ak', 'iag':'iak', 'uag':'uak', 'og':'ok', 'iog':'iok', 'ug':'uk', 'iug':'iuk',
	'er':'ə',
	'm':'m̩', 'n':'n̩', 'ng':'ŋ̩',
	'oo':'ɔ',
	'ee':'ɛ', 'eeb':'ɛp', 'eed':'ɛt', 'eem':'ɛm', 'een':'ɛn', 'eeu':'ɛu',
	'ainn':'aⁿiⁿ', 'ann':'aⁿ', 'iann':'iⁿaⁿ', 'inn':'iⁿ', 'onn':'oⁿ', 'uainn':'uⁿaⁿiⁿ',
	}

class 臺灣客家話拼音轉音值模組():
	聲母表 = 臺灣客家話拼音對照音值聲母表
	韻母表 = 臺灣客家話拼音對照音值韻母表
	聲 = None
	韻 = None
	調 = None
	def 轉(self, 聲, 韻, 調):
		if 聲 == None or 韻 == None or 調 == None:
			return
		音值聲 = self.聲母表[聲]
		音值韻 = self.韻母表[韻]
		if 音值聲 == 'ŋ' and 音值韻.startswith('i'):
			音值聲 = 'ȵ'
		音值調 = 調
		return (音值聲, 音值韻, 音值調)
