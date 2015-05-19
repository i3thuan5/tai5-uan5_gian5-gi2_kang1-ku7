import unittest


from 臺灣言語工具.翻譯.斷詞斷字翻譯 import 斷詞斷字翻譯
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.斷詞.中研院工具.官方斷詞剖析工具 import 官方斷詞剖析工具
from 臺灣言語工具.解析整理 import 物件譀鏡

class 翻譯整合試驗(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.譀鏡 = 物件譀鏡()
		
		self.官方斷詞剖析工具 = 官方斷詞剖析工具()
		self.斷詞斷字翻譯 = 斷詞斷字翻譯()
	def tearDown(self):
		pass

	def test_字串轉聲音檔(self):
		_編碼器 = 語句編碼器()
		斷詞用戶端 = 摩西用戶端('localhost', 8504, 編碼器=_編碼器)
		斷字用戶端 = 摩西用戶端('localhost', 8501, 編碼器=_編碼器)
		
		閩南語語句 = '我愛阿美'
		
		斷詞章物件 = self.官方斷詞剖析工具.斷詞(閩南語語句)
		self.assertEqual(self.譀鏡.看型(斷詞章物件, 物件分詞符號=' '), '我 愛 阿美')
		
		閩南語章物件 = self.斷詞斷字翻譯.譯(斷詞用戶端, 斷字用戶端, 斷詞章物件)
		self.assertEqual(self.譀鏡.看型(閩南語章物件, 物件分詞符號=' '), '我 愛 阿媠')
		self.assertEqual(self.譀鏡.看音(閩南語章物件, 物件分詞符號=' '), 'gua2 ai3 a1-sui2')
