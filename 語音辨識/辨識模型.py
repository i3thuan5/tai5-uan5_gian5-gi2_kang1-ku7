import os
import itertools
import shutil

class 辨識模型:
	wav副檔名 = '.wav'
	音檔副檔名 = wav副檔名
	標仔副檔名 = '.lab'
	特徵 = 'mfcc'
	特徵副檔名 = '.' + 特徵
	def 訓練(self, 音檔目錄, 標仔目錄, 資料目錄, 執行檔路徑='',
			算特徵=True, 切標仔=True,
			做初步模型=True, 加混合=True):
		執行檔路徑 = self.執行檔路徑加尾(執行檔路徑)
		全部語料 = self.揣全部語料(音檔目錄, 標仔目錄)
		
		全部特徵檔 = os.path.join(資料目錄, '全部特徵檔.scp')
		全部標仔檔 = os.path.join(資料目錄, '全部標仔檔.scp')
		os.makedirs(資料目錄, exist_ok=True)
		if 算特徵:
			算特徵參數檔 = os.path.join(資料目錄, '算特徵參數.cfg')
			self.字串寫入檔案(算特徵參數檔, self.算特徵參數)
			特徵目錄 = os.path.join(資料目錄, self.特徵)
			os.makedirs(特徵目錄, exist_ok=True)
			全部特徵 = []
			全部標仔 = []
			for 語料名, 音檔所在, 標仔所在 in 全部語料:
				特徵所在 = os.path.join(特徵目錄,
					語料名 + self.特徵副檔名)
				self.算特徵(執行檔路徑, 算特徵參數檔, 音檔所在, 特徵所在)
				全部特徵.append(特徵所在)
				全部標仔.append(標仔所在)
			self.陣列寫入檔案(全部特徵檔, 全部特徵)
			self.陣列寫入檔案(全部標仔檔, 全部標仔)
		聲韻類檔 = os.path.join(資料目錄, '聲韻類檔.list')
		聲韻檔 = os.path.join(資料目錄, '聲韻檔.mlf')
		if 切標仔:
			self.標仔加恬佮切開(執行檔路徑, 全部標仔檔, 資料目錄, 聲韻類檔, 聲韻檔)
		初步模型檔 = os.path.join(資料目錄, '初步模型檔-重估.macro')
		上尾模型檔 = None
		if 做初步模型:
			初步模型檔 = self.建立初步模型(執行檔路徑, 資料目錄, 全部特徵檔, 聲韻類檔, 聲韻檔)
			上尾模型檔 = 初步模型檔
		if 加混合:
			混合數 = [1, 2, 4, 8, 12, 16, 24, 32]
			加混合了模型 = self.加混合數(執行檔路徑, 資料目錄, 全部特徵檔, 聲韻類檔, 聲韻檔, 初步模型檔, 混合數)
			上尾模型檔 = 加混合了模型
		return 全部特徵檔, 聲韻類檔, 聲韻檔, 上尾模型檔
	def 對齊音(self, 聲韻類檔, 模型檔, 聲韻檔, 特徵檔, 資料目錄, 執行檔路徑=''):
		對照表 = []
		for 聲韻 in self.讀檔案(聲韻類檔):
			對照表.append('{0}\t{0}'.format(聲韻))
		聲韻對照檔 = os.path.join(資料目錄, '聲韻對照檔.dict')
		self.陣列寫入檔案(聲韻對照檔, 對照表)
		對齊音結果檔 = os.path.join(資料目錄, '對齊音結果檔.mlf')
		對齊音指令 = '{0}HVite -A -p -20 -o N -H {1} -l "*" -t 400 -I {2} -S {3} -i {4} {5} {6}'\
			.format(執行檔路徑, 模型檔, 聲韻檔, 特徵檔, 對齊音結果檔, 聲韻對照檔, 聲韻類檔)
		self.走指令(對齊音指令)
		return 聲韻對照檔, 對齊音結果檔
	def 揣全部語料(self, 音檔目錄, 標仔目錄):
		全部語料 = []
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
		特徵指令 = '{0}HCopy -A -C {1} {2} {3}'.format(
			執行檔路徑, 參數檔, 音檔所在, 特徵所在)
		self.走指令(特徵指令)
	def 標仔加恬佮切開(self, 執行檔路徑, 全部標仔檔, 資料目錄, 聲韻類檔, 聲韻檔):
		原來音類檔 = os.path.join(資料目錄, '原來音類檔.list')
		原來音節檔 = os.path.join(資料目錄, '原來音節檔.mlf')
		整理音節指令 = '{0}HLEd -A -l "*" -n {1} -i {2} -S {3} /dev/null'\
			.format(執行檔路徑, 原來音類檔, 原來音節檔, 全部標仔檔)
		self.走指令(整理音節指令)
		加恬音類檔 = os.path.join(資料目錄, '加恬音類檔.list')
		加恬音節檔 = os.path.join(資料目錄, '加恬音節檔.mlf')
		加恬參數檔 = os.path.join(資料目錄, '加恬參數檔.cmd')
		self.字串寫入檔案(加恬參數檔, 'IS sil sil')
		加恬音節指令 = '{0}HLEd -A -l "*" -n {1} -i {2} {3} {4}'\
			.format(執行檔路徑, 加恬音類檔, 加恬音節檔, 加恬參數檔, 原來音節檔)
		self.走指令(加恬音節指令)

		音節聲韻對照檔 = '../config/Syl2Monophone.dic.ok'  # os.path.join(資料目錄, '')
		切聲韻參數檔 = os.path.join(資料目錄, '拆聲韻參數檔.cmd')
		self.字串寫入檔案(切聲韻參數檔, 'EX')
		切聲韻指令 = '{0}HLEd -A -l "*" -i {1} -n {2} -d {3} {4} {5}'\
			.format(執行檔路徑, 聲韻檔, 聲韻類檔, 音節聲韻對照檔, 切聲韻參數檔, 加恬音節檔)
		self.走指令(切聲韻指令)
	def 建立初步模型(self, 執行檔路徑, 資料目錄, 全部特徵檔, 聲韻類檔, 聲韻檔):
		公家模型建立參數檔 = os.path.join(資料目錄, '公家模型建立參數檔.cfg')
		self.字串寫入檔案(公家模型建立參數檔, self.初步模型參數)
		公家模型檔 = os.path.join(資料目錄, '公家模型檔')
		模型版檔 = os.path.join(資料目錄, '模型版檔')
		self.字串寫入檔案(模型版檔, self.模型版參數)
		公家模型指令 = '{0}HCompV -A -C {1} -m -f 0.0001 -o {2} -M {3} -I {4} -S {5} {6}'\
			.format(執行檔路徑, 公家模型建立參數檔, 公家模型檔,
				資料目錄, 聲韻檔, 全部特徵檔, 模型版檔)
		self.走指令(公家模型指令)
		公家模型 = self.讀檔案(公家模型檔)
		公家變異數檔 = os.path.join(資料目錄, 'vFloors')
		公家變異數 = self.讀檔案(公家變異數檔)
		初步模型資料 = [公家模型[:3], 公家變異數]
		公家狀態 = 公家模型[4:]
		聲韻名 = '~h "{0}"'
		for 聲韻 in self.讀檔案(聲韻類檔):
			初步模型資料.append([聲韻名.format(聲韻)])
			初步模型資料.append(公家狀態)
		初步模型檔 = os.path.join(資料目錄, '初步模型檔.macro')
		self.陣列寫入檔案(初步模型檔,
			itertools.chain.from_iterable(初步模型資料))
		return self.模型重估(執行檔路徑, 資料目錄, 全部特徵檔, 聲韻類檔, 聲韻檔, 初步模型檔, 估幾擺=20)
	def 模型重估(self, 執行檔路徑, 資料目錄, 全部特徵檔, 聲韻類檔, 聲韻檔, 原來模型檔, 估幾擺=10):
		原來模型檔檔名 = os.path.basename(原來模型檔)
		這馬模型檔 = 原來模型檔
		基本路徑 = 原來模型檔.rsplit('.', 1)[0]
		資料夾 = 基本路徑 + '-重估'
		for 第幾擺 in range(估幾擺):
			這擺資料夾 = os.path.join(資料夾, '{0:02}'.format(第幾擺))
			os.makedirs(這擺資料夾, exist_ok=True)
			新統計檔 = os.path.join(這擺資料夾, '統計.sts')
			重估指令 = '{0}HERest -A -T 407 -t 450.0 150.0 1000.0 -M {1} -H {2} -s {3} -I {4} -S {5} {6}'\
				.format(執行檔路徑, 這擺資料夾, 這馬模型檔, 新統計檔,
					聲韻檔, 全部特徵檔, 聲韻類檔)
			self.走指令(重估指令)
			這馬模型檔 = os.path.join(這擺資料夾, 原來模型檔檔名)
		上尾模型檔 = '{0}-重估.macro'.format(基本路徑)
		shutil.copy(這馬模型檔, 上尾模型檔)
		return 上尾模型檔
	def 加混合數(self, 執行檔路徑, 資料目錄,
			全部特徵檔, 聲韻類檔, 聲韻檔,
			原來模型, 混合數):
		頂一个模型 = 原來模型
		for 擺, 混合 in enumerate(混合數):
			這擺資料夾 = os.path.join(資料目錄, '加混合數', '{0:02}'.format(擺))
			os.makedirs(這擺資料夾, exist_ok=True)
			設定檔 = os.path.join(這擺資料夾, '設定檔.cmd')
			加混合模型 = os.path.join(這擺資料夾, '加混合模型.macro')
			self.陣列寫入檔案(設定檔, [
		 		"MU {0} {{*.state[2-4].mix}}".format(混合),
		 		"MU {0} {{sil.state[2-4].mix}}".format(混合 * 2)])
			加混合數指令 = '{0}HHEd -A -H {1} -w {2} {3} {4}'\
				.format(執行檔路徑, 頂一个模型, 加混合模型, 設定檔, 聲韻類檔)
			self.走指令(加混合數指令)
			頂一个模型 = self.模型重估(執行檔路徑, 資料目錄, 全部特徵檔, 聲韻類檔, 聲韻檔, 加混合模型, 估幾擺=20)
		加混合了模型 = os.path.join(資料目錄, '加混合了模型.macro')
		shutil.copy(頂一个模型, 加混合了模型)
		return 加混合了模型
	def 辨識網路(self, 執行檔路徑, 資料目錄, 聲韻類檔):
		語法 = '(sil < {0} > sil)'.format(
			'|'.join(self.讀檔案(聲韻類檔)))
		語法檔 = os.path.join(資料目錄, '語法檔.syntax')
		self.字串寫入檔案(語法檔, 語法)
		網路檔 = os.path.join(資料目錄, '網路檔.lat')
		產生網路指令 = '{0}HParse {1} {2}'\
			.format(執行檔路徑, 語法檔, 網路檔)
		self.走指令(產生網路指令)
	def 執行檔路徑加尾(self, 執行檔路徑):
		if 執行檔路徑 != '' and not 執行檔路徑.endswith('/'):
			return 執行檔路徑 + '/'
		return 執行檔路徑
	def 走指令(self, 指令):
		回傳值 = os.system(指令)
		if 回傳值 != 0:
			raise RuntimeError('指令走到一半發生問題！！指令：{0}'
				.format(指令))
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
			一逝 = 一逝.strip()
			if 一逝 != '':
				資料.append(一逝)
		檔案.close()
		return 資料
	算特徵參數 = \
'''
SOURCEKIND = WAVEFORM
SOURCEFORMAT = WAV
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
	初步模型參數 = \
'''
SOURCEKIND = ANON
SOURCEFORMAT = HTK
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
	模型版參數 = \
'''
~o <VecSize> 39 <MFCC_E_D_A_Z> <DiagC> <StreamInfo> 1 39
<BeginHMM>
<NUMSTATES> 5
<STATE> 2
<NUMMIXES> 1 
<SWeights> 1 1 
<STREAM> 1
<MIXTURE> 1 1.000000e+000
<MEAN> 39
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
<VARIANCE> 39
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0

<STATE> 3
<NUMMIXES> 1 
<SWeights> 1 1 
<STREAM> 1
<MIXTURE> 1 1.000000e+000
<MEAN> 39
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
<VARIANCE> 39
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0

<STATE> 4
<NUMMIXES> 1 
<SWeights> 1 1 
<STREAM> 1
<MIXTURE> 1 1.000000e+000
<MEAN> 39
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
<VARIANCE> 39
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0

<TRANSP> 5
0.000000e+000 1.000000e+000 0.000000e+000 0.000000e+000 0.000000e+000 
0.000000e+000 6.000000e-001 4.000000e-001 0.000000e+000 0.000000e+000 
0.000000e+000 0.000000e+000 6.000000e-001 4.000000e-001 0.000000e+000 
0.000000e+000 0.000000e+000 0.000000e+000 6.000000e-001 4.000000e-001 
0.000000e+000 0.000000e+000 0.000000e+000 0.000000e+000 0.000000e+000 
<ENDHMM>
'''
if __name__ == '__main__':
	模型 = 辨識模型()
	這馬目錄 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	資料目錄 = 這馬目錄 + '/data'
	特徵檔, 聲韻類檔, 聲韻檔, 模型檔 = 模型.訓練(
		這馬目錄 + '/wav', 這馬目錄 + '/labels', 資料目錄,
		算特徵=False)
	聲韻對照檔, 對齊音結果檔 = 模型.對齊音(聲韻類檔, 模型檔, 聲韻檔, 特徵檔, 資料目錄)
