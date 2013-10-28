#臺灣閩南語羅馬字拼音對照音值韻母表 = {
#	'a', 'ah', 'ap', 'at', 'ak', 'ann', 'annh',
#	'am', 'an', 'ang',
#	'e', 'eh', 'enn', 'ennh',
#	'i', 'ih', 'ip', 'it', 'ik', 'inn', 'innh',
#	'im', 'in', 'ing',
#	'o', 'oh',
#	'oo', 'ooh', 'op', 'ok', 'om', 'ong', 'onn', 'onnh',
#	'oi', 'oih',  # 硩⿰落去
#	'u', 'uh', 'ut', 'un',
#	'ai', 'aih', 'ainn', 'ainnh',
#	'au', 'auh', 'aunn', 'aunnh',
#	'ia', 'iah', 'iap', 'iat', 'iak', 'iam', 'ian', 'iang', 'iann', 'iannh',
#	'io', 'ioh',
#	'iok', 'iong', 'ionn',
#	'iu', 'iuh', 'iut', 'iunn', 'iunnh',
#	'ua', 'uah', 'uat', 'uak', 'uan', 'uann', 'uannh',
#	'ue', 'ueh', 'uenn', 'uennh',
#	'ui', 'uih', 'uinn', 'uinnh',
#	'iau', 'iauh', 'iaunn', 'iaunnh',
#	'uai', 'uaih', 'uainn', 'uainnh',
#	'm', 'mh', 'ng', 'ngh',
#	'er', 'erh', 'erm', 'ere', 'ereh',  # 泉　鍋
#	'ee', 'eeh', 'eng', 'uee',  # 漳　家
#	'ir', 'irh', 'irp', 'irt', 'irk', 'irm', 'irn', 'irng', 'irinn',
#	'ioo', 'iooh',  # 諾 0hioo 0hiooh
#	'ie',  # 鹿港偏泉腔
#	'uang',
#	'or', 'orh', 'ior', 'iorh',  # 蚵
#		}
#
#class 臺灣閩南語羅馬字拼音轉音值模組():
#	韻母表 = 臺灣閩南語羅馬字拼音對照音值韻母表
#	聲 = None
#	韻 = None
#	調 = None
#	音標 = None
#	def __init__(self, 聲, 韻, 調, 輕):
#		if 聲 == None or 韻 == None or 調 == None or 輕 == None :
#			return
#		if 聲=='m' or 聲=='n' or 聲=='ng':
#			if 'm' not in 韻 and 'n' not in 韻:
#				if 韻.endswith('h') or 韻.endswith('p') or 韻.endswith('t') or 韻.endswith('k'):
#					韻=韻[:-1]+'nn'+韻[-1]
#				else:
#					韻+='nn'
#				if 韻=='oonnh':
#					韻='onnh'
#		return (聲,韻)
#		if 韻.startswith('i') and (聲 == 'ts' or 聲 == 'tsh' or 聲 == 's' or 聲 == 'j'):
#			聲 += 'i'
#		if 輕 == '0':
#			調 = '0'
#		self.聲 = self.聲母表[聲]
#		self.韻 = self.韻母表[韻]
#		self.調 = self.聲調符號表[調]
#		if 調 == '0':
#			self.音標 = self.調 + self.聲 + self.韻
#		elif 調 == '8':
#			self.音標 = self.聲 + self.韻[:-1] + self.調 + self.韻[-1:]
#		else:
#			self.音標 = self.聲 + self.韻 + self.調
