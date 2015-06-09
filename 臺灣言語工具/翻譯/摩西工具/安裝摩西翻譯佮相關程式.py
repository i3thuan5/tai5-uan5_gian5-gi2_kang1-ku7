# -*- coding: utf-8 -*-
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
import os


from 臺灣言語工具.系統整合.外部程式 import 外部程式
from shutil import move

_外部程式目錄 = 外部程式().目錄()
class 安裝摩西翻譯佮相關程式(程式腳本):
	def 安裝moses(self, mgiza安裝路徑=_外部程式目錄, 編譯CPU數=4):
		moses程式碼目錄 = os.path.join(mgiza安裝路徑, 'mosesdecoder')
		if not os.path.isdir(moses程式碼目錄):
			with self._換目錄(mgiza安裝路徑):
				self._走指令([
						'git', 'clone',
						'--depth', '1',
						'https://github.com/sih4sing5hong5/mosesdecoder.git'
					])
		with self._換目錄(moses程式碼目錄):
			self._走指令(['git', 'pull', '--depth', '1'], 愛直接顯示輸出=True)
			self._走指令(['./bjam', '-j{0}'.format(編譯CPU數)], 愛直接顯示輸出=True)
	
	def 安裝gizapp(self, gizapp安裝路徑=_外部程式目錄):
		gizapp程式碼目錄 = os.path.join(gizapp安裝路徑, 'giza-pp')
		if not os.path.isdir(gizapp程式碼目錄):
			with self._換目錄(gizapp安裝路徑):
				self._走指令([
						'git', 'clone',
						'--depth', '1',
						'https://github.com/sih4sing5hong5/giza-pp.git'
					])
		with self._換目錄(gizapp程式碼目錄):
			self._走指令(['git', 'pull', '--depth', '1'], 愛直接顯示輸出=True)
			self._走指令('make', 愛直接顯示輸出=True)
		執行檔目錄=self._細項目錄(gizapp程式碼目錄, 'bin')
		move(os.path.join(gizapp程式碼目錄,'GIZA++-v2','GIZA++'),執行檔目錄)
		move(os.path.join(gizapp程式碼目錄,'GIZA++-v2','snt2cooc.out'),執行檔目錄)
		move(os.path.join(gizapp程式碼目錄,'mkcls-v2','mkcls'),執行檔目錄)
	
	def 安裝mgiza(self, mgiza安裝路徑=_外部程式目錄):
		mgiza程式碼目錄 = os.path.join(mgiza安裝路徑, 'mgiza', 'mgizapp')
		if not os.path.isdir(mgiza程式碼目錄):
			with self._換目錄(mgiza安裝路徑):
				self._走指令([
						'git', 'clone',
						'--depth', '1',
						'https://github.com/moses-smt/mgiza.git'
					])
		with self._換目錄(mgiza程式碼目錄):
			self._走指令(['git', 'pull', '--depth', '1'], 愛直接顯示輸出=True)
			self._走指令(['cmake', '.'])
			self._走指令('make', 愛直接顯示輸出=True)
			self._走指令(['make', 'install'], 愛直接顯示輸出=True)
