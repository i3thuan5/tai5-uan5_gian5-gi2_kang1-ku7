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
from 臺灣言語工具.字詞組集句章.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.字詞組集句章.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.斷詞.型音辭典 import 型音辭典
from 臺灣言語工具.斷詞.動態規劃斷詞 import 動態規劃斷詞
from 臺灣言語工具.字詞組集句章.基本元素.組 import 組
from 臺灣言語工具.字詞組集句章.基本元素.集 import 集
from 臺灣言語工具.字詞組集句章.基本元素.句 import 句
from 臺灣言語工具.字詞組集句章.基本元素.章 import 章
from 臺灣言語工具.字詞組集句章.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.標音.語句連詞 import 語句連詞
from 臺灣言語工具.標音.動態規劃標音 import 動態規劃標音

class 動態規劃標音試驗(TestCase):
	忍受 = 1e-10
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.連詞 = 語句連詞(3)
		self.標音 = 動態規劃標音()

		self.我有一張桌仔 = self.分析器.產生對齊句(
			'我有一張桌仔！', 'gua2 u7 tsit8-tiunn1 toh4-a2!')
		self.桌仔垃圾 = self.分析器.產生對齊句(
			'桌仔垃圾！？', 'toh4-a2 lap4-sap4!?')
		self.我有一張椅仔 = self.分析器.產生對齊句(
			'我有一張椅仔！', 'gua2 u7 tsit8-tiunn1 i2-a2!')
		self.椅仔 = self.分析器.產生對齊句(
			'椅仔。', 'i2-a2.')
		self.桌仔 = self.分析器.產生對齊句(
			'桌仔。', 'toh4-a2.')
		self.柴 = self.分析器.產生對齊句(
			'柴！', 'tsha5!')
		self.我 = self.分析器.產生對齊句(
			'我', 'gua2')

	def tearDown(self):
		pass

	def test_頭中尾詞比較(self):
		self.連詞.看(self.我有一張桌仔)
		self.連詞.看(self.桌仔垃圾)
		self.assertLess(self.標音.評分(self.連詞, self.桌仔), 0.0)
		self.assertLess(self.標音.評分(self.連詞, self.椅仔), self.標音.評分(self.連詞, self.桌仔))
		self.assertEqual(self.標音.評分(self.連詞, self.柴), self.標音.評分(self.連詞, self.桌仔))

	def test_長的好句袂使輸短的爛句(self):
		self.連詞.看(self.我有一張椅仔)
		self.連詞.看(self.桌仔垃圾)
		self.assertLess(self.標音.評分(self.連詞, self.椅仔), self.標音.評分(self.連詞, self.桌仔垃圾))
		self.assertLess(self.標音.評分(self.連詞, self.柴), self.標音.評分(self.連詞, self.桌仔垃圾))

	def test_標音的分數愛佮評分仝款(self):
		self.連詞.看(self.我有一張桌仔)
		標好, 分數, 詞數 = self.標音.標音(self.連詞, self.我)
		self.assertEqual(標好, self.我)
		self.assertAlmostEqual(分數, self.標音.評分(self.連詞, self.我), delta = self.忍受)
		self.assertEqual(詞數, 3)
		標好, 分數, 詞數 = self.標音.標音(self.連詞, self.桌仔)
		self.assertEqual(標好, self.桌仔)
		self.assertAlmostEqual(分數, self.標音.評分(self.連詞, self.桌仔), delta = self.忍受)
		self.assertEqual(詞數, 4)
		標好, 分數, 詞數 = self.標音.標音(self.連詞, self.我有一張桌仔)
		self.assertEqual(標好, self.我有一張桌仔)
		self.assertAlmostEqual(分數, self.標音.評分(self.連詞, self.我有一張桌仔), delta = self.忍受)
		self.assertEqual(詞數, 7)

	def test_看機率選詞(self):
		我 = self.分析器.產生對齊集('我', 'gua2')
		的 = self.分析器.產生對齊組('的', 'e5')
		鞋 = self.分析器.產生對齊組('鞋', 'e5')
		仔 = self.分析器.產生對齊集('仔', 'a2')
		e5_鞋的 = 集([鞋, 的, ])
		我_e5_e5_仔_鞋的 = 句([我, e5_鞋的, e5_鞋的, 仔])
		e5_的鞋 = 集([的, 鞋, ])
		我_e5_e5_仔_的鞋 = 句([我, e5_的鞋, e5_的鞋, 仔])
		我鞋鞋仔 = 句([我, 集([鞋, ]), 集([鞋, ]), 仔])
		我的鞋仔 = 句([我, 集([的, ]), 集([鞋, ]), 仔])
		self.連詞.看(self.分析器.產生對齊句('我穿布鞋。', 'gua2 tshng1 poo3 e5.'))
		self.連詞.看(self.分析器.產生對齊句('我鞋仔歹去矣。', 'gua2 e5 a2 phainn2-0khi3 0ah4.'))
		我的 = [self.分析器.產生對齊詞('我', 'gua2'), self.分析器.產生對齊詞('的', 'e5')]
		self.assertEqual(self.連詞.數量(我的), [0, 0])
		我鞋 = [self.分析器.產生對齊詞('我', 'gua2'), self.分析器.產生對齊詞('鞋', 'e5')]
		self.assertEqual(self.連詞.數量(我鞋), [2, 1])
		鞋的結果, 鞋的分數 , 鞋的詞數 = self.標音.標音(self.連詞, 我_e5_e5_仔_鞋的)
		的鞋結果, 的鞋分數, 的鞋詞數 = self.標音.標音(self.連詞, 我_e5_e5_仔_的鞋)
		self.assertEqual(鞋的結果, 我鞋鞋仔)
		self.assertEqual(的鞋結果, 鞋的結果)
		self.assertLess(鞋的分數, 0.0)
		self.assertEqual(鞋的分數, 的鞋分數)
		self.assertEqual(鞋的詞數, 6)
		self.assertEqual(鞋的詞數, 的鞋詞數)
		self.連詞.看(self.分析器.產生對齊句('我的冊佇你遐。', 'gua2 e5 tsheh4 ti7 li2 hia1.'))
		鞋的結果, 鞋的分數 , 鞋的詞數 = self.標音.標音(self.連詞, 我_e5_e5_仔_鞋的)
		的鞋結果, 的鞋分數, 的鞋詞數 = self.標音.標音(self.連詞, 我_e5_e5_仔_的鞋)
		self.assertEqual(鞋的結果, 我鞋鞋仔)
		self.assertEqual(的鞋結果, 鞋的結果)
		self.assertLess(鞋的分數, 0.0)
		self.assertEqual(鞋的分數, 的鞋分數)
		self.assertEqual(鞋的詞數, 6)
		self.assertEqual(鞋的詞數, 的鞋詞數)
		self.連詞.看(self.分析器.產生對齊句('我的故鄉佇花蓮。', 'gua2 e5 koo3-hiong1 ti7 hua1-lian1.'))
		鞋的結果, 鞋的分數 , 鞋的詞數 = self.標音.標音(self.連詞, 我_e5_e5_仔_鞋的)
		的鞋結果, 的鞋分數 , 的鞋詞數 = self.標音.標音(self.連詞, 我_e5_e5_仔_的鞋)
		self.assertEqual(鞋的結果, 我的鞋仔)
		self.assertEqual(的鞋結果, 鞋的結果)
		self.assertLess(鞋的分數, 0.0)
		self.assertEqual(鞋的分數, 的鞋分數)
		self.assertEqual(鞋的詞數, 6)
		self.assertEqual(鞋的詞數, 的鞋詞數)

	def test_標了的型態愛佮原本仝款(self):
		字物件 = self.分析器.產生對齊字('媠', 'sui2')
		詞物件 = self.分析器.產生對齊詞('姑娘', 'koo1-niu5')
		組物件 = self.分析器.產生對齊組('媠姑娘', 'sui2 koo1-niu5')
		集物件 = self.分析器.產生對齊集('媠姑娘', 'sui2 koo1-niu5')
		句物件 = self.分析器.產生對齊句('我恰意媠姑娘', 'gua2 kah4 i3 sui2 koo1-niu5')
		章物件 = self.分析器.產生對齊章('我恰意媠姑娘。我愛媠姑娘。', 'gua2 kah4 i3 sui2 koo1-niu5. gua2 ai3 sui2 koo1-niu5.')
		for 物件 in [字物件, 詞物件, 組物件, 集物件, 句物件, 章物件]:
			self.assertEqual(self.標音.標音(self.連詞, 物件)[0], 物件)

	def test_選無仝長度的集(self):
		媠姑娘 = self.分析器.產生對齊組('媠姑娘', 'sui2 koo1-niu5')
		靚細妹 = self.分析器.產生對齊組('靚細妹', 'jiangˊ-se-moi')
		大美女 = self.分析器.產生對齊組('世界大大美女', 'se3-kai3 tua7 tua7 mi2-lu2')
		莉 = 集([媠姑娘, 靚細妹, 大美女])
		我 = self.分析器.產生對齊集('我', 'gua2')
		愛 = self.分析器.產生對齊集('愛', 'ai3')
		呀 = self.分析器.產生對齊集('！', '!')
		問題句物件 = 句([我, 愛, 莉, 呀])
		媠姑娘句物件 = 句([我, 愛, 集([媠姑娘, ]), 呀])
		靚細妹句物件 = 句([我, 愛, 集([靚細妹, ]), 呀])
		大美女句物件 = 句([我, 愛, 集([大美女, ]), 呀])
		self.連詞.看(媠姑娘)
		結果, 分數, 詞數 = self.標音.標音(self.連詞, 問題句物件)
		self.assertEqual(結果, 媠姑娘句物件)
		self.assertEqual(詞數, 7)
		self.連詞.看(靚細妹)
		self.連詞.看(靚細妹)
		self.連詞.看(靚細妹)
		結果, 分數, 詞數 = self.標音.標音(self.連詞, 問題句物件)
		#因為詞組干焦一个詞，所以會靚細妹輸媠姑娘
		self.assertEqual(結果, 媠姑娘句物件)
		self.assertEqual(詞數, 7)
		#詞組較長，所以應該愛搶網別人
		self.連詞.看(大美女)
# 		self.連詞.看(大美女)
# 		self.連詞.看(大美女)
		結果, 分數, 詞數 = self.標音.標音(self.連詞, 問題句物件)
		self.assertEqual(結果, 大美女句物件)
		self.assertEqual(詞數, 9)


	def test_標空的物件(self):
		# 字物件有限制毋是空的
		詞物件 = self.分析器.建立詞物件('')
		組物件 = self.分析器.建立組物件('')
		集物件 = self.分析器.建立集物件('')
		句物件 = self.分析器.建立句物件('')
		章物件 = self.分析器.建立章物件('')
		結果, 分數, 詞數 = self.標音.標音(self.連詞, 詞物件)
		全部分數 = {}
		for 物件, 詞數答案 in zip([詞物件, 組物件, 句物件, 章物件], [3, 2, 2, 0]):
			結果, 分數, 詞數 = self.標音.標音(self.連詞, 物件)
			self.assertEqual(結果, 物件)
			self.assertEqual(詞數, 詞數答案)
			if 詞數 not in 全部分數:
				全部分數[詞數] = 分數
			self.assertEqual(分數, 全部分數[詞數])
		self.assertRaises(解析錯誤, self.標音.標音, self.連詞, 集物件,)

	def test_標有空的集合(self):
		我_你 = 句([self.分析器.建立集物件('我'), self.分析器.建立集物件(''), self.分析器.建立集物件('你')])
		self.assertRaises(解析錯誤, self.標音.標音, self.連詞, 我_你)
