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
from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
import re
import time
import sys

class 官方斷詞剖析工具:
	檢查結果 = re.compile('<result>(.*)</result>')
	分句 = re.compile('<sentence>(.*?)</sentence>')
	分詞性 = re.compile('(.*)\((.*)\)')
	回傳狀況 = re.compile('<processstatus code="\d">(.*?)</processstatus>')
	def 斷詞(self, 語句, 編碼='UTF-8', 等待=1, 一定愛成功=False,
			主機='140.109.19.104', 連接埠=1501, 帳號='ihcaoe', 密碼='aip1614'):
		while True:
			try:
				逐逝 = self.連線(語句, 編碼, 等待, 主機, 連接埠, 帳號, 密碼)
			except Exception as 問題:
				if 一定愛成功:
					print('連線失敗，小等閣試……。原因：{0}'.format(問題),
						file=sys.stderr)
					time.sleep(10)
				else:
					raise
			else:
				break
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

	def 剖析(self, 語句, 編碼='Big5', 等待=3, 一定愛成功=False,
			主機='140.109.19.112', 連接埠=8000, 帳號='ihcaoe', 密碼='aip1614'):
		# 官方功能無記錄原本換逝資訊，所以愛一逐一擺
		結果 = []
		for 一逝 in 語句.split('\n'):
			愛剖逝 = 一逝.strip()
			if 愛剖逝 == '':
				continue
			while True:
				try:
					剖的結果 = self.連線(愛剖逝, 編碼, 等待, 主機, 連接埠, 帳號, 密碼)
					結果.append(剖的結果)
				except Exception as 問題:
					if 一定愛成功:
						print('連線失敗，小等閣試……。原因：{0}'.format(問題),
							file=sys.stderr)
						time.sleep(10)
					else:
						raise
				else:
					break
		return 結果

	def 連線(self, 語句, 編碼, 等待, 主機, 連接埠, 帳號, 密碼):
		連線 = socket(
			AF_INET, SOCK_STREAM)
		連線.settimeout(等待)
		try:
			連線.connect((主機, 連接埠))
		except:
			raise RuntimeError("連線逾時")
		資料 = self.傳去格式.format(編碼, 帳號, 密碼, 語句).encode(編碼)
# 		print('送出', 資料)
		已經送出去 = 0
		while 已經送出去 < len(資料):
			這擺送出去 = 連線.send(資料[已經送出去:])
			if 這擺送出去 == 0:
				raise RuntimeError("連線出問題")
			已經送出去 += 這擺送出去
		全部收著資料 = b''
		走 = True
		while 走:
			這擺收著資料 = 連線.recv(1024)
			if 這擺收著資料 == b'':
				raise RuntimeError("連線出問題")
			全部收著資料 = 全部收著資料 + 這擺收著資料
			if b'</wordsegmentation>' in 全部收著資料:
				走 = False
		連線.close()
		全部收著字串 = 全部收著資料.decode(編碼)
# 		print('收著', 全部收著字串)
		收著結果 = self.檢查結果.search(全部收著字串)
		if 收著結果 != None:
			逐逝 = self.分句.split(收著結果.group(1))[1::2]
			return 逐逝
		狀況 = self.回傳狀況.split(全部收著字串)
		if 狀況 != None:
# 			<processstatus code="1">Service internal error</processstatus>
# 			<processstatus code="2">XML format error</processstatus>
# 			<processstatus code="3">Authentication failed</processstatus>
			raise RuntimeError(狀況[1])
		raise RuntimeError('回傳的資料有問題！！')
	傳去格式 = '''
<?xml version="1.0" ?>
<wordsegmentation version="0.1" charsetcode='{}' >
<option showcategory="1" />
<authentication username="{}" password="{}" />
<text>{}</text>
</wordsegmentation>
'''
