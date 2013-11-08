import os
from tempfile import NamedTemporaryFile
from 系統整合.外部程式工具 import 外部程式工具

class 標仔轉音檔:
	程式工具 = 外部程式工具()
	def 合成(self, 模型, 標仔):
		標仔檔 = NamedTemporaryFile(delete=False)
		標仔檔.write('\n'.join(標仔).encode(
			encoding='utf_8', errors='strict'))
		編碼過標仔檔 = NamedTemporaryFile(delete=False)
		聲音檔 = NamedTemporaryFile(delete=False)
		標仔檔.close()
		編碼過標仔檔.close()
		聲音檔.close()
		程式所在 = self.程式工具.專案目錄()
		
# 		os.system(
# 			'env LC_ALL=C {0}/外部程式/HTSEngine/程式/hts_engine -m {0}/外部程式/HTSEngine/模型/{1} -ow {3} -ot /home/Ihc/trace.ttt {2}'
# 			.format(程式所在, 模型, 標仔檔.name, 聲音檔.name))
		os.system(
			'/home/Ihc/workspace-cpp/HTS-2.3/Debug/HTS-2.3 < {1} > {2}'
			.format(程式所在, 標仔檔.name, 編碼過標仔檔.name))
		os.unlink(標仔檔.name)
		os.system(
			'{0}/外部程式/HTSEngine/程式/hts_engine -m {0}/外部程式/HTSEngine/模型/{1} -ow {3} -ot /home/Ihc/trace.ttt {2}'
			.format(程式所在, 模型, 編碼過標仔檔.name, 聲音檔.name))
		os.unlink(編碼過標仔檔.name)
		音標資料 = open(聲音檔.name, 'rb').read()
		os.unlink(聲音檔.name)
		return 音標資料

if __name__ == '__main__':
	轉音檔 = 標仔轉音檔()
	音檔 = 轉音檔.合成('HTSLSPanAll.htsvoice',
		['x-sil+x/tiau3:x/su5:x!x@x/ku3:x^x_x',
		'sil-t+o/tiau3:7/su5:0!8@8/ku3:0^8_8',
		't-o+a/tiau3:7/su5:0!8@8/ku3:0^8_8',
		'o-a+ng/tiau3:1/su5:1!7@8/ku3:1^7_8',
		'a-ng+oonn/tiau3:1/su5:2!6@8/ku3:2^6_8',
		'ng-oonn+u/tiau3:1/su5:2!6@8/ku3:2^6_8',
		'oonn-u+it/tiau3:3/su5:3!5@8/ku3:3^5_8',
		'u-it+ts/tiau3:8/su5:4!4@8/ku3:4^4_8',
		'it-ts+i/tiau3:7/su5:5!3@8/ku3:5^3_8',
		'ts-i+t/tiau3:7/su5:5!3@8/ku3:5^3_8',
		'i-t+o/tiau3:7/su5:6!2@8/ku3:6^2_8',
		't-o+a/tiau3:7/su5:6!2@8/ku3:6^2_8',
		'o-a+sil/tiau3:2/su5:7!1@8/ku3:7^1_8',
		'x-sil+x/tiau3:x/su5:x!x@x/ku3:x^x_x']
		)
	輸出 = open('/home/chhsueh/a.wav', 'wb')
	輸出.write(音檔)
	輸出.close()
