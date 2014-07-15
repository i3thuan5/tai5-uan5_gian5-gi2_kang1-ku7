from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音聲母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音韻母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音轉音值模組 import 臺灣閩南語羅馬字拼音對照音值聲母表
import itertools
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音轉音值模組 import 臺灣閩南語羅馬字拼音對照音值韻母表

class 對照表:
	def 生聲韻對照(self,檔名):
		資料=[]
		格式='{0}\t{1}'
		資料.append(格式.format('sil','sil'))
		資料.append(格式.format('sp','sp'))
		for 聲母 in 臺灣閩南語羅馬字拼音聲母表:
			for 韻母 in 臺灣閩南語羅馬字拼音韻母表:
				音=聲母+韻母
				資料.append(格式.format(音,
					' '.join(臺灣閩南語羅馬字拼音(音).音值()[:-1])))
		資料.sort()
		print('\n'.join(資料),file=open(檔名,'w'))
	def 生聲韻表(self,檔名):
		資料=[]
		格式='{0}\t{1}'
		資料.append(格式.format('sp','sp'))
		for 音 in itertools.chain.from_iterable([
				['sil','sp'],
				臺灣閩南語羅馬字拼音對照音值聲母表.values(),
				臺灣閩南語羅馬字拼音對照音值韻母表.values(),
				]):
			資料.append(格式.format(音,音))
		資料.sort()
		print('\n'.join(資料),file=open(檔名,'w'))

if __name__ == '__main__':
	對照表().產生聲韻表('字典')