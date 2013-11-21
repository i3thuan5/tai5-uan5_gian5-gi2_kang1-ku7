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

class 翻譯國語服務(連線控制器):
	標音工具 = Pyro4.Proxy("PYRONAME:內部自動標音")
	查資料=查資料庫()
	譀鏡=物件譀鏡()
	def do_GET(self):
		try:
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
			章物件 = self.標音工具.語句斷詞標音(查詢腔口, 查詢語句)
			句陣列=[]
			for 句物件 in 章物件.內底句:
				集陣列=[]
				for 集物件 in 句物件.內底集:
					組陣列=[]
					for 組物件 in 集物件.內底組:
# 						詞陣列=[]
						for 詞物件 in 組物件.內底詞:
							組陣列.extend(
								self.查資料.型體翻譯著(國語臺員腔,
								self.譀鏡.看型(詞物件),查詢腔口))
# 						組陣列.append(組(詞陣列))
					集陣列.append(集(組陣列))
				句陣列.append(句(集陣列))
			翻譯了章物件=章(句陣列)
			標音結果 = 句綜合標音(閩南語字綜合標音, 翻譯了章物件)			
			self.送出連線成功資訊()
			self.輸出(標音結果.轉json格式())
		except Pyro4.errors.NamingError as 錯誤:
			self.送出連線錯誤資訊(503)
			self.輸出('暫時停止服務！！')
			print('內部自動標音關去矣！！')
			raise 錯誤
		except TypeError:
			self.送出連線錯誤資訊(503)
			self.輸出('暫時停止服務！！')
			print("Pyro traceback:")
			print("".join(Pyro4.util.getPyroTraceback()))
		except Exception as 錯誤:
			self.送出連線錯誤資訊(503)
			self.輸出('暫時停止服務！！')
			raise 錯誤
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