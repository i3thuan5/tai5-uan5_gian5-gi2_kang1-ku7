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
from http.server import HTTPServer
from 服務架設.連線控制器 import 連線控制器
import Pyro4
from 資料庫.欄位資訊 import 偏漳優勢音腔口
from 資料庫.欄位資訊 import 國語臺員腔
from 語音合成.合音檔.舊閩南語句物件轉合成標籤 import 舊閩南語句物件轉合成標籤
from 資料庫.欄位資訊 import 偏泉優勢音腔口
from 資料庫.欄位資訊 import 混合優勢音腔口
from 資料庫.欄位資訊 import 大埔腔
from 資料庫.欄位資訊 import 海陸腔
from 資料庫.欄位資訊 import 四縣腔
from 資料庫.欄位資訊 import 饒平腔
from 資料庫.欄位資訊 import 詔安腔
from 語音合成.合音檔.句物件轉合成標籤 import 句物件轉合成標籤
from 資料庫.欄位資訊 import 閩南語
from 字詞組集句章.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音
from 語音合成.合音檔.標仔轉音檔 import 標仔轉音檔
from 翻譯.翻譯者 import 翻譯者
from 資料庫.欄位資訊 import 客語
from 語音合成.合音檔.調音盒 import 調音盒
from 服務架設.合成揀字 import 合成揀字

class 翻譯合成服務(連線控制器):
	標音工具 = Pyro4.Proxy("PYRONAME:內部自動標音")
	翻譯 = 翻譯者()
	揀字 = 合成揀字()
	舊閩南語合成標籤工具 = 舊閩南語句物件轉合成標籤()
	合成標籤工具 = 句物件轉合成標籤()
	轉音檔 = 標仔轉音檔()
	音盒 = 調音盒()
	袂前遺的腔口=偏漳優勢音腔口 # bue7 tsian5 i1 e5 khiunn1 khau2
	
	腔模型 = {偏漳優勢音腔口:'HTSLSPanAll.htsvoice', 偏泉優勢音腔口:'HTSLSPanAll.htsvoice',
		混合優勢音腔口:'HTSLSPanAll.htsvoice',
		四縣腔:'HakkaSi3.htsvoice', 海陸腔:'HakkaHai2.htsvoice', 大埔腔:'HakkaTua7.htsvoice',
		饒平腔:'HakkaPhing5.htsvoice', 詔安腔:'HakkaAn1.htsvoice', }
	腔放送進度 = {偏漳優勢音腔口:1.0, 偏泉優勢音腔口:1.0,
		混合優勢音腔口:1.0,
		四縣腔:1.0, 海陸腔:1.05, 大埔腔:1.6,
		饒平腔:1.02, 詔安腔:1.02, }
	def 服務(self):
		查詢字串 = self.連線路徑()
		if 查詢字串.endswith('.wav'):
			查詢字串 = 查詢字串[:-4]
		切開資料 = 查詢字串.split('/', 2)
		原來腔口=國語臺員腔
		查詢腔口 = None
		查詢語句 = None
		集選擇 = []
		if len(切開資料) == 3:
			查詢腔口, 集選擇字串, 查詢語句 = 切開資料
			集選擇 = self.看集選擇(集選擇字串)
		if not self.腔口有支援無(查詢腔口):
			查詢腔口 = self.袂前遺的腔口
			查詢語句 = 查詢字串
		章物件 = self.標音工具.語句斷詞標音(原來腔口, 查詢語句)
		翻譯了章物件 = self.翻譯.翻譯章物件(原來腔口, 查詢腔口, 章物件)
		揀好章物件 = self.揀字.揀(翻譯了章物件, 集選擇)
		全部標仔 = self.章物件轉標仔(查詢腔口, 揀好章物件)
		音檔 = self.標仔合音檔(查詢腔口, 全部標仔)
		調好音 = self.音標調音(查詢腔口, 音檔)
		self.送出連線成功資訊('audio/x-wav')
		self.送出位元資料(調好音)
		return
	def 看集選擇(self, 集選擇字串):
		集選擇 = []
		for 選擇 in 集選擇字串.split(','):
			if 選擇.isdigit():
				集選擇.append(int(選擇))
		return 集選擇
	def 腔口有支援無(self, 查詢腔口):
		return self.標音工具.有支援無(查詢腔口)

	# 等新閩南語做好，才做伙整合到語音合成
	def 章物件轉標仔(self, 查詢腔口, 章物件):
		全部標仔 = []
		for 句物件 in 章物件.內底句:
			if 查詢腔口.startswith(閩南語):
				標仔 = self.舊閩南語合成標籤工具.句物件轉標籤(句物件)
			else:
				標仔 = self.合成標籤工具.句物件轉標籤(臺灣客家話拼音, 句物件)
			if len(全部標仔) > 0:
				全部標仔 = 全部標仔[:-1]
			全部標仔.extend(標仔)
		return 全部標仔
	def 標仔合音檔(self, 查詢腔口, 標仔):
		模型 = self.腔模型[查詢腔口]
		速度 = self.腔放送進度[查詢腔口]
		音檔 = self.轉音檔.合成(模型, 速度, 標仔)
		return 音檔
	def 音標調音(self, 查詢腔口, 音檔):
		if 查詢腔口.startswith(閩南語):
			調好音 = self.音盒.篩雜訊(音檔)
		elif 查詢腔口.startswith(客語):
			調好音 = self.音盒.篩懸音(音檔, 6000)
		else:
			調好音 = 音檔
		return 調好音

if __name__ == '__main__':
	Pyro4.config.SERIALIZER = 'pickle'
	try:
		server = HTTPServer(('localhost', 8004), 翻譯合成服務)
		print ('服務啟動！！')
		server.serve_forever()
	except KeyboardInterrupt:
		print ('^C received, shutting down server')
		server.socket.close()
