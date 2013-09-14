import unicodedata

class 文章初胚工具:
	音標工具 = None
	def __init__(self, 音標工具):
		self.音標工具 = 音標工具

	# 輕聲連字符會擲掉，但是會留一个連字符做斷詞
	def 建立物件語句前處理減號(self, 語句):
		if 語句.startswith('--'):
			if self.後壁有音標無(語句[2:]):
				語句 = '0' + 語句[2:]
			elif(2 < len(語句) and unicodedata.category(語句[2]) == 'Lo'):
				語句 = 語句[2:]
		位置 = 0
		while 位置 < len(語句) - 1:
			if 語句[位置] == '-' and 語句[位置 + 1] == '-':
				print('原本', 語句)
				if self.頭前有音標無(語句[位置 + 2:]):
					語句 = 語句[:位置] + '-0' + 語句[位置 + 2:]
				elif self.後壁有音標無(語句[:位置]) and (
					位置 + 2 < len(語句) and unicodedata.category(語句[位置 + 2]) == 'Lo'):
					語句 = 語句[:位置] + '-' + 語句[位置 + 2:]
				elif (位置 - 1 >= 0 and unicodedata.category(語句[位置 - 1]) == 'Lo') and (
					位置 + 2 < len(語句) and unicodedata.category(語句[位置 + 2]) == 'Lo'):
					語句 = 語句[:位置] + '-' + 語句[位置 + 2:]
				else:
					語句 = 語句[:位置] + ' - - ' + 語句[位置 + 2:]
					位置 += 4
				print('後來', 語句)
			elif 語句[位置] == '-':
				頭節 = self.後壁有音標無(語句[:位置])
				後節 = self.頭前有音標無(語句[位置 + 1:])
				if (頭節 and 後節) or (頭節 and 位置 + 1 < len(語句) and unicodedata.category(語句[位置 + 1]) == 'Lo'
					) or (後節 and 位置 - 1 >= 0 and unicodedata.category(語句[位置 - 1]) == 'Lo'):
					pass
				else:
					語句 = 語句[:位置] + ' - ' + 語句[位置 + 1:]
					位置 += 2
			位置 += 1
		return self.除掉重覆的空白(語句)

	def 頭前有音標無(self, 語句):
		for 長度 in range(1, min(len(語句), self.音標工具.音標上長長度) + 1):
			if self.音標工具(語句[:長度]).音標 != None:
				return True
		return False
	
	def 後壁有音標無(self, 語句):
		for 長度 in range(1, min(len(語句), self.音標工具.音標上長長度) + 1):
			if self.音標工具(語句[-長度:]).音標 != None:
				return True
		return False

	def 除掉重覆的空白(self, 語句):
		新語句 = []
		for 字 in 語句:
			if len(新語句) == 0 or 新語句[-1] != ' ' or 字 != ' ':
				新語句.append(字)
		return ''.join(新語句)

	def 解析語句(self, 語句):
		合法字元的暫時所在 = self.標點符號
		self.標點符號 = None
		解析結果 = self.解析語句佮顯示毋著字元(語句)[0]
		self.標點符號 = 合法字元的暫時所在
		return 解析結果

	def 解析語句佮顯示毋著字元(self, 語句, 音標袂使黏做伙 = False):
		解析結果 = ''
		處理位置 = 0
		語句長度 = len(語句)
		無問題諾 = True
# 		print(語句長度)
		while 處理位置 < 語句長度:
			for 音標長度 in range(16, 0, -1):
				音標 = self.音標工具(語句[處理位置:處理位置 + 音標長度])
				if 音標.音標 != None:
					臺灣閩南語羅馬字拼音 = 音標.轉換到臺灣閩南語羅馬字拼音()
					if 臺灣閩南語羅馬字拼音 == None:
						print(音標.音標 + '轉臺灣閩南語羅馬字拼音有問題！！')
						print(音標.聲韻對照表[音標.聲韻])
						無問題諾 = False
					else:
						解析結果 += 臺灣閩南語羅馬字拼音
					處理位置 += 音標長度

					if 音標袂使黏做伙 and 處理位置 < 語句長度:
						if self.標點符號 == None or 語句[處理位置] in self.標點符號:
							解析結果 += 語句[處理位置]
							處理位置 += 1
						elif 處理位置 + 1 < 語句長度 and 語句[處理位置:處理位置 + 1] in self.標點符號:
							解析結果 += 語句[處理位置:處理位置 + 1]
							處理位置 += 2
						elif 處理位置 + 2 < 語句長度 and 語句[處理位置:處理位置 + 2] in self.標點符號:
							解析結果 += 語句[處理位置:處理位置 + 2]
							處理位置 += 3
						else:
# 							print("錯誤=" + 語句[處理位置] + " 佇「" + 語句 + '」的' + str(處理位置))
							無問題諾 = False
							解析結果 += 語句[處理位置]
							處理位置 += 1

					break
			else:
				if self.標點符號 == None or 語句[處理位置] in self.標點符號:
					解析結果 += 語句[處理位置]
					處理位置 += 1
				elif 處理位置 + 1 < 語句長度 and 語句[處理位置:處理位置 + 1] in self.標點符號:
					解析結果 += 語句[處理位置:處理位置 + 1]
					處理位置 += 2
				elif 處理位置 + 2 < 語句長度 and 語句[處理位置:處理位置 + 2] in self.標點符號:
					解析結果 += 語句[處理位置:處理位置 + 2]
					處理位置 += 3
				else:
# 					print("錯誤=" + 語句[處理位置] + " 佇「" + 語句 + '」的' + str(處理位置))
					無問題諾 = False
					解析結果 += 語句[處理位置]
					處理位置 += 1
		return (解析結果, 無問題諾)

# if __name__ == '__main__':
# 	解析器 = 文章音標解析器(臺灣閩南語羅馬字拼音)
# 	解析器.標點符號 = {' ', '-'}
# 	print(解析器.解析語句('tshiǔnn	tshiūnn'))
# 	print(解析器.解析語句('tsua̋n-ne tsua̋n'))
# 	print(解析器.解析語句('--tsi̍t-kuá --tsit-kuá'))
# 	print(解析器.解析語句('--tsi̍t-kuá -@-tsit-kuá'))
# 	print(臺灣閩南語羅馬字拼音('nau2').音標)
# 	解析器 = 文章音標解析器(通用拼音音標)
# 	print(解析器.解析語句('hue2_zit6_e5_sit7_le4'))
# 	print(解析器.解析語句('17,"一下子","一時仔","zit6-si5-a4","cit8-si5-a2"'))
# 	print(解析器.解析語句('"一丁不識","[(it7)-(ding1)-(but7)-(sik7)]","文"'))
# 	print(解析器.解析語句('m33gorh66 ho23 sua12 a44 liam53 mua45mua44 e52 ve45cia11 ziah77 giann53 vor53 qo23hun12zing11 , 	'))
# 	print(解析器.解析語句('qin21 a24 dor43 i45ging12 ga23 tau55 cun22 cut76ki34 cia12 tang12a41qua22 gong44 '))
# 	print(解析器.解析語句('mui45  ging12ge34  zit68ging12cu33'))
# 	print(解析器.解析語句('nau2'))
# 	解析器 = 文章音標解析器(何澤政教會羅馬字音標)
# 	解析器.標點符號={'「',' ','-'}
# 	print(解析器.解析語句佮顯示毋著字元('Pang-liau5 hi5-kang2 「 Toa7-tiau5-hang7 」 siang7-khoah nng7-kong-chhioh'))
# 	print(解析器.解析語句佮顯示毋著字元('chu2-chhionn3'))
