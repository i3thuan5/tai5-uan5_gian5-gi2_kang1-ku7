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
from 臺灣言語工具.語音辨識.腳本程式 import 腳本程式
import gzip
import os
from 臺灣言語工具.翻譯.摩西工具.無編碼器 import 無編碼器
import shutil

class 摩西翻譯模型訓練(腳本程式):
	def 訓練(self, 來源語言平行語料, 目標語言平行語料, 目標語言語料,
			暫存資料夾,
			連紲詞長度=3,
			編碼器=無編碼器(),
			SRILM執行檔路徑='',
			GIZA執行檔路徑='',  # 愛有 mkcls, GIZA++/mgiza, & snt2cooc.out/snt2cooc
			MOSES腳本路徑=''):
		os.makedirs(暫存資料夾, exist_ok=True)
		目標語言檔名 = os.path.join(暫存資料夾, '語言模型.txt')
		self._檔案合做一个(目標語言檔名, 目標語言語料, 編碼器)
		語言模型檔 = os.path.join(暫存資料夾, '語言模型.lm')
		語言模型指令版 = \
			'{0}ngram-count -order {1} -interpolate -wbdiscount -unk -text {2} -lm {3}'
		語言模型指令 = 語言模型指令版.format(
			self.執行檔路徑加尾(SRILM執行檔路徑),
			連紲詞長度,
			目標語言檔名,
			語言模型檔
			)
		self.走指令(語言模型指令)
		
		平行檔名 = os.path.join(暫存資料夾, '翻')
		來源平行檔名 = os.path.join(暫存資料夾, '翻.源')
		self._檔案合做一个(來源平行檔名, 來源語言平行語料, 編碼器)
		目標平行檔名 = os.path.join(暫存資料夾, '翻.目')
		self._檔案合做一个(目標平行檔名, 目標語言平行語料, 編碼器)
		
		翻譯模型資料夾 = os.path.join(暫存資料夾, '翻譯模型資料夾')
		shutil.rmtree(翻譯模型資料夾)
		翻譯模型指令版 = \
			'SCRIPTS_ROOTDIR={1} {1}/training/train-model.perl -root-dir {2} -corpus {3} -f {4} -e {5} -alignment grow-diag-final-and -reordering msd-bidirectional-fe -lm 0:{7}:{6} -external-bin-dir={0}'
		翻譯模型指令 = 翻譯模型指令版.format(
			self.執行檔路徑加尾(GIZA執行檔路徑),
			self.執行檔路徑加尾(MOSES腳本路徑),
			翻譯模型資料夾,
			平行檔名,
			'源',
			'目',
			語言模型檔,
			連紲詞長度,
			)
		self.走指令(翻譯模型指令)
	def _檔案合做一个(self, 平行檔名, 語言平行語料, 編碼器):
		with open(平行檔名, 'w') as 寫檔:
			for 語言檔案 in 語言平行語料:
				if 語言檔案.endswith('.gz'):
					開檔 = gzip.open
				else:
					開檔 = open
				with 開檔(語言檔案, mode='rt') as 檔案:
					for 一逝 in 檔案.readlines():
						print(編碼器.編碼(一逝.strip()), file=寫檔)
