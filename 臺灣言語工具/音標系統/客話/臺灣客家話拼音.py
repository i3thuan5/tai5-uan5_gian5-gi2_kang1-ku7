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
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音轉音值模組 import 臺灣客家話拼音轉音值模組
臺灣客家話拼音聲母對照表 = {
		'b', 'p', 'm', 'f', 'v', 'd', 't', 'n', 'l', 'g',
		'k', 'ng', 'h', 'j', 'q', 'x', 'z', 'c', 's',
		'zh', 'ch', 'sh', 'rh', '', 'bb', 'r'
		 # 'ngi','zi', 'ci', 'si',
}
臺灣客家話拼音韻母對照表 = {
		'ii', 'i', 'e', 'a', 'o', 'u', 'ie', 'eu', 'ieu', 'ia',
		'ua', 'ai', 'iai', 'uai', 'au', 'iau', 'io', 'oi', 'ioi', 'iu',
		'ui', 'iui', 'ue', 'iim', 'im', 'em', 'iem', 'am', 'iam',
		'iin', 'in', 'en', 'ien', 'uen', 'an', 'ian', 'uan', 'on', 'ion',
		'un', 'iun', 'ang', 'iang', 'uang', 'ong', 'iong', 'ung',
		'iung', 'iib', 'ib', 'eb', 'ieb', 'ab', 'iab', 'iid', 'id',
		'ed', 'ied', 'ued', 'ad', 'iad', 'uad', 'od', 'iod', 'ud', 'iud',
		'ag', 'iag', 'uag', 'og', 'iog', 'ug', 'iug', 'er',
		'm', 'n', 'ng',
		'oo', 'ee', 'eeb', 'eed', 'eem', 'een', 'eeu',
		'ainn', 'ann', 'iann', 'inn', 'onn', 'uainn',
		}
臺灣客家話拼音調類對照表 = {
		'', 'ˊ', 'ˋ', 'ˇ', '+', '^'
}

#########################################
#  2013/11/1
#  意傳的客家話辨識用拼音
#########################################
class 臺灣客家話拼音:
	#-------成員函式--------#
	def __init__(self, 音標):
		# self.腔
		self.音標 = None
		音標 = 音標.lower()
		if 音標[-1:] in self.調類對照表:
			for 所在 in range(len(音標) - 1):
				if 音標[:所在] in self.聲母對照表 and 音標[所在:-1] in self.韻母對照表:
					self.聲 = 音標[:所在]
					self.韻 = 音標[所在:-1]
					self.調 = 音標[-1:]
					# 檢查入聲字的調是否正確（只允許1和4聲）
					if (self.韻.endswith('g')  and not self.韻.endswith('ng')) or\
						self.韻.endswith('d') or\
						self.韻.endswith('k') :
						# if(wrong)continue;
						if(self.調 == '^' or self.調 == '+'):
							continue

					self.聲韻 = 音標[:-1]
					self.音標 = 音標
					# special case
		else:  # :調是1聲
			for 所在 in range(len(音標)):
				if 音標[:所在] in self.聲母對照表 and 音標[所在:] in self.韻母對照表:
					self.聲 = 音標[:所在]
					self.韻 = 音標[所在:]
					self.調 = ''
					self.聲韻 = 音標
					self.音標 = 音標
					# special case
	def 標準音標(self):
		return self.音標
	def 音值(self):
		return self.轉音值模組.轉(self.聲, self.韻, self.調)
	def 通用音值(self):
		return (self.聲, self.韻, self.調)
	#-------成員變數--------#
	# ng uainn ˊ
	音標上長長度 = 8
	聲 = None
	韻 = None
	聲韻 = None
	調 = None
	音標 = None
	聲母對照表 = 臺灣客家話拼音聲母對照表
	韻母對照表 = 臺灣客家話拼音韻母對照表
	調類對照表 = 臺灣客家話拼音調類對照表
	轉音值模組 = 臺灣客家話拼音轉音值模組()
