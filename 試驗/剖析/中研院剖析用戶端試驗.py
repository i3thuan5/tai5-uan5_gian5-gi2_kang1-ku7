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
import unittest


from 臺灣言語工具.剖析.中研院.剖析用戶端 import 剖析用戶端

class 中研院剖析用戶端試驗(unittest.TestCase):
	def setUp(self):
		self.用戶端 = 剖析用戶端()
	def tearDown(self):
		pass

	@unittest.expectedFailure
	def test_物件剖一句(self):
		self.assertEqual(self.用戶端.剖析物件('我想吃飯'), [[
 			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#',
 			]])
	@unittest.expectedFailure
	def test_物件剖一逝字(self):
		self.assertEqual(self.用戶端.剖析物件('我想吃飯。我想吃很多飯。'), [[
 			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
 			'#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)'],
 			])
	@unittest.expectedFailure
	def test_物件剖兩逝字(self):
		self.assertEqual(self.用戶端.剖析物件('我想吃飯。我想吃很多飯。\n我吃飽了。'), [[
	 			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
	 			'#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)',
 			], [
	 			'#1:1.[0] S(NP(Head:N:我)|Head:Vi:吃飽|T:了)#。(PERIODCATEGORY)',
 			],
			])
	@unittest.expectedFailure
	def test_物件剖濟逝字(self):
		self.assertEqual(self.用戶端.剖析物件('\n\n我想吃飯。我想吃很多飯。\n\n  \n\n  　 \n\n我吃飽了。\n\n'), [[
	 			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
	 			'#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)',
 			], [
	 			'#1:1.[0] S(NP(Head:N:我)|Head:Vi:吃飽|T:了)#。(PERIODCATEGORY)',
 			],
			])
	@unittest.expectedFailure
	def test_物件剖著大於符號(self):
		self.assertEqual(self.用戶端.剖析物件('我想) :>'), [[
			'#1:1.[0] %(NP(Head:N:我)|Vt:想|COLONCATEGORY::)#&gt;(PARENTHESISCATEGORY)',
			]])
	@unittest.expectedFailure
	def test_物件剖著小於符號是空的(self):
		self.assertEqual(self.用戶端.剖析物件('我想) :<'), [[
			]])

	def test_結構剖一句(self):
		self.assertEqual(self.用戶端.語句剖析後結構化('我想吃飯'), [[
 			('1', ['S', ['NP', ('我', 'N', 'Head')], ('想', 'Vt', 'Head'), ['VP', ('吃飯', 'Vi', 'Head')]], ''),
 			]])
	def test_結構剖一逝字(self):
		self.assertEqual(self.用戶端.語句剖析後結構化('我想吃飯。我想吃很多飯。'), [[
 			('1', ['S', ['NP', ('我', 'N', 'Head')], ('想', 'Vt', 'Head'), ['VP', ('吃飯', 'Vi', 'Head')]], '。(PERIODCATEGORY)'),
		 	('2', ['S', ['NP', ('我', 'N', 'Head')], ('想', 'Vt', 'Head'), ['VP', ('吃', 'Vt', 'Head'), ['NP', ('很多', 'DET'), ('飯', 'N', 'Head')]]], '。(PERIODCATEGORY)'),
 			],
 			])
	def test_結構剖兩逝字(self):
		self.assertEqual(self.用戶端.語句剖析後結構化('我想吃飯。我想吃很多飯。\n我吃飽了。'), [[
	 			('1', ['S', ['NP', ('我', 'N', 'Head')], ('想', 'Vt', 'Head'), ['VP', ('吃飯', 'Vi', 'Head')]], '。(PERIODCATEGORY)'),
		 		('2', ['S', ['NP', ('我', 'N', 'Head')], ('想', 'Vt', 'Head'), ['VP', ('吃', 'Vt', 'Head'), ['NP', ('很多', 'DET'), ('飯', 'N', 'Head')]]], '。(PERIODCATEGORY)'),
 			], [
				('1', ['S', ['NP', ('我', 'N', 'Head')], ('吃飽', 'Vi', 'Head'), ('了', 'T')], '。(PERIODCATEGORY)'),
 			],
			])
	def test_結構剖濟逝字(self):
		self.assertEqual(self.用戶端.語句剖析後結構化('\n\n我想吃飯。我想吃很多飯。\n\n  \n\n  　 \n\n我吃飽了。\n\n'), [[
	 			('1', ['S', ['NP', ('我', 'N', 'Head')], ('想', 'Vt', 'Head'), ['VP', ('吃飯', 'Vi', 'Head')]], '。(PERIODCATEGORY)'),
		 	('2', ['S', ['NP', ('我', 'N', 'Head')], ('想', 'Vt', 'Head'), ['VP', ('吃', 'Vt', 'Head'), ['NP', ('很多', 'DET'), ('飯', 'N', 'Head')]]], '。(PERIODCATEGORY)'),
 			], [
				('1', ['S', ['NP', ('我', 'N', 'Head')], ('吃飽', 'Vi', 'Head'), ('了', 'T')], '。(PERIODCATEGORY)'),
 			],
			])
	def test_結構剖著大於符號(self):
		self.assertEqual(self.用戶端.語句剖析後結構化('我想) :>'), [[
			('1', ['%', ['NP', ('我', 'N', 'Head')], ('想', 'Vt'), ('', '', 'COLONCATEGORY')], '&gt;(PARENTHESISCATEGORY)'),
			]])
	def test_結構剖著小於符號是空的(self):
		self.assertEqual(self.用戶端.語句剖析後結構化('我想) :<'), [[
			]])

	def test_語句剖一句(self):
		self.assertEqual(self.用戶端.語句剖析做語句('我想吃飯'), [[
 			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#',
 			]])
	def test_語句剖一逝字(self):
		self.assertEqual(self.用戶端.語句剖析做語句('我想吃飯。我想吃很多飯。'), [[
 			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
 			'#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)'],
 			])
	def test_語句剖兩逝字(self):
		self.assertEqual(self.用戶端.語句剖析做語句('我想吃飯。我想吃很多飯。\n我吃飽了。'), [[
	 			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
	 			'#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)',
 			], [
	 			'#1:1.[0] S(NP(Head:N:我)|Head:Vi:吃飽|T:了)#。(PERIODCATEGORY)',
 			],
			])
	def test_語句剖濟逝字(self):
		self.assertEqual(self.用戶端.語句剖析做語句('\n\n我想吃飯。我想吃很多飯。\n\n  \n\n  　 \n\n我吃飽了。\n\n'), [[
	 			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
	 			'#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)',
 			], [
	 			'#1:1.[0] S(NP(Head:N:我)|Head:Vi:吃飽|T:了)#。(PERIODCATEGORY)',
 			],
			])
	def test_語句剖著大於符號(self):
		self.assertEqual(self.用戶端.語句剖析做語句('我想) :>'), [[
			'#1:1.[0] %(NP(Head:N:我)|Vt:想|COLONCATEGORY::)#&gt;(PARENTHESISCATEGORY)',
			]])
	def test_語句剖著小於符號是空的(self):
		self.assertEqual(self.用戶端.語句剖析做語句('我想) :<'), [[
			]])
