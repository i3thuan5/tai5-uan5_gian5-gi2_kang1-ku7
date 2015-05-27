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


from 臺灣言語工具.斷詞.中研院.斷詞用戶端 import 斷詞用戶端


class 中研院斷詞用戶端整合試驗(unittest.TestCase):
	def setUp(self):
		self.用戶端 = 斷詞用戶端()
	def tearDown(self):
		pass

	def test_語句斷空字串(self):
		self.assertEqual(self.用戶端.語句斷詞做語句(''), [])
	def test_語句斷空白佮換逝(self):
		self.assertEqual(self.用戶端.語句斷詞做語句('\n \n'), [])
	def test_語句斷一句話(self):
		self.assertEqual(self.用戶端.語句斷詞做語句('我想吃飯。'), [[
				'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
			]])
	def test_語句斷一句話閣換逝(self):
		self.assertEqual(self.用戶端.語句斷詞做語句('我想吃飯。\n'),[ [
				'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
			]])
	def test_語句斷一逝字(self):
		self.assertEqual(self.用戶端.語句斷詞做語句('我想吃飯。我想吃很多飯。'), [[
				'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
				'\u3000我(N)\u3000想(Vt)\u3000吃(Vt)\u3000很多(DET)\u3000飯(N)\u3000。(PERIODCATEGORY)',
			]])
	def test_語句斷兩逝字(self):
		self.assertEqual(self.用戶端.語句斷詞做語句('我想吃飯。我想吃很多飯。\n我吃飽了。'), [
				[
					'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
					'\u3000我(N)\u3000想(Vt)\u3000吃(Vt)\u3000很多(DET)\u3000飯(N)\u3000。(PERIODCATEGORY)',
				],
				[
					'\u3000我(N)\u3000吃飽(Vi)\u3000了(T)\u3000。(PERIODCATEGORY)',
				]
			])
	def test_語句斷濟逝字(self):
		self.assertEqual(self.用戶端.語句斷詞做語句('\n\n我想吃飯。我想吃很多飯。\n\n  \n\n  　 \n\n我吃飽了。\n\n'), [
				[
					'\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
					'\u3000我(N)\u3000想(Vt)\u3000吃(Vt)\u3000很多(DET)\u3000飯(N)\u3000。(PERIODCATEGORY)',
				],
				[
					'\u3000我(N)\u3000吃飽(Vi)\u3000了(T)\u3000。(PERIODCATEGORY)',
				]
			])
	def test_語句斷大於符號(self):
		self.assertEqual(self.用戶端.語句斷詞做語句('我想) :>'),[[
				'\u3000我(N)\u3000想(Vt)\u3000)(PARENTHESISCATEGORY)\u3000:(COLONCATEGORY)\u3000&gt;(PARENTHESISCATEGORY)'
			]])
	def test_語句斷小於符號的空白結果(self):
		self.assertEqual(self.用戶端.語句斷詞做語句('我想) :<'), [[
			]])
