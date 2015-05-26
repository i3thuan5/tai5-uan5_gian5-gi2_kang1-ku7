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
import re
import sys
import time


from 臺灣言語工具.斷詞.中研院.用戶端連線 import 用戶端連線

class 斷詞用戶端(用戶端連線):
	分詞性 = re.compile('(.*)\((.*)\)')
	def __init__(self, 主機='140.109.19.104', 連接埠=1501, 編碼='UTF-8',
			帳號='ihcaoe', 密碼='aip1614'):
		self.編碼 = 編碼
		self.主機 = 主機
		self.連接埠 = 連接埠
		self.帳號 = 帳號
		self.密碼 = 密碼
	def 語句斷詞後結構化(self, 語句):
		逐逝 = self.語句斷詞做語句(語句)
		結果 = [[]]
		for 一逝 in 逐逝:
			逝結果 = []
			for 詞 in 一逝.strip().split('　'):
				if 詞 == '':
					continue
				# 1989 年 5 月 19, 32 歲 ê 詹益樺為 tio̍h 「台灣獨立」 , tī 台北總督府頭前自焚 .
				# ['\u30001989(DET)\u3000年5(N)\u3000月(N)\u300019,\u300032(DET)\u3000歲(M)\u3000ê(FW)\u3000詹益樺(N)\u3000為(P)\u3000tio(FW)\u3000̍(FW)\u3000h(FW)\u3000「(PARENTHESISCATEGORY)\u3000台灣(N)\u3000獨立(Vi)\u3000」(PARENTHESISCATEGORY)\u3000,(COMMACATEGORY)', '\u3000t(FW)\u3000ī(FW)\u3000台北(N)\u3000總督府(N)\u3000頭(N)\u3000前(N)\u3000自焚(Vi)\u3000.(PERIODCATEGORY)']
				try:
					字, 性 = self.分詞性.split(詞)[1:3]
				except:
					字, 性 = 詞, None
				逝結果.append((字, 性))
			if 逝結果 == []:
				結果.append([])
			else:
				結果[-1].append(逝結果)
		return 結果
	def 語句斷詞做語句(self, 語句, 等待=3, 一定愛成功=False):
		while True:
			try:
				逐逝 = self.連線(語句, 等待, self.編碼, self.主機, self.連接埠, self.帳號, self.密碼)
			except Exception as 問題:
				if 一定愛成功:
					print('連線失敗，小等閣試……。原因：{0}'.format(問題),
						file=sys.stderr)
					time.sleep(10)
				else:
					raise
			else:
				break
		return 逐逝
