# -*- coding: utf-8 -*-
import kenlm
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.基本元素.公用變數 import 分詞符號
from 臺灣言語工具.語言模型.語言模型 import 語言模型

class KenLM語言模型(語言模型):
	_譀鏡 = 物件譀鏡()
	def __init__(self, 語言模型檔案):
		self._語言模型 = kenlm.LanguageModel(語言模型檔案)
	def 上濟詞數(self):
		return self._語言模型.order
	def 評詞陣列分(self, 詞陣列, 開始的所在=0):
		字串 = []
		for 詞物件 in 詞陣列: 
			字串.append(self._譀鏡.看分詞(詞物件))
		for 所在, 結果 in enumerate(
				self._語言模型.full_scores(分詞符號.join(字串), bos=False, eos=False)):
			if 所在 >= 開始的所在:
				分數 = 結果[0]
# 				長度 = 結果[1] #這个機率連詞長度
				try:
					分數 += 詞陣列[所在].屬性['機率']
				except:
					pass
				yield 分數
