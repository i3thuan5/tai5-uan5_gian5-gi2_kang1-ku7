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

from 資料佮語料匯入整合.客語能力認證資訊區.能力認證網頁剖析工具 import 能力認證網頁剖析工具
from 資料佮語料匯入整合.信望愛台語語料庫.剖析信望愛語料庫表格 import 剖析信望愛語料庫表格
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡
from 字詞組集句章.解析整理工具.轉物件音家私 import 轉物件音家私
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具

class 信望愛語料庫資料處理():
	初胚工具 = 文章初胚工具()
	分析器 = 拆文分析器()
	家私 = 轉物件音家私()
	譀鏡 = 物件譀鏡()
	def 處理(self, 資料):
		組陣列 = []
		for 筆 in 資料:
			try:
				音, 型 = 筆.rsplit(' ', 1)
				型 = self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 型)
				音 = self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 音)
				組物件 = self.分析器.產生對齊組(型, 音)
				標準組物件 = self.家私.轉做標準音標(臺灣閩南語羅馬字拼音, 組物件)
				組陣列.append(標準組物件)
			except Exception as 錯誤:
				print(筆, 錯誤)
		return 組陣列

if __name__ == "__main__":
	網頁剖析工具 = 剖析信望愛語料庫表格(strict = False)
	資料 = 網頁剖析工具.剖析信望愛語料庫檔案('/home/Ihc/tmpfs/nan/nan.lift')
	print(資料[:10])
	語料庫資料處理 = 信望愛語料庫資料處理()
	組陣列 = 語料庫資料處理.處理(資料)
	print(組陣列[:10])
