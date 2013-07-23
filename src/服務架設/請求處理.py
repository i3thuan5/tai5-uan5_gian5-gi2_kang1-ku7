#Copyright Jon Berg , turtlemeat.com

import string,cgi,time
from os import curdir, sep
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
#import pri

class MyHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		try:
			if self.path.endswith(".html"):
				f = open(curdir + sep + self.path) #self.path has /test.html
#note that this potentially makes every file on your computer readable by the internet

				self.send_response(200)
				self.send_header('Content-type',	'text/html')
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
				return
			print(type("self.path="))
			print(type(self.path))
			print(type(self.path.encode()))
			self.send_response(200)
			self.send_header('Content-type',	'text/html')
			self.end_headers()
			self.wfile.write(("self.path="+urllib.parse.unquote(self.path)).encode())
			self.wfile.write("<br/>".encode(encoding='utf_8', errors='strict'))
			self.wfile.write(("hey, today is the"+ str(time.localtime()[7])).encode(encoding='utf_8', errors='strict') )
#			 self.wfile.write("hey, today is the" + str(time.localtime()[7]))
			self.wfile.write(("你好 day in the year " + str(time.localtime()[0])).encode())
			return
				
				
		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)
	


def main():
	try:
		server = HTTPServer(('', 8000), MyHandler)
		print ('started httpserver...')
		server.serve_forever()
	except KeyboardInterrupt:
		print ('^C received, shutting down server')
		server.socket.close()

if __name__ == '__main__':
	main()
