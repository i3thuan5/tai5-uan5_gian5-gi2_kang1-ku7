from 言語資料庫.公用資料 import 組字式符號
from 字詞組集句章.基本元素.公用變數 import 分字符號
from 字詞組集句章.基本元素.公用變數 import 分詞符號
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.基本元素.詞 import 詞
from 字詞組集句章.基本元素.組 import 組
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.基本元素.章 import 章
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤

class 拆文分析器:
	分字符號 = 分字符號
	分詞符號 = 分詞符號
	標點符號 = None

	def 產生對齊組(self, 型, 音):
		# 可能是漢羅，愛閣改
		型陣列 = self.分離漢字(型)
		詞陣列 = []
		第幾字 = 0
		for 詞音 in 音.split(self.分詞符號):
			字音陣列 = 詞音.split(self.分字符號)
			if 第幾字 + len(字音陣列) > len(型陣列):
				raise 解析錯誤('詞組內底的型「{0}」佮音「{1}」的數量無仝！配對結果：'.format(
					str(型), str(音), str(詞陣列)))
			詞陣列.append(
				self.產生對齊詞(型陣列[第幾字:第幾字 + len(字音陣列)], 字音陣列))
		return 組(詞陣列)

	def 產生對齊詞(self, 型陣列, 音陣列):
		if not isinstance(型陣列, list):
			raise 型態錯誤('傳入來的型毋是陣列：型陣列＝{}'.format(str(型陣列)))
		if not isinstance(音陣列, list):
			raise 型態錯誤('傳入來的音毋是陣列：音陣列＝{}'.format(str(音陣列)))
		if len(型陣列) != len(音陣列):
			raise 解析錯誤('詞內底的型「{0}」佮音「{1}」的數量無仝！'.format(str(型陣列), str(音陣列)))
		長度 = len(型陣列)
		字陣列 = []
		for 位置 in range(長度):
			if not isinstance(型陣列[位置], str):
				raise 型態錯誤('型陣列[{1}]毋是字串：型陣列＝{0}'.format(str(型陣列),型陣列[位置]))
			if not isinstance(音陣列[位置], str):
				raise 型態錯誤('音陣列[{1}]毋是字串：音陣列＝{0}'.format(str(音陣列),音陣列[位置]))
			字陣列.append(字(型陣列[位置], 音陣列[位置]))
		return 詞(字陣列)

	def 切開語句(self, 語句):
		切開結果 = []
		目前字串 = ''
		處理位置 = 0
		語句長度 = len(語句)
# 		print(語句)
# 		print(語句長度)
		while 處理位置 < 語句長度:
			for 音標長度 in range(3, 0, -1):
				一段 = 語句[處理位置:處理位置 + 音標長度]
				if 一段 in self.斷字符號:
					目前字串 += 語句[處理位置]
					處理位置 += 音標長度
					break
				elif 一段 in self.標點符號:
					# 字佮普通的標點符號中央愛有空白
					if len(切開結果) > 0 and 切開結果[-1] != ' ' and (目前字串 != '' or 一段 != ' '):
						切開結果.append('')
						切開結果.append(' ')
# 						print(切開結果)
					切開結果.append(目前字串)
					# 普通的標點符號頭前愛有空白
					if 目前字串 != '' and 一段 != ' ':
						切開結果.append(' ')
						切開結果.append('')
					目前字串 = ''
					切開結果.append(一段)
					處理位置 += 音標長度
					break
			else:
				目前字串 += 語句[處理位置]
				處理位置 += 1
		if 目前字串 != '':
			切開結果.append(目前字串)
		return 切開結果

	def 分離漢字(self, 語句):
		漢字陣列 = []
		一个漢字 = ''
		長度 = 0
		for 字 in 語句:
			一个漢字 += 字
			if 字 in 組字式符號:
				長度 -= 1
			else:
				長度 += 1
			if 長度 == 1:
				漢字陣列.append(一个漢字)
				一个漢字 = ''
				長度 = 0
		return 漢字陣列

	def 計算漢字語句漢字數量(self, 語句):
		長度 = 0
		for 字 in 語句:
			if 字 in 組字式符號:
				長度 -= 1
			else:
				長度 += 1
		return len(語句)

	def 計算音標語句音標數量(self, 語句):
		return len(語句.replace('--', '-').split(self.斷字符號[0]))

