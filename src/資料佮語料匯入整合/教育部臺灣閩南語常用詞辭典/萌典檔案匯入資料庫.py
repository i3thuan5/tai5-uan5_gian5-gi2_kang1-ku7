
from 資料庫.資料庫連線 import 資料庫連線
import urllib.request
import json

class 萌典檔案匯入資料庫:
	資料庫名 = '教育部臺灣閩南語常用詞辭典'
	清資料庫指令 = ('DELETE FROM "{0}"."{1}" ')
	加資料指令 = ('INSERT INTO "{0}"."{1}" ({2})' +
			'VALUES ({3})')
	def __init__(self):
		self.匯華語對照表()
		self.匯異用字表()
	def 匯華語對照表(self):
		表格名 = '華語對照表'
		清資料庫 = self.清資料庫指令.format(self.資料庫名, 表格名)
		print(清資料庫)
		資料庫連線.execute(清資料庫)
		欄位 = ['"主編號"', '"華語"']
		網址 = 'https://raw.github.com/g0v/moedict-data-twblg/master/x-%E8%8F%AF%E8%AA%9E%E5%B0%8D%E7%85%A7%E8%A1%A8.csv'
		資料 = urllib.request.urlopen(網址)
		for 一逝 in 資料.read().decode("utf8").split('\n')[1:]:
			一逝 = 一逝.strip()
			if 一逝 == '':
				continue
			華語, 詞條編號, 詞條名稱 = 一逝.split(',')
			華語 = "'{0}'".format(華語)
			加資料 = self.加資料指令.format(
				self.資料庫名, 表格名, ','.join(欄位), ','.join([詞條編號, 華語]))
			print(加資料)
			資料庫連線.execute(加資料)
	def 匯異用字表(self):
		表格名 = '異用字表'
		清資料庫 = self.清資料庫指令.format(self.資料庫名, 表格名)
		print(清資料庫)
		資料庫連線.execute(清資料庫)
		欄位 = ['"主編號"', '"異用字"']
		網址 = 'https://raw.github.com/g0v/moedict-data-twblg/master/x-%E7%95%B0%E7%94%A8%E5%AD%97.json'
		字串資料 = urllib.request.urlopen(網址)
		表資料 = json.loads(字串資料.read().decode("utf8"))
		for 主編號, 異用字 in 表資料.items():
			異用字 = "'{0}'".format(','.join(異用字))
			加資料 = self.加資料指令.format(
				self.資料庫名, 表格名, ','.join(欄位), ','.join([主編號, 異用字]))
			print(加資料)
			資料庫連線.execute(加資料)

if __name__ == '__main__':
	萌典檔案匯入資料庫()
