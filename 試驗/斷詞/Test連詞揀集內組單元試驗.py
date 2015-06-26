# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.斷詞.連詞揀集內組 import 連詞揀集內組
from 臺灣言語工具.語言模型.實際語言模型 import 實際語言模型


class 連詞揀集內組單元試驗(TestCase):
    忍受 = 1e-10

    def setUp(self):
        self.分析器 = 拆文分析器()
        self.連詞 = 實際語言模型(3)
        self.用連詞揀 = 連詞揀集內組()

        self.我有一張桌仔 = self.分析器.產生對齊句(
                '我有一張桌仔！', 'gua2 u7 tsit8-tiunn1 toh4-a2!')
        self.桌仔垃圾 = self.分析器.產生對齊句(
                '桌仔垃圾！？', 'toh4-a2 lap4-sap4!?')
        self.我有一張椅仔 = self.分析器.產生對齊句(
                '我有一張椅仔！', 'gua2 u7 tsit8-tiunn1 i2-a2!')
        self.椅仔 = self.分析器.產生對齊句(
                '椅仔。', 'i2-a2.')
        self.桌仔 = self.分析器.產生對齊句(
                '桌仔。', 'toh4-a2.')
        self.柴 = self.分析器.產生對齊句(
                '柴！', 'tsha5!')
        self.我 = self.分析器.產生對齊句(
                '我', 'gua2')

    def tearDown(self):
        pass

    def test_標音的分數愛佮評分仝款(self):
        '「分數 * (詞數 - 1)」因為頭一个開始的機率是1'
        self.連詞.看(self.我有一張桌仔)
        標好, 分數, 詞數 = self.用連詞揀.揀(self.連詞, self.我)
        self.assertEqual(標好, self.我)
        self.assertEqual(3, 詞數)
        self.assertAlmostEqual(分數 * (詞數 - 1),
                               sum(self.連詞.評分(self.我)), delta=self.忍受)
        標好, 分數, 詞數 = self.用連詞揀.揀(self.連詞, self.桌仔)
        self.assertEqual(標好, self.桌仔)
        self.assertEqual(4, 詞數)
        self.assertAlmostEqual(分數 * (詞數 - 1),
                               sum(self.連詞.評分(self.桌仔)), delta=self.忍受)
        標好, 分數, 詞數 = self.用連詞揀.揀(self.連詞, self.我有一張桌仔)
        self.assertEqual(標好, self.我有一張桌仔)
        self.assertEqual(7, 詞數)
        self.assertAlmostEqual(分數 * (詞數 - 1),
                               sum(self.連詞.評分(self.我有一張桌仔)), delta=self.忍受)

    def test_看機率選詞(self):
        我 = self.分析器.產生對齊集('我', 'gua2')
        的 = self.分析器.產生對齊組('的', 'e5')
        鞋 = self.分析器.產生對齊組('鞋', 'e5')
        仔 = self.分析器.產生對齊集('仔', 'a2')
        e5_鞋的 = 集()
        e5_鞋的.內底組 = [鞋, 的, ]
        我_e5_e5_仔_鞋的 = 句()
        我_e5_e5_仔_鞋的 .內底集 = [我, e5_鞋的, e5_鞋的, 仔]
        e5_的鞋 = 集()
        e5_的鞋.內底組 = [的, 鞋, ]
        我_e5_e5_仔_的鞋 = 句()
        我_e5_e5_仔_的鞋 .內底集 = [我, e5_的鞋, e5_的鞋, 仔]
        鞋集 = 集()
        鞋集.內底組 = [鞋, ]
        的集 = 集()
        的集.內底組 = [的, ]
        我鞋鞋仔 = 句()
        我鞋鞋仔.內底集 = [我, 鞋集, 鞋集, 仔]
        我的鞋仔 = 句()
        我的鞋仔.內底集 = [我, 的集, 鞋集, 仔]
        self.連詞.看(self.分析器.產生對齊句('我穿布鞋。', 'gua2 tshng1 poo3 e5.'))
        self.連詞.看(self.分析器.產生對齊句('我鞋仔歹去矣。', 'gua2 e5 a2 phainn2-0khi3 0ah4.'))
        我的 = [self.分析器.產生對齊詞('我', 'gua2'), self.分析器.產生對齊詞('的', 'e5')]
        self.assertEqual(self.連詞.數量(我的), [0, 0])
        我鞋 = [self.分析器.產生對齊詞('我', 'gua2'), self.分析器.產生對齊詞('鞋', 'e5')]
        self.assertEqual(self.連詞.數量(我鞋), [2, 1])
        鞋的結果, 鞋的分數, 鞋的詞數 = self.用連詞揀.揀(self.連詞, 我_e5_e5_仔_鞋的)
        的鞋結果, 的鞋分數, 的鞋詞數 = self.用連詞揀.揀(self.連詞, 我_e5_e5_仔_的鞋)
        self.assertEqual(鞋的結果, 我鞋鞋仔)
        self.assertEqual(的鞋結果, 鞋的結果)
        self.assertLess(鞋的分數, 0.0)
        self.assertEqual(鞋的分數, 的鞋分數)
        self.assertEqual(鞋的詞數, 6)
        self.assertEqual(鞋的詞數, 的鞋詞數)
        頂擺分數 = 鞋的分數
        self.連詞.看(self.分析器.產生對齊句('我的冊佇你遐。', 'gua2 e5 tsheh4 ti7 li2 hia1.'))
        鞋的結果, 鞋的分數, 鞋的詞數 = self.用連詞揀.揀(self.連詞, 我_e5_e5_仔_鞋的)
        的鞋結果, 的鞋分數, 的鞋詞數 = self.用連詞揀.揀(self.連詞, 我_e5_e5_仔_的鞋)
        self.assertEqual(鞋的結果, 我鞋鞋仔)
        self.assertEqual(的鞋結果, 鞋的結果)
        self.assertLess(鞋的分數, 0.0)
        self.assertLess(鞋的分數, 頂擺分數)
        self.assertEqual(鞋的分數, 的鞋分數)
        self.assertEqual(鞋的詞數, 6)
        self.assertEqual(鞋的詞數, 的鞋詞數)
        頂擺分數 = 鞋的分數
        self.連詞.看(self.分析器.產生對齊句('我的故鄉佇花蓮。', 'gua2 e5 koo3-hiong1 ti7 hua1-lian1.'))
        鞋的結果, 鞋的分數, 鞋的詞數 = self.用連詞揀.揀(self.連詞, 我_e5_e5_仔_鞋的)
        的鞋結果, 的鞋分數, 的鞋詞數 = self.用連詞揀.揀(self.連詞, 我_e5_e5_仔_的鞋)
        self.assertEqual(鞋的結果, 我的鞋仔)
        self.assertEqual(的鞋結果, 鞋的結果)
        self.assertLess(鞋的分數, 0.0)
        self.assertGreater(鞋的分數, 頂擺分數)
        self.assertEqual(鞋的分數, 的鞋分數)
        self.assertEqual(鞋的詞數, 6)
        self.assertEqual(鞋的詞數, 的鞋詞數)
        頂擺分數 = 鞋的分數
        的.內底詞[0].屬性 = {'機率': self.連詞.對數(0.01)}
        鞋.內底詞[0].屬性 = {'機率': self.連詞.對數(0.99)}
        鞋的結果, 鞋的分數, 鞋的詞數 = self.用連詞揀.揀(self.連詞, 我_e5_e5_仔_鞋的)
        的鞋結果, 的鞋分數, 的鞋詞數 = self.用連詞揀.揀(self.連詞, 我_e5_e5_仔_的鞋)
        self.assertEqual(鞋的結果, 我鞋鞋仔)
        self.assertEqual(的鞋結果, 鞋的結果)
        self.assertLess(鞋的分數, 0.0)
        self.assertLess(鞋的分數, 頂擺分數)
        self.assertEqual(鞋的分數, 的鞋分數)
        self.assertEqual(鞋的詞數, 6)
        self.assertEqual(鞋的詞數, 的鞋詞數)

    def test_標了的型態愛佮原本仝款(self):
        字物件 = self.分析器.產生對齊字('媠', 'sui2')
        詞物件 = self.分析器.產生對齊詞('姑娘', 'koo1-niu5')
        組物件 = self.分析器.產生對齊組('媠姑娘', 'sui2 koo1-niu5')
        集物件 = self.分析器.產生對齊集('媠姑娘', 'sui2 koo1-niu5')
        句物件 = self.分析器.產生對齊句('我佮意媠姑娘', 'gua2 kah4 i3 sui2 koo1-niu5')
        章物件 = self.分析器.產生對齊章('我佮意媠姑娘。我愛媠姑娘。', 'gua2 kah4 i3 sui2 koo1-niu5. gua2 ai3 sui2 koo1-niu5.')
        for 物件 in [字物件, 詞物件, 組物件, 集物件, 句物件, 章物件]:
            self.assertEqual(self.用連詞揀.揀(self.連詞, 物件)[0], 物件)

    def test_選無仝長度的集(self):
        媠姑娘 = self.分析器.產生對齊組('媠姑娘', 'sui2 koo1-niu5')
        靚細妹 = self.分析器.產生對齊組('靚細妹', 'jiangˊ-se-moi')
        大美女 = self.分析器.產生對齊組('世界大大美女', 'se3-kai3 tua7 tua7 mi2-lu2')
        莉 = 集([媠姑娘, 靚細妹, 大美女])
        我 = self.分析器.產生對齊集('我', 'gua2')
        愛 = self.分析器.產生對齊集('愛', 'ai3')
        呀 = self.分析器.產生對齊集('！', '!')
        問題句物件 = 句([我, 愛, 莉, 呀])
        媠姑娘句物件 = 句([我, 愛, 集([媠姑娘, ]), 呀])
        靚細妹句物件 = 句([我, 愛, 集([靚細妹, ]), 呀])
        大美女句物件 = 句([我, 愛, 集([大美女, ]), 呀])
        self.連詞.看(媠姑娘句物件)
        結果, 分數, 詞數 = self.用連詞揀.揀(self.連詞, 問題句物件)
        self.assertEqual(結果, 媠姑娘句物件)
        self.assertLess(分數, 0.0)
        self.assertEqual(詞數, 7)
        self.連詞.看(靚細妹句物件)
        self.連詞.看(靚細妹句物件)
        self.連詞.看(靚細妹句物件)
        結果, 分數, 詞數 = self.用連詞揀.揀(self.連詞, 問題句物件)
        # 因為詞組干焦一个詞，所以會靚細妹輸媠姑娘？
        self.assertEqual(結果, 靚細妹句物件)
        self.assertLess(分數, 0.0)
        self.assertEqual(詞數, 6)
        # 詞組較長，所以應該愛搶贏別人？
        self.連詞.看(大美女句物件)
        self.連詞.看(大美女句物件)
        self.連詞.看(大美女句物件)
        self.連詞.看(大美女句物件)
        self.連詞.看(大美女句物件)
        結果, 分數, 詞數 = self.用連詞揀.揀(self.連詞, 問題句物件)
        self.assertEqual(結果, 大美女句物件)
        self.assertLess(分數, 0.0)
        self.assertEqual(詞數, 9)

    def test_標空的物件(self):
        # 字物件有限制毋是空的
        詞物件 = self.分析器.建立詞物件('')
        組物件 = self.分析器.建立組物件('')
        集物件 = self.分析器.建立集物件('')
        句物件 = self.分析器.建立句物件('')
        章物件 = self.分析器.建立章物件('')
        結果, 分數, 詞數 = self.用連詞揀.揀(self.連詞, 詞物件)
        全部分數 = {}
        for 物件, 詞數答案 in zip([詞物件, 組物件, 句物件, 章物件], [3, 2, 2, 0]):
            結果, 分數, 詞數 = self.用連詞揀.揀(self.連詞, 物件)
            self.assertEqual(結果, 物件)
            self.assertEqual(詞數, 詞數答案)
            if 詞數 not in 全部分數:
                全部分數[詞數] = 分數
            self.assertEqual(分數, 全部分數[詞數])
        self.assertRaises(解析錯誤, self.用連詞揀.揀, self.連詞, 集物件,)

    def test_標有空的集合(self):
        我_你 = 句([self.分析器.建立集物件('我'), self.分析器.建立集物件(''), self.分析器.建立集物件('你')])
        self.assertRaises(解析錯誤, self.用連詞揀.揀, self.連詞, 我_你)
