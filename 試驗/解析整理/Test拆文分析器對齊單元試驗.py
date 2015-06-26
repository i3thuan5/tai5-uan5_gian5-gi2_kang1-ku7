# -*- coding: utf-8 -*-
import unittest
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 拆文分析器對齊單元試驗(unittest.TestCase):
    def setUp(self):
        self.分析器 = 拆文分析器()
        self.粗胚 = 文章粗胚()

    def tearDown(self):
        pass

    def test_對齊字孤字(self):
        型 = '媠'
        音 = 'ㄙㄨㄧˋ'
        字物件 = self.分析器.產生對齊字(型, 音)
        self.assertEqual(字物件.型, 型)
        self.assertEqual(字物件.音, 音)

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

    def test_對齊詞濟字頭配教羅型(self):
        詞型 = 'tsa̍p-目'
        詞音 = 'tsa̍p-ba̍k'
        詞 = self.分析器.產生對齊詞(詞型, 詞音)
        self.assertEqual(len(詞.內底字), 2)
        型一 = 'tsa̍p'
        型二 = '目'
        音一 = 'tsa̍p'
        音二 = 'ba̍k'
        self.assertEqual(詞.內底字[0], self.分析器.產生對齊字(型一, 音一))
        self.assertEqual(詞.內底字[1], self.分析器.產生對齊字(型二, 音二))

    def test_對齊詞濟字尾配教羅型(self):
        詞型 = '雜-tso̍h'
        詞音 = 'tsa̍p-tso̍h'
        詞 = self.分析器.產生對齊詞(詞型, 詞音)
        self.assertEqual(len(詞.內底字), 2)
        型一 = '雜'
        型二 = 'tso̍h'
        音一 = 'tsa̍p'
        音二 = 'tso̍h'
        self.assertEqual(詞.內底字[0], self.分析器.產生對齊字(型一, 音一))
        self.assertEqual(詞.內底字[1], self.分析器.產生對齊字(型二, 音二))

    def test_對齊詞濟字有符號(self):
        詞型 = '媠姑娘？'
        詞音 = 'sui2-koo1-niu5-?'
        詞 = self.分析器.產生對齊詞(詞型, 詞音)
        self.assertEqual(len(詞.內底字), 4)
        型一 = '媠'
        型二 = '姑'
        型三 = '娘'
        型四 = '？'
        音一 = 'sui2'
        音二 = 'koo1'
        音三 = 'niu5'
        音四 = '?'
        self.assertEqual(詞.內底字[0], self.分析器.產生對齊字(型一, 音一))
        self.assertEqual(詞.內底字[1], self.分析器.產生對齊字(型二, 音二))
        self.assertEqual(詞.內底字[2], self.分析器.產生對齊字(型三, 音三))
        self.assertEqual(詞.內底字[3], self.分析器.產生對齊字(型四, 音四))

    def test_對齊詞濟字有空白(self):
        self.assertRaises(解析錯誤, self.分析器.產生對齊詞, '媠姑娘', 'sui2-koo1 niu5')
        self.assertRaises(解析錯誤, self.分析器.產生對齊詞, '媠姑娘', 'sui2 koo1 niu5')
        self.assertRaises(解析錯誤, self.分析器.產生對齊詞, '媠姑娘', 'sui2 koo1-niu5')
        self.assertRaises(解析錯誤, self.分析器.產生對齊詞, '媠姑娘？', 'sui2-koo1 niu5?')
        self.assertRaises(解析錯誤, self.分析器.產生對齊詞, '媠姑娘？', 'sui2-koo1-niu5?')

    def test_對齊詞客話懸降調(self):
        詞型 = '耳子'
        詞音 = 'ngi^-zu^'
        詞物件 = self.分析器.產生對齊詞(詞型, 詞音)
        型一 = '耳'
        型二 = '子'
        音一 = 'ngi^'
        音二 = 'zu^'
        self.assertEqual(len(詞物件.內底字), 2)
        self.assertEqual(詞物件.內底字[0], self.分析器.產生對齊字(型一, 音一))
        self.assertEqual(詞物件.內底字[1], self.分析器.產生對齊字(型二, 音二))

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

    def test_對齊組濟字輕聲(self):
        型 = '物件無去矣！'
        原來音 = 'mi2-kiann7 boo5-0ki3 ah!'
        處理好音 = 'mi2-kiann7 boo5-0ki3 ah!'
        加空白後音 = 'mi2-kiann7 boo5-0ki3 ah ! '
        self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來音), 處理好音)
        self.assertEqual(self.粗胚.符號邊仔加空白(處理好音), 加空白後音)
        組物件 = self.分析器.產生對齊組(型, 加空白後音)
        self.assertEqual(len(組物件.內底詞), 4)
        self.assertEqual(組物件.內底詞, [
            self.分析器.產生對齊詞('物件', 'mi2-kiann7'),
            self.分析器.產生對齊詞('無去', 'boo5-0ki3'),
            self.分析器.產生對齊詞('矣', 'ah'),
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

    def test_對齊詞客話音標(self):
        詞型 = '天頂落水'
        詞音 = 'tienˊ-dangˋ-log-suiˋ'
        詞物件 = self.分析器.產生對齊詞(詞型, 詞音)
        型一 = '天'
        型二 = '頂'
        型三 = '落'
        型四 = '水'
        音一 = 'tienˊ'
        音二 = 'dangˋ'
        音三 = 'log'
        音四 = 'suiˋ'
        self.assertEqual(len(詞物件.內底字), 4)
        self.assertEqual(詞物件.內底字[0], self.分析器.產生對齊字(型一, 音一))
        self.assertEqual(詞物件.內底字[1], self.分析器.產生對齊字(型二, 音二))
        self.assertEqual(詞物件.內底字[2], self.分析器.產生對齊字(型三, 音三))
        self.assertEqual(詞物件.內底字[3], self.分析器.產生對齊字(型四, 音四))

    def test_對齊組客話音標(self):
        詞型 = '天頂落水'
        詞音 = 'tienˊ-dangˋ log-suiˋ'
        組物件 = self.分析器.產生對齊組(詞型, 詞音)
        型一 = '天頂'
        型二 = '落水'
        音一 = 'tienˊ-dangˋ'
        音二 = 'log-suiˋ'
        self.assertEqual(len(組物件.內底詞), 2)
        self.assertEqual(組物件.內底詞[0], self.分析器.產生對齊詞(型一, 音一))
        self.assertEqual(組物件.內底詞[1], self.分析器.產生對齊詞(型二, 音二))

    def test_對齊組客話加號調(self):
        詞型 = '樹仔'
        詞音 = 'shu+ er'
        組物件 = self.分析器.產生對齊組(詞型, 詞音)
        型一 = '樹'
        型二 = '仔'
        音一 = 'shu+'
        音二 = 'er'
        self.assertEqual(len(組物件.內底詞), 2)
        self.assertEqual(組物件.內底詞[0], self.分析器.產生對齊詞(型一, 音一))
        self.assertEqual(組物件.內底詞[1], self.分析器.產生對齊詞(型二, 音二))

    def test_對齊組客話懸降調(self):
        詞型 = '耳子'
        詞音 = 'ngi^ zu^'
        組物件 = self.分析器.產生對齊組(詞型, 詞音)
        型一 = '耳'
        型二 = '子'
        音一 = 'ngi^'
        音二 = 'zu^'
        self.assertEqual(len(組物件.內底詞), 2)
        self.assertEqual(組物件.內底詞[0], self.分析器.產生對齊詞(型一, 音一))
        self.assertEqual(組物件.內底詞[1], self.分析器.產生對齊詞(型二, 音二))

    def test_客話音標對齊組(self):
        詞音 = 'tienˊ-dangˋ log-suiˋ'
        組物件 = self.分析器.產生對齊組(詞音, 詞音)
        音一 = 'tienˊ-dangˋ'
        音二 = 'log-suiˋ'
        self.assertEqual(len(組物件.內底詞), 2)
        self.assertEqual(組物件.內底詞[0], self.分析器.產生對齊詞(音一, 音一))
        self.assertEqual(組物件.內底詞[1], self.分析器.產生對齊詞(音二, 音二))

    def test_客話音標對齊組加號調(self):
        詞音 = 'shu+ er'
        組物件 = self.分析器.產生對齊組(詞音, 詞音)
        音一 = 'shu+'
        音二 = 'er'
        self.assertEqual(len(組物件.內底詞), 2)
        self.assertEqual(組物件.內底詞[0], self.分析器.產生對齊詞(音一, 音一))
        self.assertEqual(組物件.內底詞[1], self.分析器.產生對齊詞(音二, 音二))

    def test_客話音標對齊組懸降調(self):
        詞音 = 'ngi^ zu^'
        組物件 = self.分析器.產生對齊組(詞音, 詞音)
        音一 = 'ngi^'
        音二 = 'zu^'
        self.assertEqual(len(組物件.內底詞), 2)
        self.assertEqual(組物件.內底詞[0], self.分析器.產生對齊詞(音一, 音一))
        self.assertEqual(組物件.內底詞[1], self.分析器.產生對齊詞(音二, 音二))

    def test_對齊組濟字佮符號(self):
        詞型 = '枋寮漁港「大條巷」上闊兩公尺。'
        原來詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh.'
        處理好詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh.'
        加空白後詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh . '
        self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來詞音), 處理好詞音)
        self.assertEqual(self.粗胚.符號邊仔加空白(處理好詞音), 加空白後詞音)
        組物件 = self.分析器.產生對齊組(詞型, 加空白後詞音)
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

    def test_對齊組濟字標點錯(self):
        詞型 = '枋寮漁港「大條巷」上闊兩。公尺'
        原來詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh.'
        處理好詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh.'
        加空白後詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh . '
        self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來詞音), 處理好詞音)
        self.assertEqual(self.粗胚.符號邊仔加空白(處理好詞音), 加空白後詞音)
        self.assertRaises(解析錯誤, self.分析器.產生對齊組, 詞型, 加空白後詞音)

    def test_對齊組連字號漢羅(self):
        型 = 'gua有tsit8-tiunn1椅仔！'
        原來詞音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
        處理好詞音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
        加空白後詞音 = 'gua2 u7 tsit8-tiunn1 i2-a2 ! '
        self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來詞音), 處理好詞音)
        self.assertEqual(self.粗胚.符號邊仔加空白(處理好詞音), 加空白後詞音)
        組物件 = self.分析器.產生對齊組(型, 處理好詞音)
        self.assertEqual(len(組物件.內底詞), 5)
        self.assertEqual(組物件.內底詞, [
            self.分析器.產生對齊詞('gua', 'gua2'),
            self.分析器.產生對齊詞('有', 'u7'),
            self.分析器.產生對齊詞('tsit8-tiunn1', 'tsit8-tiunn1'),
            self.分析器.產生對齊詞('椅仔', 'i2-a2'),
            self.分析器.產生對齊詞('！', '!'),
        ])
        self.assertEqual(組物件, self.分析器.產生對齊組(型, 加空白後詞音))
        減號後型 = self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 型)
        self.assertEqual(組物件, self.分析器.產生對齊組(減號後型, 處理好詞音))
        self.assertEqual(組物件, self.分析器.產生對齊組(減號後型, 加空白後詞音))

    def test_對齊組空白漢羅(self):
        型 = 'gua有tsit tiunn椅仔！'
        原來詞音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
        處理好詞音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
        加空白後詞音 = 'gua2 u7 tsit8-tiunn1 i2-a2 ! '
        self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來詞音), 處理好詞音)
        self.assertEqual(self.粗胚.符號邊仔加空白(處理好詞音), 加空白後詞音)
        組物件 = self.分析器.產生對齊組(型, 處理好詞音)
        self.assertEqual(len(組物件.內底詞), 5)
        self.assertEqual(組物件.內底詞, [
            self.分析器.產生對齊詞('gua', 'gua2'),
            self.分析器.產生對齊詞('有', 'u7'),
            self.分析器.產生對齊詞('tsit tiunn', 'tsit8-tiunn1'),
            self.分析器.產生對齊詞('椅仔', 'i2-a2'),
            self.分析器.產生對齊詞('！', '!'),
        ])
        self.assertEqual(
            組物件, self.分析器.產生對齊組(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 型), 處理好詞音))

    def test_對齊組一般符號(self):
        型 = '。'
        原來音 = '.'
        處理好音 = '.'
        加空白後音 = ' . '
        self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來音), 處理好音)
        self.assertEqual(self.粗胚.符號邊仔加空白(處理好音), 加空白後音)
        組物件 = self.分析器.產生對齊組(型, 加空白後音)
        self.assertEqual(組物件.內底詞, [self.分析器.產生對齊詞(型, 原來音)])
        self.assertEqual(self.分析器.產生對齊組(型, 原來音), 組物件)

    def test_對齊組分字符號(self):
        型 = '-'
        空白型 = ' - '
        原來音 = '-'
        處理好音 = ' - '
        加空白後音 = ' - '
        self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來音), 處理好音)
        self.assertEqual(self.粗胚.符號邊仔加空白(處理好音), 加空白後音)
        組物件 = self.分析器.產生對齊組(空白型, 加空白後音)
        self.assertEqual(組物件.內底詞, [self.分析器.產生對齊詞(型, 原來音)])
        組物件 = self.分析器.產生對齊組(型, 加空白後音)
        self.assertEqual(組物件.內底詞, [self.分析器.產生對齊詞(型, 原來音)])
        組物件 = self.分析器.產生對齊組(型, 原來音)
        self.assertEqual(組物件.內底詞, [self.分析器.產生對齊詞(型, 原來音)])
        組物件 = self.分析器.產生對齊組(空白型, 原來音)
        self.assertEqual(組物件.內底詞, [self.分析器.產生對齊詞(型, 原來音)])

    def test_對齊組大寫專有符號袂使拆開(self):
        型 = 'H1N1 新型 流感 包含 四種 病毒'
        音 = 'H1N1 sin1-hing5 liu5-kam2 pau1-ham5 si3-tsiong2 pinn7-tok8'
        組物件 = self.分析器.產生對齊組(型, 音)
        self.assertEqual(len(組物件.內底詞), 6)
        self.assertEqual(len(組物件.內底詞[0].內底字), 1)

    def test_對齊組小寫專有符號袂使拆開(self):
        型 = 'g0v 是 咱 的 好 厝邊'
        音 = 'g0v si7 lan2 e5 ho2 tshu3-pinn1'
        組物件 = self.分析器.產生對齊組(型, 音)
        self.assertEqual(len(組物件.內底詞), 6)
        self.assertEqual(len(組物件.內底詞[0].內底字), 1)

    def test_對齊組大寫音標袂使拆開(self):
        # 愛予粗胚處理
        型 = 'Sui2sui2 是 咱 的 好 厝邊'
        音 = 'Sui2-sui2 si7 lan2 e5 ho2 tshu3-pinn1'
        self.assertRaises(解析錯誤, self.分析器.產生對齊組, 型, 音)

    def test_對齊組小寫音標袂使拆開(self):
        # 愛予粗胚處理
        型 = 'sui2sui2 是 咱 的 好 厝邊'
        音 = 'sui2-sui2 si7 lan2 e5 ho2 tshu3-pinn1'
        self.assertRaises(解析錯誤, self.分析器.產生對齊組, 型, 音)

    def test_對齊教羅符號(self):
        型音 = 'taⁿh'
        字物件 = self.分析器.產生對齊字(型音, 型音)
        詞物件 = self.分析器.產生對齊詞(型音, 型音)
        self.assertEqual(詞物件.內底字, [字物件])
        組物件 = self.分析器.產生對齊組(型音, 型音)
        self.assertEqual(組物件.內底詞, [詞物件])

    def test_對齊連紲教羅符號(self):
        型音 = 'taⁿtī'
        字物件 = self.分析器.產生對齊字(型音, 型音)
        詞物件 = self.分析器.產生對齊詞(型音, 型音)
        self.assertEqual(詞物件.內底字, [字物件])
        組物件 = self.分析器.產生對齊組(型音, 型音)
        self.assertEqual(組物件.內底詞, [詞物件])

    def test_對齊集濟字(self):
        型 = '我有一張椅仔！'
        原來詞音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
        處理好詞音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
        加空白後詞音 = 'gua2 u7 tsit8-tiunn1 i2-a2 ! '
        self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來詞音), 處理好詞音)
        self.assertEqual(self.粗胚.符號邊仔加空白(處理好詞音), 加空白後詞音)
        集物件 = self.分析器.產生對齊集(型, 處理好詞音)
        self.assertEqual(len(集物件.內底組), 1)
        self.assertEqual(集物件.內底組, [
            self.分析器.產生對齊組(型, 處理好詞音),
        ])
        self.assertEqual(集物件,
                         self.分析器.產生對齊集(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 型), 加空白後詞音))

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
        原來詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh.'
        處理好詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh.'
        加空白後詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh . '
        self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來詞音), 處理好詞音)
        self.assertEqual(self.粗胚.符號邊仔加空白(處理好詞音), 加空白後詞音)
        集物件 = self.分析器.產生對齊集(詞型, 處理好詞音)
        self.assertEqual(len(集物件.內底組), 1)
        self.assertEqual(集物件.內底組, [
            self.分析器.產生對齊組(詞型, 處理好詞音),
        ])

    def test_對齊句濟字(self):
        型 = '我有一張椅仔！'
        音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
        音 = self.粗胚.符號邊仔加空白(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 音))
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
        原來詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh.'
        處理好詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh.'
        加空白後詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh . '
        self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來詞音), 處理好詞音)
        self.assertEqual(self.粗胚.符號邊仔加空白(處理好詞音), 加空白後詞音)
        句物件 = self.分析器.產生對齊句(詞型, 處理好詞音)
        self.assertEqual(len(句物件.內底集), 1)
        self.assertEqual(句物件.內底集, [
            self.分析器.產生對齊集(詞型, 處理好詞音),
        ])
        self.assertEqual(句物件, self.分析器.產生對齊句(詞型, 加空白後詞音))

    def test_對齊章濟字(self):
        詞型 = '點仔膠，黏著跤，叫阿爸，買豬跤，豬跤箍仔焄爛爛，枵鬼囡仔流水瀾。'
        原來詞音 = 'tiam2-a2-ka1, liam5-tioh8 kha1, kio3 a1-pah4, be2 ti1-kha1, ti1-kha1 khoo1-a2 kun5 nua7-nua7, iau1-kui2 gin2-a2 lau5 tsui2-nua7.'
        處理好詞音 = 'tiam2-a2-ka1, liam5-tioh8 kha1, kio3 a1-pah4, be2 ti1-kha1, ti1-kha1 khoo1-a2 kun5 nua7-nua7, iau1-kui2 gin2-a2 lau5 tsui2-nua7.'
        加空白後詞音 = 'tiam2-a2-ka1 , liam5-tioh8 kha1 , kio3 a1-pah4 , be2 ti1-kha1 , ti1-kha1 khoo1-a2 kun5 nua7-nua7 , iau1-kui2 gin2-a2 lau5 tsui2-nua7 . '
        self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來詞音), 處理好詞音)
        self.assertEqual(self.粗胚.符號邊仔加空白(處理好詞音), 加空白後詞音)
        章物件 = self.分析器.產生對齊章(詞型, 原來詞音)
        self.assertEqual(章物件.內底句, [
            self.分析器.產生對齊句('點仔膠，', 'tiam2-a2-ka1,'),
            self.分析器.產生對齊句('黏著跤，', 'liam5-tioh8 kha1,'),
            self.分析器.產生對齊句('叫阿爸，', 'kio3 a1-pah4,'),
            self.分析器.產生對齊句('買豬跤，', 'be2 ti1-kha1,'),
            self.分析器.產生對齊句('豬跤箍仔焄爛爛，', 'ti1-kha1 khoo1-a2 kun5 nua7-nua7,'),
            self.分析器.產生對齊句('枵鬼囡仔流水瀾。', 'iau1-kui2 gin2-a2 lau5 tsui2-nua7.'),
        ])
        self.assertEqual(章物件, self.分析器.產生對齊章(詞型, 處理好詞音))
        self.assertEqual(章物件, self.分析器.產生對齊章(詞型, 加空白後詞音))

    def test_對齊章頭尾分詞(self):
        答案 = self.分析器.產生對齊句('點仔膠，', 'tiam2-a2-ka1,')
        self.assertEqual(
            self.分析器.產生對齊句(' 點仔膠，', 'tiam2-a2-ka1,'), 答案)
        self.assertEqual(
            self.分析器.產生對齊句(' 點仔膠， ', 'tiam2-a2-ka1, '), 答案)
        self.assertEqual(
            self.分析器.產生對齊句(' 點 仔膠， ', ' tiam2-a2-ka1  ,'), 答案)

    def test_對齊章濟符號(self):
        詞型 = '！！。。，。你好？'
        原來詞音 = '!!..,.li2 ho2?'
        處理好詞音 = '!!..,.li2 ho2?'
        self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來詞音), 處理好詞音)
        章物件 = self.分析器.產生對齊章(詞型, 處理好詞音)
        self.assertEqual(章物件.內底句, [
            self.分析器.產生對齊句('！！。。，。', '!!..,.'),
            self.分析器.產生對齊句('你好？', 'li2 ho2?'),
        ])
        加空白後詞型 = ' ！ ！ 。 。 ， 。 你好 ？ '
        加空白後詞音 = ' ! ! . . , . li2 ho2 ? '
        self.assertEqual(self.粗胚.符號邊仔加空白(詞型), 加空白後詞型)
        self.assertEqual(self.粗胚.符號邊仔加空白(處理好詞音), 加空白後詞音)
        章物件 = self.分析器.產生對齊章(加空白後詞型, 加空白後詞音)
        self.assertEqual(章物件.內底句, [
            self.分析器.產生對齊句('！！。。，。', ' ! ! . . , .'),
            self.分析器.產生對齊句(' 你好？', ' li2 ho2?'),
        ])

    def test_對齊詞傳無仝濟字(self):
        型 = '姑娘'
        音 = 'ㄙㄨㄧˋ ㄍㆦ ㄋㄧㄨˊ'
        self.assertRaises(解析錯誤, self.分析器.產生對齊詞, 型, 音)
        self.assertRaises(解析錯誤, self.分析器.產生對齊詞, '', 音)
        self.assertRaises(解析錯誤, self.分析器.產生對齊詞, 型, '')
        self.assertRaises(解析錯誤, self.分析器.產生對齊詞, 型, 'sui2-koo1-miu5')

    def test_對齊章換逝(self):
        型 = '恁老母ti3佗位！\n恁老母ti3佗位！'
        加空白後型 = '恁老母ti3佗位 ！ \n 恁老母ti3佗位 ！ '
        音 = 'lin1 lau3 bu2 ti3 to1 ui7 ! \n lin1 lau3 bu2 ti3 to1 ui7 !'
        加空白後音 = 'lin1 lau3 bu2 ti3 to1 ui7 ! \n lin1 lau3 bu2 ti3 to1 ui7 ! '
        self.assertEqual(self.粗胚.符號邊仔加空白(型), 加空白後型)
        self.assertEqual(self.粗胚.符號邊仔加空白(音), 加空白後音)
        章物件 = self.分析器.產生對齊章(加空白後型, 加空白後音)
# 		print('@@',章物件.內底句[0])
# 		print('@@', [
# 			self.分析器.產生對齊句('恁老母ti3佗位 ！ \n', 'lin1 lau3 bu2 ti3 to1 ui7 ! \n'),
# 			self.分析器.產生對齊句(' 恁老母ti3佗位 ！', ' lin1 lau3 bu2 ti3 to1 ui7 !'),
# 			][0])
# 		self.assertEqual(章物件.內底句[0], [
# 			self.分析器.產生對齊句('恁老母ti3佗位 ！ \n', 'lin1 lau3 bu2 ti3 to1 ui7 ! \n'),
# 			self.分析器.產生對齊句(' 恁老母ti3佗位 ！', ' lin1 lau3 bu2 ti3 to1 ui7 !'),
# 			][0])
        self.assertEqual(章物件.內底句, [
            self.分析器.產生對齊句('恁老母ti3佗位 ！ \n', 'lin1 lau3 bu2 ti3 to1 ui7 ! \n'),
            self.分析器.產生對齊句(' 恁老母ti3佗位 ！', ' lin1 lau3 bu2 ti3 to1 ui7 !'),
        ])

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
        self.assertRaises(解析錯誤, self.分析器.產生對齊字, 型, 音)

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
