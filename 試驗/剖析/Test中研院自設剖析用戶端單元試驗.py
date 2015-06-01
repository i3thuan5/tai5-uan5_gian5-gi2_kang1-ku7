# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch


from 臺灣言語工具.剖析.中研院.自設剖析用戶端 import 自設剖析用戶端

class 中研院自設剖析用戶端單元試驗(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	@patch('telnetlib.Telnet')
	def test_自設剖析工具(self, 連線mock):
		連線mock.return_value.read_all.return_value.decode.return_value = '#1:1.[0] S(agent:NP(Head:Nhaa:我)|Head:VE2:想|goal:VP(Head:VA4:吃飯))#。(PERIODCATEGORY)\r\n#2:1.[0] S(agent:NP(Head:Nhaa:我)|Head:VE2:想|goal:VP(Head:VC31:吃|theme:NP(quantifier:Neqa:很多|Head:Nab:飯)))#。(PERIODCATEGORY)\r\n'
		工具 = 自設剖析用戶端()
		self.assertEqual(工具.剖析('我想吃飯。我想吃很多飯。'),
			['#1:1.[0] S(agent:NP(Head:Nhaa:我)|Head:VE2:想|goal:VP(Head:VA4:吃飯))#。(PERIODCATEGORY)',
			'#2:1.[0] S(agent:NP(Head:Nhaa:我)|Head:VE2:想|goal:VP(Head:VC31:吃|theme:NP(quantifier:Neqa:很多|Head:Nab:飯)))#。(PERIODCATEGORY)'
			])
