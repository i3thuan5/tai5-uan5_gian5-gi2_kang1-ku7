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
import unittest
from 臺灣言語工具.字音字型出題.揣閩南語辭典 import 揣閩南語題目
from 臺灣言語工具.字詞組集句章.解析整理.拆文分析器 import 拆文分析器
class 揣閩南語題目試驗(unittest.TestCase):
	def setUp(self):
		self.閩南語題目 = 揣閩南語題目()
		self.__分析器 = 拆文分析器()
	def tearDown(self):
		pass
	
	def test_三字(self):
		self.閩南語題目.資料.append((self.__分析器.產生對齊組('媠噹噹', 'sui2-tang1-tang1'), 3))
		答案 = [[('「媠」噹噹', '「sui2」-tang1-tang1')],
			[('媠「噹」噹', 'sui2-「tang1」-tang1')],[('媠噹「噹」', 'sui2-tang1-「tang1」')],
			]
		for 擺 in range(10):
			self.assertIn(self.閩南語題目.出題(1), 答案) 
	def test_四字(self):
		self.閩南語題目.資料.append((self.__分析器.產生對齊組('一心一意', 'it4-sim1-it4-i3'), 4))
		答案 = [[('「一」心一意', '「it4」-sim1-it4-i3')],[('一「心」一意', 'it4-「sim1」-it4-i3')],
			[('一心「一」意', 'it4-sim1-「it4」-i3')],[('一心一「意」', 'it4-sim1-it4-「i3」')],
			]
		for 擺 in range(10):
			self.assertIn(self.閩南語題目.出題(1), 答案)
	def test_輕聲(self):
		self.閩南語題目.資料.append((self.__分析器.產生對齊組('一來', 'it-0lâi'), 2))
		答案 = [[('「一」來', '「it」--lâi')], [('一「來」', 'it-「--lâi」')]]
		for 擺 in range(10):
			self.assertIn(self.閩南語題目.出題(1), 答案)
