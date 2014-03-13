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
from 臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from 臺灣言語工具.斷詞.中研院工具.自設剖析工具 import 自設剖析工具

class 中研院工具試驗(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass

	def test_官方斷詞工具(self):
		工具 = 官方斷詞剖析工具()
		self.assertEqual(工具.斷詞('我想吃飯。我想吃很多飯。'), [[
			[('我', 'N'), ('想', 'Vt'), ('吃飯', 'Vi'), ('。', 'PERIODCATEGORY')],
			[('我', 'N'), ('想', 'Vt'), ('吃', 'Vt'), ('很多', 'DET'), ('飯', 'N'), ('。', 'PERIODCATEGORY')]
			]])
		self.assertEqual(工具.斷詞('我想吃飯。我想吃很多飯。\n我吃飽了。'), [
			[
				[('我', 'N'), ('想', 'Vt'), ('吃飯', 'Vi'), ('。', 'PERIODCATEGORY')],
				[('我', 'N'), ('想', 'Vt'), ('吃', 'Vt'), ('很多', 'DET'), ('飯', 'N'), ('。', 'PERIODCATEGORY')]
			],
			[
				[('我', 'N'), ('吃飽', 'Vi'), ('了', 'T'), ('。', 'PERIODCATEGORY')],
			],
			])
		self.assertEqual(工具.斷詞('\n\n我想吃飯。我想吃很多飯。\n\n  \n\n  　 \n\n我吃飽了。\n\n'), [
			[
				[('我', 'N'), ('想', 'Vt'), ('吃飯', 'Vi'), ('。', 'PERIODCATEGORY')],
				[('我', 'N'), ('想', 'Vt'), ('吃', 'Vt'), ('很多', 'DET'), ('飯', 'N'), ('。', 'PERIODCATEGORY')]
			],
			[
				[('我', 'N'), ('吃飽', 'Vi'), ('了', 'T'), ('。', 'PERIODCATEGORY')],
			],
			])

	def test_官方斷詞工具標點符號(self):
		工具 = 官方斷詞剖析工具()
		self.assertEqual(工具.斷詞('> >'), [[
			[('&gt;', 'PARENTHESISCATEGORY'), ('&gt;', 'PARENTHESISCATEGORY')],
			]])
		self.assertEqual(工具.斷詞('我想) :>'), [[
			[('我', 'N'), ('想', 'Vt'), (')', 'PARENTHESISCATEGORY'), (':', 'COLONCATEGORY'), ('&gt;', 'PARENTHESISCATEGORY')],
			]])
		self.assertRaises(RuntimeError, 工具.斷詞, '我想) :<')

	def test_官方剖析工具(self):
		工具 = 官方斷詞剖析工具()
		self.assertEqual(工具.剖析('我想吃飯。我想吃很多飯。'), [[
 			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
 			'#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)'],
 			])
		self.assertEqual(工具.剖析('我想吃飯。我想吃很多飯。\n我吃飽了。'), [[
	 			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
	 			'#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)',
 			], [
	 			'#1:1.[0] S(NP(Head:N:我)|Head:Vi:吃飽|T:了)#。(PERIODCATEGORY)',
 			],
			])
		self.assertEqual(工具.剖析('\n\n我想吃飯。我想吃很多飯。\n\n  \n\n  　 \n\n我吃飽了。\n\n'), [[
	 			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
	 			'#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)',
 			], [
	 			'#1:1.[0] S(NP(Head:N:我)|Head:Vi:吃飽|T:了)#。(PERIODCATEGORY)',
 			],
			])

	def test_官方剖析工具標點符號(self):
		工具 = 官方斷詞剖析工具()
		self.assertEqual(工具.剖析('> >'), [[
			'#1:1.[0] NP(Head:N:&gt;&gt;)#',
			]])
		self.assertEqual(工具.剖析('我想) :>'), [[
			'#1:1.[0] S(NP(Head:N:我)|Head:Vt:想)#:(COLONCATEGORY)',
			]])
		self.assertRaises(RuntimeError, 工具.剖析, '我想) :<')

	def test_自設剖析工具(self):
		工具 = 自設剖析工具()
		self.assertEqual(工具.剖析('我想吃飯。我想吃很多飯。'),
			['#1:1.[0] S(agent:NP(Head:Nhaa:我)|Head:VE2:想|goal:VP(Head:VA4:吃飯))#。(PERIODCATEGORY)',
			'#2:1.[0] S(agent:NP(Head:Nhaa:我)|Head:VE2:想|goal:VP(Head:VC31:吃|theme:NP(quantifier:Neqa:很多|Head:Nab:飯)))#。(PERIODCATEGORY)'
			])

if __name__ == '__main__':
	unittest.main()
