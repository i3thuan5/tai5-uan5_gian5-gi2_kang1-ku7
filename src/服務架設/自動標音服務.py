
from http.server import HTTPServer
from 服務架設.連線控制器 import 連線控制器
from 標音系統整合.標音整合 import 標音整合
from 標音系統整合.句綜合標音 import 句綜合標音
from 標音系統整合.閩南語綜合標音 import 閩南語字詞綜合標音

class 自動標音服務(連線控制器):
	def do_GET(self):
		try:
			self.送出連線成功資訊()
			# 共上頭前的「/」提掉
			查詢語句 = self.連線路徑()[1:]
			標音 = 標音整合('漢語族閩方言閩南語偏漳優勢音')
			詞標音 = 標音.產生標音結果(查詢語句, 標音.全部)
		# 	print(詞標音)
			標音句 = 句綜合標音(詞標音, 閩南語字詞綜合標音)
			self.輸出(標音句.綜合標音佮詞組陣列)
			return
		except IOError:
			self.send_error(404, 'File Not Found: %s' % self.path)



if __name__ == '__main__':
	try:
		server = HTTPServer(('localhost', 8001), 自動標音服務)
		print ('服務啟動！！')
		server.serve_forever()
	except KeyboardInterrupt:
		print ('^C received, shutting down server')
		server.socket.close()
