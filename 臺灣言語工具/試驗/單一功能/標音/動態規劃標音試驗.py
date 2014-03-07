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
from unittest.case import TestCase
from 臺灣言語工具.字詞組集句章.解析整理工具.文章粗胚工具 import 文章粗胚工具
from 臺灣言語工具.字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 臺灣言語工具.斷詞.型音辭典 import 型音辭典
from 臺灣言語工具.斷詞.動態規劃斷詞 import 動態規劃斷詞
from 臺灣言語工具.字詞組集句章.基本元素.組 import 組
from 臺灣言語工具.字詞組集句章.基本元素.集 import 集
from 臺灣言語工具.字詞組集句章.基本元素.句 import 句
from 臺灣言語工具.字詞組集句章.基本元素.章 import 章
from 臺灣言語工具.字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤

class 動態規劃標音試驗(TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.連詞 = 語句連詞(3)
		self.標音 = 動態規劃標音()

		self.我有一張椅仔 = self.分析器.產生對齊句(
			'我有一張椅仔！！', 'gua2 u7 tsit8-tiunn1 i2-a2!!')
		self.桌仔垃圾 = self.分析器.產生對齊句(
			'桌仔垃圾！！', 'toh4-a2 lap4-sap4!!')
		self.椅仔 = self.分析器.產生對齊句(
			'椅仔。', 'i2-a2.')
		self.桌仔 = self.分析器.產生對齊句(
			'桌仔。', 'toh4-a2.')
		self.柴 = self.分析器.產生對齊句(
			'柴！', 'tsha5!')

	def tearDown(self):
		pass

	def test_看機率選詞(self):
		我 = self.分析器.產生對齊集('我', 'gua2')
		的 = self.分析器.產生對齊組('的', 'e5')
		鞋 = self.分析器.產生對齊組('鞋', 'e5')
		仔 = self.分析器.產生對齊集('仔', 'ia2')
		e5_鞋的 = 集([鞋, 的, ])
		我_e5_e5_仔_鞋的 = 句([我, e5_鞋的, e5_鞋的, 仔])
		e5_的鞋 = 集([的, 鞋, ])
		我_e5_e5_仔_的鞋 = 句([我, e5_的鞋, e5_的鞋, 仔])
		self.連詞.看(self.分析器.產生對齊句('我穿布鞋。', 'li2 hoo2-bo5 ?'))
		self.連詞.看(self.分析器.產生對齊句('我鞋仔歹去矣。', 'li2 hoo2-bo5 ?'))
		鞋的結果, 鞋的分數 = self.標音.self.標音(self.連詞, 我_e5_e5_仔_鞋的)
		的鞋結果, 的鞋分數 = self.標音.self.標音(self.連詞, 我_e5_e5_仔_的鞋)
		self.assertEqual(鞋的結果, '我鞋鞋仔')
		self.assertEqual(的鞋結果, 鞋的結果)
		self.assertLess(鞋的分數, 0.0)
		self.assertEqual(鞋的分數, 的鞋分數)
		self.連詞.看(self.分析器.產生對齊句('我的冊佇你遐。', 'li2 hoo2-bo5 ?'))
		self.assertEqual(鞋的結果, '我鞋鞋仔')
		self.assertEqual(的鞋結果, 鞋的結果)
		self.assertLess(鞋的分數, 0.0)
		self.assertEqual(鞋的分數, 的鞋分數)
		self.連詞.看(self.分析器.產生對齊句('我的故鄉佇花蓮。', 'li2 hoo2-bo5 ?'))
		self.assertEqual(鞋的結果, '我的鞋仔')
		self.assertEqual(的鞋結果, 鞋的結果)
		self.assertLess(鞋的分數, 0.0)
		self.assertEqual(鞋的分數, 的鞋分數)

	def test_頭中尾詞比較(self):
		self.連詞.看(self.我有一張椅仔)
		self.連詞.看(self.桌仔垃圾)
		self.assertLess(self.標音.評分(self.連詞, self.桌仔), 0.0)
		self.assertLess(self.標音.評分(self.連詞, self.椅仔), self.標音.評分(self.連詞, self.桌仔))
		self.assertEqual(self.標音.評分(self.連詞, self.柴), self.標音.評分(self.連詞, self.桌仔))
		
	def test_長的好句袂使輸短的爛句(self):
		self.連詞.看(self.我有一張椅仔)
		self.連詞.看(self.桌仔垃圾)
		self.assertLess(self.標音.評分(self.連詞, self.椅仔), self.標音.評分(self.連詞, self.桌仔垃圾))
		self.assertLess(self.標音.評分(self.連詞, self.柴), self.標音.評分(self.連詞, self.桌仔垃圾))
