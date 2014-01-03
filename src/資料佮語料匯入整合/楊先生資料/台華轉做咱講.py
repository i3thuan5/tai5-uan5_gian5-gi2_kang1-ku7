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
from 資料庫.資料庫連線 import 資料庫連線
from 資料庫.欄位資訊 import 字詞
from 資料庫.整合.整合入言語 import 加文字佮版本
from 資料庫.整合.整合入言語 import 加關係
from 資料庫.欄位資訊 import 義近
from 資料庫.欄位資訊 import 會當替換
from 資料庫.整合.教育部閩南語常用詞辭典 import 設定詞性
from 資料庫.欄位資訊 import 臺員
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.轉物件音家私 import 轉物件音家私
from 字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡
from 字詞組集句章.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
import hashlib

class 整合台華:
	揣台華資料 = 資料庫連線.prepare('SELECT "ID","台語羅馬字","台語羅馬字2","台語漢字","華語對譯","英文","pos_h" ' + 
		'FROM "楊允言先生資料"."台華" ORDER BY "ID"')
	揣台華資料 = 資料庫連線.prepare('SELECT "ID","台語羅馬字","台語羅馬字2","台語漢字","華語對譯","英文","pos_h" ' + 
		'FROM "楊允言先生資料"."台華" WHERE "ID"= 658 ORDER BY "ID"')
	辭典名 = '楊允言台華辭典'
	
	初胚工具 = 文章初胚工具()
	分析器 = 拆文分析器()
	轉音家私 = 轉物件音家私()
	譀鏡 = 物件譀鏡()
	def __init__(self):
		print(self.檔頭())
		for ID, 台語羅馬字, 台語羅馬字2, 台語漢字, 華語對譯, 英文, pos_h in self.揣台華資料():
			try:
# 				print(ID, 台語羅馬字, 台語羅馬字2, 台語漢字, 華語對譯, 英文, pos_h)
				臺語資料 = []
				# 來源, 種類, 腔口, 地區, 年代, 型體, 音標, 版本
				for 台語音 in [台語羅馬字, 台語羅馬字2]:
					音 = 台語音.strip()
					if 音 != '':
						漢字解析結果 = self.初胚工具.建立物件語句前處理減號(教會羅馬字音標, 台語漢字)
						音解析結果 = self.初胚工具.建立物件語句前處理減號(教會羅馬字音標, 音)
						組物件 = self.分析器.產生對齊組(漢字解析結果, 音解析結果)
						標準物件 = self.轉音家私.轉做標準音標(教會羅馬字音標, 組物件)
						# 來源, 種類, 腔口, 地區, 年代, 型體, 音標, 版本
						臺語資料.append((	self.譀鏡.看型(標準物件), self.譀鏡.看音(標準物件)))
				國語資料=[]
				for 國語字 in 華語對譯.strip().split(';'):
					if 國語字 != '':
						國語資料.append(國語字)
				英文資料=[]
				for 英文字 in 英文.strip().split(';'):
					if 英文字 != '':
						英文資料.append(英文字)
# 				print(文字資料)
			except Exception as 錯誤:
# 				print(ID, 台語羅馬字, 台語羅馬字2, 台語漢字, 華語對譯, 英文, pos_h, 錯誤)
				pass
			else:
				詞性 = pos_h.strip()
				條目頭=self.條目頭(臺語資料[0])
				print(條目頭)
				if 詞性 == '':
					資料=self.一个意思(None,
						'、'.join(國語資料)+'。',','.join(英文資料)+'.')
					print(資料)
				else:
					for 孤單詞性 in 詞性:
						if 孤單詞性 != '':
							資料=self.一个意思(孤單詞性,
								'、'.join(國語資料)+'。',','.join(英文資料)+'.')
							print(資料)
				條目尾=self.條目尾()
				print(條目尾)
				for 後壁資料 in 臺語資料[1:]:
					條目頭=self.條目頭(後壁資料)
					print(條目頭)
					參考=self.參考別人(臺語資料[0])
					print(參考)
					條目尾=self.條目尾()
					print(條目尾)
		print(self.檔尾())
					
				
	def 檔頭(self):
		return self.檔頭表
	def 檔尾(self):
		return self.檔尾表
	def 條目雜湊資料(self,臺語字音):
		雜湊=hashlib.md5()
		雜湊.update((臺語字音[0]+臺語字音[1]).encode(encoding='utf_8', errors='strict'))
		return 雜湊.hexdigest()
	def 條目頭(self,臺語字音):
		臺語字,臺語音=臺語字音
		雜湊=self.條目雜湊資料(臺語字音)
		return self.條目頭表.format(臺語字,臺語音,雜湊)
	def 一个意思(self,詞性,中文,英文):
		詞=''
		中=''
		英=''
		if 詞性!=None:
			詞=self.詞性表.format(詞性)
		if 中文!=None:
			中=self.中文表.format(中文)
		if 英文!=None:
			英=self.英文表.format(英文)
		意思=self.意思表.format(詞,中,英)
		雜湊=hashlib.md5()
		雜湊.update(意思.encode(encoding='utf_8', errors='strict'))
		雜湊資料=雜湊.hexdigest()
		return 意思.format(雜湊資料)
	def 參考別人(self,第一人):
		臺語字,臺語音=第一人
		雜湊=self.條目雜湊資料(第一人)
		return self.參考表.format(臺語字,臺語音,雜湊)
		
	檔頭表=(
"""<?xml version="1.0" encoding="utf-8"?>
<lift
    version="0.13"
    producer="Palaso.DictionaryServices.LiftWriter 2.1.27.0">""")
	檔尾表="</lift>" 
	參考表=(
"""	<relation
		type="confer"
		ref="{0} {1}_{2}" />""")
	def 條目尾(self):
		return self.條目尾表
	條目頭表=(	
"""	<entry
		id="{0} {1}_{2}"
		dateCreated="2013-12-16T13:53:11Z"
		dateModified="2013-12-16T13:56:48Z"
		guid="{2}">
		<lexical-unit>
			<form
				lang="nan">
				<text>{0} {1}</text>
			</form>
		</lexical-unit>""")
	條目尾表="	</entry>"
	意思表=(
"""	<sense
		id="{{0}}">
		<definition>
{0}
{1}
{2}
		</definition>
	</sense>""")
	詞性表=(
"""		<grammatical-info
			value="{0}" />""")
	中文表=(
"""	<form
		lang="cmn">
		<text>{0}</text>
	</form>""")
	英文表=(
"""	<form
		lang="en">
		<text>{0}</text>
	</form>""")
		
if __name__ == '__main__':
	整合台華()
