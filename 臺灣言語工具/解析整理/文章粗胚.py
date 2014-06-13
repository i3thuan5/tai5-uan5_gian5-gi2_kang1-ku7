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
import unicodedata
from 臺灣言語工具.基本元素.公用變數 import 標點符號
from 臺灣言語工具.基本元素.公用變數 import 分字符號
from 臺灣言語工具.基本元素.公用變數 import 分詞符號
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.基本元素.公用變數 import 組字式符號
from 臺灣言語工具.基本元素.公用變數 import 統一碼漢字佮組字式類
from 臺灣言語工具.基本元素.公用變數 import 統一碼羅馬字類
from 臺灣言語工具.基本元素.公用變數 import 統一碼數字類
from 臺灣言語工具.基本元素.公用變數 import 聲調符號

class 文章粗胚:
	分字符號代表字 = '{0}{1}{0}'.format(分詞符號, 分字符號)
	兩分字符號代表字 = '{0}{1}{0}{1}{0}'.format(分詞符號, 分字符號)
	雙分字符號 = 分字符號 * 2
	三分字符號 = 分字符號 * 3
	_一般 = '_一般'
	_組字 = '_組字'

	def 建立物件語句前減號變標點符號(self, 語句):
		return 語句.replace(分字符號, self.分字符號代表字)

	# 輕聲連字符會擲掉，但是會留一个連字符做斷詞
	# 若減號兩邊毋是漢字、組字號，就是合法的音標，伊就當作連字符來斷詞
	def 建立物件語句前處理減號(self, 音標工具, 語句):
		if not isinstance(語句, str):
			raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
		if 語句 == 分字符號:
			return self.分字符號代表字
		if 語句.startswith(分字符號 + 分字符號):
			if self.後壁有音標無(音標工具, 語句[2:]):
				語句 = '0' + 語句[2:]
			elif(2 < len(語句) and unicodedata.category(語句[2]) in 統一碼漢字佮組字式類):
				語句 = 語句[2:]
		位置 = 0
		狀態 = self._一般
		這回一開始狀態 = 狀態
		前回一開始狀態 = 狀態
		組字式長度 = 0
		字元陣列 = []
		while 位置 < len(語句):
			前回一開始狀態 = 這回一開始狀態
			這回一開始狀態 = 狀態
# 			print(狀態)
			if 語句[位置] in 組字式符號:
				組字式長度 -= 1
				狀態 = self._組字
			else:
				組字式長度 += 1
			if 狀態 == self._一般 and 組字式長度 == 1:
				if 語句[位置:].startswith(self.三分字符號):
					字元陣列.append(分詞符號)
					while 位置 < len(語句) and 語句[位置] == 分字符號:
						字元陣列.append(分字符號)
						字元陣列.append(分詞符號)
						位置 += 1
					位置 -= 1
				elif 語句[位置:].startswith(self.雙分字符號):
					if self.頭前有音標無(音標工具, 語句[位置 + 2:]):
						if 前回一開始狀態 == self._組字 or \
								len(字元陣列) > 0 and unicodedata.category(字元陣列[-1][-1]) in 統一碼漢字佮組字式類 or\
								self.後壁有音標無(音標工具, 語句[:位置]):
							字元陣列.append('-0')
						else:
							字元陣列.append('0')
					elif (位置 + 2 < len(語句) and unicodedata.category(語句[位置 + 2]) in 統一碼漢字佮組字式類):
						if 前回一開始狀態 == self._組字 or \
								len(字元陣列) > 0 and unicodedata.category(字元陣列[-1][-1]) in 統一碼漢字佮組字式類 or\
								self.後壁有音標無(音標工具, 語句[:位置]):
							字元陣列.append(分字符號)
					else:
						字元陣列.append(self.兩分字符號代表字)
					位置 += 1
	# 				print('後來', 語句)
				elif 語句[位置] == 分字符號:
					頭節 = self.後壁有音標無(音標工具, 語句[:位置])
					後節 = self.頭前有音標無(音標工具, 語句[位置 + 1:])
					頭前漢字抑是組字式 = (位置 - 1 >= 0 and unicodedata.category(語句[位置 - 1]) in 統一碼漢字佮組字式類)
					後壁漢字抑是組字式 = (位置 + 1 < len(語句) and unicodedata.category(語句[位置 + 1]) in 統一碼漢字佮組字式類)
					頭前閣是組字式 = (前回一開始狀態 == self._組字)
# 					print(頭節 , 頭前漢字抑是組字式 , 頭前閣是組字式,後節 , 後壁漢字抑是組字式)
					if (頭節 or 頭前漢字抑是組字式 or 頭前閣是組字式) and (後節 or 後壁漢字抑是組字式):
						字元陣列.append(語句[位置])
					else:
						字元陣列.append(self.分字符號代表字)
				else:
					字元陣列.append(語句[位置])
				組字式長度 = 0
			elif 狀態 == self._組字 and 組字式長度 == 1:
				狀態 = self._一般
				組字式長度 = 0
				字元陣列.append(語句[位置])
			else:
				字元陣列.append(語句[位置])
			位置 += 1
		if 前回一開始狀態 == self._一般 and 語句.endswith(分字符號):
			字元陣列.append(分詞符號)
		return self.除掉重覆的空白(''.join(字元陣列))

	def 符號邊仔加空白(self, 語句):
		if not isinstance(語句, str):
			raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
		self.減號有照規則無(語句)
# 		for 符號 in 標點符號:
# 			if 符號 != 分字符號 and 符號 != 分詞符號:
# 				語句 = 語句.replace(符號, '{0}{1}{0}'.format(分詞符號, 符號))
		位置 = 0
		狀態 = self._一般
		組字式長度 = 0
		while 位置 < len(語句):
			if 語句[位置] in 組字式符號:
				組字式長度 -= 1
				狀態 = self._組字
			else:
				組字式長度 += 1
			if 狀態 == self._一般 and 組字式長度 == 1:
				if 語句[位置] in 聲調符號 \
					and 位置 - 1 >= 0 and unicodedata.category(語句[位置 - 1]) in 統一碼羅馬字類:
					pass
				elif 語句[位置] != 分字符號 and 語句[位置] != 分詞符號 and 語句[位置] in 標點符號:
					語句 = 語句[:位置] + '{0}{1}{0}'.format(分詞符號, 語句[位置]) + 語句[位置 + 1:]
					位置 += 2
				組字式長度 = 0
			elif 狀態 == self._組字 and 組字式長度 == 1:
				狀態 = self._一般
				組字式長度 = 0
			位置 += 1
		return self.除掉重覆的空白(語句)

	def 減號有照規則無(self, 語句):
		分字符號合法 = True
		狀態 = self._一般
		組字式長度 = 0
		for 位置 in range(len(語句)):
			if 語句[位置] in 組字式符號:
				組字式長度 -= 1
				狀態 = self._組字
			else:
				組字式長度 += 1
			if 狀態 == self._一般 and 組字式長度 == 1:
				if 語句[位置] == 分字符號:
					if 位置 + 1 < len(語句) and 語句[位置 + 1] == 分字符號:
						raise 解析錯誤('語句內底袂使有連紲兩个減號，愛用空白隔開：{0}'.format(str(語句)))
					if 分字符號合法:
						上尾會使位置 = 位置
					if 位置 == 0:
						if len(語句) > 1:
							分字符號合法 = False
					elif 位置 == len(語句) - 1:
						if len(語句) > 1:
							分字符號合法 = False
					elif 語句[位置 - 1] != 分詞符號 and 語句[位置 + 1] == 分詞符號:
						分字符號合法 = False
					elif 語句[位置 - 1] == 分詞符號 and 語句[位置 + 1] != 分詞符號:
						分字符號合法 = False
				組字式長度 = 0
			elif 狀態 == self._組字 and 組字式長度 == 1:
				狀態 = self._一般
				組字式長度 = 0
		if not 分字符號合法:
			raise 解析錯誤('語句內底減號，兩邊袂使干焦一邊是空白：位置＝{1}，語句＝{0}'.format(str(語句), 上尾會使位置))

	def 頭前有音標無(self, 音標工具, 語句):
		for 長度 in range(1, min(len(語句), 音標工具.音標上長長度) + 1):
			if 音標工具(語句[:長度]).音標 != None:
				return True
		return False

	def 後壁有音標無(self, 音標工具, 語句):
		for 長度 in range(1, min(len(語句), 音標工具.音標上長長度) + 1):
			if 音標工具(語句[-長度:]).音標 != None:
				return True
		return False

	def 除掉重覆的空白(self, 語句):
		新語句 = []
		for 字 in 語句:
			if len(新語句) == 0 or 新語句[-1] != 分詞符號 or 字 != 分詞符號:
				新語句.append(字)
		return ''.join(新語句)

	def 數字調英文中央加分字符號(self, 語句):
		新語句 = []
		舊字 = '0'
		for 字 in 語句:
			if 舊字 != '0' and \
				unicodedata.category(舊字) in 統一碼數字類 and \
				unicodedata.category(字) in 統一碼羅馬字類:
				新語句.append(分字符號)
			新語句.append(字)
			舊字 = 字
		return self.除掉重覆的空白(''.join(新語句))
