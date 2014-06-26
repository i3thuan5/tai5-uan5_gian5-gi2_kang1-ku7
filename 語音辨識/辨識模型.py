import os

class 辨識模型:
	wav副檔名 = '.wav'
	音檔副檔名 = wav副檔名
	標仔副檔名 = '.lab'
	特徵 = 'mfcc'
	特徵副檔名 = '.' + 特徵
	def 訓練(self, 音檔目錄, 標仔目錄, 資料目錄, 執行檔路徑=''):
		if 執行檔路徑 != '' and not 執行檔路徑.endswith('/'):
			執行檔路徑 = 執行檔路徑 + '/'
		全部語料 = self.揣全部語料(音檔目錄, 標仔目錄)
		全部特徵檔 = os.path.join(資料目錄, '全部特徵檔')
		算特徵 = True
		if 算特徵:
			參數檔 = '../config/mfcc39.cfg.44100'
			特徵目錄 = os.path.join(資料目錄, self.特徵)
			os.makedirs(特徵目錄, exist_ok=True)
			全部特徵 = []
			for 語料名, 音檔所在, 標仔所在 in 全部語料:
				特徵所在 = os.path.join(特徵目錄,
					語料名 + self.特徵副檔名)
				self.算特徵(執行檔路徑, 參數檔, 音檔所在, 特徵所在)
				全部特徵.append(特徵所在)
			self.陣列寫入檔案(全部特徵檔, 全部特徵)
	def 揣全部語料(self,音檔目錄,標仔目錄):
		全部語料=[]
		for 音檔檔名 in os.listdir(音檔目錄):
			if 音檔檔名.endswith(self.音檔副檔名):
				語料名 = 音檔檔名[:-len(self.音檔副檔名)]
				標仔所在 = os.path.join(標仔目錄,
					語料名 + self.標仔副檔名)
				if os.path.isfile(標仔所在):
					音檔所在 = os.path.join(音檔目錄, 音檔檔名)
					全部語料.append((語料名, 音檔所在, 標仔所在))
		return 全部語料
	def 算特徵(self, 執行檔路徑, 參數檔, 音檔所在, 特徵所在):
		特徵指令 = '{0}HCopy -C {1} {2} {3}'.format(
			執行檔路徑, 參數檔, 音檔所在, 特徵所在)
		print(特徵指令)
		os.system(特徵指令)
	def 陣列寫入檔案(self, 檔名, 陣列):
		self.字串寫入檔案(檔名, '\n'.join(陣列))
	def 字串寫入檔案(self, 檔名, 字串):
		檔案 = open(檔名, 'w')
		print(字串, file=檔案)
		檔案.close()
if __name__ == '__main__':
	模型 = 辨識模型()
	這馬目錄 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	模型.訓練(這馬目錄 + '/wav', 這馬目錄 + '/labels', 這馬目錄 + '/data')
		
