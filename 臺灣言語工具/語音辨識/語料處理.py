# -*- coding: utf-8 -*-
import os
from 臺灣言語工具.語音合成.語音標仔轉換 import 語音標仔轉換

class 語料處理:
	wav副檔名 = '.wav'
	音檔副檔名 = wav副檔名
	標仔副檔名 = '.lab'
	特徵 = 'mfcc'
	特徵副檔名 = '.' + 特徵
	音檔結束符號 = '.'
	_轉合成標仔 = 語音標仔轉換()
	恬音 = _轉合成標仔.提出標仔主要音值(_轉合成標仔.恬音)
	短恬 = _轉合成標仔.提出標仔主要音值(_轉合成標仔.短恬)
	def 揣全部語料(self, 音檔目錄, 標仔目錄):
		全部語料 = []
		for 音檔檔名 in os.listdir(音檔目錄):
			if 音檔檔名.endswith(self.音檔副檔名):
				語料名 = 音檔檔名[:-len(self.音檔副檔名)]
				音檔所在 = os.path.join(音檔目錄, 音檔檔名)
				if 標仔目錄 == None:
					全部語料.append((語料名, 音檔所在))
				else:
					標仔所在 = os.path.join(標仔目錄,
						語料名 + self.標仔副檔名)
					if os.path.isfile(標仔所在):
						全部語料.append((語料名, 音檔所在, 標仔所在))
		return 全部語料
	def 揣特徵而且算(self, 執行檔路徑, 資料目錄, 全部語料, 全部特徵檔):
		算特徵參數檔 = os.path.join(資料目錄, '算特徵參數.cfg')
		self.字串寫入檔案(算特徵參數檔,
			self.特徵參數.format('WAVEFORM', 'WAV'))
		特徵目錄 = os.path.join(資料目錄, self.特徵)
		os.makedirs(特徵目錄, exist_ok=True)
		全部特徵 = []
		for 語料 in 全部語料:
			語料名, 音檔所在 = 語料[0:2]
			特徵所在 = os.path.join(特徵目錄,
				語料名 + self.特徵副檔名)
			self.算特徵(執行檔路徑, 算特徵參數檔, 音檔所在, 特徵所在)
			全部特徵.append(特徵所在)
		self.陣列寫入檔案(全部特徵檔, 全部特徵)
	def 算特徵(self, 執行檔路徑, 參數檔, 音檔所在, 特徵所在):
		執行檔路徑 = self.執行檔路徑加尾(執行檔路徑)
		特徵指令 = '{0}HCopy -A -C {1} {2} {3}'.format(
			執行檔路徑, 參數檔, 音檔所在, 特徵所在)
		self.走指令(特徵指令)
	def 標仔收集起來(self, 執行檔路徑, 全部標仔檔, 資料目錄, 原來音類檔, 原來音節檔):
		執行檔路徑 = self.執行檔路徑加尾(執行檔路徑)
		莫跳脫聲韻 = os.path.join(資料目錄, '莫跳脫聲韻.cfg')
		self.字串寫入檔案(莫跳脫聲韻, 'noNumEscapes = T')
		整理音節指令 = '{0}HLEd -A -C {1} -l "*" -n {2} -i {3} -S {4} /dev/null'\
			.format(執行檔路徑, 莫跳脫聲韻, 原來音類檔, 原來音節檔, 全部標仔檔)
		self.走指令(整理音節指令)
	def 標仔切做聲韻(self, 執行檔路徑, 音節檔, 音節聲韻對照檔, 資料目錄, 聲韻類檔, 聲韻檔):
		執行檔路徑 = self.執行檔路徑加尾(執行檔路徑)
		莫跳脫聲韻 = os.path.join(資料目錄, '莫跳脫聲韻.cfg')
		self.字串寫入檔案(莫跳脫聲韻, 'noNumEscapes = T')
		切聲韻參數檔 = os.path.join(資料目錄, '拆聲韻參數檔.led')
		self.字串寫入檔案(切聲韻參數檔, 'EX')
		切聲韻指令 = '{0}HLEd -A -C {1} -l "*" -i {2} -n {3} -d {4} {5} {6}'\
			.format(執行檔路徑, 莫跳脫聲韻,
				聲韻檔, 聲韻類檔, 音節聲韻對照檔, 切聲韻參數檔, 音節檔)
		self.走指令(切聲韻指令)
	特徵參數 = \
'''
SOURCEKIND = {0}
SOURCEFORMAT = {1}
TARGETKIND = MFCC_E_D_A_Z
TARGETRATE = 100000.0
WINDOWSIZE = 200000.0
PREEMCOEF = 0.975
NUMCHANS = 26
CEPLIFTER = 22
NUMCEPS = 12
USEHAMMING = T
DELTAWINDOW = 2	
ACCWINDOW= 2
'''
