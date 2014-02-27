import os
from 臺灣言語工具.字詞組集句章.音標系統.國語.國語注音符號 import 國語注音符號

class 工研院標音變注音:
	所在='/home/Ihc/意傳計劃/機構資料/工研院合成語音/SyllableNumber.utf8'
	對應表={}
	調號表={1:'',2:'ˊ',3:'ˇ',4:'ˋ',5:'˙'}
	def __init__(self):
		for 逝 in open(self.所在):
			數字,注音 = 逝.split()
			self.對應表[int(數字)]=注音
	def 產生字典檔(self,檔案):
		字典檔=open(檔案,'w')
		for 音 in self.對應表.values():
			注音=國語注音符號(音)
			if 注音.聲韻==None:
				print (音)
			print(注音.聲韻,注音.聲,注音.韻,file=字典檔)
		字典檔.close()
	def 轉注音(self,檔案,愛調=True):
		上尾一逝=None
		for 逝 in open(檔案):
			上尾一逝=逝
			pass
		if 上尾一逝==None:
			return None
# 		print(檔案)
		注音=[]
		for 音標 in 上尾一逝.split():
			音=int(音標)
			調=self.調號表[音//1000]
			注音聲韻=self.對應表[音%1000]
# 			print(注音聲韻,調)
			if 愛調:
				注音.append(注音聲韻+調)
			else:
				注音.append(注音聲韻)
		return '\n'.join(注音)

if __name__ == '__main__':
	標音變注音=工研院標音變注音()
	標音變注音.產生字典檔('/home/Ihc/tmpfs/tian2')
# 	標音變注音.轉注音('/home/Ihc/tmpfs/piau1/1306401.lab')
	目標='/home/Ihc/tmpfs/tsu3/'
	os.chdir('/home/Ihc/tmpfs/piau1/')
	for 檔名 in os.listdir(".")[:]:
		if 檔名.endswith('lab'):
			try:
				注音資料=標音變注音.轉注音(檔名,愛調=False)
				if 注音資料==None:
					continue
			except:
				pass
			else:
				輸出=open(目標+檔名,'w')
				print(注音資料, file=輸出, flush=False)
				輸出.close()
