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
import Pyro4
from 服務架設.翻譯合成服務 import 翻譯合成服務

class 自動標音服務(翻譯合成服務):
	def 服務(self):
		查詢字串 = self.連線路徑()
		切開資料 = 查詢字串.split('/', 1)
		查詢腔口 = None
		查詢語句 = None
		if len(切開資料) == 2:
			查詢腔口, 查詢語句 = 切開資料
		if not self.腔口有支援無(查詢腔口):
			查詢腔口 = self.袂前遺的腔口
			查詢語句 = 查詢字串
		標音結果 = self.標音工具.語句標音(查詢腔口, 查詢語句)
		self.送出連線成功資訊()
		self.送出字串資料(標音結果)
		return

if __name__ == '__main__':
	Pyro4.config.SERIALIZER = 'pickle'
	try:
		server = HTTPServer(('localhost', 8001), 自動標音服務)
		print ('服務啟動！！')
		server.serve_forever()
	except KeyboardInterrupt:
		print ('^C received, shutting down server')
		server.socket.close()
