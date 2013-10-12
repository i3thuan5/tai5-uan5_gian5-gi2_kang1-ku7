import unittest
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡

class 物件譀鏡測試(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.譀鏡 = 物件譀鏡()
	def tearDown(self):
		pass

	def test_看字(self):
		型 = '我'
		音 = 'gua2'
		字物件 = self.分析器.產生對齊字(型, 音)
		self.assertEqual(self.譀鏡.看型(字物件), 型)
		self.assertEqual(self.譀鏡.看音(字物件), 音)

	def test_看詞(self):
		型 = '姑娘'
		音 = 'koo1-niu5'
		詞物件 = self.分析器.產生對齊詞(型, 音)
		self.assertEqual(self.譀鏡.看型(詞物件), 型)
		self.assertEqual(self.譀鏡.看音(詞物件), 音)

	def test_看組孤字(self):
		型 = '恁老母ti3佗位！'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7 !'
		組物件 = self.分析器.產生對齊組(型, 音)
		self.assertEqual(self.譀鏡.看型(組物件), 型)
		self.assertEqual(self.譀鏡.看音(組物件), 音)

	def test_看組連字(self):
		型 = '恁老母ti3佗位！'
		音 = 'lin1 lau3-bu2 ti3 to1-ui7 !'
		組物件 = self.分析器.產生對齊組(型, 音)
		self.assertEqual(self.譀鏡.看型(組物件), 型)
		self.assertEqual(self.譀鏡.看音(組物件), 音)

	def test_看集(self):
		型 = '恁老母ti3佗位'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7'
		集物件 = self.分析器.產生對齊集(型, 音)
		self.assertEqual(self.譀鏡.看型(集物件), 型)
		self.assertEqual(self.譀鏡.看音(集物件), 音)

	def test_看集內底有兩組以上(self):
		型 = '恁老母ti3佗位'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7'
		集物件 = 集([self.分析器.產生對齊組(型, 音), self.分析器.產生對齊組(型, 音)])
		self.assertRaises(解析錯誤, self.譀鏡.看型, 集物件)
		self.assertRaises(解析錯誤, self.譀鏡.看音, 集物件)

	def test_看句(self):
		型 = '恁老母ti3佗位'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7'
		句物件 = self.分析器.產生對齊句(型, 音)
		self.assertEqual(self.譀鏡.看型(句物件), 型)
		self.assertEqual(self.譀鏡.看音(句物件), 音)

	def test_看章(self):
		型 = '恁老母ti3佗位！恁老母ti3佗位！'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7 ! lin1 lau3-bu2 ti3 to1-ui7 !'
		章物件 = self.分析器.產生對齊章(型, 音)
		self.assertEqual(self.譀鏡.看型(章物件), 型)
		self.assertEqual(self.譀鏡.看音(章物件), 音)

	def test_看章換符合(self):
		型 = '恁老母ti3佗位！恁老母ti3佗位！'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7 ! lin1 lau3 bu2 ti3 to1 ui7 !'
		章物件 = self.分析器.產生對齊組(型, 音)
		self.assertEqual(self.譀鏡.看型(章物件), 型)
		self.assertEqual(self.譀鏡.看音(章物件), 音)


if __name__ == '__main__':
	unittest.main()
