# -*- coding: utf-8 -*-
import unittest
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.字 import 字


class 拆文分析器對齊單元試驗(unittest.TestCase):

    def test_對齊字孤字(self):
        型 = '媠'
        音 = 'ㄙㄨㄧˋ'
        字物件 = 拆文分析器.對齊字物件(型, 音)
        self.assertEqual(字物件.型, 型)
        self.assertEqual(字物件.音, 音)

    def test_對齊詞孤字(self):
        型 = '媠'
        音 = 'ㄙㄨㄧˋ'
        詞 = 拆文分析器.對齊詞物件(型, 音)
        self.assertEqual(len(詞.內底字), 1)
        self.assertEqual(詞.內底字[0].型, 型)
        self.assertEqual(詞.內底字[0].音, 音)
        self.assertEqual(詞.內底字[-1].型, 型)
        self.assertEqual(詞.內底字[-1].音, 音)

    def test_對齊組孤字(self):
        型 = '媠'
        音 = 'ㄙㄨㄧˋ'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        詞物件 = 拆文分析器.對齊詞物件(型, 音)
        self.assertEqual(len(組物件.內底詞), 1)
        self.assertEqual(組物件.內底詞[0], 詞物件)

    def test_對齊集孤字(self):
        型 = '媠'
        音 = 'ㄙㄨㄧˋ'
        集物件 = 拆文分析器.對齊集物件(型, 音)
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(len(集物件.內底組), 1)
        self.assertEqual(集物件.內底組[0], 組物件)

    def test_對齊句孤字(self):
        型 = '媠'
        音 = 'ㄙㄨㄧˋ'
        句物件 = 拆文分析器.對齊句物件(型, 音)
        集物件 = 拆文分析器.對齊集物件(型, 音)
        self.assertEqual(len(句物件.內底集), 1)
        self.assertEqual(句物件.內底集[0], 集物件)

    def test_對齊章孤字(self):
        型 = '媠'
        音 = 'ㄙㄨㄧˋ'
        章物件 = 拆文分析器.對齊章物件(型, 音)
        句物件 = 拆文分析器.對齊句物件(型, 音)
        self.assertEqual(len(章物件.內底句), 1)
        self.assertEqual(章物件.內底句[0], 句物件)

    def test_對齊詞濟字(self):
        詞型 = '媠姑娘'
        詞音 = 'sui2-koo1-niu5'
        詞 = 拆文分析器.對齊詞物件(詞型, 詞音)
        self.assertEqual(len(詞.內底字), 3)
        型一 = '媠'
        型二 = '姑'
        型三 = '娘'
        音一 = 'sui2'
        音二 = 'koo1'
        音三 = 'niu5'
        self.assertEqual(詞.內底字[0], 拆文分析器.對齊字物件(型一, 音一))
        self.assertEqual(詞.內底字[1], 拆文分析器.對齊字物件(型二, 音二))
        self.assertEqual(詞.內底字[2], 拆文分析器.對齊字物件(型三, 音三))

    def test_對齊詞濟字頭配教羅型(self):
        詞型 = 'tsa̍p-目'
        詞音 = 'tsa̍p-ba̍k'
        詞 = 拆文分析器.對齊詞物件(詞型, 詞音)
        self.assertEqual(len(詞.內底字), 2)
        型一 = 'tsa̍p'
        型二 = '目'
        音一 = 'tsa̍p'
        音二 = 'ba̍k'
        self.assertEqual(詞.內底字[0], 拆文分析器.對齊字物件(型一, 音一))
        self.assertEqual(詞.內底字[1], 拆文分析器.對齊字物件(型二, 音二))

    def test_對齊詞濟字尾配教羅型(self):
        詞型 = '雜-tso̍h'
        詞音 = 'tsa̍p-tso̍h'
        詞 = 拆文分析器.對齊詞物件(詞型, 詞音)
        self.assertEqual(len(詞.內底字), 2)
        型一 = '雜'
        型二 = 'tso̍h'
        音一 = 'tsa̍p'
        音二 = 'tso̍h'
        self.assertEqual(詞.內底字[0], 拆文分析器.對齊字物件(型一, 音一))
        self.assertEqual(詞.內底字[1], 拆文分析器.對齊字物件(型二, 音二))

    def test_對齊詞濟字有符號(self):
        詞型 = '媠姑娘？'
        詞音 = 'sui2-koo1-niu5-?'
        詞 = 拆文分析器.對齊詞物件(詞型, 詞音)
        self.assertEqual(len(詞.內底字), 4)
        型一 = '媠'
        型二 = '姑'
        型三 = '娘'
        型四 = '？'
        音一 = 'sui2'
        音二 = 'koo1'
        音三 = 'niu5'
        音四 = '?'
        self.assertEqual(詞.內底字[0], 拆文分析器.對齊字物件(型一, 音一))
        self.assertEqual(詞.內底字[1], 拆文分析器.對齊字物件(型二, 音二))
        self.assertEqual(詞.內底字[2], 拆文分析器.對齊字物件(型三, 音三))
        self.assertEqual(詞.內底字[3], 拆文分析器.對齊字物件(型四, 音四))

    def test_對齊詞濟字有空白(self):
        self.assertRaises(解析錯誤, 拆文分析器.對齊詞物件, '媠姑娘', 'sui2-koo1 niu5')
        self.assertRaises(解析錯誤, 拆文分析器.對齊詞物件, '媠姑娘', 'sui2 koo1 niu5')
        self.assertRaises(解析錯誤, 拆文分析器.對齊詞物件, '媠姑娘', 'sui2 koo1-niu5')
        self.assertRaises(解析錯誤, 拆文分析器.對齊詞物件, '媠姑娘？', 'sui2-koo1 niu5?')
        self.assertRaises(解析錯誤, 拆文分析器.對齊詞物件, '媠姑娘？', 'sui2-koo1-niu5?')

    def test_對齊詞客話懸降調(self):
        詞型 = '耳子'
        詞音 = 'ngi^-zu^'
        詞物件 = 拆文分析器.對齊詞物件(詞型, 詞音)
        型一 = '耳'
        型二 = '子'
        音一 = 'ngi^'
        音二 = 'zu^'
        self.assertEqual(len(詞物件.內底字), 2)
        self.assertEqual(詞物件.內底字[0], 拆文分析器.對齊字物件(型一, 音一))
        self.assertEqual(詞物件.內底字[1], 拆文分析器.對齊字物件(型二, 音二))

    def test_對齊組濟字(self):
        型 = '我有一張椅仔！'
        音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(len(組物件.內底詞), 5)
        self.assertEqual(組物件.內底詞, [
            拆文分析器.對齊詞物件('我', 'gua2'),
            拆文分析器.對齊詞物件('有', 'u7'),
            拆文分析器.對齊詞物件('一張', 'tsit8-tiunn1'),
            拆文分析器.對齊詞物件('椅仔', 'i2-a2'),
            拆文分析器.對齊詞物件('！', '!'),
        ])

    def test_對齊組濟字輕聲(self):
        型 = '物件無去矣！'
        加空白後音 = 'mi2-kiann7 boo5-0ki3 ah ! '
        組物件 = 拆文分析器.對齊組物件(型, 加空白後音)
        self.assertEqual(len(組物件.內底詞), 4)
        self.assertEqual(組物件.內底詞, [
            拆文分析器.對齊詞物件('物件', 'mi2-kiann7'),
            拆文分析器.對齊詞物件('無去', 'boo5-0ki3'),
            拆文分析器.對齊詞物件('矣', 'ah'),
            拆文分析器.對齊詞物件('！', '!'),
        ])

    def test_對齊組濟字注音(self):
        詞型 = '媠姑娘'
        詞音 = 'ㄙㄨㄧˋ ㄍㆦ ㄋㄧㄨˊ'
        組物件 = 拆文分析器.對齊組物件(詞型, 詞音)
        型一 = '媠'
        型二 = '姑'
        型三 = '娘'
        音一 = 'ㄙㄨㄧˋ'
        音二 = 'ㄍㆦ'
        音三 = 'ㄋㄧㄨˊ'
        self.assertEqual(len(組物件.內底詞), 3)
        self.assertEqual(組物件.內底詞[0], 拆文分析器.對齊詞物件(型一, 音一))
        self.assertEqual(組物件.內底詞[1], 拆文分析器.對齊詞物件(型二, 音二))
        self.assertEqual(組物件.內底詞[2], 拆文分析器.對齊詞物件(型三, 音三))

    def test_對齊詞客話音標(self):
        詞型 = '天頂落水'
        詞音 = 'tienˊ-dangˋ-log-suiˋ'
        詞物件 = 拆文分析器.對齊詞物件(詞型, 詞音)
        型一 = '天'
        型二 = '頂'
        型三 = '落'
        型四 = '水'
        音一 = 'tienˊ'
        音二 = 'dangˋ'
        音三 = 'log'
        音四 = 'suiˋ'
        self.assertEqual(len(詞物件.內底字), 4)
        self.assertEqual(詞物件.內底字[0], 拆文分析器.對齊字物件(型一, 音一))
        self.assertEqual(詞物件.內底字[1], 拆文分析器.對齊字物件(型二, 音二))
        self.assertEqual(詞物件.內底字[2], 拆文分析器.對齊字物件(型三, 音三))
        self.assertEqual(詞物件.內底字[3], 拆文分析器.對齊字物件(型四, 音四))

    def test_對齊組客話音標(self):
        詞型 = '天頂落水'
        詞音 = 'tienˊ-dangˋ log-suiˋ'
        組物件 = 拆文分析器.對齊組物件(詞型, 詞音)
        型一 = '天頂'
        型二 = '落水'
        音一 = 'tienˊ-dangˋ'
        音二 = 'log-suiˋ'
        self.assertEqual(len(組物件.內底詞), 2)
        self.assertEqual(組物件.內底詞[0], 拆文分析器.對齊詞物件(型一, 音一))
        self.assertEqual(組物件.內底詞[1], 拆文分析器.對齊詞物件(型二, 音二))

    def test_對齊組客話加號調(self):
        詞型 = '樹仔'
        詞音 = 'shu+ er'
        組物件 = 拆文分析器.對齊組物件(詞型, 詞音)
        型一 = '樹'
        型二 = '仔'
        音一 = 'shu+'
        音二 = 'er'
        self.assertEqual(len(組物件.內底詞), 2)
        self.assertEqual(組物件.內底詞[0], 拆文分析器.對齊詞物件(型一, 音一))
        self.assertEqual(組物件.內底詞[1], 拆文分析器.對齊詞物件(型二, 音二))

    def test_對齊組客話懸降調(self):
        詞型 = '耳子'
        詞音 = 'ngi^ zu^'
        組物件 = 拆文分析器.對齊組物件(詞型, 詞音)
        型一 = '耳'
        型二 = '子'
        音一 = 'ngi^'
        音二 = 'zu^'
        self.assertEqual(len(組物件.內底詞), 2)
        self.assertEqual(組物件.內底詞[0], 拆文分析器.對齊詞物件(型一, 音一))
        self.assertEqual(組物件.內底詞[1], 拆文分析器.對齊詞物件(型二, 音二))

    def test_客話音標對齊組(self):
        詞音 = 'tienˊ-dangˋ log-suiˋ'
        組物件 = 拆文分析器.對齊組物件(詞音, 詞音)
        音一 = 'tienˊ-dangˋ'
        音二 = 'log-suiˋ'
        self.assertEqual(len(組物件.內底詞), 2)
        self.assertEqual(組物件.內底詞[0], 拆文分析器.對齊詞物件(音一, 音一))
        self.assertEqual(組物件.內底詞[1], 拆文分析器.對齊詞物件(音二, 音二))

    def test_客話音標對齊組加號調(self):
        詞音 = 'shu+ er'
        組物件 = 拆文分析器.對齊組物件(詞音, 詞音)
        音一 = 'shu+'
        音二 = 'er'
        self.assertEqual(len(組物件.內底詞), 2)
        self.assertEqual(組物件.內底詞[0], 拆文分析器.對齊詞物件(音一, 音一))
        self.assertEqual(組物件.內底詞[1], 拆文分析器.對齊詞物件(音二, 音二))

    def test_客話音標對齊組懸降調(self):
        詞音 = 'ngi^ zu^'
        組物件 = 拆文分析器.對齊組物件(詞音, 詞音)
        音一 = 'ngi^'
        音二 = 'zu^'
        self.assertEqual(len(組物件.內底詞), 2)
        self.assertEqual(組物件.內底詞[0], 拆文分析器.對齊詞物件(音一, 音一))
        self.assertEqual(組物件.內底詞[1], 拆文分析器.對齊詞物件(音二, 音二))

    def test_對齊組濟字佮符號(self):
        詞型 = '枋寮漁港「大條巷」上闊兩公尺。'
        加空白後詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh . '
        組物件 = 拆文分析器.對齊組物件(詞型, 加空白後詞音)
        self.assertEqual(len(組物件.內底詞), 8)
        self.assertEqual(組物件.內底詞, [
            拆文分析器.對齊詞物件('枋寮', 'Pang-liau5'),
            拆文分析器.對齊詞物件('漁港', 'hi5-kang2'),
            拆文分析器.對齊詞物件('「', '「'),
            拆文分析器.對齊詞物件('大條巷', 'Tua7-tiau5-hang7'),
            拆文分析器.對齊詞物件('」', '」'),
            拆文分析器.對齊詞物件('上闊', 'siang7-khoah'),
            拆文分析器.對齊詞物件('兩公尺', 'nng7-kong-tshioh'),
            拆文分析器.對齊詞物件('。', '.'),
        ])

    def test_對齊組連字號漢羅(self):
        型 = 'gua有tsit8-tiunn1椅仔！'
        加空白後詞音 = 'gua2 u7 tsit8-tiunn1 i2-a2 ! '
        組物件 = 拆文分析器.對齊組物件(型, 加空白後詞音)
        self.assertEqual(len(組物件.內底詞), 5)
        self.assertEqual(組物件.內底詞, [
            拆文分析器.對齊詞物件('gua', 'gua2'),
            拆文分析器.對齊詞物件('有', 'u7'),
            拆文分析器.對齊詞物件('tsit8-tiunn1', 'tsit8-tiunn1'),
            拆文分析器.對齊詞物件('椅仔', 'i2-a2'),
            拆文分析器.對齊詞物件('！', '!'),
        ])

    def test_對齊組空白漢羅(self):
        型 = 'gua有tsit tiunn椅仔！'
        加空白後詞音 = 'gua2 u7 tsit8-tiunn1 i2-a2 ! '
        組物件 = 拆文分析器.對齊組物件(型, 加空白後詞音)
        self.assertEqual(len(組物件.內底詞), 5)
        self.assertEqual(組物件.內底詞, [
            拆文分析器.對齊詞物件('gua', 'gua2'),
            拆文分析器.對齊詞物件('有', 'u7'),
            拆文分析器.對齊詞物件('tsit tiunn', 'tsit8-tiunn1'),
            拆文分析器.對齊詞物件('椅仔', 'i2-a2'),
            拆文分析器.對齊詞物件('！', '!'),
        ])

    def test_對齊組一般符號(self):
        型 = '。'
        原來音 = '.'
        加空白後音 = ' . '
        組物件 = 拆文分析器.對齊組物件(型, 加空白後音)
        self.assertEqual(組物件.內底詞, [拆文分析器.對齊詞物件(型, 原來音)])
        self.assertEqual(拆文分析器.對齊組物件(型, 原來音), 組物件)

    def test_對齊組分字符號(self):
        型 = '-'
        空白型 = ' - '
        原來音 = '-'
        加空白後音 = ' - '
        組物件 = 拆文分析器.對齊組物件(空白型, 加空白後音)
        self.assertEqual(組物件.內底詞, [拆文分析器.對齊詞物件(型, 原來音)])
        組物件 = 拆文分析器.對齊組物件(型, 加空白後音)
        self.assertEqual(組物件.內底詞, [拆文分析器.對齊詞物件(型, 原來音)])
        組物件 = 拆文分析器.對齊組物件(型, 原來音)
        self.assertEqual(組物件.內底詞, [拆文分析器.對齊詞物件(型, 原來音)])
        組物件 = 拆文分析器.對齊組物件(空白型, 原來音)
        self.assertEqual(組物件.內底詞, [拆文分析器.對齊詞物件(型, 原來音)])

    def test_對齊組換逝(self):
        換逝 = '\n'
        組物件 = 拆文分析器.對齊組物件(換逝, 換逝)
        self.assertEqual(組物件.內底詞, [拆文分析器.對齊詞物件(換逝, 換逝)])
        self.assertEqual(組物件.內底詞[0].內底字, [字(換逝, 換逝)])

    def test_對齊組大寫專有符號袂使拆開(self):
        型 = 'H1N1 新型 流感 包含 四種 病毒'
        音 = 'H1N1 sin1-hing5 liu5-kam2 pau1-ham5 si3-tsiong2 pinn7-tok8'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(len(組物件.內底詞), 6)
        self.assertEqual(len(組物件.內底詞[0].內底字), 1)

    def test_對齊組小寫專有符號袂使拆開(self):
        型 = 'g0v 是 咱 的 好 厝邊'
        音 = 'g0v si7 lan2 e5 ho2 tshu3-pinn1'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(len(組物件.內底詞), 6)
        self.assertEqual(len(組物件.內底詞[0].內底字), 1)

    def test_對齊組大寫音標袂使拆開(self):
        # 愛予粗胚處理
        型 = 'Sui2sui2 是 咱 的 好 厝邊'
        音 = 'Sui2-sui2 si7 lan2 e5 ho2 tshu3-pinn1'
        self.assertRaises(解析錯誤, 拆文分析器.對齊組物件, 型, 音)

    def test_對齊組小寫音標袂使拆開(self):
        # 愛予粗胚處理
        型 = 'sui2sui2 是 咱 的 好 厝邊'
        音 = 'sui2-sui2 si7 lan2 e5 ho2 tshu3-pinn1'
        self.assertRaises(解析錯誤, 拆文分析器.對齊組物件, 型, 音)

    def test_對齊教羅符號(self):
        型音 = 'taⁿh'
        字物件 = 拆文分析器.對齊字物件(型音, 型音)
        詞物件 = 拆文分析器.對齊詞物件(型音, 型音)
        self.assertEqual(詞物件.內底字, [字物件])
        組物件 = 拆文分析器.對齊組物件(型音, 型音)
        self.assertEqual(組物件.內底詞, [詞物件])

    def test_對齊連紲教羅符號(self):
        型音 = 'taⁿtī'
        字物件 = 拆文分析器.對齊字物件(型音, 型音)
        詞物件 = 拆文分析器.對齊詞物件(型音, 型音)
        self.assertEqual(詞物件.內底字, [字物件])
        組物件 = 拆文分析器.對齊組物件(型音, 型音)
        self.assertEqual(組物件.內底詞, [詞物件])

    def test_對齊空佮空白(self):
        組物件 = 拆文分析器.對齊組物件('', '   ')
        self.assertEqual(組物件.內底詞, [])

    def test_對齊無仝數量空白(self):
        組物件 = 拆文分析器.對齊組物件(' ', '   ')
        self.assertEqual(組物件.內底詞, [])

    def test_莫插全形空白(self):
        漢字 = '意中人走佗藏'
        羅馬字 = 'Ì-tiong-lâng tsáu tó tshàng　'
        組物件 = 拆文分析器.對齊組物件(漢字, 羅馬字)
        self.assertEqual(組物件.篩出字物件()[-1].音, 'tshàng')

    def test_對齊物件對空白(self):
        with self.assertRaises(解析錯誤):
            拆文分析器.對齊組物件('sui2', '   ')

    def test_一字對無音(self):
        with self.assertRaises(解析錯誤):
            拆文分析器.對齊組物件('sui2', '')

    def test_對齊集濟字(self):
        型 = '我有一張椅仔！'
        加空白後詞音 = 'gua2 u7 tsit8-tiunn1 i2-a2 ! '
        集物件 = 拆文分析器.對齊集物件(型, 加空白後詞音)
        self.assertEqual(len(集物件.內底組), 1)
        self.assertEqual(集物件.內底組, [
            拆文分析器.對齊組物件(型, 加空白後詞音),
        ])

    def test_對齊集濟字注音(self):
        詞型 = '人生若有媠姑娘。'
        詞音 = 'ㆢㄧㄣˊ ㄒㄧㄥ ㄋㄚ˫ ㄨ˫ ㄙㄨㄧˋ ㄍㆦ ㄋㄧㄨˊ 。'
        集物件 = 拆文分析器.對齊集物件(詞型, 詞音)
        self.assertEqual(len(集物件.內底組), 1)
        self.assertEqual(集物件.內底組, [
            拆文分析器.對齊組物件(詞型, 詞音),
        ])

    def test_對齊集濟字佮符號(self):
        詞型 = '枋寮漁港「大條巷」上闊兩公尺。'
        加空白後詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh . '
        集物件 = 拆文分析器.對齊集物件(詞型, 加空白後詞音)
        self.assertEqual(len(集物件.內底組), 1)
        self.assertEqual(集物件.內底組, [
            拆文分析器.對齊組物件(詞型, 加空白後詞音),
        ])

    def test_對齊句濟字(self):
        型 = '我有一張椅仔！'
        音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
        句物件 = 拆文分析器.對齊句物件(型, 音)
        self.assertEqual(len(句物件.內底集), 1)
        self.assertEqual(句物件.內底集, [
            拆文分析器.對齊集物件(型, 音),
        ])

    def test_對齊句濟字注音(self):
        詞型 = '人生若有媠姑娘。'
        詞音 = 'ㆢㄧㄣˊ ㄒㄧㄥ ㄋㄚ˫ ㄨ˫ ㄙㄨㄧˋ ㄍㆦ ㄋㄧㄨˊ 。'
        句物件 = 拆文分析器.對齊句物件(詞型, 詞音)
        self.assertEqual(len(句物件.內底集), 1)
        self.assertEqual(句物件.內底集, [
            拆文分析器.對齊集物件(詞型, 詞音),
        ])

    def test_對齊句濟字佮符號(self):
        詞型 = '枋寮漁港「大條巷」上闊兩公尺。'
        加空白後詞音 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh . '
        句物件 = 拆文分析器.對齊句物件(詞型, 加空白後詞音)
        self.assertEqual(len(句物件.內底集), 1)
        self.assertEqual(句物件.內底集, [
            拆文分析器.對齊集物件(詞型, 加空白後詞音),
        ])

    def test_對齊章濟字(self):
        詞型 = '點仔膠，黏著跤，叫阿爸，買豬跤，豬跤箍仔焄爛爛，枵鬼囡仔流水瀾。'
        加空白後詞音 = (
            'tiam2-a2-ka1 , liam5-tioh8 kha1 , kio3 a1-pah4 , be2 ti1-kha1 , '
            'ti1-kha1 khoo1-a2 kun5 nua7-nua7 , iau1-kui2 gin2-a2 lau5 tsui2-nua7 . '
        )
        章物件 = 拆文分析器.對齊章物件(詞型, 加空白後詞音)
        self.assertEqual(章物件.內底句, [
            拆文分析器.對齊句物件('點仔膠，', 'tiam2-a2-ka1,'),
            拆文分析器.對齊句物件('黏著跤，', 'liam5-tioh8 kha1,'),
            拆文分析器.對齊句物件('叫阿爸，', 'kio3 a1-pah4,'),
            拆文分析器.對齊句物件('買豬跤，', 'be2 ti1-kha1,'),
            拆文分析器.對齊句物件('豬跤箍仔焄爛爛，', 'ti1-kha1 khoo1-a2 kun5 nua7-nua7,'),
            拆文分析器.對齊句物件('枵鬼囡仔流水瀾。', 'iau1-kui2 gin2-a2 lau5 tsui2-nua7.'),
        ])

    def test_對齊章頭尾分詞(self):
        答案 = 拆文分析器.對齊句物件('點仔膠，', 'tiam2-a2-ka1,')
        self.assertEqual(
            拆文分析器.對齊句物件(' 點仔膠，', 'tiam2-a2-ka1,'), 答案)
        self.assertEqual(
            拆文分析器.對齊句物件(' 點仔膠， ', 'tiam2-a2-ka1, '), 答案)
        self.assertEqual(
            拆文分析器.對齊句物件(' 點 仔膠， ', ' tiam2-a2-ka1  ,'), 答案)

    def test_對齊章濟符號(self):
        詞型 = '！！。。，。你好？'
        處理好詞音 = '!!..,.li2 ho2?'
        章物件 = 拆文分析器.對齊章物件(詞型, 處理好詞音)
        self.assertEqual(章物件.內底句, [
            拆文分析器.對齊句物件('！！。。，。', '!!..,.'),
            拆文分析器.對齊句物件('你好？', 'li2 ho2?'),
        ])
        加空白後詞型 = ' ！ ！ 。 。 ， 。 你好 ？ '
        加空白後詞音 = ' ! ! . . , . li2 ho2 ? '
        章物件 = 拆文分析器.對齊章物件(加空白後詞型, 加空白後詞音)
        self.assertEqual(章物件.內底句, [
            拆文分析器.對齊句物件('！！。。，。', ' ! ! . . , .'),
            拆文分析器.對齊句物件(' 你好？', ' li2 ho2?'),
        ])

    def test_對齊詞傳無仝濟字(self):
        型 = '姑娘'
        音 = 'ㄙㄨㄧˋ ㄍㆦ ㄋㄧㄨˊ'
        self.assertRaises(解析錯誤, 拆文分析器.對齊詞物件, 型, 音)
        self.assertRaises(解析錯誤, 拆文分析器.對齊詞物件, '', 音)
        self.assertRaises(解析錯誤, 拆文分析器.對齊詞物件, 型, '')
        self.assertRaises(解析錯誤, 拆文分析器.對齊詞物件, 型, 'sui2-koo1-miu5')

    def test_對齊章換逝(self):
        加空白後型 = '恁老母ti3佗位 ！ \n 恁老母ti3佗位 ！ '
        加空白後音 = 'lin1 lau3 bu2 ti3 to1 ui7 ! \n lin1 lau3 bu2 ti3 to1 ui7 ! '
        章物件 = 拆文分析器.對齊章物件(加空白後型, 加空白後音)
# 		print('@@',章物件.內底句[0])
# 		print('@@', [
# 			拆文分析器.對齊句物件('恁老母ti3佗位 ！ \n', 'lin1 lau3 bu2 ti3 to1 ui7 ! \n'),
# 			拆文分析器.對齊句物件(' 恁老母ti3佗位 ！', ' lin1 lau3 bu2 ti3 to1 ui7 !'),
# 			][0])
# 		self.assertEqual(章物件.內底句[0], [
# 			拆文分析器.對齊句物件('恁老母ti3佗位 ！ \n', 'lin1 lau3 bu2 ti3 to1 ui7 ! \n'),
# 			拆文分析器.對齊句物件(' 恁老母ti3佗位 ！', ' lin1 lau3 bu2 ti3 to1 ui7 !'),
# 			][0])
        self.assertEqual(章物件.內底句, [
            拆文分析器.對齊句物件('恁老母ti3佗位 ！ \n', 'lin1 lau3 bu2 ti3 to1 ui7 ! \n'),
            拆文分析器.對齊句物件(' 恁老母ti3佗位 ！', ' lin1 lau3 bu2 ti3 to1 ui7 !'),
        ])

    def test_對齊組型較濟(self):
        型 = '我有一張媠椅仔'
        音 = 'gua2 u7 tsit8-tiunn1 i2-a2'
        with self.assertRaises(解析錯誤):
            拆文分析器.對齊組物件(型, 音)

    def test_對齊組音較濟(self):
        型 = '有一張椅仔'
        音 = 'gua2 u7 tsit8-tiunn1 i2-a2'
        with self.assertRaises(解析錯誤):
            拆文分析器.對齊組物件(型, 音)

    def test_對齊集傳無仝濟字(self):
        型 = '我有一張媠椅仔！'
        音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
        self.assertRaises(解析錯誤, 拆文分析器.對齊集物件, 型, 音)
        型 = '有一張椅仔！'
        音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
        self.assertRaises(解析錯誤, 拆文分析器.對齊集物件, 型, 音)

    def test_對齊句傳無仝濟字(self):
        型 = '我有一張媠椅仔！'
        音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
        self.assertRaises(解析錯誤, 拆文分析器.對齊句物件, 型, 音)
        型 = '有一張椅仔！'
        音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
        self.assertRaises(解析錯誤, 拆文分析器.對齊句物件, 型, 音)

    def test_對齊章傳無仝濟字(self):
        型 = '我有一張媠椅仔！媠！'
        音 = 'gua2 u7 tsit8-tiunn1 i2-a2 !'
        self.assertRaises(解析錯誤, 拆文分析器.對齊章物件, 型, 音)
        型 = '有一張椅仔！'
        音 = 'gua2 u7 tsit8-tiunn1 i2-a2 ! sui2 !'
        self.assertRaises(解析錯誤, 拆文分析器.對齊章物件, 型, 音)

    def test_對齊字無字(self):
        型 = ''
        音 = ''
        self.assertRaises(解析錯誤, 拆文分析器.對齊字物件, 型, 音)

    def test_對齊詞無字(self):
        型 = ''
        音 = ''
        詞 = 拆文分析器.對齊詞物件(型, 音)
        self.assertEqual(len(詞.內底字), 0)

    def test_對齊組無字(self):
        型 = ''
        音 = ''
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(len(組物件.內底詞), 0)

    def test_對齊集無字(self):
        型 = ''
        音 = ''
        集物件 = 拆文分析器.對齊集物件(型, 音)
        self.assertEqual(len(集物件.內底組), 0)

    def test_對齊句無字(self):
        型 = ''
        音 = ''
        句物件 = 拆文分析器.對齊句物件(型, 音)
        self.assertEqual(len(句物件.內底集), 0)

    def test_對齊章無字(self):
        型 = ''
        音 = ''
        章物件 = 拆文分析器.對齊章物件(型, 音)
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
        self.assertRaises(型態錯誤, 拆文分析器.對齊詞物件, None, None)
        self.assertRaises(型態錯誤, 拆文分析器.對齊詞物件, [型一, 型二, 型三], 3)
        self.assertRaises(型態錯誤, 拆文分析器.對齊詞物件, [型一, 型二, 型三], None)
        self.assertRaises(型態錯誤, 拆文分析器.對齊詞物件, None, [音一, 音二, 音三])
        self.assertRaises(型態錯誤, 拆文分析器.對齊詞物件, [型一, 型二, None], [音一, 音二, 音三])
        self.assertRaises(型態錯誤, 拆文分析器.對齊詞物件, [型一, 型二, 型三], [音一, 音二, 3])

    def test_對齊組烏白傳(self):
        self.assertRaises(型態錯誤, 拆文分析器.對齊組物件, None, None)
        self.assertRaises(型態錯誤, 拆文分析器.對齊組物件, 'None', None)
        self.assertRaises(型態錯誤, 拆文分析器.對齊組物件, None, 'None')

    def test_對齊集烏白傳(self):
        self.assertRaises(型態錯誤, 拆文分析器.對齊集物件, None, None)
        self.assertRaises(型態錯誤, 拆文分析器.對齊集物件, '', None)
        self.assertRaises(型態錯誤, 拆文分析器.對齊集物件, None, '')

    def test_對齊句烏白傳(self):
        self.assertRaises(型態錯誤, 拆文分析器.對齊句物件, None, None)
        self.assertRaises(型態錯誤, 拆文分析器.對齊句物件, '', None)
        self.assertRaises(型態錯誤, 拆文分析器.對齊句物件, None, '')

    def test_對齊章烏白傳(self):
        self.assertRaises(型態錯誤, 拆文分析器.對齊章物件, None, None)
        self.assertRaises(型態錯誤, 拆文分析器.對齊章物件, '', None)
        self.assertRaises(型態錯誤, 拆文分析器.對齊章物件, None, '')

    def test_分號愛斷句(self):
        拆文分析器.對齊章物件(
            '僥倖錢，失德了；冤枉錢，跋輸筊。',
            'Hiau-hīng-tsînn, sit-tik liáu, uan-óng tsînn, pua̍h-su kiáu. '
        )

    def test_kaxabu辭典的oo音標(self):
        型 = '頭的全部'
        音 = 'thâu ê tsoân-pō•'
        拆文分析器.對齊句物件(型, 音)

    def test_kaxabu辭典的oo型(self):
        型 = 'thâu ê tsoân-pō•'
        音 = 'thâu ê tsoân-pō•'
        拆文分析器.對齊句物件(型, 音)

    def test_對齊章音標標點符號斷開(self):
        型 = '生理人初二、十六攏有拜土地公。'
        音 = 'Sing-lí-lâng tshe-jī, tsa̍p-la̍k lóng ū pài Thóo-tī-kong.'
        章物件 = 拆文分析器.對齊章物件(型, 音)
        self.assertEqual(len(章物件.內底句), 1)

    def test_對齊章漢字標點符號斷開(self):
        型 = '生理人初二、十六攏有拜土地公。'
        音 = 'Sing-lí-lâng tshe-jī、tsa̍p-la̍k lóng ū pài Thóo-tī-kong.'
        章物件 = 拆文分析器.對齊章物件(型, 音)
        self.assertEqual(len(章物件.內底句), 1)

    def test_對齊章標點符號斷句(self):
        型 = '生理人初二，十六攏有拜土地公。'
        音 = 'Sing-lí-lâng tshe-jī, tsa̍p-la̍k lóng ū pài Thóo-tī-kong.'
        章物件 = 拆文分析器.對齊章物件(型, 音)
        self.assertEqual(len(章物件.內底句), 2)

    def test_音標有華語而且華語當作一个詞(self):
        型 = '是華語叫做『陀螺』的「干樂」。'
        音 = 'sī huâ-gí kiò-tsò “陀螺” ê “kan-lo̍k”.'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(len(組物件.內底詞), 11)

    def test_客話聲調(self):
        組物件 = 拆文分析器.對齊組物件('𠊎當好！', 'ngaiˇ dong+-ho^ ！')
        self.assertEqual(len(組物件.篩出字物件()), 4)

    def test_標準刪節號(self):
        型 = '枋寮漁港……'
        音 = 'Pang-liau5 hi5-kang2...'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(len(組物件.網出詞物件()), 3)
        self.assertEqual(組物件.篩出字物件()[-1], 拆文分析器.對齊字物件('……', '...'))

    def test_刪節號佇句尾(self):
        型 = '枋寮漁港……。'
        音 = 'Pang-liau5 hi5-kang2....'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(len(組物件.網出詞物件()), 4)
        self.assertEqual(組物件.篩出字物件()[-2], 拆文分析器.對齊字物件('……', '...'))
        self.assertEqual(組物件.篩出字物件()[-1], 拆文分析器.對齊字物件('。', '.'))

    def test_刪節號減一點就對袂齊(self):
        型 = '枋寮漁港……'
        音 = 'Pang-liau5 hi5-kang2..'
        with self.assertRaises(解析錯誤):
            拆文分析器.對齊組物件(型, 音)

    def test_刪節號濟標點(self):
        型 = '針對講稿的內容、聲調、動作、表情、眼神……，'
        音 = 'tsiam-tuì káng-kó ê luē-iông, siann-tiāu, tōng-tsok, piáu-tsîng, gán-sîn...,'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(len(組物件.網出詞物件()), 14)

    def test_濟刪節號(self):
        型 = '啥物代誌？……………………'
        音 = 'Siánn-mih tāi-tsì?............'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(len(組物件.網出詞物件()), 7)

    def test_仝種刪節號敆做伙(self):
        刪節號 = '………....…'
        組物件 = 拆文分析器.對齊組物件(刪節號, 刪節號)
        self.assertEqual(len(組物件.網出詞物件()), 5)

    def test_純注音(self):
        注音 = 'ㄙㄨㄧˋ ㄍㆦ ㄋㄧㄨˊ'
        組物件 = 拆文分析器.對齊組物件(注音, 注音)
        self.assertEqual(len(組物件.網出詞物件()), 3)

    def test_純日文(self):
        日文 = "オートバイ"
        組物件 = 拆文分析器.對齊組物件(日文, 日文)
        self.assertEqual(len(組物件.篩出字物件()), 5)

    def test_台語前tab(self):
        型 = '千金小姐'
        音 = '\ttshian1-kim1-sio2-tsia2'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(組物件.篩出字物件()[0].看分詞(), '千｜tshian1')

    def test_漢字前tab(self):
        型 = '\t千金小姐'
        音 = 'tshian1-kim1-sio2-tsia2'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(組物件.篩出字物件()[0].看分詞(), '千｜tshian1')

    def test_台語後tab(self):
        型 = '千金小姐'
        音 = 'tshian1-kim1-sio2-tsia2\t'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(組物件.篩出字物件()[-1].看分詞(), '姐｜tsia2')

    def test_漢字後tab(self):
        型 = '千金小姐\t'
        音 = 'tshian1-kim1-sio2-tsia2'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(組物件.篩出字物件()[-1].看分詞(), '姐｜tsia2')

    def test_對齊攏是漢羅(self):
        型 = '0mh4按怎'
        音 = '0mh4按怎'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(len(組物件.篩出字物件()), 3)
        self.assertEqual(組物件.篩出字物件()[0].看分詞(), '0mh4｜0mh4')
        self.assertEqual(組物件.篩出字物件()[-1].看分詞(), '怎｜怎')

    def test_標點連做伙(self):
        漢 = '「Haih！喔～」'
        羅 = '“Haih! Ooh~”'
        組物件 = 拆文分析器.對齊組物件(漢, 羅)
        self.assertEqual(len(組物件.篩出字物件()), 6)

    def test_有大括對袂濟愛一般解析錯誤(self):
        漢 = '{Haih}'
        羅 = '{Haih'
        with self.assertRaises(解析錯誤):
            拆文分析器.對齊組物件(漢, 羅)

    def test_孤引號一ê(self):
        漢 = '『'
        羅 = "'"
        組物件 = 拆文分析器.對齊組物件(漢, 羅)
        self.assertEqual(len(組物件.篩出字物件()), 1)

    def test_孤引號tī詞內就是詞ê一部份(self):
        漢 = "學講 nga'ay ho"
        羅 = "O̍h kóng nga'ay ho"
        組物件 = 拆文分析器.對齊組物件(漢, 羅)
        self.assertEqual(len(組物件.篩出字物件()), 4)

    def test_孤引號邊仔有字就是詞ê一部份(self):
        漢 = "有教著 'a'adopen kah ngala' 遮ê詞"
        羅 = "Ū kàu-tio̍h 'a'adopen kah ngala' tsia ê sû"
        組物件 = 拆文分析器.對齊組物件(漢, 羅)
        self.assertEqual(len(組物件.篩出字物件()), 9)

    def test_孤引號佇句中(self):
        漢 = '是『風颱天』啦！'
        羅 = "Sī ' hong-thai-thinn ' lah!"
        組物件 = 拆文分析器.對齊組物件(漢, 羅)
        self.assertEqual(len(組物件.篩出字物件()), 8)
