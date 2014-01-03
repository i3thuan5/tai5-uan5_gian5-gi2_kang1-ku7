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
import hashlib

class 轉做咱講工具:
	檔頭表=(
"""<?xml version="1.0" encoding="utf-8"?>
<lift
    version="0.13"
    producer="Palaso.DictionaryServices.LiftWriter 2.1.27.0">""")
	檔尾表="</lift>" 
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
	參考表=(
"""	<relation
		type="confer"
		ref="{0} {1}_{2}" />""")
	def 檔頭(self):
		return self.檔頭表
	def 檔尾(self):
		return self.檔尾表
	def 條目頭(self,臺語字音):
		臺語字,臺語音=臺語字音
		雜湊=self.條目雜湊資料(臺語字音)
		return self.條目頭表.format(臺語字,臺語音,雜湊)
	def 條目尾(self):
		return self.條目尾表
	def 條目雜湊資料(self,臺語字音):
		雜湊=hashlib.md5()
		雜湊.update((臺語字音[0]+臺語字音[1]).encode(encoding='utf_8', errors='strict'))
		return 雜湊.hexdigest()
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
		