'''
Created on 2013/3/1

@author: Ihc
'''
from subprocess import Popen, PIPE
class 官方剖析工具:
	def 剖析(self, 愛轉換的字串):
		找位置 = Popen(['pwd'], stdout = PIPE)
		for 一逝 in 找位置.stdout:
			程式所在 = 一逝[:-1].decode("utf-8")
		程式所在, 資料夾 = 程式所在.rsplit('/', 1)
		while 資料夾 != 'src':
			程式所在, 資料夾 = 程式所在.rsplit('/', 1)
		程序輸出 = Popen(['/bin/bash' , 程式所在 + '/CKIPClient/剖析.sh', 愛轉換的字串 ], stdout = PIPE)
		return [ 一逝[:-1].decode("utf-8") for 一逝 in 程序輸出.stdout]

if __name__ == '__main__':
	工具 = 官方剖析工具()
	print(工具.剖析('我想吃飯。我想吃很多飯。'))
