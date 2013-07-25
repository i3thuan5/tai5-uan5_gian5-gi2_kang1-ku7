
from http.server import HTTPServer
from 服務架設.連線控制器 import 連線控制器
from 剖析相關工具.自設剖析工具 import 自設剖析工具
from 系統整合.翻譯整合 import 翻譯整合

class 國閩翻譯服務(連線控制器):
	剖析工具 = 自設剖析工具()
	整合工具 = 翻譯整合()
	def do_GET(self):
		try:
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
		server = HTTPServer(('', 8000), 國閩翻譯服務)
		print ('started httpserver...')
		server.serve_forever()
	except KeyboardInterrupt:
		print ('^C received, shutting down server')
		server.socket.close()
