from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.句 import 句


class 句單元試驗(TestCase):

    def test_句烏白傳(self):
        self.assertRaises(型態錯誤, 句, None)
        self.assertRaises(型態錯誤, 句, [None])
        self.assertRaises(型態錯誤, 句, ['sui2'])

    def test_看句(self):
        型 = '恁老母ti3佗位'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7'
        句物件 = 拆文分析器.對齊句物件(型, 音)
        self.assertEqual(句物件.看語句(), 型)
        self.assertEqual(句物件.看音(), 音)
        分詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7'
        self.assertEqual(句物件.看分詞(), 分詞)
