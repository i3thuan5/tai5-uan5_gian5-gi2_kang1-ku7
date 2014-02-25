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
from 資料庫.資料庫連線 import 資料庫連線
from 字詞組集句章.解析整理工具.文章粗胚工具 import 文章粗胚工具
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.轉物件音家私 import 轉物件音家私
from 字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡
from 字詞組集句章.音標系統.閩南語.臺灣語言音標 import 臺灣語言音標
from 資料庫.欄位資訊 import 字詞
from 資料庫.欄位資訊 import 臺員
from 資料庫.整合.整合入言語 import 加文字佮版本
from 資料庫.欄位資訊 import 義近
from 資料庫.欄位資訊 import 會當替換
from 資料庫.整合.整合入言語 import 加關係
from 字詞組集句章.基本元素.公用變數 import 統一碼音標類
import unicodedata
'''
Created on 2013/3/3

@author: Ihc
'''

class 整理中的台語詞典07:
	揣攏總資料 = 資料庫連線.prepare('SELECT "識別碼","CHINESE","TAIWANESE","ForPA","TLPA" ' +
		'FROM "整理中的台語詞典"."整理中的台語詞典07" ORDER BY "識別碼" ASC')
	辭典名 = '整理中的台語詞典07'
	加到資料庫 = False

	粗胚工具 = 文章粗胚工具()
	分析器 = 拆文分析器()
	轉音家私 = 轉物件音家私()
	譀鏡 = 物件譀鏡()

	音轉字 = {'khiap4':'㾀','thai5':'刣', 'sui2':'媠', 'bai2':'䆀',
		'e5':'的',}
	def __init__(self):
		for 識別碼, CHINESE, TAIWANESE, ForPA , TLPA in self.揣攏總資料():
			try:
	# 			print(識別碼)
				漢羅 = self.粗胚工具.數字調英文中央加分字符號(TAIWANESE)
				詞物件 = self.分析器.產生對齊詞(漢羅, TLPA)
				self.共通用換做ＴＬＰＡ(詞物件)
				標準物件 = self.轉音家私.轉做標準音標(臺灣語言音標, 詞物件)
	# 			print(self.譀鏡.看型(標準物件), self.譀鏡.看音(標準物件),)
			except Exception as 錯誤:
# 				print(識別碼, CHINESE, TAIWANESE, ForPA , TLPA, 錯誤)
				pass
			else:
				有英文數字 = False
				for 字 in self.譀鏡.看型(標準物件):
					if unicodedata.category(字) in 統一碼音標類:
						有英文數字 = True
				if 有英文數字:
					print(self.譀鏡.看型(標準物件), self.譀鏡.看音(標準物件), CHINESE)
				if self.加到資料庫:
					閩流 = 加文字佮版本(self.辭典名, 字詞, '漢語族閩方言閩南語', 臺員, 89,
						self.譀鏡.看型(標準物件), self.譀鏡.看音(標準物件), '正常')
					國流 = 加文字佮版本(self.辭典名, 字詞, '漢語族官話方言北京官話臺灣腔', 臺員, 89,
						CHINESE, '', '正常')
					加關係(閩流, 國流, 義近, 會當替換)
					加關係(國流, 閩流, 義近, 會當替換)
	def 共通用換做ＴＬＰＡ(self,詞物件):
		for 字物件 in 詞物件.內底字:
			有英文數字 = False
			for 字 in 字物件.型:
				if unicodedata.category(字) in 統一碼音標類:
					有英文數字 = True
			if 有英文數字:
				字物件.型=字物件.音
				if 字物件.音 in self.音轉字:
					字物件.型=self.音轉字[字物件.音]
		return
if __name__ == '__main__':
	整理中的台語詞典07()
