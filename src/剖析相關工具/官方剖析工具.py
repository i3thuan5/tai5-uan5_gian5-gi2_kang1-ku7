'''
Created on 2013/3/1

@author: Ihc
'''
from subprocess import Popen, PIPE
from 系統整合.外部程式工具 import 外部程式工具
class 官方剖析工具:
	程式工具=外部程式工具()
	def 剖析(self, 愛轉換的字串):
		程式所在=self.程式工具.專案目錄()
		程序輸出 = Popen(['/bin/bash' , 程式所在 + '/外部程式/CKIPClient/剖析.sh', 愛轉換的字串 ], stdout = PIPE)
		剖析結果 = [ 一逝[:-1].decode("utf-8") for 一逝 in 程序輸出.stdout ]
		程序輸出.stdout.close()
		return 剖析結果