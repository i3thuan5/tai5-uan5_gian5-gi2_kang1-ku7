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
from unittest.case import TestCase
from unittest.mock import patch, call


from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本元素.章 import 章

@patch('xmlrpc.client.ServerProxy')
class 摩西用戶端試驗(TestCase):
	def setUp(self):
		self.用戶端 = 摩西用戶端()  # 'localhost', '8080'
		華語語句 = "我 們 要 去 吃 飯 。"
		self.華語句物件 = self.分析器.建立句物件(華語語句)
		self.華語句物件二 = self.分析器.建立句物件('好喲！')
		self.華語章物件 = 章([self.華語句物件, self.華語句物件二])
		
		翻譯對應關係 = [
			{'tgt-start': 0, 'src-start': 0, 'src-end': 1},
			{'tgt-start': 1, 'src-start': 2, 'src-end': 2},
			{'tgt-start': 2, 'src-start': 3, 'src-end': 3},
			{'tgt-start': 3, 'src-start': 4, 'src-end': 5},
			{'tgt-start': 5, 'src-start': 6, 'src-end': 6},
			]
		self.全漢翻譯結果 = {'nbest':[{
			'text':'阮  欲  去  食  飯  。  ',
			'align':翻譯對應關係,
			'totalScore':-21.66,
			}]}
		self.全漢全羅分詞翻譯結果 = {'nbest':[{
			'text':'阮｜gun2  欲｜beh4  去｜khi3  食｜tsiah8  飯｜png7  。｜.  ',
			'align':翻譯對應關係,
			'totalScore':-21.66,
			}]}
		self.全漢全羅分詞含詞翻譯結果 = {'nbest':[{
			'text':'阮｜gun2  欲｜beh4  去｜khi3  食｜tsiah8  炒-飯｜tsha2-png7  。｜.  ',
			'align':翻譯對應關係,
			'totalScore':-21.66,
			}]}
		self.翻譯結果有未知詞出來 = {'nbest':[{
			'text':'阮  要|UNK|UNK|UNK  去  食  飯  。  ',
			'align':翻譯對應關係,
			'totalScore':-21.66,
			}]}
	
		self.分析器 = 拆文分析器()
	def tearDown(self):
		pass
	@patch('臺灣言語工具.解析整理.物件譀鏡.物件譀鏡.看分詞')
	def test_用看分詞(self, 分詞mock, xmlrpcMock):
		xmlrpcMock.translate.return_value = self.全漢翻譯結果
		self.用戶端.翻譯(self.華語句物件)
		分詞mock.assert_called_once_with(self.華語句物件)
	@patch('臺灣言語工具.翻譯.摩西工具.語句編碼器.語句編碼器.編碼')
	def test_有編碼(self, 編碼mock, xmlrpcMock):
		xmlrpcMock.translate.return_value = self.全漢翻譯結果
		self.用戶端.翻譯(self.華語句物件)
		編碼mock.assert_called_once_with("我 們 要 去 吃 飯 。")
	@patch('臺灣言語工具.翻譯.摩西工具.語句編碼器.語句編碼器.解碼')
	def test_有解碼(self, 解碼mock, xmlrpcMock):
		xmlrpcMock.translate.return_value = self.全漢翻譯結果
		self.用戶端.翻譯(self.華語句物件)
		解碼mock.assert_called_once_with(self.全漢翻譯結果['text'])
	def test_翻譯結果是章物件(self, xmlrpcMock):
		xmlrpcMock.translate.return_value = self.全漢翻譯結果
		結果句物件, _, _ = self.用戶端.翻譯(self.華語句物件)
		self.assertIsInstance(結果句物件, 章)
	def test_翻譯結果結構(self, xmlrpcMock):
		xmlrpcMock.translate.return_value = self.全漢翻譯結果
		結果句物件, _, _ = self.用戶端.翻譯(self.華語句物件)
		閩南語集物件 = self.分析器.建立集物件('')
		閩南語集物件.內底組 = [
			self.分析器.建立組物件('阮'),
			self.分析器.建立組物件('欲'),
			self.分析器.建立組物件('去'),
			self.分析器.建立組物件('食飯'),
			self.分析器.建立組物件('。'),
			]
		閩南語句物件 = self.分析器.建立句物件('')
		閩南語句物件.內底集 = [閩南語集物件]
		self.assertEqual(結果句物件, 閩南語句物件)
	def test_來源新結構檢查(self, xmlrpcMock):
		xmlrpcMock.translate.return_value = self.全漢翻譯結果
		_, 華語新結構句物件, _ = self.用戶端.翻譯(self.華語句物件)
		self.fail()
		華語集物件 = self.分析器.建立集物件('')
		華語集物件.內底組 = [
			self.分析器.建立組物件('我們'),
			self.分析器.建立組物件('要'),
			self.分析器.建立組物件('去'),
			self.分析器.建立組物件('吃飯'),
			self.分析器.建立組物件('。'),
			]
		華語句物件 = self.分析器.建立句物件('')
		華語句物件.內底集 = [華語集物件]
		self.assertEqual(華語新結構句物件, 華語句物件)
	def test_翻譯結果佮來源長度相仝(self):
		結果句物件, 華語新結構句物件, _ = self.用戶端.翻譯(self.華語句物件)
		self.assertEqual(len(結果句物件.內底集[0].內底組),
			len(華語新結構句物件.內底集[0].內底組))
	def test_翻譯結果對齊檢查(self):
		結果句物件, _, _ = self.用戶端.翻譯(self.華語句物件)
		for 組物件 in 結果句物件.內底集[0].內底組:
			self.assertEqual(組物件, 組物件.翻譯來源組物件.翻譯目標組物件)
	def test_來源新結構對齊檢查(self, xmlrpcMock):
		xmlrpcMock.translate.return_value = self.全漢翻譯結果
		_, 華語新結構句物件, _ = self.用戶端.翻譯(self.華語句物件)
		for 組物件 in 華語新結構句物件.內底集[0].內底組:
			self.assertEqual(組物件, 組物件.翻譯目標組物件.翻譯來源組物件)
	def test_翻譯分數(self, xmlrpcMock):
		xmlrpcMock.translate.return_value = self.全漢翻譯結果
		_, _, 分數 = self.用戶端.翻譯(self.華語句物件)
		self.assertEqual(分數, -21.66)
	def test_無仝結果(self):
		self.fail('3個')
		XX
		self.全漢全羅分詞翻譯結果
		self.全漢全羅分詞含詞翻譯結果
		self.翻譯結果有未知詞出來
	@patch('臺灣言語工具.翻譯.摩西工具.摩西用戶端.摩西用戶端.翻譯句物件')
	def test_章物件的結果是章物件(self, 翻譯句物件mock, xmlrpcMock):
		翻譯句物件mock.return_value = None, None, None
		結果章物件, _, _ = self.用戶端.翻譯(self.華語句物件)
		self.assertIsInstance(結果章物件, 章)
	@patch('臺灣言語工具.翻譯.摩西工具.摩西用戶端.摩西用戶端.翻譯句物件')
	def test_章物件的來源新結構章物件(self, 翻譯句物件mock, xmlrpcMock):
		翻譯句物件mock.return_value = None, None, None
		_, 華語新結構章物件, _ = self.用戶端.翻譯(self.華語句物件)
		self.assertIsInstance(華語新結構章物件, 章)
	@patch('臺灣言語工具.翻譯.摩西工具.摩西用戶端.摩西用戶端.翻譯句物件')
	def test_翻譯章物件的分數(self, 翻譯句物件mock, xmlrpcMock):
		翻譯句物件mock.return_value = None, None, -21.66
		_, _, 分數 = self.用戶端.翻譯(self.華語句物件)
		self.assertEqual(分數, -21.66 - 21.66)
	@patch('臺灣言語工具.翻譯.摩西工具.摩西用戶端.摩西用戶端.翻譯句物件')
	def test_章物件是一句一句翻譯(self, 翻譯句物件mock, xmlrpcMock):
		self.用戶端.翻譯(self.華語句物件)
		翻譯句物件mock.assert_has_calls(
			[call(self.華語句物件), call(self.華語句物件二)],
			any_order=True
		)
