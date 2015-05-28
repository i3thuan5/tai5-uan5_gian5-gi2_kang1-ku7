# -*- coding: utf-8 -*-
import itertools
from 臺灣言語工具.語音合成.語音標仔轉換 import 語音標仔轉換

class 生文本音值對照表:
	_轉合成標仔 = 語音標仔轉換()
	def 生音節佮聲韻對照(self, 拼音, 拼音聲母表, 拼音韻母表):
		資料 = []
		格式 = '{0}\t{1}'
		資料.append(格式.format(self._轉合成標仔.恬音,
			self._轉合成標仔.提出標仔主要音值(self._轉合成標仔.恬音)))
		資料.append(格式.format(self._轉合成標仔.短恬,
			self._轉合成標仔.提出標仔主要音值(self._轉合成標仔.短恬)))
		for 聲母 in 拼音聲母表:
			for 韻母 in 拼音韻母表:
				音 = 聲母 + 韻母
				資料.append(格式.format(音,
						' '.join(拼音(音).音值()[:-1])))
		資料.sort()
		return 資料
	def 生聲韻表(self, 對照音值聲母表, 對照音值韻母表):
		資料 = []
		格式 = '{0}\t{1}'
		for 音 in itertools.chain.from_iterable([
				[self._轉合成標仔.恬音, self._轉合成標仔.短恬],
				對照音值聲母表.values(),
				對照音值韻母表.values(),
				]):
			標仔 = self._轉合成標仔.提出標仔主要音值(音)
			資料.append(格式.format(標仔, 標仔))
		資料.sort()
		return 資料
