# -*- coding: utf-8 -*-
import unittest

from 臺灣言語工具.基本元素.公用變數 import 分字符號
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


class 物件譀鏡單元試驗(unittest.TestCase):
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
        分詞 = 型 + '｜' + 音
        self.assertEqual(self.譀鏡.看分詞(字物件), 分詞)

    def test_看詞(self):
        型 = '姑-娘'
        音 = 'koo1-niu5'
        詞物件 = self.分析器.產生對齊詞(型, 音)
        無分字型 = 型.replace(分字符號, '')
        self.assertEqual(self.譀鏡.看型(詞物件), 無分字型)
        self.assertEqual(self.譀鏡.看音(詞物件), 音)
        分詞 = 型 + '｜' + 音
        self.assertEqual(self.譀鏡.看分詞(詞物件), 分詞)

    def test_看組孤字(self):
        型 = '恁老母ti3佗位！'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7 !'
        組物件 = self.分析器.產生對齊組(型, 音)
        self.assertEqual(self.譀鏡.看型(組物件), 型)
        self.assertEqual(self.譀鏡.看音(組物件), 音)
        分詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜!'
        self.assertEqual(self.譀鏡.看分詞(組物件), 分詞)

    def test_看組連字(self):
        型 = '恁老母ti3佗位！'
        音 = 'lin1 lau3-bu2 ti3 to1-ui7 !'
        組物件 = self.分析器.產生對齊組(型, 音)
        self.assertEqual(self.譀鏡.看型(組物件), 型)
        self.assertEqual(self.譀鏡.看音(組物件), 音)
        分詞 = '恁｜lin1 老-母｜lau3-bu2 ti3｜ti3 佗-位｜to1-ui7 ！｜!'
        self.assertEqual(self.譀鏡.看分詞(組物件), 分詞)

    def test_看集(self):
        型 = '恁老母ti3佗位'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7'
        集物件 = self.分析器.產生對齊集(型, 音)
        self.assertEqual(self.譀鏡.看型(集物件), 型)
        self.assertEqual(self.譀鏡.看音(集物件), 音)
        分詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7'
        self.assertEqual(self.譀鏡.看分詞(集物件), 分詞)

    def test_看集內底有兩組以上(self):
        型 = '恁老母ti3佗位'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7'
        集物件 = 集([self.分析器.產生對齊組(型, 音), self.分析器.產生對齊組(型, 音)])
        self.assertRaises(解析錯誤, self.譀鏡.看型, 集物件)
        self.assertRaises(解析錯誤, self.譀鏡.看音, 集物件)
        self.assertRaises(解析錯誤, self.譀鏡.看分詞, 集物件)

    def test_看句(self):
        型 = '恁老母ti3佗位'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7'
        句物件 = self.分析器.產生對齊句(型, 音)
        self.assertEqual(self.譀鏡.看型(句物件), 型)
        self.assertEqual(self.譀鏡.看音(句物件), 音)
        分詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7'
        self.assertEqual(self.譀鏡.看分詞(句物件), 分詞)

    def test_看章(self):
        型 = '恁老母ti3佗位！恁老母ti3佗位！'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7 ! lin1 lau3 bu2 ti3 to1 ui7 !'
        章物件 = self.分析器.產生對齊章(型, 音)
        self.assertEqual(self.譀鏡.看型(章物件), 型)
        self.assertEqual(self.譀鏡.看音(章物件), 音)
        分詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜! 恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜!'
        self.assertEqual(self.譀鏡.看分詞(章物件), 分詞)
        self.assertEqual(self.譀鏡.看分詞(章物件, '｜'), 分詞)
        分詞加 = '恁+lin1 老+lau3 母+bu2 ti3+ti3 佗+to1 位+ui7 ！+! 恁+lin1 老+lau3 母+bu2 ti3+ti3 佗+to1 位+ui7 ！+!'
        self.assertEqual(self.譀鏡.看分詞(章物件, '+'), 分詞加)

    def test_看章加連字符(self):
        型 = '恁老母ti3佗位！恁lau3-bu2-ti3佗位！'
        音 = 'lin1 lau3-bu2 ti3 to1 ui7 ! lin1 lau3-bu2-ti3 to1-ui7 !'
        章物件 = self.分析器.產生對齊章(型, 音)
        無分字型 = 型.replace(分字符號, '')
        self.assertEqual(self.譀鏡.看型(章物件), 無分字型)
        self.assertEqual(self.譀鏡.看音(章物件), 音)
        分詞 = '恁｜lin1 老-母｜lau3-bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜! 恁｜lin1 lau3-bu2-ti3｜lau3-bu2-ti3 佗-位｜to1-ui7 ！｜!'
        self.assertEqual(self.譀鏡.看分詞(章物件), 分詞)
        self.assertEqual(self.譀鏡.看分詞(章物件, '｜'), 分詞)
        self.assertEqual(self.譀鏡.看分詞(章物件, 物件分型音符號='｜'), 分詞)

    def test_看章換連字符(self):
        型 = '恁老母ti3佗位！恁老母ti3佗位！'
        音 = 'lin1 lau3-bu2 ti3 to1 ui7 ! lin1 lau3-bu2-ti3 to1-ui7 !'
        答型 = '恁|老_母|ti3|佗|位|！^恁|老_母_ti3|佗_位|！'
        答音 = 'lin1|lau3_bu2|ti3|to1|ui7|!^lin1|lau3_bu2_ti3|to1_ui7|!'
        章物件 = self.分析器.產生對齊章(型, 音)
        self.assertEqual(self.譀鏡.看型(章物件, '_', '|', '^'), 答型)
        self.assertEqual(self.譀鏡.看音(章物件, '_', '|', '^'), 答音)
        self.assertEqual(
            self.譀鏡.看型(章物件, 物件分字符號='_', 物件分詞符號='|', 物件分句符號='^'), 答型)
        self.assertEqual(
            self.譀鏡.看音(章物件, 物件分字符號='_', 物件分詞符號='|', 物件分句符號='^'), 答音)
        分詞 = '恁@lin1^老_母@lau3_bu2^ti3@ti3^佗@to1^位@ui7^！@!|恁@lin1^老_母_ti3@lau3_bu2_ti3^佗_位@to1_ui7^！@!'
        self.assertEqual(self.譀鏡.看分詞(章物件, '@', '_', '^', '|'), 分詞)
        self.assertEqual(
            self.譀鏡.看分詞(章物件, 物件分型音符號='@', 物件分字符號='_', 物件分詞符號='^', 物件分句符號='|'), 分詞)

    def test_參數烏白傳(self):
        self.assertRaises(型態錯誤, self.譀鏡.看型, 790830)
        self.assertRaises(型態錯誤, self.譀鏡.看音, None)
        self.assertRaises(型態錯誤, self.譀鏡.看分詞, '｜', '｜')

    def test_無音字(self):
        字物件 = self.分析器.建立字物件('媠')
        self.assertEqual(self.譀鏡.看型(字物件), '媠')
        self.assertEqual(self.譀鏡.看音(字物件), '')
        self.assertEqual(self.譀鏡.看分詞(字物件), '媠')

    def test_接受無音的詞(self):
        組物件 = self.分析器.建立組物件('')
        組物件.內底詞 = [
            self.分析器.建立詞物件('梅山'),
            self.分析器.建立詞物件('猴-災'),
            self.分析器.產生對齊詞('鄉-公所', 'hiong1-kong1-soo2'),
            self.分析器.建立詞物件('tshiann2-lang5'),
            self.分析器.產生對齊詞('趕-走', 'kuann2-tsau2'),
            self.分析器.產生對齊詞('猴山', 'kau5-san1'),
        ]
        分詞答案 = '梅-山 猴-災 鄉-公-所｜hiong1-kong1-soo2 tshiann2-lang5 趕-走｜kuann2-tsau2 猴-山｜kau5-san1'
        self.assertEqual(self.譀鏡.看分詞(組物件), 分詞答案)

    def test_兩字詞有字無音(self):
        梅詞物件 = self.分析器.建立詞物件('')
        梅詞物件.內底字 = [
            self.分析器.產生對齊字('梅', 'mui5'),
            self.分析器.建立字物件('山'),
        ]
        梅分詞答案 = '梅-山｜mui5-'
        self.assertEqual(self.譀鏡.看分詞(梅詞物件), 梅分詞答案)
        山詞物件 = self.分析器.建立詞物件('')
        山詞物件.內底字 = [
            self.分析器.建立字物件('梅'),
            self.分析器.產生對齊字('山', 'san1'),
        ]
        山分詞答案 = '梅-山｜-san1'
        self.assertEqual(self.譀鏡.看分詞(山詞物件), 山分詞答案)

    def test_三字詞有字無音(self):
        公詞物件 = self.分析器.建立詞物件('')
        公詞物件.內底字 = [
            self.分析器.建立字物件('鄉'),
            self.分析器.產生對齊字('公', 'kong1'),
            self.分析器.建立字物件('所'),
        ]
        公分詞答案 = '鄉-公-所｜-kong1-'
        self.assertEqual(self.譀鏡.看分詞(公詞物件), 公分詞答案)

        鄉所詞物件 = self.分析器.建立詞物件('')
        鄉所詞物件.內底字 = [
            self.分析器.產生對齊字('鄉', 'hiang1'),
            self.分析器.建立字物件('公'),
            self.分析器.產生對齊字('所', 'soo2'),
        ]
        鄉所分詞答案 = '鄉-公-所｜hiang1--soo2'
        self.assertEqual(self.譀鏡.看分詞(鄉所詞物件), 鄉所分詞答案)

        公鄉所組物件 = self.分析器.建立組物件('')
        公鄉所組物件.內底詞 = [公詞物件, 鄉所詞物件]
        self.assertEqual(self.譀鏡.看分詞(公鄉所組物件), ' '.join([公分詞答案, 鄉所分詞答案]))

    def test_預設分句符號(self):
        原本語句 = '食-飽｜tsiah8-pa2 未｜0bue7 ？｜? 食-飽｜tsiah8-pa2 矣｜0ah4 ！｜!'
        章物件 = self.分析器.轉做章物件(原本語句)
        self.assertEqual(self.譀鏡.看型(章物件),
                         '食飽未？食飽矣！')
        self.assertEqual(self.譀鏡.看音(章物件),
                         'tsiah8-pa2 0bue7 ? tsiah8-pa2 0ah4 !')
        self.assertEqual(self.譀鏡.看分詞(章物件),
                         '食-飽｜tsiah8-pa2 未｜0bue7 ？｜? 食-飽｜tsiah8-pa2 矣｜0ah4 ！｜!')

    def test_換句分句符號(self):
        原本語句 = '食-飽｜tsiah8-pa2 未｜0bue7 ？｜? 食-飽｜tsiah8-pa2 矣｜0ah4 ！｜!'
        章物件 = self.分析器.轉做章物件(原本語句)
        self.assertEqual(self.譀鏡.看型(章物件, 物件分句符號='\n'),
                         '食飽未？\n食飽矣！')
        self.assertEqual(self.譀鏡.看音(章物件, 物件分句符號='\n'),
                         'tsiah8-pa2 0bue7 ?\ntsiah8-pa2 0ah4 !')
        self.assertEqual(self.譀鏡.看分詞(章物件, 物件分句符號='\n'),
                         '食-飽｜tsiah8-pa2 未｜0bue7 ？｜?\n食-飽｜tsiah8-pa2 矣｜0ah4 ！｜!')
