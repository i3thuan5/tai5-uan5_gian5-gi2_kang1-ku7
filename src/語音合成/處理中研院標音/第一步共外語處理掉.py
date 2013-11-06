'''
Created on 2013/10/12

@author: Ihc
'''
class 第一步共外語處理掉:
	def 擲掉外語佮空逝(self,句集):
		資料=[]
		頂一逝是標籤=True
		有外語=False
		for 句 in 句集:
			句=句.strip()
			if 句=='':
				continue
			elif 'language' in 句 or '[//]' in 句 or '_' in 句:
				if not 頂一逝是標籤:
					資料=資料[:-1]
				有外語=True
				頂一逝是標籤=False
			elif 句.startswith('<') or 句.startswith('\ufeff'):
				頂一逝是標籤=True
				有外語=False
			else:
				if 有外語:
					頂一逝是標籤=True
				else:
					if 頂一逝是標籤:
						資料.append(句.strip())
					else:
						資料[-1]+=句.strip()
					頂一逝是標籤=False
		return 資料