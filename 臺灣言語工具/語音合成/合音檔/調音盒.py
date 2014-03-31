# -*- coding: utf-8 -*-
from tempfile import NamedTemporaryFile
import os
from 臺灣言語工具.系統整合.外部程式工具 import 外部程式工具

class 調音盒:
	指令 = '/usr/bin/sox '
	單指令 = 指令+'{{0}} {{1}} '
	大細聲指令 = 單指令 + 'vol {0}'
	音懸指令 = 單指令 + 'pitch {0}'
	篩雜訊指令 = (指令 + '-c 1 -t s16 -r 16000 {0} -n noiseprof |'
		+ 單指令 + ' noisered')
	篩懸音指令 = (指令 + '{{0}} -n highpass {0} noiseprof |'
		+ 單指令 + ' noisered')
	程式工具 = 外部程式工具()
	def 用指令調(self, 音, 指令):
		舊音 = NamedTemporaryFile(mode = 'wb', suffix = '.wav',
			delete = False)
		舊音.write(音)
		舊音.close()
		新音 = NamedTemporaryFile(suffix = '.wav', delete = False)
		新音.close()
		os.system(指令.format(舊音.name, 新音.name))
		調好音 = open(新音.name, 'rb').read()
		os.unlink(舊音.name)
		os.unlink(新音.name)
		return 調好音
	def 改大細聲(self, 音, 大細聲):
		return self.用指令調(音, self.大細聲指令.format(大細聲))
	def 改音懸(self, 音, 音懸):
		return self.用指令調(音, self.音懸指令.format(音懸))
	def 篩雜訊(self, 音, 雜訊=程式工具.專案目錄()+'/外部程式/Sox/雜訊.wav'):
		return self.用指令調(音, self.篩雜訊指令.format(雜訊))
	def 篩懸音(self, 音, 懸音):
		return self.用指令調(音, self.篩懸音指令.format(懸音))
