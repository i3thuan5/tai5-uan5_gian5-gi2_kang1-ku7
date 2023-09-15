from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.章 import 章


class 章單元試驗(TestCase):

    def test_章烏白傳(self):
        self.assertRaises(型態錯誤, 章, None)
        self.assertRaises(型態錯誤, 章, [None])
        self.assertRaises(型態錯誤, 章, ['sui2'])

    def test_看章(self):
        型 = '恁老母ti3佗位！恁老母ti3佗位！'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7 ! lin1 lau3 bu2 ti3 to1 ui7 !'
        章物件 = 拆文分析器.對齊章物件(型, 音)
        self.assertEqual(章物件.看語句(物件分句符號=''), 型)
        self.assertEqual(章物件.看音(), 音)
        分詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜! 恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜!'
        self.assertEqual(章物件.看分詞(), 分詞)

    def test_看章加連字符(self):
        型 = '恁老母ti3佗位！恁lau3-bu2-ti3佗位！'
        音 = 'lin1 lau3-bu2 ti3 to1 ui7 ! lin1 lau3-bu2-ti3 to1-ui7 !'
        章物件 = 拆文分析器.對齊章物件(型, 音)
        self.assertEqual(章物件.看語句(物件分句符號=''), 型)
        self.assertEqual(章物件.看音(), 音)
        分詞 = '恁｜lin1 老-母｜lau3-bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜! 恁｜lin1 lau3-bu2-ti3｜lau3-bu2-ti3 佗-位｜to1-ui7 ！｜!'
        self.assertEqual(章物件.看分詞(), 分詞)

    def test_預設分句符號(self):
        原本語句 = '食-飽｜tsiah8-pa2 未｜0bue7 ？｜? 食-飽｜tsiah8-pa2 矣｜0ah4 ！｜!'
        章物件 = 拆文分析器.分詞章物件(原本語句)
        self.assertEqual(章物件.看語句(物件分句符號=''),
                         '食飽未？食飽矣！')
        self.assertEqual(章物件.看音(),
                         'tsiah8-pa2 0bue7 ? tsiah8-pa2 0ah4 !')
        self.assertEqual(章物件.看分詞(),
                         '食-飽｜tsiah8-pa2 未｜0bue7 ？｜? 食-飽｜tsiah8-pa2 矣｜0ah4 ！｜!')

    def test_換句分句符號(self):
        原本語句 = '食-飽｜tsiah8-pa2 未｜0bue7 ？｜? 食-飽｜tsiah8-pa2 矣｜0ah4 ！｜!'
        章物件 = 拆文分析器.分詞章物件(原本語句)
        self.assertEqual(
            章物件.看語句(物件分句符號='\n'),
            '食飽未？\n食飽矣！'
        )
        self.assertEqual(
            章物件.看音(物件分句符號='\n'),
            'tsiah8-pa2 0bue7 ?\ntsiah8-pa2 0ah4 !'
        )
