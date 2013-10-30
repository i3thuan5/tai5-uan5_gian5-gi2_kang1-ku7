import os
from tempfile import NamedTemporaryFile
from 系統整合.外部程式工具 import 外部程式工具

class 標仔轉音檔:
	程式工具=外部程式工具()
	def 合成(self,模型,標仔):
		標仔檔 = NamedTemporaryFile(delete=False)
		標仔檔.write('\n'.join(標仔))
		標仔檔.close()
		聲音檔 = NamedTemporaryFile(delete=False)
		聲音檔.close()
		程式所在=self.程式工具.專案目錄()
		os.system(
			'{0}/外部程式/HTSEngine/程式/hts_engine -m {0}/外部程式/HTSEngine/模型/{1} -ow {3} {2}'
			.format(程式所在,'HTSLSPanAll.htsvoice',
			標仔檔.name,聲音檔.name) )
		os.unlink(標仔檔.name)
		音標資料=open(聲音檔.name,'wb').read()
		os.unlink(聲音檔.name)
		return 音標資料