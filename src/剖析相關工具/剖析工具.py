'''
Created on 2013/3/1

@author: Ihc
'''
from 剖析相關工具.官方剖析工具 import 官方剖析工具
from 剖析相關工具.自設剖析工具 import 自設剖析工具
class 剖析工具:
	官方工具 = 官方剖析工具()
	自設工具 = 自設剖析工具()
	def 剖析(self, 愛轉換的字串):
		return self.官方工具.剖析(愛轉換的字串)
#		return self.自設工具.剖析(愛轉換的字串)

if __name__ == '__main__':
	工具 = 剖析工具()
	print(工具.剖析('我想吃飯。我想吃很多飯。'))
