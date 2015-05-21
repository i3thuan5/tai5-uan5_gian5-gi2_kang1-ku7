# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國103年 意傳文化科技
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
import xmlrpc.client


from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.翻譯.摩西工具.無編碼器 import 無編碼器
from 臺灣言語工具.基本元素.章 import 章
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔
from 臺灣言語工具.基本元素.組 import 組
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.基本元素.句 import 句

class 摩西用戶端():
	網址格式 = "http://{0}:{1}/{2}"
	未知詞記號 = '|UNK|UNK|UNK'
	def __init__(self, 位址='localhost', 埠='8080', 路徑='RPC2', 編碼器=無編碼器()):
		網址 = self.網址格式.format(位址, 埠, 路徑)
		self.主機 = xmlrpc.client.ServerProxy(網址)
		self.編碼器 = 編碼器
		
		self.分析器 = 拆文分析器()
		self.譀鏡 = 物件譀鏡()
		self.網仔 = 詞物件網仔()
	def 翻譯(self, 物件):
		if isinstance(物件, 章):
			return self._翻譯章物件(物件)
		return self._翻譯句物件(物件)
	def _翻譯章物件(self, 來源章物件):
		結果章物件 = 章()
		來源新結構章物件 = 章()
		總分=0
		for 來源句物件 in 來源章物件.內底句:
			結果句物件, 來源新結構句物件,分數=self._翻譯句物件(來源句物件)
			結果章物件.內底句.append(結果句物件)
			來源新結構章物件.內底句.append(來源新結構句物件)
			總分+=分數
		return 結果章物件,來源新結構章物件,總分
	def _翻譯句物件(self, 來源句物件):
		參數 = {
			"text":self.編碼器.編碼(self.譀鏡.看分詞(來源句物件)),
			"align":"true",
			"report-all-factors":"true",
			'nbest':1,
			}
		翻譯結果 = self.主機.translate(參數)
		翻譯結果物件 = 翻譯結果['nbest'][0]
		
		翻譯結果語句 = self.編碼器.解碼(翻譯結果物件['text'])
		結果詞物件陣列 = []
		for 分詞 in 翻譯結果語句.split('  ')[:-1]:
			if 分詞.endswith(self.未知詞記號):
				詞物件 = self.分析器.轉做詞物件(分詞[:-len(self.未知詞記號)])
				詞物件.屬性 = {'未知詞':'是'}
			else:
				詞物件 = self.分析器.轉做詞物件(分詞)
			結果詞物件陣列.append(詞物件)
			
		翻譯結果對齊 = 翻譯結果物件['align']
		結果對齊陣列, 來源對齊陣列 = self._對齊索引轉陣列(翻譯結果對齊, len(結果詞物件陣列))
		
		結果句物件 = self._詞陣列照對齊轉句物件(結果詞物件陣列, 結果對齊陣列)
		來源新結構句物件 = self._詞陣列照對齊轉句物件(self.網仔.網出詞物件(來源句物件), 來源對齊陣列)
		
		return 結果句物件, 來源新結構句物件, 翻譯結果物件['totalScore']
	def _對齊索引轉陣列(self, 對齊索引陣列, 結果長度):
		結果陣列 = []
		來源陣列 = []
		頂一个結果 = 0
		for 對齊索引 in 對齊索引陣列:
			這个結果 = 對齊索引['tgt-start']
			結果陣列.append((頂一个結果, 這个結果))
			來源陣列.append((對齊索引['src-start'], 對齊索引['src-end'] + 1))
			頂一个結果 = 這个結果
		結果陣列.append((頂一个結果, 結果長度))
		return 結果陣列[1:], 來源陣列
	def _詞陣列照對齊轉句物件(self, 詞陣列, 對齊陣列):
		集物件 = 集()
		for 頭, 尾 in 對齊陣列:
			集物件.內底組.append(組(詞陣列[頭:尾]))
			if 尾-頭==1 and hasattr(詞陣列[頭],'屬性'):
				集物件.內底組[-1].屬性 = {'未知詞':'是'}
		句物件 = 句()
		句物件.內底集.append(集物件)
		return 句物件		

if __name__ == '__main__':
	編碼器 = 語句編碼器()
	用戶端 = 摩西用戶端('localhost', '8103',)
	語句 = "他 和 我 要 去 吃 飯 。"
	結果 = 用戶端.翻譯(語句, 另外參數={'nbest':1})
# 	print(結果['nbest'][0]['hyp'].split())
	if 'align' in 結果:
		print("Phrase alignments:")
		aligns = 結果['align']
		for align in aligns:
			print("%s,%s,%s" % (align['tgt-start'], align['src-start'], align['src-end']))
	print(結果)
