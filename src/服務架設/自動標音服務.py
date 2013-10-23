
from http.server import HTTPServer
from 服務架設.連線控制器 import 連線控制器
from 資料庫.欄位資訊 import 偏漳優勢音腔口
from 資料庫.欄位資訊 import 偏泉優勢音腔口
from 資料庫.欄位資訊 import 混合優勢音腔口
from 斷詞標音.閩南語標音整合 import 閩南語標音整合
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.綜合標音.句綜合標音 import 句綜合標音
from 字詞組集句章.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音

class 自動標音服務(連線控制器):
	閩南語偏漳標音 = 閩南語標音整合(偏漳優勢音腔口)
	閩南語偏泉標音 = 閩南語標音整合(偏泉優勢音腔口)
	閩南語混合標音 = 閩南語標音整合(混合優勢音腔口)
	支援腔口 = {偏漳優勢音腔口:(閩南語偏漳標音,閩南語字綜合標音),
		偏泉優勢音腔口:(閩南語偏泉標音,閩南語字綜合標音),
		混合優勢音腔口:(閩南語混合標音,閩南語字綜合標音),
		}
	def do_GET(self):
		try:
			self.送出連線成功資訊()
			# 共上頭前的「/」提掉
			查詢語句 = self.連線路徑()[1:]
			切開資料 = 查詢語句.split('/', 1)
			查詢腔口 = None
			翻譯資料 = None
			if len(切開資料) == 2:
				查詢腔口, 翻譯資料 = 切開資料
			if 查詢腔口 not in self.支援腔口:
				查詢腔口 = 偏漳優勢音腔口
				翻譯資料 = 查詢語句
			標音工具, 字綜合標音 = self.支援腔口[查詢腔口]
			章物件=標音工具.產生標音結果(翻譯資料)
			集陣列=[]
			for 句物件 in 章物件.內底句:
				for 集物件 in 句物件.內底集:
					集陣列.append(集物件)

			標音句 = 句綜合標音(字綜合標音, 句(集陣列))
# 			print(標音句.綜合標音佮詞組陣列)
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
