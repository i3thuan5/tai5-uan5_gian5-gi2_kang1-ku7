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
from 剖析相關工具.自設剖析工具 import 自設剖析工具
from 系統整合.翻譯整合 import 翻譯整合

class 國閩翻譯服務(連線控制器):
	剖析工具 = 自設剖析工具()
	整合工具 = 翻譯整合()
	def do_GET(self):
		try:
			self.送出連線成功資訊()
			#共上頭前的「/」提掉
			查詢語句 = self.連線路徑()[1:]
			剖析結果字串集 = self.剖析工具.剖析(查詢語句)
			翻譯結果 = self.整合工具.國閩翻譯(剖析結果字串集)
			self.輸出(翻譯結果)
			return
		except IOError:
			self.send_error(404, 'File Not Found: %s' % self.path)



if __name__ == '__main__':
	try:
		server = HTTPServer(('localhost', 8000), 國閩翻譯服務)
		print ('started httpserver...')
		server.serve_forever()
	except KeyboardInterrupt:
		print ('^C received, shutting down server')
		server.socket.close()
