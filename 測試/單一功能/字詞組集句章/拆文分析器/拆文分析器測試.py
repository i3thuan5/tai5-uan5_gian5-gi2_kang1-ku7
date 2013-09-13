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
		詞 = self.分析器.產生對齊詞(型, 音)
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
		型一 = '媠'
		型二 = '姑'
		型三 = '娘'
		音一 = 'sui2'
		音二 = 'koo1'
		音三 = 'niu5'
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

	def test_對齊組濟字佮符號(self):
		詞型 = '枋寮漁港「大條巷」上闊兩公尺。'
		詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh.'
		組物件 = self.分析器.產生對齊組(詞型, 詞音)
		self.assertEqual(len(組物件.內底詞), 8)
		self.assertEqual(組物件.內底詞, [
			self.分析器.產生對齊詞('枋寮', 'Pang-liau5'),
			self.分析器.產生對齊詞('漁港', 'hi5-kang2'),
			self.分析器.產生對齊詞('「', '「'),
			self.分析器.產生對齊詞('大條巷', 'Tua7-tiau5-hang7'),
			self.分析器.產生對齊詞('」', '」'),
			self.分析器.產生對齊詞('上闊', 'siang7-khoah'),
			self.分析器.產生對齊詞('兩公尺', 'nng7-kong-tshioh'),
			self.分析器.產生對齊詞('。', '.'),
			])

	def test_對齊組濟字漢羅(self):
		型 = 'gua有tsit8-tiunn1椅仔！'
		音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
		組物件 = self.分析器.產生對齊組(型, 音)
		self.assertEqual(len(組物件.內底詞), 5)
		self.assertEqual(組物件.內底詞, [
			self.分析器.產生對齊詞('gua', 'gua2'),
			self.分析器.產生對齊詞('有', 'u7'),
			self.分析器.產生對齊詞('tsit8-tiunn1', 'tsit8-tiunn1'),
			self.分析器.產生對齊詞('椅仔', 'i2-a2'),
			self.分析器.產生對齊詞('！', '!'),
			])
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
			self.分析器.產生對齊組(詞型, 詞音),
			])

	def test_對齊集濟字佮符號(self):
		詞型 = '枋寮漁港「大條巷」上闊兩公尺。'
		詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh.'
		集物件 = self.分析器.產生對齊集(詞型, 詞音)
		self.assertEqual(len(集物件.內底組), 1)
		self.assertEqual(集物件.內底組, [
			self.分析器.產生對齊組(詞型, 詞音),
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
		句物件 = self.分析器.產生對齊句(詞型, 詞音)
		self.assertEqual(len(句物件.內底集), 1)
		self.assertEqual(句物件.內底集, [
			self.分析器.產生對齊集(詞型, 詞音),
			])

	def test_對齊句濟字佮符號(self):
		詞型 = '枋寮漁港「大條巷」上闊兩公尺。'
		詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh.'
		句物件 = self.分析器.產生對齊句(詞型, 詞音)
		self.assertEqual(len(句物件.內底集), 1)
		self.assertEqual(句物件.內底集, [
			self.分析器.產生對齊集(詞型, 詞音),
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
			self.分析器.產生對齊句('枵鬼囡仔流水瀾。', 'iau1-kui2 gin2-a2 lau5 tsui2-nua7.'),
			])

	def test_對齊章濟符號(self):
		詞型 = '！！。。，。你好？'
		詞音 = '!!..,.li2 ho2?'
		章物件 = self.分析器.產生對齊章(詞型, 詞音)
		self.assertEqual(章物件.內底句, [
			self.分析器.產生對齊句('！！。。，。', '!!..,.'),
			self.分析器.產生對齊句('你好？', 'li2 ho2?'),
			])

	def test_對齊詞傳無仝濟字(self):
		型 = '姑娘'
		音 = 'ㄙㄨㄧˋ ㄍㆦ ㄋㄧㄨˊ'
		self.assertRaises(解析錯誤, self.分析器.產生對齊詞, 型, 音)
		self.assertRaises(解析錯誤, self.分析器.產生對齊詞, '', 音)
		self.assertRaises(解析錯誤, self.分析器.產生對齊詞, 型, '')
		self.assertRaises(解析錯誤, self.分析器.產生對齊詞, 型, 'sui2-koo1-miu5')

	def test_拆好陣列產生對齊詞傳無仝濟字(self):
		型一 = '媠'
		型二 = '姑'
		型三 = '娘'
		音一 = 'ㄙㄨㄧˋ'
		音二 = 'ㄍㆦ'
		音三 = 'ㄋㄧㄨˊ'
		self.assertRaises(解析錯誤, self.分析器.拆好陣列產生對齊詞, [型一, 型二, 型三], [音一, 音二])
		self.assertRaises(解析錯誤, self.分析器.拆好陣列產生對齊詞, [型一, 型二], [音一, 音二, 音三])
		self.assertRaises(解析錯誤, self.分析器.拆好陣列產生對齊詞, [型一, 型二, 型三], [])
		self.assertRaises(解析錯誤, self.分析器.拆好陣列產生對齊詞, [], [音一, 音二, 音三])

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
		self.assertRaises(型態錯誤, self.分析器.產生對齊字, 型, 音)

	def test_對齊詞無字(self):
		型 = ''
		音 = ''
		詞 = self.分析器.產生對齊詞(型, 音)
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
		self.assertEqual(len(集物件.內底組), 0)

	def test_對齊句無字(self):
		型 = ''
		音 = ''
		句物件 = self.分析器.產生對齊句(型, 音)
		self.assertEqual(len(句物件.內底集), 0)

	def test_對齊章無字(self):
		型 = ''
		音 = ''
		章物件 = self.分析器.產生對齊章(型, 音)
		self.assertEqual(型, '')
		self.assertEqual(音, '')
		self.assertEqual(章物件.內底句, [])
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

	def test_符號邊仔加空白(self):
		self.assertEqual(self.分析器.符號邊仔加空白('腹肚枵'), '腹肚枵')
		self.assertEqual(self.分析器.符號邊仔加空白('腹肚枵,'), '腹肚枵 ,')
		self.assertEqual(self.分析器.符號邊仔加空白(':sui2,koo1,niu5...'), ': sui2 , koo1 , niu5 . . .')
		self.assertEqual(self.分析器.符號邊仔加空白(' :sui2,   koo1 ,niu5 .  .  .  '), ': sui2 , koo1 , niu5 . . .')
		self.assertEqual(self.分析器.符號邊仔加空白(':sui2,koo1,niu5...'), ': sui2 , koo1 , niu5 . . .')
		self.assertEqual(self.分析器.符號邊仔加空白(':sui2,koo1,niu5..a.'), ': sui2 , koo1 , niu5 . . a .')
		self.assertEqual(self.分析器.符號邊仔加空白('sui2 koo1-niu5'), 'sui2 koo1-niu5')
		self.assertEqual(self.分析器.符號邊仔加空白('sui2 koo1  -  niu5'), 'sui2 koo1 - niu5')
		self.assertEqual(self.分析器.符號邊仔加空白('sui2 koo1--niu5'), 'sui2 koo1--niu5')
		self.assertEqual(self.分析器.符號邊仔加空白('sui2 koo1- -niu5'), 'sui2 koo1- -niu5')
		self.assertEqual(self.分析器.符號邊仔加空白('sui2 koo1 --niu5'), 'sui2 koo1 --niu5')
		self.assertEqual(self.分析器.符號邊仔加空白('sui2 koo1  --niu5'), 'sui2 koo1 --niu5')
		self.assertEqual(self.分析器.符號邊仔加空白('sui2 koo1-- niu5'), 'sui2 koo1-- niu5')
		self.assertEqual(self.分析器.符號邊仔加空白('sui2 koo1--   niu5'), 'sui2 koo1-- niu5')
		self.assertEqual(self.分析器.符號邊仔加空白('我有100箍'), '我有100箍')
		self.assertEqual(self.分析器.符號邊仔加空白('這馬時間12:20，'), '這馬時間12 : 20 ，')

	def test_拆句做字(self):
		self.assertEqual(self.分析器.拆句做字('腹肚枵'), ['腹', '肚', '枵'])
		self.assertRaises(型態錯誤, self.分析器.拆句做字, None)

	def test_拆句做字標點符號(self):
		self.assertEqual(self.分析器.拆句做字('腹肚枵。'), ['腹', '肚', '枵', '。'])
		self.assertEqual(self.分析器.拆句做字('！！。。，。'), ['！', '！', '。', '。', '，', '。'])
		self.assertEqual(self.分析器.拆句做字('!!..,.'), ['!', '!', '.', '.', ',', '.'])

	def test_拆句做字無愛空白(self):
		self.assertEqual(self.分析器.拆句做字('腹 肚枵矣'), ['腹', '肚', '枵', '矣'])
		self.assertEqual(self.分析器.拆句做字('  腹 肚枵矣  '), ['腹', '肚', '枵', '矣'])

	def test_拆句做字摻組字式(self):
		self.assertEqual(self.分析器.拆句做字('⿰因腹肚枵'), ['⿰因', '腹', '肚', '枵'])
		self.assertEqual(self.分析器.拆句做字('你同⿰厓去睡目。'), ['你', '同', '⿰厓', '去', '睡', '目', '。'])
		self.assertEqual(self.分析器.拆句做字('⿰22腹肚枵'), ['⿰2', '2', '腹', '肚', '枵'])
		self.assertRaises(解析錯誤, self.分析器.拆句做字, '腹肚枵⿰')
		self.assertRaises(解析錯誤, self.分析器.拆句做字, '腹肚枵⿰⿰')
		self.assertEqual(self.分析器.拆句做字('腹肚枵⿰⿰因'), ['腹', '肚', '枵', '⿰⿰因'])

	def test_拆句做字摻漢羅佮數字(self):
		self.assertEqual(self.分析器.拆句做字('腹肚枵ah'), ['腹', '肚', '枵', 'ah'])
		self.assertEqual(self.分析器.拆句做字('我e腹肚枵ah'), ['我', 'e', '腹', '肚', '枵', 'ah'])
		self.assertEqual(self.分析器.拆句做字('我ê腹肚枵ah'), ['我', 'ê', '腹', '肚', '枵', 'ah'])
		self.assertEqual(self.分析器.拆句做字('我ê pak tóo枵ah'), ['我', 'ê', 'pak', 'tóo', '枵', 'ah'])
		self.assertEqual(self.分析器.拆句做字('我ê pak-tóo枵ah'), ['我', 'ê', 'pak', 'tóo', '枵', 'ah'])
		self.assertEqual(self.分析器.拆句做字('我ê pak-tóo枵ah.'), ['我', 'ê', 'pak', 'tóo', '枵', 'ah', '.'])
		self.assertEqual(self.分析器.拆句做字('我ê pak-tóo枵ah,.'), ['我', 'ê', 'pak', 'tóo', '枵', 'ah', ',', '.'])
		self.assertEqual(self.分析器.拆句做字('我有100箍'), ['我', '有', '100', '箍', ])
		self.assertEqual(self.分析器.拆句做字('這馬時間12:20，'), ['這', '馬', '時', '間', '12', ':', '20', '，'])
		self.assertEqual(self.分析器.拆句做字('物件tsin1 ho2食。'), ['物', '件', 'tsin1', 'ho2', '食', '。'])

	def test_拆章做句(self):
		self.assertEqual(self.分析器.拆章做句('我腹肚枵，欲來去食飯。'), ['我腹肚枵，', '欲來去食飯。'])
		self.assertEqual(self.分析器.拆章做句('伊講：我腹肚枵，欲來去食飯。'), ['伊講：我腹肚枵，', '欲來去食飯。'])
		self.assertEqual(self.分析器.拆章做句('伊講:我腹肚枵，欲來去食飯。'), ['伊講:我腹肚枵，', '欲來去食飯。'])
		self.assertEqual(self.分析器.拆章做句('這馬分數1:2，誠緊張。'), ['這馬分數1:2，', '誠緊張。'])
		self.assertEqual(self.分析器.拆章做句('今日8/30。'), ['今日8/30。'])
		self.assertEqual(self.分析器.拆章做句('啥物！！？你轉去矣？'), ['啥物！！？', '你轉去矣？'])
		self.assertEqual(self.分析器.拆章做句('！！？你轉去？矣'), ['！！？', '你轉去？', '矣'])
		self.assertEqual(self.分析器.拆章做句('你！！？轉去？矣'), ['你！！？', '轉去？', '矣'])
		self.assertEqual(self.分析器.拆章做句('！你！？轉去？矣'), ['！', '你！？', '轉去？', '矣'])
		self.assertEqual(self.分析器.拆章做句('！你！？轉去？矣？？'), ['！', '你！？', '轉去？', '矣？？'])
		self.assertEqual(self.分析器.拆章做句('！！。。，。你好？'), ['！！。。，。', '你好？'])
		self.assertEqual(self.分析器.拆章做句('!!..,.li2 ho2?'), ['!!..,.', 'li2 ho2?'])
		self.assertEqual(self.分析器.拆章做句('!!..,.li2-ho2?'), ['!!..,.', 'li2-ho2?'])

if __name__ == '__main__':
	unittest.main()
