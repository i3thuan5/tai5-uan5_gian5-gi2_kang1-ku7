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
from 字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡
from 資料庫.欄位資訊 import 國語臺員腔
from 資料庫.查資料庫 import 查資料庫
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.基本元素.章 import 章
from 字詞組集句章.綜合標音.句綜合標音 import 句綜合標音
from 字詞組集句章.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 翻譯.翻譯者 import 翻譯者

class 翻譯國語服務(連線控制器):
	標音工具 = Pyro4.Proxy("PYRONAME:內部自動標音")
	查資料 = 查資料庫()
	譀鏡 = 物件譀鏡()
	翻譯=翻譯者()
	def 服務(self):
		# 共上頭前的「/」提掉
		查詢字串 = self.連線路徑()[1:]
		切開資料 = 查詢字串.split('/', 1)
		查詢腔口 = None
		查詢語句 = None
		if len(切開資料) == 2:
			查詢腔口, 查詢語句 = 切開資料
		if not self.標音工具.有支援無(查詢腔口):
			查詢腔口 = 偏漳優勢音腔口
			查詢語句 = 查詢字串
		章物件 = self.標音工具.語句斷詞標音(國語臺員腔, 查詢語句)
		翻譯了章物件=self.翻譯.翻譯章物件(國語臺員腔, 查詢腔口, 章物件)
		print(self.標音工具.物件綜合標音(
			查詢腔口,翻譯了章物件))
		標音結果 = self.標音工具.物件綜合標音(
			查詢腔口, 翻譯了章物件)
		self.送出連線成功資訊()
		self.輸出(標音結果)
		return

if __name__ == '__main__':
	Pyro4.config.SERIALIZER = 'pickle'
	try:
		server = HTTPServer(('localhost', 8002), 翻譯國語服務)
		print ('服務啟動！！')
		server.serve_forever()
	except KeyboardInterrupt:
		print ('^C received, shutting down server')
		server.socket.close()
