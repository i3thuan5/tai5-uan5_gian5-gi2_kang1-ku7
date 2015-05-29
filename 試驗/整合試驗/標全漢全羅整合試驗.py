from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
import unittest


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.表單.肯語句連詞 import 肯語句連詞
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
from 臺灣言語工具.斷詞.連詞揀集內組 import 連詞揀集內組
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡

class 標全漢全羅整合試驗(unittest.TestCase):
	def setUp(self):
		self.粗胚 = 文章粗胚()
		self.分析器 = 拆文分析器()
		self.家私 = 轉物件音家私()
		self.譀鏡 = 物件譀鏡()
		
		self.揣詞 = 拄好長度辭典揣詞()
		self.揀集內組 = 連詞揀集內組()
	def tearDown(self):
		pass

	@unittest.expectedFailure
	def test_字串斷詞後轉聲音檔(self):
		閩南語辭典 = ("PYRO:閩南語辭典@localhost:9839")
		閩南語連詞 = 肯語句連詞('語料/翻譯/閩.lm') 
		
		閩南語語句 = 'gua2 ai3 a1-sui2'
		
		處理減號 = self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 閩南語語句)
		章物件 = self.分析器.建立章物件(處理減號)
		標準章物件 = self.家私.轉音(臺灣閩南語羅馬字拼音, 章物件)
		斷詞章物件, _, _ = self.揣詞.揣詞(閩南語辭典, 標準章物件)
		選好章物件, _, _ = self.揀集內組.揀(閩南語連詞, 斷詞章物件)
		
		self.assertEqual(self.譀鏡.看音(選好章物件), 閩南語語句)
		self.assertEqual(self.譀鏡.看型(選好章物件), '我愛阿媠')
