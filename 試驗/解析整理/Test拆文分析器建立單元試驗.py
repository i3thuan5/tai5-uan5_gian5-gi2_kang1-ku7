# -*- coding: utf-8 -*-
import unittest
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.公用變數 import 無音


class 拆文分析器建立單元試驗(unittest.TestCase):

    def test_建立字孤字(self):
        型 = '媠'
        字物件 = 拆文分析器.建立字物件(型)
        self.assertEqual(字物件.型, 型)

    def test_建立字無字(self):
        型 = ''
        self.assertRaises(解析錯誤, 拆文分析器.建立字物件, 型)

    def test_建立詞孤字(self):
        型 = '媠'
        詞物件 = 拆文分析器.建立詞物件(型)
        self.assertEqual(len(詞物件.內底字), 1)
        self.assertEqual(詞物件.內底字[0].型, 型)
        self.assertEqual(詞物件.內底字[0].音, 無音)
        self.assertEqual(詞物件.內底字[0], 拆文分析器.建立字物件(型))

    def test_建立詞無字(self):
        型 = ''
        詞物件 = 拆文分析器.建立詞物件(型)
        self.assertEqual(len(詞物件.內底字), 0)
        self.assertEqual(詞物件.內底字, [])

    def test_建立詞濟字漢字(self):
        語句 = '椅仔！'
        self.assertEqual(拆文分析器.建立詞物件(語句).內底字,
                         [拆文分析器.建立字物件('椅'), 拆文分析器.建立字物件('仔'), 拆文分析器.建立字物件('！')])

    def test_建立詞濟字音標(self):
        語句 = 'tsit8-tiunn1 !'
        self.assertEqual(拆文分析器.建立詞物件(語句).內底字,
                         [拆文分析器.建立字物件('tsit8'), 拆文分析器.建立字物件('tiunn1'), 拆文分析器.建立字物件('!')])

    def test_建立詞濟字漢羅(self):
        語句 = 'tsit8-張!'
        self.assertEqual(拆文分析器.建立詞物件(語句).內底字,
                         [拆文分析器.建立字物件('tsit8'), 拆文分析器.建立字物件('張'), 拆文分析器.建立字物件('!')])

    def test_建立組聲調符號接音標(self):
        詞物件 = 拆文分析器.建立詞物件('suiˋsuiˋ')
        self.assertEqual(詞物件.內底字, [
            拆文分析器.建立字物件('suiˋ'), 拆文分析器.建立字物件('suiˋ')
        ])

    def test_建立組孤字(self):
        型 = '媠'
        組物件 = 拆文分析器.建立組物件(型)
        self.assertEqual(len(組物件.內底詞), 1)
        self.assertEqual(組物件.內底詞[0], 拆文分析器.建立詞物件(型))
        self.assertEqual(len(組物件.內底詞[0].內底字), 1)
        self.assertEqual(組物件.內底詞[0].內底字[0].型, 型)
        self.assertEqual(組物件.內底詞[0].內底字[0].音, 無音)
        self.assertEqual(組物件.內底詞[0].內底字[0], 拆文分析器.建立字物件(型))

    def test_建立組無字(self):
        型 = ''
        組物件 = 拆文分析器.建立組物件(型)
        self.assertEqual(len(組物件.內底詞), 0)
        self.assertEqual(組物件.內底詞, [])

    def 建立組檢查(self, 原來語句, 切好語句):
        return (拆文分析器.建立組物件(原來語句),
                [拆文分析器.建立詞物件(詞) for 詞 in 切好語句])

    def 建立組的切字檢查(self, 原來語句, 切好語句):
        切好詞陣列 = []
        for 一字 in 切好語句:
            詞物件 = 拆文分析器.建立詞物件('')
            詞物件.內底字.append(拆文分析器.建立字物件(一字))
            切好詞陣列.append(詞物件)
        return (拆文分析器.建立組物件(原來語句), 切好詞陣列)

    def test_建立組濟字(self):
        原來語句 = '我有一張椅仔！'
        切好語句 = ['我', '有', '一', '張', '椅', '仔', '！']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    # 為著通用佮一致性，這愛家己建立詞來鬥。大部份攏是無細膩揤著，親像平行語料庫才另外閣包一層
    def test_建立組濟字配空白(self):
        原來語句 = '我 有 一張 椅仔！'
        切好語句 = ['我', '有', '一', '張', '椅', '仔', '！']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組濟字有詞(self):
        原來語句 = '我有一-張椅仔！'
        切好語句 = ['我', '有', '一張', '椅', '仔', '！']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組濟字有詞配空白(self):
        原來語句 = '我 有 一-張 椅仔！'
        切好語句 = ['我', '有', '一張', '椅', '仔', '！']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組濟音標(self):
        加空白後語句 = 'gua2 u7 tsit8-tiunn1 i2-a2'
        切好語句 = ['gua2', 'u7', 'tsit8-tiunn1', 'i2-a2']
        組物件, 詞陣列 = self.建立組檢查(加空白後語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組濟字輕聲(self):
        加空白後語句 = 'mi2-kiann7 boo5-0ki3 ah ! '
        切好語句 = ['mi2-kiann7', 'boo5-0ki3', 'ah', '!']
        組物件, 詞陣列 = self.建立組檢查(加空白後語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組的組字式注音(self):
        原來語句 = '⿿⿿⿿ㄙㄨㄧˋ⿿ㄍㆦ⿿⿿⿿ㄋㄧㄨˊ'
        切好語句 = ['⿿⿿⿿ㄙㄨㄧˋ', '⿿ㄍㆦ', '⿿⿿⿿ㄋㄧㄨˊ']
        組物件, 詞陣列 = self.建立組的切字檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組的注音符號(self):
        原來語句 = 'ㄙㄨㄧˋ ㄍㆦ ㄋㄧㄨˊ'
        切好語句 = ['ㄙㄨㄧˋ', 'ㄍㆦ', 'ㄋㄧㄨˊ']
        組物件, 詞陣列 = self.建立組的切字檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組的注音摻漢字(self):
        原來語句 = 'ㄙㄨㄧˋ姑ㄋㄧㄨˊ'
        切好語句 = ['ㄙㄨㄧˋ', '姑', 'ㄋㄧㄨˊ']
        組物件, 詞陣列 = self.建立組的切字檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組的注音摻英文數字(self):
        原來語句 = 'threeㄙㄨㄧˋ3姑ㄋㄧㄨˊ'
        切好語句 = ['three', 'ㄙㄨㄧˋ', '3', '姑', 'ㄋㄧㄨˊ']
        組物件, 詞陣列 = self.建立組的切字檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組的注音摻數字調(self):
        原來語句 = 'ㄙㄨㄧ51姑ㄋㄧㄨˊ'
        切好語句 = ['ㄙㄨㄧ51', '姑', 'ㄋㄧㄨˊ']
        組物件, 詞陣列 = self.建立組的切字檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組的方言注音(self):
        原來語句 = 'ㆣㄨㄚˋ ㄍㆰˊ ㄗㄨㆪˋ'
        切好語句 = ['ㆣㄨㄚˋ', 'ㄍㆰˊ', 'ㄗㄨㆪˋ']
        組物件, 詞陣列 = self.建立組的切字檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組濟字佮符號(self):
        原來語句 = '枋寮漁港「大條巷」上闊兩公尺。'
        切好語句 = ['枋', '寮', '漁', '港', '「', '大', '條',
                '巷', '」', '上', '闊', '兩', '公', '尺', '。']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組濟連字佮符號(self):
        原來語句 = '枋-寮漁-港「大-條-巷」上-闊兩-公-尺。'
        切好語句 = ['枋寮', '漁港', '「', '大條巷', '」', '上闊', '兩公尺', '。']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組濟連紲連字(self):
        原來語句 = '欲看-一-个-無？'
        切好語句 = ['欲', '看一个無', '？']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組音標佮符號(self):
        加空白後語句 = 'Pang-liau5 hi5-kang2 「 Tua7-tiau5-hang7 」 siang7-khoah nng7-kong-tshioh . '
        切好語句 = ['Pang-liau5', 'hi5-kang2', '「', 'Tua7-tiau5-hang7', '」',
                'siang7-khoah', 'nng7-kong-tshioh', '.']
        組物件, 詞陣列 = self.建立組檢查(加空白後語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組濟字漢羅連字(self):
        加空白後語句 = 'gua有tsit8-tiunn1椅仔 ！ '
        切好語句 = ['gua', '有', 'tsit8-tiunn1', '椅', '仔', '！']
        組物件, 詞陣列 = self.建立組檢查(加空白後語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組濟字漢羅空白(self):
        原來語句 = 'gua u一張椅仔！'
        切好語句 = ['gua', 'u', '一', '張', '椅', '仔', '！']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組濟字算式(self):
        加空白後語句 = '所以是5 - 3 = 2 ! ! '
        切好語句 = ['所', '以', '是', '5', '-', '3', '=', '2', '!', '!']
        組物件, 詞陣列 = self.建立組檢查(加空白後語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組濟字其他符號(self):
        原來語句 = '伊18:30會來'
        切好語句 = ['伊', '18', ':', '30', '會', '來']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組減號(self):
        with self.assertRaises(解析錯誤):
            拆文分析器.建立組物件('--')

    def test_雙數字音標(self):
        原來語句 = 'gua51 ai51 li51'
        切好語句 = ['gua51', 'ai51', 'li51']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組濟字算式佮連字號(self):
        加空白後語句 = '食-0tsit8-kua5才來 ， 阮hak8-hau7佇大學路1001 - 1號 ， 儂莫走boo5-0ki3 。 '
        切好語句 = [
            '食-0tsit8-kua5', '才', '來', '，',
            '阮', 'hak8-hau7', '佇', '大', '學', '路', '1001', '-', '1', '號', '，',
            '儂', '莫', '走', 'boo5-0ki3', '。'
        ]
        組物件, 詞陣列 = self.建立組檢查(加空白後語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組濟字連字號尾(self):
        加空白後語句 = 'king2-tshat4 tsioh4-ue7 tsio1 sian3 - '
        切好語句 = [
            'king2-tshat4', 'tsioh4-ue7',
            'tsio1', 'sian3', '-'
        ]
        組物件, 詞陣列 = self.建立組檢查(加空白後語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_無空白分開的閩南語音標(self):
        有空白 = 'sui2 sui2 e5 koo1 niu5'
        無空白 = 有空白.replace(' ', '')
        self.assertNotEqual(拆文分析器.建立組物件(有空白), 拆文分析器.建立組物件(無空白))

    def test_無空白分開的音調音標(self):
        有空白 = 'sui55 sui51 e13 koo33 niu13'
        無空白 = 有空白.replace(' ', '')
        self.assertNotEqual(拆文分析器.建立組物件(有空白), 拆文分析器.建立組物件(無空白))

    def test_大寫專有符號袂寫拆開(self):
        無空白 = 'H1N1 新型 流感 包含 四種 病毒'
        有空白 = 'H1 N1 新型 流感 包含 四種 病毒'
        self.assertEqual(len(拆文分析器.建立組物件(無空白).內底詞), 11)
        self.assertNotEqual(拆文分析器.建立組物件(有空白), 拆文分析器.建立組物件(無空白))

    def test_小寫專有符號袂使拆開(self):
        無空白 = 'g0v 是 咱 的 好 厝邊'
        有空白 = 'g0 v 是 咱 的 好 厝邊'
        self.assertEqual(len(拆文分析器.建立組物件(無空白).內底詞),
                         7)
        self.assertNotEqual(
            拆文分析器.建立組物件(有空白), 拆文分析器.建立組物件(無空白))

    def test_大寫音標袂使拆開(self):
        # 愛予粗胚處理
        無空白 = 'Sui2sui2 是 咱 的 好 厝邊'
        有空白 = 'Sui2 sui2 是 咱 的 好 厝邊'
        self.assertEqual(len(拆文分析器.建立組物件(無空白).內底詞), 7)
        self.assertNotEqual(拆文分析器.建立組物件(有空白), 拆文分析器.建立組物件(無空白))

    def test_小寫音標袂使拆開(self):
        # 愛予粗胚處理
        無空白 = 'sui2sui2 是 咱 的 好 厝邊'
        有空白 = 'sui2 sui2 是 咱 的 好 厝邊'
        self.assertEqual(len(拆文分析器.建立組物件(無空白).內底詞), 7)
        self.assertNotEqual(拆文分析器.建立組物件(有空白), 拆文分析器.建立組物件(無空白))

    def test_建立集孤字(self):
        型 = '媠'
        集物件 = 拆文分析器.建立集物件(型)
        self.assertEqual(len(集物件.內底組), 1)
        self.assertEqual(集物件.內底組[0], 拆文分析器.建立組物件(型))
        組物件 = 集物件.內底組[0]
        self.assertEqual(len(組物件.內底詞), 1)
        self.assertEqual(組物件.內底詞[0], 拆文分析器.建立詞物件(型))
        self.assertEqual(len(組物件.內底詞[0].內底字), 1)
        self.assertEqual(組物件.內底詞[0].內底字[0].型, 型)
        self.assertEqual(組物件.內底詞[0].內底字[0].音, 無音)
        self.assertEqual(組物件.內底詞[0].內底字[0], 拆文分析器.建立字物件(型))

    def test_建立集無字(self):
        型 = ''
        集物件 = 拆文分析器.建立集物件(型)
        self.assertEqual(len(集物件.內底組), 0)
        self.assertEqual(集物件.內底組, [])

    def test_建立集濟字(self):
        語句 = '欲看-一-个-無？'
        集物件 = 拆文分析器.建立集物件(語句)
        self.assertEqual(集物件.內底組, [拆文分析器.建立組物件(語句)])

    def test_建立句孤字(self):
        型 = '媠'
        句物件 = 拆文分析器.建立句物件(型)
        self.assertEqual(len(句物件.內底集), 1)
        self.assertEqual(句物件.內底集[0], 拆文分析器.建立集物件(型))
        集物件 = 句物件.內底集[0]
        self.assertEqual(len(集物件.內底組), 1)
        self.assertEqual(集物件.內底組[0], 拆文分析器.建立組物件(型))
        組物件 = 集物件.內底組[0]
        self.assertEqual(len(組物件.內底詞), 1)
        self.assertEqual(組物件.內底詞[0], 拆文分析器.建立詞物件(型))
        self.assertEqual(len(組物件.內底詞[0].內底字), 1)
        self.assertEqual(組物件.內底詞[0].內底字[0].型, 型)
        self.assertEqual(組物件.內底詞[0].內底字[0].音, 無音)
        self.assertEqual(組物件.內底詞[0].內底字[0], 拆文分析器.建立字物件(型))

    def test_建立句無字(self):
        型 = ''
        句物件 = 拆文分析器.建立句物件(型)
        self.assertEqual(len(句物件.內底集), 0)
        self.assertEqual(句物件.內底集, [])

    def test_建立句濟字(self):
        語句 = '欲看-一-个-無？'
        句物件 = 拆文分析器.建立句物件(語句)
        self.assertEqual(句物件.內底集, [拆文分析器.建立集物件(語句)])

    def test_建立章孤字(self):
        型 = '媠'
        章物件 = 拆文分析器.建立章物件(型)
        self.assertEqual(len(章物件.內底句), 1)
        self.assertEqual(章物件.內底句[0], 拆文分析器.建立句物件(型))
        句物件 = 章物件.內底句[0]
        self.assertEqual(len(句物件.內底集), 1)
        self.assertEqual(句物件.內底集[0], 拆文分析器.建立集物件(型))
        集物件 = 句物件.內底集[0]
        self.assertEqual(len(集物件.內底組), 1)
        self.assertEqual(集物件.內底組[0], 拆文分析器.建立組物件(型))
        組物件 = 集物件.內底組[0]
        self.assertEqual(len(組物件.內底詞), 1)
        self.assertEqual(組物件.內底詞[0], 拆文分析器.建立詞物件(型))
        self.assertEqual(len(組物件.內底詞[0].內底字), 1)
        self.assertEqual(組物件.內底詞[0].內底字[0].型, 型)
        self.assertEqual(組物件.內底詞[0].內底字[0].音, 無音)
        self.assertEqual(組物件.內底詞[0].內底字[0], 拆文分析器.建立字物件(型))

    def test_建立章無字(self):
        型 = ''
        章物件 = 拆文分析器.建立章物件(型)
        self.assertEqual(len(章物件.內底句), 0)
        self.assertEqual(章物件.內底句, [])

    def test_建立章濟字(self):
        語句 = '欲看-一-个-無？點仔膠，黏著跤，叫阿爸，買豬跤，豬跤箍仔焄爛爛，枵鬼囡仔流水瀾。'
        章物件 = 拆文分析器.建立章物件(語句)
        self.assertEqual(章物件.內底句, [
            拆文分析器.建立句物件('欲看-一-个-無？'),
            拆文分析器.建立句物件('點仔膠，'),
            拆文分析器.建立句物件('黏著跤，'),
            拆文分析器.建立句物件('叫阿爸，'),
            拆文分析器.建立句物件('買豬跤，'),
            拆文分析器.建立句物件('豬跤箍仔焄爛爛，'),
            拆文分析器.建立句物件('枵鬼囡仔流水瀾。'),
        ])

    def test__拆句做字(self):
        self.assertEqual(拆文分析器._拆句做字('腹肚枵'), ['腹', '肚', '枵'])
        self.assertRaises(型態錯誤, 拆文分析器._拆句做字, None)

    def test__拆句做字標點符號(self):
        self.assertEqual(拆文分析器._拆句做字('腹肚枵。'), ['腹', '肚', '枵', '。'])
        self.assertEqual(
            拆文分析器._拆句做字('！！。。，。'), ['！', '！', '。', '。', '，', '。'])
        self.assertEqual(
            拆文分析器._拆句做字('!!..,.'), ['!', '!', '.', '.', ',', '.'])

    def test__拆句做字無愛空白(self):
        self.assertEqual(拆文分析器._拆句做字('腹 肚枵矣'), ['腹', '肚', '枵', '矣'])
        self.assertEqual(拆文分析器._拆句做字('  腹 肚枵矣  '), ['腹', '肚', '枵', '矣'])

    def test__拆句做字摻組字式(self):
        self.assertEqual(拆文分析器._拆句做字('⿰因腹肚枵'), ['⿰因', '腹', '肚', '枵'])
        self.assertEqual(
            拆文分析器._拆句做字('你同⿰厓去睡目。'), ['你', '同', '⿰厓', '去', '睡', '目', '。'])
        self.assertEqual(拆文分析器._拆句做字('⿰22腹肚枵'), ['⿰2', '2', '腹', '肚', '枵'])
        self.assertRaises(解析錯誤, 拆文分析器._拆句做字, '腹肚枵⿰')
        self.assertRaises(解析錯誤, 拆文分析器._拆句做字, '腹肚枵⿰⿰')
        self.assertEqual(拆文分析器._拆句做字('腹肚枵⿰⿰因'), ['腹', '肚', '枵', '⿰⿰因'])

    def test__拆句做字摻漢羅佮數字(self):
        self.assertEqual(拆文分析器._拆句做字('腹肚枵ah'), ['腹', '肚', '枵', 'ah'])
        self.assertEqual(
            拆文分析器._拆句做字('我e腹肚枵ah'), ['我', 'e', '腹', '肚', '枵', 'ah'])
        self.assertEqual(
            拆文分析器._拆句做字('我ê腹肚枵ah'), ['我', 'ê', '腹', '肚', '枵', 'ah'])
        self.assertEqual(
            拆文分析器._拆句做字('我ê pak tóo枵ah'), ['我', 'ê', 'pak', 'tóo', '枵', 'ah'])
        self.assertEqual(
            拆文分析器._拆句做字('我ê pak-tóo枵ah'), ['我', 'ê', 'pak', 'tóo', '枵', 'ah'])
        self.assertEqual(
            拆文分析器._拆句做字('我ê pak - tóo枵ah'), ['我', 'ê', 'pak', '-', 'tóo', '枵', 'ah'])
        self.assertEqual(
            拆文分析器._拆句做字('我ê pak-tóo枵ah.'), ['我', 'ê', 'pak', 'tóo', '枵', 'ah', '.'])
        self.assertEqual(
            拆文分析器._拆句做字('我ê pak-tóo枵ah,.'), ['我', 'ê', 'pak', 'tóo', '枵', 'ah', ',', '.'])
        self.assertEqual(拆文分析器._拆句做字('我有100箍'), ['我', '有', '100', '箍', ])
        self.assertEqual(
            拆文分析器._拆句做字('這馬時間12:20，'), ['這', '馬', '時', '間', '12', ':', '20', '，'])
        self.assertEqual(
            拆文分析器._拆句做字('物件tsin1 ho2食。'), ['物', '件', 'tsin1', 'ho2', '食', '。'])

    def test__拆句做巢狀詞摻漢羅佮數字(self):
        self.assertEqual(
            拆文分析器._拆句做巢狀詞('腹肚枵ah'), [['腹'], ['肚'], ['枵'], ['ah']])
        self.assertEqual(
            拆文分析器._拆句做巢狀詞('我ê腹肚枵ah'), [['我'], ['ê'], ['腹'], ['肚'], ['枵'], ['ah']])
        self.assertEqual(拆文分析器._拆句做巢狀詞('我ê pak tóo枵ah'),
                         [['我'], ['ê'], ['pak'], ['tóo'], ['枵'], ['ah']])
        self.assertEqual(
            拆文分析器._拆句做巢狀詞('我ê pak-tóo枵ah'), [['我'], ['ê'], ['pak', 'tóo'], ['枵'], ['ah']])
        self.assertEqual(拆文分析器._拆句做巢狀詞(
            '我ê pak - tóo枵ah'), [['我'], ['ê'], ['pak'], ['-'], ['tóo'], ['枵'], ['ah']])

    def test__拆句做巢狀詞摻組字式(self):
        原本語句 = '⿰---⿰-- - ⿱--,⿰-,⿱⿰-,--⿱--'
        斷詞後巢狀陣列 = [['⿰--', '⿰--'], ['-'], ['⿱--'],
                   [','], ['⿰-,'], ['⿱⿰-,-', '⿱--']]
        self.assertEqual(拆文分析器._拆句做巢狀詞(原本語句), 斷詞後巢狀陣列)

    def test__拆章做句(self):
        self._拆章做句('我腹肚枵，欲來去食飯。', ['我腹肚枵，', '欲來去食飯。'])
        self._拆章做句('伊講：我腹肚枵，欲來去食飯。', ['伊講：我腹肚枵，', '欲來去食飯。'])
        self._拆章做句('伊講:我腹肚枵，欲來去食飯。', ['伊講:我腹肚枵，', '欲來去食飯。'])
        self._拆章做句('這馬分數1:2，誠緊張。', ['這馬分數1:2，', '誠緊張。'])
        self._拆章做句('今日8/30。', ['今日8/30。'])
        self._拆章做句('啥物！！？你轉去矣？', ['啥物！！？', '你轉去矣？'])
        self._拆章做句('！！？你轉去？矣', ['！！？', '你轉去？', '矣'])
        self._拆章做句('你！！？轉去？矣', ['你！！？', '轉去？', '矣'])
        self._拆章做句('！你！？轉去？矣', ['！', '你！？', '轉去？', '矣'])
        self._拆章做句('！你！？轉去？矣？？', ['！', '你！？', '轉去？', '矣？？'])
        self._拆章做句('！！。。，。你好？', ['！！。。，。', '你好？'])

    def _拆章做句(self, 語句, 答案):
        self.assertEqual(
            [句物件.看型() for 句物件 in 拆文分析器.建立章物件(語句).內底句],
            答案
        )

    def test__拆章做句配分詞符號(self):
        原來 = '!!..,.li2-ho2?'
        加空白 = ' ! ! . . , . li2-ho2 ? '
        答案 = ['! ! . . , .', 'li2-ho2 ?']
        self.assertEqual(
            [
                拆文分析器.建立章物件(原來).內底句[0].看分詞(),
                拆文分析器.建立章物件(原來).內底句[1].看分詞(),
            ],
            答案
        )
        self.assertEqual(
            [
                拆文分析器.建立章物件(加空白).內底句[0].看分詞(),
                拆文分析器.建立章物件(加空白).內底句[1].看分詞(),
            ],
            答案
        )

    def test__拆章做句有分字符號配分詞符號(self):
        加空白 = 'tsong-biau7 bo5 tse3 ” , - - - tsiah e5 ue7 , '
        空白答案 = ['tsong-biau7 bo5 tse3 ” , ', ' - - - tsiah e5 ue7 , ']
        self.assertEqual(len(拆文分析器.建立章物件(加空白).內底句),
                         2)
        self.assertEqual(拆文分析器.建立章物件(加空白).內底句[0],
                         拆文分析器.建立句物件(空白答案[0]))
        self.assertEqual(拆文分析器.建立章物件(加空白).內底句[1],
                         拆文分析器.建立句物件(空白答案[1]))

    def test_外來語拉鍊(self):
        拆文分析器.對齊組物件(
            '拉鍊',
            'la55-lian51'
        )

    def test_字物件語句毋是字串(self):
        with self.assertRaises(型態錯誤):
            拆文分析器.建立字物件(['k', 'o', 'n', 'n'])

    def test_詞物件語句毋是字串(self):
        with self.assertRaises(型態錯誤):
            拆文分析器.建立詞物件(['k', 'o', 'n', 'n'])

    def test_組物件語句毋是字串(self):
        with self.assertRaises(型態錯誤):
            拆文分析器.建立組物件(['k', 'o', 'n', 'n'])

    def test_集物件語句毋是字串(self):
        with self.assertRaises(型態錯誤):
            拆文分析器.建立集物件(['k', 'o', 'n', 'n'])

    def test_句物件語句毋是字串(self):
        with self.assertRaises(型態錯誤):
            拆文分析器.建立句物件(['k', 'o', 'n', 'n'])

    def test_章物件語句毋是字串(self):
        with self.assertRaises(型態錯誤):
            拆文分析器.建立章物件(['k', 'o', 'n', 'n'])

    def test_南島用字物件(self):
        字物件 = 拆文分析器.建立字物件("Nga'ay")
        self.assertEqual(字物件.型, "Nga'ay")
        self.assertEqual(字物件.音, 無音)

    def test_南島詞袂切開(self):
        詞物件 = 拆文分析器.建立詞物件("Nga'ay")
        self.assertEqual(詞物件.內底字, [拆文分析器.建立字物件("Nga'ay")])

    def test_南島組有照切(self):
        組物件 = 拆文分析器.建立組物件("Nga'ay ho?")
        self.assertEqual(組物件.內底詞, [
            拆文分析器.建立詞物件("Nga'ay"),
            拆文分析器.建立詞物件("ho"),
            拆文分析器.建立詞物件("?"),
        ])

    def test_南島語句(self):
        self.assertEqual(
            拆文分析器.建立句物件("Nga'ay ho?").網出詞物件(),
            拆文分析器.建立組物件("Nga'ay ho?").網出詞物件(),
        )

    def test_客話聲調(self):
        self.assertEqual(len(拆文分析器.建立句物件('ngaiˇ dong+-ho^ ！').篩出字物件()), 4)

    def test_標準刪節號(self):
        組物件 = 拆文分析器.建立組物件('Pang-liau5 hi5-kang2...')
        self.assertEqual(len(組物件.網出詞物件()), 3)
        self.assertEqual(組物件.篩出字物件()[-1], 拆文分析器.建立字物件('...'))
