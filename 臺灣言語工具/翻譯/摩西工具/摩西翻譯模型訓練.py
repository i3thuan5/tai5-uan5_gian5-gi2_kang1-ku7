# -*- coding: utf-8 -*-
from 臺灣言語工具.系統整合.腳本程式 import 腳本程式
import os
import shutil


from 臺灣言語工具.翻譯.摩西工具.無編碼器 import 無編碼器
from 臺灣言語工具.表單.KenLM語言模型訓練 import KenLM語言模型訓練

class 摩西翻譯模型訓練(腳本程式):
	def 訓練(self, 來源語言平行語料, 目標語言平行語料, 目標語言語料,
			暫存資料夾,
			連紲詞長度=3,
			編碼器=無編碼器(),
			SRILM執行檔路徑='',
			GIZA執行檔路徑='',  # 愛有 mkcls, GIZA++/mgiza, & snt2cooc.out/snt2cooc
			MOSES腳本路徑=''):
		_斯里語句連詞訓練 = KenLM語言模型訓練()
		os.makedirs(暫存資料夾, exist_ok=True)
		語言模型檔 = _斯里語句連詞訓練.訓練(目標語言語料, 暫存資料夾, 連紲詞長度, 編碼器, SRILM執行檔路徑)
		
		平行檔名 = os.path.join(暫存資料夾, '翻')
		來源平行檔名 = os.path.join(暫存資料夾, '翻.源')
		self._檔案合做一个(來源平行檔名, 來源語言平行語料, 編碼器)
		目標平行檔名 = os.path.join(暫存資料夾, '翻.目')
		self._檔案合做一个(目標平行檔名, 目標語言平行語料, 編碼器)
		
		翻譯模型資料夾 = os.path.join(暫存資料夾, '翻譯模型資料夾')
		if os.path.exists(翻譯模型資料夾):
			shutil.rmtree(翻譯模型資料夾)
		翻譯模型指令版 = \
			'SCRIPTS_ROOTDIR={1} {1}/training/train-model.perl -root-dir {2} -corpus {3} -f {4} -e {5} -alignment grow-diag-final-and -reordering msd-bidirectional-fe -lm 0:{7}:{6} --mgiza -external-bin-dir={0}'
		翻譯模型指令 = 翻譯模型指令版.format(
			self._執行檔路徑加尾(GIZA執行檔路徑),
			self._執行檔路徑加尾(MOSES腳本路徑),
			翻譯模型資料夾,
			平行檔名,
			'源',
			'目',
			語言模型檔,
			連紲詞長度,
			)
		self._走指令(翻譯模型指令)
