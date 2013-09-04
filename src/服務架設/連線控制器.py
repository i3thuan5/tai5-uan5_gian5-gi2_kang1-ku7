
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib

class 連線控制器(BaseHTTPRequestHandler):
	def 輸出(self, 資料):
		self.wfile.write(str(資料).encode(encoding = 'utf_8', errors = 'strict'))
	def 連線路徑(self):
		return urllib.parse.unquote(self.path)
	def 送出連線成功資訊(self):
		self.send_response(200)
		self.send_header('Content-type', 	'text/html')
		self.end_headers()

if __name__ == '__main__':
	try:
		server = HTTPServer(('', 8000), 連線控制器)
		print ('started httpserver...')
		server.serve_forever()
	except KeyboardInterrupt:
		print ('^C received, shutting down server')
		server.socket.close()
