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
from 資料庫.欄位資訊 import 國語臺員腔
from 資料庫.欄位資訊 import 語句
from 資料庫.整合.教育部閩南語常用詞辭典 import 教育部閩南語辭典名
from 資料庫.整合.教育部閩南語常用詞辭典 import 教育部閩南語辭典地區
from 資料庫.整合.教育部閩南語常用詞辭典 import 教育部閩南語辭典年代
from 資料庫.欄位資訊 import 版本正常
from 資料庫.整合.整合入言語 import 加文字佮版本
from 資料庫.整合.整合入言語 import 揣文字上大流水號
from 資料庫.整合.教育部閩南語常用詞辭典 import 用釋義揣例句
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.轉物件音家私 import 轉物件音家私
from 資料庫.整合.整合入言語 import 用流水號揣文字
from 資料庫.欄位資訊 import 閩南語
from 資料庫.欄位資訊 import 義近
from 資料庫.欄位資訊 import 袂當替換
from 資料庫.整合.整合入言語 import 加關係
from 資料庫.整合.教育部閩南語常用詞辭典 import 設定詞性
from 資料庫.整合.整合入言語 import 揣關係上大流水號
from 資料庫.整合.教育部閩南語常用詞辭典 import 詞性對照表
from 資料庫.整合.教育部閩南語常用詞辭典 import 文字無音設定
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤
from 資料庫.整合.教育部閩南語常用詞辭典 import 用流水號揣腔口
from 資料庫.欄位資訊 import 文字組合符號
from 資料庫.欄位資訊 import 會當替換
from 資料庫.整合.整合入言語 import 設定文字組合
from 資料庫.整合.教育部閩南語常用詞辭典 import 主編號揣釋義
from 字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡
from 字詞組集句章.基本元素.公用變數 import 分字符號
from 字詞組集句章.基本元素.公用變數 import 分詞符號
from 資料庫.整合.教育部閩南語常用詞辭典 import 揣例句
from 資料佮語料匯入整合.教育部臺灣閩南語常用詞辭典.教育部閩南語辭典工具 import 教育部閩南語辭典工具

class 整合釋義佮例句:
	辭典工具=教育部閩南語辭典工具()
	初胚工具 = 文章初胚工具()
	分析器 = 拆文分析器()
	轉音家私 = 轉物件音家私()
	譀鏡 = 物件譀鏡()
	顯示資料=False
	def 建立釋義(self, 主編號, 流水號集):
		來源資料 = []
		for 釋義編號, 主編號, 義項順序, 詞性, 釋義 in 主編號揣釋義(主編號):
			print(釋義編號)
			if 主編號 == 5843:
				if 義項順序 == 0:
					if 釋義 == '麻雀。見【粟鳥仔】<font class=tlsound>tshik-tsiáu-á </font>條。':
						釋義 = '麻雀。見【粟鳥仔】tshik-tsiáu-á 條。'
				else:
					continue
		
			加文字佮版本(教育部閩南語辭典名, 語句, 國語臺員腔, 教育部閩南語辭典地區,
				教育部閩南語辭典年代, 釋義, '', 版本正常)
			釋義流水號 = 揣文字上大流水號()
			來源資料.append((釋義流水號, 主編號))
			例句資料 = 用釋義揣例句(釋義編號)
			臺語流水號集 = 流水號集  # 用主碼號揣流水號(主編號)
			if self.顯示資料:
				print('臺語流水號集', 臺語流水號集)
			for 例句, 標音, 例句翻譯 in 例句資料:
				if 例句翻譯 == '':
					例句翻譯 = 例句
				加文字佮版本(教育部閩南語辭典名, 語句, 國語臺員腔, 教育部閩南語辭典地區,
					教育部閩南語辭典年代, 例句翻譯, '', 版本正常)
				國語例句流水號 = 揣文字上大流水號()
				來源資料.append((國語例句流水號, 主編號))
		
		
				if 標音[0].isupper():
					種類 = '語句'
				else:
					種類 = '字詞'
		
				例句 = self.辭典工具.共造字換做統一碼表示法(例句)
				組字式型 = self.初胚工具.符號邊仔加空白(例句).strip()
				標音 = self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 標音)
				標音 = self.初胚工具.符號邊仔加空白(標音).strip()
				
				換字表 = {'且慢一下':'且慢一下。',
					
					}
				if 組字式型 in 換字表:
					組字式型 = 換字表[組字式型]
					
				換音表 = {'Sing-lí-lâng tshe-jī tsa̍p-la̍k lóng ū pài Thóo-tī-kong .':
					'Sing-lí-lâng tshe-jī 、 tsa̍p-la̍k lóng ū pài Thóo-tī-kong .',
					'Tiūnn-ḿ tō sī guán bóo ê lāu-bú .':
					'「 Tiūnn-ḿ 」 tō sī guán bóo ê lāu-bú .',
					'Nā siūnn-tio̍h tsit tsân tāi-tsì guá tō hué-tuā .':
					'Nā siūnn-tio̍h tsit tsân tāi-tsì ， guá tō hué-tuā .',
					'Kóo-tsá sî-tāi , Gio̍k-tsénn kiò-tsò Ta-pa-nî .':
					'Kóo-tsá sî-tāi , 「 Gio̍k-tsénn 」 kiò-tsò 「 Ta-pa-nî 」 .',
					'Tsit tè tinn-kué tshiám tsi̍t-ē suah nah-0lo̍h-khì .':
					'Tsit tè tinn-kué tshiám tsi̍t-ē ， suah nah-0lo̍h-khì .',
					'Lí kah m̄ tah-ìng , gáun tsí-hó tshuē pa̍t-lâng .':
					'Lí kah m̄ tah-ìng , guán tsí-hó tshuē pa̍t-lâng .',
					'Kah hiah sue , ē khì tú-tio̍h tsit kháun tāi-tsì ?':
					'Kah hiah sue , ē khì tú-tio̍h tsit khuán tāi-tsì ?',
					'hô sū ?':'hô sū',
					'Guá khuànn-kuè tsiânn tsē āu-bú khóo-to̍k tsîng-lâng-kiánn ê tāi-tsì .':
				'Guá khuànn-kuè tsiânn tsē 「 āu-bú khóo-to̍k tsîng-lâng-kiánn 」 ê tāi-tsì .',
				'Tshuan-san-kah sio̍k-miâ kiò-tsò lâ-lí .':
				'Tshuan-san-kah sio̍k-miâ kiò-tsò 「 lâ-lí 」 .',
				'」 Sio̍k-gí-uē kóng : " Tsi̍t hó kah tsi̍t bái , bô nn̄g hó sio pâi . "':
				'Sio̍k-gí-uē kóng : 「 Tsi̍t hó kah tsi̍t bái , bô nn̄g hó sio pâi . 」',
				'tsio pó-hiám .':'tsio pó-hiám',
				'Kìnn-tio̍h lâng ài sio-tsioh-mn̄g tsiah ū lé-māu .':
				'Kìnn-tio̍h lâng ài sio-tsioh-mn̄g ， tsiah ū lé-māu .',
				'Tsoh-sit-lâng lóng ài khò thinn-kong-peh-0á tsiah ū tsia̍h-tshīng .':
				'Tsoh-sit-lâng lóng ài khò thinn-kong-peh-0á ， tsiah ū tsia̍h-tshīng .',
				'Tsit tè bah pōo bē nuā':
				'Tsit tè bah pōo bē nuā .',
					}
				if self.顯示資料:
					print(標音)
				if 標音 in 換音表:
					標音 = 換音表[標音]
					print('有換音',釋義編號)
					
				原音句物件 = self.分析器.產生對齊句(組字式型, 標音)
				標準句物件 = self.轉音家私.轉做標準音標(臺灣閩南語羅馬字拼音, 原音句物件)
				
				標準例句 = self.譀鏡.看型(標準句物件)
				標準標音 = self.譀鏡.看音(標準句物件)
				拍毋著換音表 = {
					'tong1-sun2':'tang1-sun2',
					}
				if 標準標音 in 拍毋著換音表:
					標準標音 = 拍毋著換音表[標準標音]
					print('拍毋著換音表',釋義編號)
				
				例句內底漢字 = None
				例句內底音標 = None
				查著資料 = []
				for 臺語流水號 in 臺語流水號集:
					文字資料 = 用流水號揣文字(臺語流水號)
					if 文字資料[2].startswith(閩南語):
						查著資料.append((文字資料[6], 文字資料[7]))
						if 文字資料[6] in 標準例句 and 文字資料[7] in 標準標音:
							try:
								# 共句切開
								漢字頭前, 漢字後壁 = 標準例句.split(文字資料[6], 1)
								音標頭前, 音標後壁 = 標準標音.split(文字資料[7], 1)
								# 小等一下。 sio2-tan2-0tsit8-e7 . 小等 sio2-tan2-0 。  .
								self.分析器.產生對齊句(漢字頭前, 音標頭前.strip(分字符號))
								self.分析器.產生對齊句(漢字後壁, 音標後壁.strip(分字符號))
								#
							except Exception as 錯誤:
								print(錯誤, 標準例句, 標準標音,
									漢字頭前, 音標頭前, 漢字後壁, 音標後壁)
								try:
									# 共句切開
									漢字頭前, 漢字後壁 = 標準例句.rsplit(文字資料[6], 1)
									音標頭前, 音標後壁 = 標準標音.rsplit(文字資料[7], 1)
									# 小等一下。 sio2-tan2-0tsit8-e7 . 小等 sio2-tan2-0 。  .
									self.分析器.產生對齊句(漢字頭前, 音標頭前.strip(分字符號))
									self.分析器.產生對齊句(漢字後壁, 音標後壁.strip(分字符號))
									#
								except Exception as 錯誤:
									print(錯誤, 標準例句, 標準標音,
										漢字頭前, 音標頭前, 漢字後壁, 音標後壁)
								else:
									例句內底漢字 = 文字資料[6]
									例句內底音標 = 文字資料[7]
							else:
								例句內底漢字 = 文字資料[6]
								例句內底音標 = 文字資料[7]
		
				if 例句內底漢字 == None or 例句內底音標 == None:
					print('警告！！符號變動才揣看覓有對著無')
					改標準例句 = 標準例句.replace(分字符號, 分詞符號)
					改標準標音 = 標準標音.replace(分字符號, 分詞符號)
					for 臺語流水號 in 臺語流水號集:
						文字資料 = 用流水號揣文字(臺語流水號)
						if 文字資料[2].startswith(閩南語):
							文字資料六 = 文字資料[6].replace(分字符號, 分詞符號)
							文字資料七 = 文字資料[7].replace(分字符號, 分詞符號).lstrip('0')
							if 文字資料六 in 改標準例句 and 文字資料七 in 改標準標音:
								try:
									# 共句切開
									漢字頭前, 漢字後壁 = 改標準例句.split(文字資料六, 1)
									音標頭前, 音標後壁 = 改標準標音.split(文字資料七, 1)
									# 小等一下。 sio2-tan2-0tsit8-e7 . 小等 sio2-tan2-0 。  .
									self.分析器.產生對齊句(漢字頭前, 音標頭前.strip(分字符號 + '0'))
									self.分析器.產生對齊句(漢字後壁, 音標後壁.strip(分字符號))
									#
								except Exception as 錯誤:
									print(錯誤, 標準例句, 標準標音,
										漢字頭前, 音標頭前, 漢字後壁, 音標後壁)
								else:
									if len(漢字後壁)==0 and len(音標後壁)==0:
										例句內底漢字 = 標準例句[len(漢字頭前):]
										例句內底音標 = 標準標音[len(音標頭前):]
									else:
										例句內底漢字 = 標準例句[len(漢字頭前):-len(漢字後壁)]
										例句內底音標 = 標準標音[len(音標頭前):-len(音標後壁)]
									print('@@', 標準例句, 標準標音,
										漢字頭前, 音標頭前, 漢字後壁, 音標後壁,len(音標頭前),-len(音標後壁))
		
				if 例句內底漢字 == None or 例句內底音標 == None:
					raise 解析錯誤('揣無元素：{0}，{1}。資料是：{2}'
						.format(標準例句, 標準標音, 查著資料))
				print('@@揣有元素：{0}，{1}。資料是：{2}'
						.format(標準例句, 標準標音, 查著資料),例句內底音標,例句內底漢字)
				for 臺語流水號 in 臺語流水號集:
					文字資料 = 用流水號揣文字(臺語流水號)
					if not 文字資料[2].startswith(閩南語):
						continue
		
					加關係(臺語流水號, 釋義流水號, 義近, 袂當替換)
					解釋關係流水號 = 揣關係上大流水號()
					設定詞性(解釋關係流水號, 詞性對照表[詞性])
		
					愛加句物件 = self.分析器.產生對齊句(標準例句.replace(例句內底漢字, 文字資料[6], 1),
						標準標音.replace(例句內底音標, 文字資料[7], 1))
					臺語資料腔口 = 用流水號揣腔口(臺語流水號)
		
					加文字佮版本(教育部閩南語辭典名, 種類, 臺語資料腔口,
						教育部閩南語辭典地區, 教育部閩南語辭典年代,
						self.譀鏡.看型(愛加句物件), self.譀鏡.看音(愛加句物件),
						版本正常)
		
					例句流水號 = 揣文字上大流水號()
					設定文字組合(例句流水號, 文字組合符號 + str(解釋關係流水號) + 文字組合符號)
		# 			設定編修狀況(例句流水號, 臺語腔口 + "的例句")
					加關係(例句流水號, 國語例句流水號, 義近, 會當替換)
					加關係(國語例句流水號, 例句流水號, 義近, 會當替換)
		
		文字無音設定()
			
	def 檢查例句(self):
		for 釋義編號,例句,標音 in 揣例句():
			新例句 = self.辭典工具.共造字換做統一碼表示法(例句)
			組字式型 = self.初胚工具.符號邊仔加空白(新例句).strip()
			新標音 = self.初胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 標音)
			新標音 = self.初胚工具.符號邊仔加空白(新標音).strip()
							
			try:
				原音句物件 = self.分析器.產生對齊句(組字式型, 新標音)
				標準句物件 = self.轉音家私.轉做標準音標(臺灣閩南語羅馬字拼音, 原音句物件)
				
				標準例句 = self.譀鏡.看型(標準句物件)
				標準標音 = self.譀鏡.看音(標準句物件)
			except:
				print('無對齊',釋義編號,例句,標音,sep='@')
			

if __name__ == '__main__':
	工具=整合釋義佮例句()
	工具.檢查例句()
