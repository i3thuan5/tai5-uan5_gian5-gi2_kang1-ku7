# -*- coding: utf-8 -*-
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
import io
import wave
class 音檔頭前表:
	def 提掉(self, 音):
		音檔 = io.BytesIO(音)
		音物件 = wave.open(音檔, mode = 'rb')
		原始 = 音物件.readframes(音物件.getnframes())
		音物件.close()
		音檔.close()
		return 原始
	def 加起哩(self, 原始, 一點幾位元組, 一秒幾點, 幾个聲道):
		音檔 = io.BytesIO()
		音物件 = wave.open(音檔, mode = 'wb')
		音物件.setsampwidth(一點幾位元組)
		音物件.setframerate(一秒幾點)
		音物件.setnchannels(幾个聲道)
		音物件.writeframesraw(原始)
		音物件.close()
		音 = 音檔.getvalue()
		音檔.close()
		return 音

