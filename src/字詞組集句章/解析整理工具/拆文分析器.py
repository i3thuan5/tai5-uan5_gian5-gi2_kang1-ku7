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
from 字詞組集句章.基本元素.公用變數 import 無音
from 字詞組集句章.基本元素.公用變數 import 組字式符號
from 字詞組集句章.基本元素.公用變數 import 斷句標點符號
from 字詞組集句章.基本元素.公用變數 import 標點符號
import unicodedata

class 拆文分析器:
	def 產生對齊字(self, 型, 音):
		if not isinstance(型, str):
			raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if not isinstance(音, str):
			raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if 型 == '':
			raise 型態錯誤('傳入來的型是空的！')
		return 字(型, 音)

	def 產生對齊詞(self, 型, 音):
		if not isinstance(型, str):
			raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if not isinstance(音, str):
			raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if 型 == '' and 音 == 無音:
			return 詞()
		型陣列 = self.拆句做字(型)
		音陣列 = 音.split(分字符號)
		if len(型陣列) > len(音陣列):
			raise 解析錯誤('詞內底的型「{0}」比音「{1}」少！'.format(
				str(型), str(音)))
		if len(型陣列) < len(音陣列):
			raise 解析錯誤('詞內底的型「{0}」比音「{1}」濟！'.format(
				str(型), str(音)))
		return self.拆好陣列產生對齊詞(型陣列, 音陣列)

	def 拆好陣列產生對齊詞(self, 型陣列, 音陣列):
		if not isinstance(型陣列, list):
			raise 型態錯誤('傳入來的型毋是陣列：型陣列＝{}'.format(str(型陣列)))
		if not isinstance(音陣列, list):
			raise 型態錯誤('傳入來的音毋是陣列：音陣列＝{}'.format(str(音陣列)))
		if len(型陣列) < len(音陣列):
			raise 解析錯誤('詞內底的型「{0}」比音「{1}」少！'.format(str(型陣列), str(音陣列)))
		if len(型陣列) > len(音陣列):
			raise 解析錯誤('詞內底的型「{0}」比音「{1}」濟！'.format(str(型陣列), str(音陣列)))
		if 型陣列 == [] and 音陣列 == []:
			return 詞()
		長度 = len(型陣列)
		字陣列 = []
		for 位置 in range(長度):
			if not isinstance(型陣列[位置], str):
				raise 型態錯誤('型陣列[{1}]毋是字串：型陣列＝{0}'.format(str(型陣列), 型陣列[位置]))
			if not isinstance(音陣列[位置], str):
				raise 型態錯誤('音陣列[{1}]毋是字串：音陣列＝{0}'.format(str(音陣列), 音陣列[位置]))
			字陣列.append(字(型陣列[位置], 音陣列[位置]))
		return 詞(字陣列)

	def 產生對齊組(self, 型, 音):
		if not isinstance(型, str):
			raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if not isinstance(音, str):
			raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if 型 == '' and 音 == 無音:
			return 組()
		型 = self.符號邊仔加空白(型)
		音 = self.符號邊仔加空白(音)
		型陣列 = self.拆句做字(型)
		詞陣列 = []
		第幾字 = 0
		for 詞音 in 音.split(分詞符號):
			字音陣列 = 詞音.split(分字符號)
			if 第幾字 + len(字音陣列) > len(型陣列):
				raise 解析錯誤('詞組內底的型「{0}」比音「{1}」少！配對結果：{2}'.format(
					str(型), str(音), str(詞陣列)))
			詞陣列.append(
				self.拆好陣列產生對齊詞(型陣列[第幾字:第幾字 + len(字音陣列)], 字音陣列))
			第幾字 += len(字音陣列)
		if 第幾字 < len(型陣列):
			raise 解析錯誤('詞組內底的型「{0}」比音「{1}」濟！配對結果：{2}'.format(
				str(型), str(音), str(詞陣列)))
		return 組(詞陣列)

	def 產生對齊集(self, 型, 音):
		if not isinstance(型, str):
			raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if not isinstance(音, str):
			raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if 型 == '' and 音 == 無音:
			return 集()
		return 集([self.產生對齊組(型, 音)])

	def 產生對齊句(self, 型, 音):
		if not isinstance(型, str):
			raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if not isinstance(音, str):
			raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if 型 == '' and 音 == 無音:
			return 句()
		return 句([self.產生對齊集(型, 音)])

	def 產生對齊章(self, 型, 音):
		if not isinstance(型, str):
			raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if not isinstance(音, str):
			raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
		if 型 == '' and 音 == 無音:
			return 章()
#  		raise 型態錯誤('QQ型＝{0}，音＝{1}'.format(str(型), str(音)))
		型陣列 = self.拆章做句(型)
		音陣列 = self.拆章做句(音)
		if len(型陣列) > len(音陣列):
			raise 解析錯誤('詞內底的型「{0}」比音「{1}」少！'.format(
				str(型), str(音)))
		if len(型陣列) < len(音陣列):
			raise 解析錯誤('詞內底的型「{0}」比音「{1}」濟！'.format(
				str(型), str(音)))
		章物件 = 章()
		for 型物件, 音物件 in zip(型陣列, 音陣列):
			章物件.內底句.append(self.產生對齊句(型物件, 音物件))
		return 章物件

	def 符號邊仔加空白(self, 語句):
		for 符號 in 標點符號:
			if 符號 != 分字符號 and 符號 != 分詞符號:
				語句 = 語句.replace(符號, ' ' + 符號 + ' ')
		語句 = 語句.strip()
		無仝 = True
		while 無仝:
			新語句 = 語句.replace('  ', ' ')
			if 新語句 == 語句:
				無仝 = False
			語句 = 新語句
		return 語句

	def 拆句做字(self, 語句):
		if not isinstance(語句, str):
			raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
		字陣列 = []
		# 一般　組字
		狀態 = '一般'
		# 下組字式抑是數羅
		一个字 = ''
		長度 = 0
		for 字 in 語句:
			字種類 = unicodedata.category(字)
			print(字, 狀態, 字陣列, 一个字)
			print(字種類)
			if 狀態 == '組字':
				一个字 += 字
				if 字 in 組字式符號:
					長度 -= 1
				else:
					長度 += 1
				if 長度 == 1:
					字陣列.append(一个字)
					狀態 = '一般'
					一个字 = ''
					長度 = 0
			elif 狀態 == '一般':
				if 長度 != 0:
					raise RuntimeError('程式發生內部錯誤，語句={0}'.format(str(語句)))
				if 字 in 分字符號 or 字 in 分詞符號:
					if 一个字 != '':
						字陣列.append(一个字)
						一个字 = ''
				elif 字 in 標點符號:
					if 一个字 != '':
						字陣列.append(一个字)
						一个字 = ''
					字陣列.append(字)
				# Ll　小寫， Lu　大寫， Md　數字，Lo　其他, So 組字式符號…
				elif 字種類 == 'Ll' or 字種類 == 'Lu' or 字種類 == 'Nd':
					print('en')
					一个字 += 字
				else:
					print('ch')
					if 一个字 != '':
						字陣列.append(一个字)
						一个字 = ''
					一个字 += 字
					if 字 in 組字式符號:
						長度 -= 1
						狀態 = '組字'
					else:
						長度 += 1
					if 長度 == 1:
						字陣列.append(一个字)
						一个字 = ''
						長度 = 0
			else:
				raise RuntimeError('程式發生內部錯誤，語句={0}'.format(str(語句)))
		if 一个字 != '':
			if 狀態 == '一般':
				字陣列.append(一个字)
			elif 狀態 == '組字':
				raise 解析錯誤('語句組字式無完整，語句={0}'.format(str(語句)))
			else:
				raise RuntimeError('程式發生內部錯誤，語句={0}'.format(str(語句)))
		return 字陣列

	def 拆章做句(self, 語句):
		# 敢有需要做
		# 枋寮漁港「大條巷」上闊兩公尺。=> 枋寮漁港  「  大條巷  」  上闊兩公尺  。
		# =>無，下佇仝詞組，予斷詞處理
		if not isinstance(語句, str):
			raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
		句陣列 = []
		頭前 = 0
		for 第幾字 in range(1, len(語句)):
			if 語句[第幾字] not in 斷句標點符號:
				if 語句[第幾字 - 1] in 斷句標點符號:
					句陣列.append(語句[頭前:第幾字])
					頭前 = 第幾字
		句陣列.append(語句[頭前:])
		return 句陣列



# 	def 計算漢字語句漢字數量(self, 語句):
# 		長度 = 0
# 		for 字 in 語句:
# 			if 字 in 組字式符號:
# 				長度 -= 1
# 			else:
# 				長度 += 1
# 		return len(語句)
#
# 	def 計算音標語句音標數量(self, 語句):
# 		return len(語句.replace('--', '-').split(self.斷字符號[0]))

分析器 = 拆文分析器()
# print(分析器.拆句做字('⿰因腹肚枵'))
# print(unicodedata.category('2'))
# print(分析器.產生對齊章('', '').內底句)
