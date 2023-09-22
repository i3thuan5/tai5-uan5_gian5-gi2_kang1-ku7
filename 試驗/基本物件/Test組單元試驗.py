from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.組 import 組


class 組單元試驗(TestCase):

    def test_組烏白傳(self):
        self.assertRaises(型態錯誤, 組, None)
        self.assertRaises(型態錯誤, 組, [None])
        self.assertRaises(型態錯誤, 組, ['sui2'])

    def test_看組孤字(self):
        型 = '恁老母ti3佗位！'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7 !'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(組物件.看語句(), 型)
        self.assertEqual(組物件.看音(), 音)
        分詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜!'
        self.assertEqual(組物件.看分詞(), 分詞)

    def test_看組連字(self):
        型 = '恁老母ti3佗位！'
        音 = 'lin1 lau3-bu2 ti3 to1-ui7 !'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(組物件.看語句(), 型)
        self.assertEqual(組物件.看音(), 音)
        分詞 = '恁｜lin1 老-母｜lau3-bu2 ti3｜ti3 佗-位｜to1-ui7 ！｜!'
        self.assertEqual(組物件.看分詞(), 分詞)

    def test_接受無音的詞(self):
        組物件 = 拆文分析器.建立組物件('')
        組物件.內底詞 = [
            拆文分析器.建立詞物件('梅山'),
            拆文分析器.建立詞物件('猴-災'),
            拆文分析器.對齊詞物件('鄉-公所', 'hiong1-kong1-soo2'),
            拆文分析器.建立詞物件('tshiann2-lang5'),
            拆文分析器.對齊詞物件('趕-走', 'kuann2-tsau2'),
            拆文分析器.對齊詞物件('猴山', 'kau5-san1'),
        ]
        分詞答案 = '梅-山 猴-災 鄉-公-所｜hiong1-kong1-soo2 tshiann2-lang5 趕-走｜kuann2-tsau2 猴-山｜kau5-san1'
        self.assertEqual(組物件.看分詞(), 分詞答案)

    def test_有字無音的詞(self):
        公詞物件 = 拆文分析器.建立詞物件('')
        公詞物件.內底字 = [
            拆文分析器.建立字物件('鄉'),
            拆文分析器.對齊字物件('公', 'kong1'),
            拆文分析器.建立字物件('所'),
        ]
        鄉所詞物件 = 拆文分析器.建立詞物件('')
        鄉所詞物件.內底字 = [
            拆文分析器.對齊字物件('鄉', 'hiang1'),
            拆文分析器.建立字物件('公'),
            拆文分析器.對齊字物件('所', 'soo2'),
        ]
        公鄉所組物件 = 拆文分析器.建立組物件('')
        公鄉所組物件.內底詞 = [公詞物件, 鄉所詞物件]
        self.assertEqual(
            公鄉所組物件.看分詞(),
            '鄉-公-所｜-kong1- 鄉-公-所｜hiang1--soo2'
        )
