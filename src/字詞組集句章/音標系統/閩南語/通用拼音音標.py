from 字詞組集句章.音標系統.閩南語.閩南語音標介面 import 閩南語音標介面
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音

通用拼音佮臺灣羅馬聲母對照表 = {
'b':'p',
'p':'ph',
'bh':'b',
'v':'b',
'm':'m',
'd':'t',
't':'th',
'n':'n',
'l':'l',
'g':'k',
'k':'kh',
'gh':'g',
'q':'g',
'ng':'ng',
'z':'ts',
'c':'tsh',
's':'s',
'r':'j',
'h':'h',
'':'',
}
通用拼音佮臺灣羅馬韻母對照表 = {
'a':'a',
'ah':'ah',
'ai':'ai',
'ainn':'ainn',
'ak':'ak',
'am':'am',
'an':'an',
'ang':'ang',
'ann':'ann',
'ap':'ap',
'at':'at',
'au':'au',
'aunn':'aunn',
'e':'e',
'eh':'eh',
'en':'ian',
'enn':'enn',
'erh':'oh',
'ernn':'onn',
'er':'o',
'et':'iat',
'iah':'iah',
'ia':'ia',
'iak':'iak',
'iam':'iam',
'iang':'iang',
'iannh':'iannh',
'iann':'iann',
'iap':'iap',
'iau':'iau',
'iaunn':'iaunn',
'ierh':'ioh',
'ier':'io',
'ih':'ih',
'i':'i',
'ik':'ik',
'im':'im',
'ing':'ing',
'in':'in',
'innh':'innh',
'inn':'inn',
'io':'io',
'iok':'iok',
'iong':'iong',
'ionn':'ionn',
'iorh':'ioh',
'ior':'io',
'ip':'ip',
'it':'it',
'iu':'iu',
'iunn':'iunn',
'm':'m',
'ng':'ng',
'oh':'ooh',
'ok':'ok',
'om':'om',
'ong':'ong',
'onn':'onn',
'o':'oo',
'orh':'oh',
'ornn':'onn',
'or':'o',
'uah':'uah',
'uainnh':'uainnh',
'uainn':'uainn',
'uai':'uai',
'uann':'uann',
'uan':'uan',
'uat':'uat',
'ua':'ua',
'ueh':'ueh',
'ue':'ue',
'uh':'uh',
'uih':'uih',
'uinn':'uinn',
'ui':'ui',
'un':'un',
'ut':'ut',
'u':'u',
	}
通用拼音佮臺灣羅馬調類對照表 = {
	'1':'1', '2':'7', '3':'3', '4':'2', '5':'5',
	'6':'8', '7':'4', '8':'10', '9':'9'}
class 通用拼音音標(閩南語音標介面):
	# 0 bh iaunnh 9 保險
	音標上長長度 = 1 + 2 + 6 + 1 + 1
	聲 = None
	韻 = None
	聲韻 = None
	調 = None
	音標 = None
	def __init__(self, 音標):
		self.聲母對照表 = 通用拼音佮臺灣羅馬聲母對照表
		self.韻母對照表 = 通用拼音佮臺灣羅馬韻母對照表
		self.調類對照表 = 通用拼音佮臺灣羅馬調類對照表
		self.音標 = None
		self.音標 = None
		if 音標[-1:] in self.調類對照表:
			for 所在 in range(len(音標) - 1):
				if 音標[:所在] in self.聲母對照表 and 音標[所在:-1] in self.韻母對照表:
					self.聲 = 音標[:所在]
					self.韻 = 音標[所在:-1]
					self.調 = 音標[-1:]
					if self.韻.endswith('h') or self.韻.endswith('p') or \
						self.韻.endswith('t') or self.韻.endswith('k'):
						if self.調=='1':
							self.調='6'
						elif self.調=='2':
							self.調='7'
						elif self.調=='3':
							self.調='8'
					self.聲韻 = self.聲 + self.韻
					self.音標 = self.聲韻 + self.調
		if self.轉換到臺灣閩南語羅馬字拼音()==None:
			self.聲韻 = None
			self.音標 = None
		
	def 轉換到臺灣閩南語羅馬字拼音(self):
		if self.音標 == None:
			return None
		聲 = self.聲母對照表[self.聲]
		韻 = self.韻母對照表[self.韻]
		調 = self.調類對照表[self.調]
		臺羅=臺灣閩南語羅馬字拼音(聲 + 韻 + 調)
		return 臺羅.音標

# if __name__ == '__main__':
# 	print(通用拼音佮臺灣語言音標聲韻對照表)
# 	for 通, 臺 in 通用拼音佮臺灣語言音標聲韻對照表.items():
# 		臺羅 = 臺灣閩南語羅馬字拼音(臺)
# 		if 臺羅.聲 == '':
# # 	 			print("'{0}':'{1}',".format(通,臺))
# 			pass
# 		else:
# 			好通 = ''
# 			好韻 = ''
# 			for 通韻, 臺韻 in 通用拼音佮臺灣語言音標韻母對照表.items():
# 				if 通.endswith(通韻) and len(通韻) > len(好通):
# 					好通 = 通韻
# 					好韻 = 臺韻
# 			print(通[:-len(好通)], 臺[:-len(好韻)])
# 	字音對照 = 通用拼音音標('bai5')
# 	print(字音對照.音標)
# 	print(字音對照.轉換到臺灣閩南語羅馬字拼音())
# 	print(通用拼音音標('zit3').轉換到臺灣閩南語羅馬字拼音())
# 	print(通用拼音音標('zit3').轉換到臺灣閩南語羅馬字拼音())
# 	print('gior4')
# 	print(通用拼音音標('gior4').轉換到臺灣閩南語羅馬字拼音())
# 	print('gier3')
# 	print(通用拼音音標('gier3').轉換到臺灣閩南語羅馬字拼音())
# 	print(max([len (a) for a in 通用拼音佮臺灣語言音標聲韻對照表]))
