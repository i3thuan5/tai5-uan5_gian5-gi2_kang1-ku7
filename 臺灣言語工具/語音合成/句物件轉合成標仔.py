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
from 臺灣言語工具.語音合成.臺羅變調暫時處理 import 臺羅變調暫時處理
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔
from 臺灣言語工具.基本元素.公用變數 import 標點符號
"""
變調
處理無音的字物件
轉聲韻
算佇詞句中的所在
產生標仔
"""
# 前音-此音+後音/調：調類/詞：第幾字!上尾第幾字@攏總字/句：第幾字^上尾第幾字_攏總字/驗:md5
class 句物件轉合成標仔:
	恬音 = 'sil'
	短恬 = 'sp'
	免知 = 'x'
	恬標仔 = None
	音標格式 = '{0}-{1}+{2}/調:{3}<{4}>{5}/詞:{6}!{7}@{8}/句:{9}^{10}_{11}'
	音值格式 = '{0}'
	_篩仔 = 字物件篩仔()
	_網仔 = 詞物件網仔()
	變調處理 = 臺羅變調暫時處理()
	def __init__(self):
		self.恬標仔 = self.產生合成標仔(self.免知, self.恬音, self.免知,
			self.免知, self.免知, self.免知,
			self.免知, self.免知, self.免知,
			self.免知, self.免知, self.免知,
			)
	def 句物件轉標仔(self, 句物件):
		for 集物件 in 句物件.內底集:
			新組陣列 = []
			for 詞物件 in 集物件.內底組[0].內底詞:
				if len(詞物件.內底字) > 1 or\
						詞物件.內底字[0].型 not in 標點符號:
					新組陣列.append(詞物件)
			集物件.內底組[0].內底詞 = 新組陣列
		詞陣列 = self._網仔.網出詞物件(句物件)
		攏總詞數量 = len(詞陣列)
		if 攏總詞數量 == 0:
			return ([self.恬標仔], [self.恬音])
		句中第幾詞 = 0
		全部詞資料 = []
		全部字資料 = []
		全部聲韻資料 = []
		for 詞物件 in 詞陣列:
			字陣列 = self._篩仔.篩出字物件(詞物件)
			攏總字數量 = len(字陣列)
			詞中第幾字 = 0
			for 字物件 in 字陣列:
				try:
					聲, 韻, 調 = 字物件.音
					全部聲韻資料.append((聲, len(全部字資料)))
					全部聲韻資料.append((韻, len(全部字資料)))
				except:
					調 = self.免知
					全部聲韻資料.append((self.恬音, len(全部字資料)))
				全部字資料.append((調, 詞中第幾字, 攏總字數量, len(全部詞資料)))
				詞中第幾字 += 1
			全部詞資料.append((句中第幾詞, 攏總詞數量))
			句中第幾詞 += 1
		合成標仔 = [self.恬標仔]
		for 聲韻資料所在 in range(len(全部聲韻資料)):
			這馬聲韻, 這馬字所在 = 全部聲韻資料[聲韻資料所在]
			if 這馬聲韻 == self.恬標仔:
				合成標仔.append(self.恬標仔)
				continue
			if 聲韻資料所在 - 1 >= 0:
				頭前聲韻 = 全部聲韻資料[聲韻資料所在 - 1][0]
			else:
				頭前聲韻 = self.恬音
			if 聲韻資料所在 + 1 < len(全部聲韻資料):
				後壁聲韻 = 全部聲韻資料[聲韻資料所在 + 1][0]
			else:
				後壁聲韻 = self.恬音

			這馬字調, 詞中第幾字, 攏總字數量, 這馬詞所在 = \
				全部字資料[這馬字所在]
			if 這馬字所在 - 1 >= 0:
				頭前字調 = 全部字資料[這馬字所在 - 1][0]
			else:
				頭前字調 = self.免知
			if 這馬字所在 + 1 < len(全部字資料):
				後壁字調 = 全部字資料[這馬字所在 + 1][0]
			else:
				後壁字調 = self.免知
			句中第幾詞, 攏總詞數量 = 全部詞資料[這馬詞所在]

			聲韻標仔 = self.產生一般標仔(
				頭前聲韻, 這馬聲韻, 後壁聲韻,
				頭前字調, 這馬字調, 後壁字調,
				詞中第幾字, 攏總字數量,
				句中第幾詞, 攏總詞數量)
			合成標仔.append(聲韻標仔)
		合成標仔.append(self.恬標仔)
		return 合成標仔
	def 產生合成標仔(self, 前音, 此音, 後音, 前字調, 此字調, 後字調,
			詞中第幾字, 詞中上尾幾字, 詞攏總字數,
			句中第幾詞, 句中上尾幾詞, 句攏總詞數):
		原本音標 = self.音標格式.format(
			前音, 此音, 後音, 前字調, 此字調, 後字調,
			詞中第幾字, 詞中上尾幾字, 詞攏總字數,
			句中第幾詞, 句中上尾幾詞, 句攏總詞數)
		return 原本音標
	def 產生一般標仔(self, 前音, 此音, 後音, 前字調, 此字調, 後字調,
			詞中第幾字, 詞攏總字數, 句中第幾詞, 句攏總詞數):
		return self.產生合成標仔(
			前音, 此音, 後音, 前字調, 此字調, 後字調,
			詞中第幾字, 詞攏總字數 - 詞中第幾字, 詞攏總字數,
			句中第幾詞, 句攏總詞數 - 句中第幾詞, 句攏總詞數)
	def 提出標仔主要音值(self, 完整標仔):
		'''予HTK切音，而且HTS粗胚用的'''
		音值標仔 = []
		for 標仔 in 完整標仔:
			音值標仔.append(self.產生主要音值標仔(標仔))
		return 音值標仔
	def 產生主要音值標仔(self, 完整標仔):
		音 = 完整標仔.split('+', 1)[0].split('-', 1)[-1]
		return 音
