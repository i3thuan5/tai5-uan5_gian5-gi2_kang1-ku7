# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch


from 臺灣言語工具.剖析.中研院.剖析用戶端 import 剖析用戶端


@patch('臺灣言語工具.剖析.中研院.剖析用戶端.剖析用戶端.語句剖析做語句')
class 中研院剖析用戶端單元試驗(unittest.TestCase):
	def setUp(self):
		self.用戶端 = 剖析用戶端()

	def tearDown(self):
		pass

	def test_結構剖一句(self, 語句剖析做語句mock):
		語句剖析做語句mock.return_value=[[
 			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#',
 			]]
		self.assertEqual(self.用戶端.語句剖析後結構化('我想吃飯'), [[
 			('1', ['S', ['NP', ('我', 'N', 'Head')], ('想', 'Vt', 'Head'), ['VP', ('吃飯', 'Vi', 'Head')]], ''),
 			]])

	def test_結構剖一逝字(self, 語句剖析做語句mock):
		語句剖析做語句mock.return_value=[[
		 			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
 			'#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)',
 			]]
		self.assertEqual(self.用戶端.語句剖析後結構化('我想吃飯。我想吃很多飯。'), [[
 			('1', ['S', ['NP', ('我', 'N', 'Head')], ('想', 'Vt', 'Head'), ['VP', ('吃飯', 'Vi', 'Head')]], '。(PERIODCATEGORY)'),
		 	('2', ['S', ['NP', ('我', 'N', 'Head')], ('想', 'Vt', 'Head'), ['VP', ('吃', 'Vt', 'Head'), ['NP', ('很多', 'DET'), ('飯', 'N', 'Head')]]], '。(PERIODCATEGORY)'),
 			],
 			])

	def test_結構剖有換逝句(self, 語句剖析做語句mock):
		語句剖析做語句mock.return_value= [[
		 			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
		 			'#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)',
	 			], [
		 			'#1:1.[0] S(NP(Head:N:我)|Head:Vi:吃飽|T:了)#。(PERIODCATEGORY)',
	 			],
			]
		self.assertEqual(self.用戶端.語句剖析後結構化('我想吃飯。我想吃很多飯。\n我吃飽了。'), [[
	 			('1', ['S', ['NP', ('我', 'N', 'Head')], ('想', 'Vt', 'Head'), ['VP', ('吃飯', 'Vi', 'Head')]], '。(PERIODCATEGORY)'),
		 		('2', ['S', ['NP', ('我', 'N', 'Head')], ('想', 'Vt', 'Head'), ['VP', ('吃', 'Vt', 'Head'), ['NP', ('很多', 'DET'), ('飯', 'N', 'Head')]]], '。(PERIODCATEGORY)'),
 			], [
				('1', ['S', ['NP', ('我', 'N', 'Head')], ('吃飽', 'Vi', 'Head'), ('了', 'T')], '。(PERIODCATEGORY)'),
 			],
			])

	def test_結構剖著大於符號(self, 語句剖析做語句mock):
		語句剖析做語句mock.return_value= [[
			'#1:1.[0] %(NP(Head:N:我)|Vt:想|COLONCATEGORY::)#&gt;(PARENTHESISCATEGORY)',
			]]
		self.assertEqual(self.用戶端.語句剖析後結構化('我想) :>'), [[
			('1', ['%', ['NP', ('我', 'N', 'Head')], ('想', 'Vt'), ('', '', 'COLONCATEGORY')], '&gt;(PARENTHESISCATEGORY)'),
			]])

	def test_結構剖著小於符號是空的(self, 語句剖析做語句mock):
		語句剖析做語句mock.return_value= [[]]
		self.assertEqual(self.用戶端.語句剖析後結構化('我想) :<'), [[
			]])
