# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
import os
from tempfile import NamedTemporaryFile
from 臺灣言語工具.系統整合.外部程式工具 import 外部程式工具
import curses.ascii

class 標仔轉音檔:
	程式工具 = 外部程式工具()
	def 合成(self, 模型, 速度, 標仔):
		標仔檔 = NamedTemporaryFile(delete = False)
		標仔檔.write('\n'.join(self.跳脫標仔(標仔)).encode(
			encoding = 'utf_8', errors = 'strict'))
		聲音檔 = NamedTemporaryFile(delete = False)
		標仔檔.close()
		聲音檔.close()
		程式所在 = self.程式工具.專案目錄()
		os.system(
			'{0}/外部程式/HTSEngine/程式/hts_engine -m {0}/外部程式/HTSEngine/模型/{1} -ow {3} -r {4} {2}'
			.format(程式所在, 模型, 標仔檔.name, 聲音檔.name, 速度))
		音標資料 = open(聲音檔.name, 'rb').read()
		os.unlink(聲音檔.name)
		return 音標資料
	
	def 跳脫標仔(self, 標仔):
		新標仔=[]
		for 語句 in 標仔:
			新標仔.append(self.跳脫字元(語句))
		return 新標仔

	def 跳脫字元(self, 語句):
		"""
		佇HTK內底的HShell.c
		ReWriteString((char*)s.c_str(), NULL, ESCAPE_CHAR)
		....
		else if (isprint(*p) || noNumEscapes) fputc(*p,f);
	  	else {
		 n=*p;
		 fputc(ESCAPE_CHAR,f);
		 fputc(((n/64)%8)+'0',f);fputc(((n/8)%8)+'0',f);fputc((n%8)+'0',f);
		 """
		處理了 = []
		for 字元編碼 in 語句.encode(encoding = 'utf_8', errors = 'strict'):
			字元 = chr(字元編碼)
			if curses.ascii.isprint(字元):
				處理了.append(字元)
			else:
				處理了.append('\\')
				數值 = 字元編碼
				for 編碼 in [(數值 // 64) % 8, (數值 // 8) % 8, 數值 % 8]:
					處理了.append(chr(ord('0') + 編碼))
		return ''.join(處理了)


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
