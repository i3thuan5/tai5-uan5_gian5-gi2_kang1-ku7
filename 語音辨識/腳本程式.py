import os

class 腳本程式:
	def 執行檔路徑加尾(self, 執行檔路徑):
		if 執行檔路徑 != '' and not 執行檔路徑.endswith('/'):
			return 執行檔路徑 + '/'
		return 執行檔路徑
	def 走指令(self, 指令):
		回傳值 = os.system(指令)
		if 回傳值 != 0:
			raise RuntimeError('指令走到一半發生問題！！指令：{0}'
				.format(指令))
	def 細項目錄(self, 資料目錄, 細項名):
		細項目錄 = os.path.join(資料目錄, 細項名)
		os.makedirs(細項目錄, exist_ok=True)
		return 細項目錄
	def 陣列寫入檔案(self, 檔名, 陣列):
		self.字串寫入檔案(檔名, '\n'.join(陣列))
	def 字串寫入檔案(self, 檔名, 字串):
		檔案 = open(檔名, 'w')
		print(字串, file=檔案)
		檔案.close()
	def 讀檔案(self, 檔名):
		檔案 = open(檔名, 'r')
		資料 = []
		for 一逝 in 檔案:
			一逝 = 一逝.rstrip()
			if 一逝 != '':
				資料.append(一逝)
		檔案.close()
		return 資料