import unittest
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.基本元素.詞 import 詞
from 字詞組集句章.基本元素.組 import 組
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.基本元素.章 import 章
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤

class 拆文分析器測試(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
	def tearDown(self):
		pass
	
	def test_對齊字孤字(self):
		型 = '媠'
		音 = 'ㄙㄨㄧˋ'
		字物件 = self.分析器.產生對齊字(型, 音)
		self.assertEqual(字物件, 字(型, 音))

	def test_對齊詞孤字(self):
		型 = '媠'
		音 = 'ㄙㄨㄧˋ'
		詞 = self.分析器.產生對齊詞([型], [音])
		self.assertEqual(len(詞.內底字), 1)
		self.assertEqual(詞.內底字[0].型, 型)
		self.assertEqual(詞.內底字[0].音, 音)
		self.assertEqual(詞.內底字[-1].型, 型)
		self.assertEqual(詞.內底字[-1].音, 音)

	def test_對齊組孤字(self):
		型 = '媠'
		音 = 'ㄙㄨㄧˋ'
		組物件 = self.分析器.產生對齊組(型, 音)
		詞物件 = self.分析器.產生對齊詞(型, 音)
		self.assertEqual(len(組物件.內底詞), 1)
		self.assertEqual(組物件.內底詞[0], 詞物件)

	def test_對齊集孤字(self):
		型 = '媠'
		音 = 'ㄙㄨㄧˋ'
		集物件 = self.分析器.產生對齊集(型, 音)
		組物件 = self.分析器.產生對齊組(型, 音)
		self.assertEqual(len(集物件.內底組), 1)
		self.assertEqual(集物件.內底組[0], 組物件)

	def test_對齊句孤字(self):
		型 = '媠'
		音 = 'ㄙㄨㄧˋ'
		句物件 = self.分析器.產生對齊句(型, 音)
		集物件 = self.分析器.產生對齊集(型, 音)
		self.assertEqual(len(句物件.內底集), 1)
		self.assertEqual(句物件.內底集[0], 集物件)

	def test_對齊章孤字(self):
		型 = '媠'
		音 = 'ㄙㄨㄧˋ'
		章物件 = self.分析器.產生對齊章(型, 音)
		句物件 = self.分析器.產生對齊句(型, 音)
		self.assertEqual(len(章物件.內底句), 1)
		self.assertEqual(章物件.內底句[0], 句物件)

	def test_對齊詞濟字(self):
		詞型 = '媠姑娘'
		詞音 = 'sui2-koo1-niu5'
		詞 = self.分析器.產生對齊詞(詞型, 詞音)
		self.assertEqual(len(詞.內底字), 3)
		self.assertEqual(詞.內底字[0], self.分析器.產生對齊字(型一, 音一))
		self.assertEqual(詞.內底字[1], self.分析器.產生對齊字(型二, 音二))
		self.assertEqual(詞.內底字[2], self.分析器.產生對齊字(型三, 音三))

	def test_拆好陣列產生對齊詞濟字(self):
		詞型 = '媠姑娘'
		詞音 = 'sui2-koo1-niu5'
		詞 = self.分析器.產生對齊詞(詞型, 詞音)
		型一 = '媠'
		型二 = '姑'
		型三 = '娘'
		音一 = 'sui2'
		音二 = 'koo1'
		音三 = 'niu5'
		拆好陣列詞 = self.分析器.拆好陣列產生對齊詞([型一, 型二, 型三], [音一, 音二, 音三])
		self.assertEqual(詞.內底字[0].型, 型一)
		self.assertEqual(詞.內底字[0].音, 音一)
		self.assertEqual(詞.內底字[1].型, 型二)
		self.assertEqual(詞.內底字[1].音, 音二)
		self.assertEqual(詞.內底字[2].型, 型三)
		self.assertEqual(詞.內底字[2].音, 音三)
		self.assertEqual(詞.內底字[0], self.分析器.產生對齊字(型一, 音一))
		self.assertEqual(詞.內底字[1], self.分析器.產生對齊字(型二, 音二))
		self.assertEqual(詞.內底字[2], self.分析器.產生對齊字(型三, 音三))
		self.assertEqual(詞, 拆好陣列詞)

	def test_對齊組濟字(self):
		型 = '我有一張椅仔！'
		音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
		組物件 = self.分析器.產生對齊組(型, 音)
		self.assertEqual(len(組物件.內底詞), 5)
		self.assertEqual(組物件.內底詞, [
			self.分析器.產生對齊詞('我', 'gua2'),
			self.分析器.產生對齊詞('有', 'u7'),
			self.分析器.產生對齊詞('一張', 'tsit8-tiunn1'),
			self.分析器.產生對齊詞('椅仔', 'i2-a2'),
			self.分析器.產生對齊詞('！', '!'),
			])

	def test_對齊組濟字注音(self):
		詞型 = '媠姑娘'
		詞音 = 'ㄙㄨㄧˋ ㄍㆦ ㄋㄧㄨˊ'
		組物件 = self.分析器.產生對齊組(詞型, 詞音)
		型一 = '媠'
		型二 = '姑'
		型三 = '娘'
		音一 = 'ㄙㄨㄧˋ'
		音二 = 'ㄍㆦ'
		音三 = 'ㄋㄧㄨˊ'
		self.assertEqual(len(組物件.內底詞), 3)
		self.assertEqual(組物件.內底詞[0], self.分析器.產生對齊詞(型一, 音一))
		self.assertEqual(組物件.內底詞[1], self.分析器.產生對齊詞(型二, 音二))
		self.assertEqual(組物件.內底詞[2], self.分析器.產生對齊詞(型三, 音三))

	def test_對齊集濟字(self):
		型 = '我有一張椅仔！'
		音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
		集物件 = self.分析器.產生對齊集(型, 音)
		self.assertEqual(len(集物件.內底組), 1)
		self.assertEqual(集物件.內底組, [
			self.分析器.產生對齊組(型, 音),
			])

	def test_對齊集濟字注音(self):
		詞型 = '人生若有媠姑娘。'
		詞音 = 'ㆢㄧㄣˊ ㄒㄧㄥ ㄋㄚ˫ ㄨ˫ ㄙㄨㄧˋ ㄍㆦ ㄋㄧㄨˊ 。'
		集物件 = self.分析器.產生對齊集(詞型, 詞音)
		self.assertEqual(len(集物件.內底組), 1)
		self.assertEqual(集物件.內底組, [
			self.分析器.產生對齊組(型, 音),
			])

	def test_對齊句濟字(self):
		型 = '我有一張椅仔！'
		音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
		句物件 = self.分析器.產生對齊句(型, 音)
		self.assertEqual(len(句物件.內底集), 1)
		self.assertEqual(句物件.內底集, [
			self.分析器.產生對齊集(型, 音),
			])

	def test_對齊句濟字注音(self):
		詞型 = '人生若有媠姑娘。'
		詞音 = 'ㆢㄧㄣˊ ㄒㄧㄥ ㄋㄚ˫ ㄨ˫ ㄙㄨㄧˋ ㄍㆦ ㄋㄧㄨˊ 。'
		句物件 = self.分析器.產生對齊句(型, 音)
		self.assertEqual(len(句物件.內底集), 1)
		self.assertEqual(句物件.內底集, [
			self.分析器.產生對齊集(型, 音),
			])

	def test_對齊章濟字(self):
		詞型 = '點仔膠，黏著跤，叫阿爸，買豬跤，豬跤箍仔焄爛爛，枵鬼囡仔流水瀾。'
		詞音 = 'tiam2-a2-ka1, liam5-tioh8 kha1, kio3 a1-pah4, be2 ti1-kha1, ti1-kha1 khoo1-a2 kun5 nua7-nua7, iau1-kui2 gin2-a2 lau5 tsui2-nua7.'
		章物件 = self.分析器.產生對齊章(詞型, 詞音)
		self.assertEqual(章物件.內底句, [
			self.分析器.產生對齊句('點仔膠，', 'tiam2-a2-ka1,'),
			self.分析器.產生對齊句('黏著跤，', 'liam5-tioh8 kha1,'),
			self.分析器.產生對齊句('叫阿爸，', 'kio3 a1-pah4,'),
			self.分析器.產生對齊句('買豬跤，', 'be2 ti1-kha1,'),
			self.分析器.產生對齊句('豬跤箍仔焄爛爛，', 'ti1-kha1 khoo1-a2 kun5 nua7-nua7,'),
			self.分析器.產生對齊句('枵鬼囡仔流水爛。', 'iau1-kui2 gin2-a2 lau5 tsui2-nua7.'),
			])

	def test_對齊章濟符號(self):
		詞型 = '！！。。，。你好？'
		詞音 = '!!..,.li2 ho2?'
		章物件 = self.分析器.產生對齊章(詞型, 詞音)
		self.assertEqual(章物件.內底句, [
			self.分析器.產生對齊句('！', '!'),
			self.分析器.產生對齊句('！', '!'),
			self.分析器.產生對齊句('。', '.'),
			self.分析器.產生對齊句('。', '.'),
			self.分析器.產生對齊句('，', ','),
			self.分析器.產生對齊句('。', '/'),
			self.分析器.產生對齊句('你好？', 'liam5-tioh8 kha1,'),
			self.分析器.產生對齊句('', 'kio3 a1-pah4,'),
			self.分析器.產生對齊句('買豬跤，', 'li2 ho2?'),
			])

	def test_對齊詞傳無仝濟字(self):
		型一 = '媠'
		型二 = '姑'
		型三 = '娘'
		音一 = 'ㄙㄨㄧˋ'
		音二 = 'ㄍㆦ'
		音三 = 'ㄋㄧㄨˊ'
		self.assertRaises(解析錯誤, self.分析器.產生對齊詞, [型一, 型二, 型三], [音一, 音二])
		self.assertRaises(解析錯誤, self.分析器.產生對齊詞, [型一, 型二], [音一, 音二, 音三])
		self.assertRaises(解析錯誤, self.分析器.產生對齊詞, [型一, 型二, 型三], [])
		self.assertRaises(解析錯誤, self.分析器.產生對齊詞, [], [音一, 音二, 音三])
	def test_對齊組傳無仝濟字(self):
		型 = '我有一張媠椅仔！'
		音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
		self.assertRaises(解析錯誤, self.分析器.產生對齊組, 型, 音)
		型 = '有一張椅仔！'
		音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
		self.assertRaises(解析錯誤, self.分析器.產生對齊組, 型, 音)

	def test_對齊集傳無仝濟字(self):
		型 = '我有一張媠椅仔！'
		音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
		self.assertRaises(解析錯誤, self.分析器.產生對齊集, 型, 音)
		型 = '有一張椅仔！'
		音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
		self.assertRaises(解析錯誤, self.分析器.產生對齊集, 型, 音)

	def test_對齊句傳無仝濟字(self):
		型 = '我有一張媠椅仔！'
		音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
		self.assertRaises(解析錯誤, self.分析器.產生對齊句, 型, 音)
		型 = '有一張椅仔！'
		音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
		self.assertRaises(解析錯誤, self.分析器.產生對齊句, 型, 音)

	def test_對齊章傳無仝濟字(self):
		型 = '我有一張媠椅仔！媠！'
		音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
		self.assertRaises(解析錯誤, self.分析器.產生對齊章, 型, 音)
		型 = '有一張椅仔！'
		音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
		self.assertRaises(解析錯誤, self.分析器.產生對齊章, 型, 音)

	def test_對齊字無字(self):
		型 = ''
		音 = ''
		詞 = self.分析器.產生對齊字(型, 音)
		self.assertRaises(型態錯誤, self.分析器.產生對齊字, 型, 音)

	def test_對齊詞無字(self):
		型 = ''
		音 = ''
		詞 = self.分析器.產生對齊字(型, 音)
		self.assertEqual(len(詞.內底字), 0)

	def test_拆好陣列產生對齊詞無字(self):
		詞 = self.分析器.拆好陣列產生對齊詞([], [])
		self.assertEqual(len(詞.內底字), 0)

	def test_對齊組無字(self):
		型 = ''
		音 = ''
		組物件 = self.分析器.產生對齊組(型, 音)
		self.assertEqual(len(組物件.內底詞), 0)

	def test_對齊集無字(self):
		型 = ''
		音 = ''
		集物件 = self.分析器.產生對齊集(型, 音)
		self.assertEqual(len(集物件.內底詞), 0)

	def test_對齊句無字(self):
		型 = ''
		音 = ''
		句物件 = self.分析器.產生對齊句(型, 音)
		self.assertEqual(len(句物件.內底集), 0)

	def test_對齊章無字(self):
		型 = ''
		音 = ''
		章物件 = self.分析器.產生對齊章(型, 音)
		self.assertEqual(len(章物件.內底句), 0)

	def test_對齊詞烏白傳(self):
		型一 = '媠'
		型二 = '姑'
		型三 = '娘'
		音一 = 'ㄙㄨㄧˋ'
		音二 = 'ㄍㆦ'
		音三 = 'ㄋㄧㄨˊ'
		self.assertRaises(型態錯誤, self.分析器.產生對齊詞, None, None)
		self.assertRaises(型態錯誤, self.分析器.產生對齊詞, [型一, 型二, 型三], 3)
		self.assertRaises(型態錯誤, self.分析器.產生對齊詞, [型一, 型二, 型三], None)
		self.assertRaises(型態錯誤, self.分析器.產生對齊詞, None, [音一, 音二, 音三])
		self.assertRaises(型態錯誤, self.分析器.產生對齊詞, [型一, 型二, None], [音一, 音二, 音三])
		self.assertRaises(型態錯誤, self.分析器.產生對齊詞, [型一, 型二, 型三], [音一, 音二, 3])
	def test_對齊組烏白傳(self):
		self.assertRaises(型態錯誤, self.分析器.產生對齊組, None, None)
		self.assertRaises(型態錯誤, self.分析器.產生對齊組, None, None)
		self.assertRaises(型態錯誤, self.分析器.產生對齊組, None, None)
	def test_對齊集烏白傳(self):
		self.assertRaises(型態錯誤, self.分析器.產生對齊集, None, None)
		self.assertRaises(型態錯誤, self.分析器.產生對齊集, '', None)
		self.assertRaises(型態錯誤, self.分析器.產生對齊集, None, '')
	def test_對齊句烏白傳(self):
		self.assertRaises(型態錯誤, self.分析器.產生對齊句, None, None)
		self.assertRaises(型態錯誤, self.分析器.產生對齊句, '', None)
		self.assertRaises(型態錯誤, self.分析器.產生對齊句, None, '')
	def test_對齊章烏白傳(self):
		self.assertRaises(型態錯誤, self.分析器.產生對齊章, None, None)
		self.assertRaises(型態錯誤, self.分析器.產生對齊章, '', None)
		self.assertRaises(型態錯誤, self.分析器.產生對齊章, None, '')

	def tst_詞(self):
		print(標點處理工具.切開語句('bin5-si7-sin1-bun5-po3-to7'))
		print(標點處理工具.切開語句('tsit8-ui7 tan5-sio2-tsia2 kap4 han5-kok4-tsik8 e5 ang1-sai3 tshut4-kok4 ，'))
		print(標點處理工具.切開語句('bo5-siunn7-tioh8 thong1-kuan1 tsa1-giam7 ho1u7-tsio3 e5 si5-tsun7 ，'))
		print(標點處理工具.切開語句('pi7 ko1-hiong5 sio2-kang2-ki1-tiunn5 e5 tsa1-giam7-uan5 suan1-tshio3 。'))
		print(標點處理工具.切開語句('kong2 i1 ke3-ho1u7 tsit8-e5 bun5-hua3 「 thau1-khioh4-tsia2 」 ，'))
		print(標點處理工具.切開語句('khi3-kah8 tan5-sio2-tsia2 tong1-tiunn5 lau5-bak8-sai2 tshi1-tsham2-khau3 ，'))
		print(標點處理工具.切開語句('tshin1-iu2 hiong3 bin5-si7 sin1-bun5-tai5 tau5-ue7 。'))
		print(標點處理工具.切開語句('king1-kue3 hiong3 iu2-kuan1-tan1-ui7 tsa1-tsing3 ，'))
		print(標點處理工具.切開語句('i5-bin5-su2 than2-sing5 tsa1-giam7-uan5 sit4-gian5 ，'))
		print(標點處理工具.切開語句('i2-king1 tiau3-li7 hian7-tsit4 gian2-gi2 tshu2-hun1 。'))
		print(標點處理工具.切開語句('Pang-liau5 hi5-kang2 「 Toa7-tiau5-hang7 」 siang7-khoah nng7-kong-chhioh'))
		print(標點處理工具.計算音標語句音標數量('kau2-chap8-lak8-hoe3'))

if __name__ == '__main__':
	unittest.main()
