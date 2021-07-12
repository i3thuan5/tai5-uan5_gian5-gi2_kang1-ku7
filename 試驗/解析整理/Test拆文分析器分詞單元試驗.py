# -*- coding: utf-8 -*-
import unittest
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.基本物件.字 import 字


class 拆文分析器分詞單元試驗(unittest.TestCase):

    def test_分詞字孤字(self):
        分詞 = '𪜶｜in1'
        型 = '𪜶'
        音 = 'in1'
        字物件 = 拆文分析器.分詞字物件(分詞)
        self.assertEqual(字物件.型, 型)
        self.assertEqual(字物件.音, 音)

    # 分詞字無檢查有對齊無，這應該是轉物件音的空課
    def test_分詞字無對齊(self):
        分詞 = '美-麗｜sui2'
        with self.assertRaises(解析錯誤):
            拆文分析器.分詞字物件(分詞)

    def test_分詞字有兩字(self):
        分詞 = '兩｜nng7 个｜e5'
        self.assertRaises(解析錯誤, 拆文分析器.分詞字物件, 分詞)

    def test_分詞字無半字(self):
        分詞 = ''
        self.assertRaises(解析錯誤, 拆文分析器.分詞字物件, 分詞)

    def test_分詞字有分型音無半字(self):
        分詞 = '｜'
        self.assertRaises(解析錯誤, 拆文分析器.分詞字物件, 分詞)

    def test_分詞字無分型音(self):
        分詞 = '無'
        字物件 = 拆文分析器.分詞字物件(分詞)
        self.assertEqual(字物件.型, 分詞)
        self.assertEqual(字物件.音, 無音)

    def test_分詞字連字(self):
        分詞 = '-｜-'
        型 = '-'
        音 = '-'
        字物件 = 拆文分析器.分詞字物件(分詞)
        self.assertEqual(字物件.型, 型)
        self.assertEqual(字物件.音, 音)

    def test_分詞詞孤字(self):
        分詞 = '𪜶｜in1'
        型 = '𪜶'
        音 = 'in1'
        詞物件 = 拆文分析器.分詞詞物件(分詞)
        self.assertEqual(len(詞物件.內底字), 1)
        self.assertEqual(詞物件.內底字[0].型, 型)
        self.assertEqual(詞物件.內底字[0].音, 音)

    def test_分詞詞濟字(self):
        分詞 = '美-麗｜bi2-le7'
        型甲 = '美'
        音甲 = 'bi2'
        型乙 = '麗'
        音乙 = 'le7'
        詞物件 = 拆文分析器.分詞詞物件(分詞)
        self.assertEqual(len(詞物件.內底字), 2)
        self.assertEqual(詞物件.內底字[0].型, 型甲)
        self.assertEqual(詞物件.內底字[0].音, 音甲)
        self.assertEqual(詞物件.內底字[1].型, 型乙)
        self.assertEqual(詞物件.內底字[1].音, 音乙)

    def test_分詞詞漢字無連字(self):
        分詞 = '美麗｜bi2-le7'
        型甲 = '美'
        音甲 = 'bi2'
        型乙 = '麗'
        音乙 = 'le7'
        詞物件 = 拆文分析器.分詞詞物件(分詞)
        self.assertEqual(len(詞物件.內底字), 2)
        self.assertEqual(詞物件.內底字[0].型, 型甲)
        self.assertEqual(詞物件.內底字[0].音, 音甲)
        self.assertEqual(詞物件.內底字[1].型, 型乙)
        self.assertEqual(詞物件.內底字[1].音, 音乙)

    def test_分詞詞無對齊(self):
        分詞 = '美-麗｜sui2'
        self.assertRaises(解析錯誤, 拆文分析器.分詞詞物件, 分詞)

    def test_分詞詞有兩詞(self):
        分詞 = '兩｜nng7 个｜e5'
        self.assertRaises(解析錯誤, 拆文分析器.分詞詞物件, 分詞)

    def test_分詞詞無半字(self):
        分詞 = ''
        詞物件 = 拆文分析器.分詞詞物件(分詞)
        self.assertEqual(len(詞物件.內底字), 0)

    def test_分詞詞是分詞ê符號(self):
        分詞 = '｜'
        詞物件 = 拆文分析器.分詞詞物件(分詞)
        self.assertEqual(len(詞物件.內底字), 1)
        self.assertEqual(詞物件.內底字[0].型, '｜')
        self.assertEqual(詞物件.內底字[0].音, 無音)

    def test_分詞詞無分型音(self):
        分詞 = '美麗'
        詞物件 = 拆文分析器.分詞詞物件(分詞)
        self.assertEqual(len(詞物件.內底字), 2)
        self.assertEqual(詞物件.內底字[0].型, '美')
        self.assertEqual(詞物件.內底字[0].音, 無音)
        self.assertEqual(詞物件.內底字[1].型, '麗')
        self.assertEqual(詞物件.內底字[1].音, 無音)

    def test_分詞詞空白(self):
        分詞 = ' ｜ '
        詞物件 = 拆文分析器.分詞詞物件(分詞)
        self.assertEqual(len(詞物件.內底字), 1)
        self.assertEqual(詞物件.內底字[0].型, '｜')
        self.assertEqual(詞物件.內底字[0].音, 無音)

    def test_分詞全是分詞符號(self):
        詞物件 = 拆文分析器.分詞詞物件('｜｜｜')
        self.assertEqual(len(詞物件.內底字), 1)
        self.assertEqual(詞物件.內底字[0].型, '｜')
        self.assertEqual(詞物件.內底字[0].音, '｜')

    def test_分詞字全是分詞符號_行為愛kah分詞詞仝款(self):
        字物件 = 拆文分析器.分詞字物件('｜｜｜')
        self.assertEqual(字物件.型, '｜')
        self.assertEqual(字物件.音, '｜')

    def test_分詞型是分詞符號(self):
        詞物件 = 拆文分析器.分詞詞物件('｜｜=')
        self.assertEqual(len(詞物件.內底字), 1)
        self.assertEqual(詞物件.內底字[0].型, '｜')
        self.assertEqual(詞物件.內底字[0].音, '=')

    def test_分詞音是分詞符號(self):
        詞物件 = 拆文分析器.分詞詞物件('-｜｜')
        self.assertEqual(len(詞物件.內底字), 1)
        self.assertEqual(詞物件.內底字[0].型, '-')
        self.assertEqual(詞物件.內底字[0].音, '｜')

    def test_分詞內有一个全是分詞符號(self):
        組物件 = 拆文分析器.分詞組物件('＝｜＝ ｜｜｜')
        self.assertEqual(len(組物件.內底詞), 2)
        self.assertEqual(組物件.內底詞[1].內底字[0].型, '｜')
        self.assertEqual(組物件.內底詞[1].內底字[0].音, '｜')

    def test_分詞組集句章孤字(self):
        分詞 = '𪜶｜in1'
        組物件 = 拆文分析器.分詞組物件(分詞)
        self.assertEqual(len(組物件.內底詞), 1)
        self.assertEqual(組物件.內底詞[0], 拆文分析器.分詞詞物件('𪜶｜in1'))
        集物件 = 拆文分析器.分詞集物件(分詞)
        self.assertEqual(len(集物件.內底組), 1)
        self.assertEqual(集物件.內底組[0], 組物件)
        句物件 = 拆文分析器.分詞句物件(分詞)
        self.assertEqual(len(句物件.內底集), 1)
        self.assertEqual(句物件.內底集[0], 集物件)
        章物件 = 拆文分析器.分詞章物件(分詞)
        self.assertEqual(len(章物件.內底句), 1)
        self.assertEqual(章物件.內底句[0], 句物件)

    def test_分詞組集句章濟字(self):
        分詞 = '𪜶｜in1 兩｜nng7 个｜e5 生-做｜senn1-tso3 一-模-一-樣｜it4-boo5-it4-iunn7 。｜.'
        組物件 = 拆文分析器.分詞組物件(分詞)
        self.assertEqual(len(組物件.內底詞), 6)
        self.assertEqual(組物件.內底詞[0], 拆文分析器.分詞詞物件('𪜶｜in1'))
        self.assertEqual(組物件.內底詞[1], 拆文分析器.分詞詞物件('兩｜nng7'))
        self.assertEqual(組物件.內底詞[2], 拆文分析器.分詞詞物件('个｜e5'))
        self.assertEqual(組物件.內底詞[3], 拆文分析器.分詞詞物件('生-做｜senn1-tso3'))
        self.assertEqual(
            組物件.內底詞[4], 拆文分析器.分詞詞物件('一-模-一-樣｜it4-boo5-it4-iunn7'))
        self.assertEqual(組物件.內底詞[5], 拆文分析器.分詞詞物件('。｜.'))
        集物件 = 拆文分析器.分詞集物件(分詞)
        self.assertEqual(len(集物件.內底組), 1)
        self.assertEqual(集物件.內底組[0], 組物件)
        句物件 = 拆文分析器.分詞句物件(分詞)
        self.assertEqual(len(句物件.內底集), 1)
        self.assertEqual(句物件.內底集[0], 集物件)
        章物件 = 拆文分析器.分詞章物件(分詞)
        self.assertEqual(len(章物件.內底句), 1)
        self.assertEqual(章物件.內底句[0], 句物件)

    def test_分詞組集句章濟字佮有連字(self):
        分詞 = '兩｜nng7 个｜e5 -｜- -｜- 一-模-一-樣｜it4-boo5-it4-iunn7 。｜.'
        組物件 = 拆文分析器.分詞組物件(分詞)
        self.assertEqual(len(組物件.內底詞), 6)
        self.assertEqual(組物件.內底詞[0], 拆文分析器.分詞詞物件('兩｜nng7'))
        self.assertEqual(組物件.內底詞[1], 拆文分析器.分詞詞物件('个｜e5'))
        self.assertEqual(組物件.內底詞[2], 拆文分析器.分詞詞物件('-｜-'))
        self.assertEqual(組物件.內底詞[3], 拆文分析器.分詞詞物件('-｜-'))
        self.assertEqual(
            組物件.內底詞[4], 拆文分析器.分詞詞物件('一-模-一-樣｜it4-boo5-it4-iunn7'))
        self.assertEqual(組物件.內底詞[5], 拆文分析器.分詞詞物件('。｜.'))
        集物件 = 拆文分析器.分詞集物件(分詞)
        self.assertEqual(len(集物件.內底組), 1)
        self.assertEqual(集物件.內底組[0], 組物件)
        句物件 = 拆文分析器.分詞句物件(分詞)
        self.assertEqual(len(句物件.內底集), 1)
        self.assertEqual(句物件.內底集[0], 集物件)
        章物件 = 拆文分析器.分詞章物件(分詞)
        self.assertEqual(len(章物件.內底句), 1)
        self.assertEqual(章物件.內底句[0], 句物件)

    def test_分詞組集句濟字有加的空白佮換逝符號(self):
        分詞 = '  𪜶｜in1    兩｜nng7     个｜e5 \n'\
            '  生-做｜senn1-tso3 一-模-一-樣｜it4-boo5-it4-iunn7 。｜.    '
        組物件 = 拆文分析器.分詞組物件(分詞)
        self.assertEqual(組物件.內底詞, [
            拆文分析器.分詞詞物件('𪜶｜in1'),
            拆文分析器.分詞詞物件('兩｜nng7'),
            拆文分析器.分詞詞物件('个｜e5'),
            拆文分析器.分詞詞物件('\n'),
            拆文分析器.分詞詞物件('生-做｜senn1-tso3'),
            拆文分析器.分詞詞物件('一-模-一-樣｜it4-boo5-it4-iunn7'),
            拆文分析器.分詞詞物件('。｜.')
        ])
        集物件 = 拆文分析器.分詞集物件(分詞)
        self.assertEqual(len(集物件.內底組), 1)
        self.assertEqual(集物件.內底組[0], 組物件)
        句物件 = 拆文分析器.分詞句物件(分詞)
        self.assertEqual(len(句物件.內底集), 1)
        self.assertEqual(句物件.內底集[0], 集物件)

    def test_分詞組大寫專有符號袂使拆開(self):
        分詞 = 'H1N1 新型｜sin1-hing5 流感｜liu5-kam2 包含｜pau1-ham5 四種｜si3-tsiong2 病毒｜pinn7-tok8'
        組物件 = 拆文分析器.分詞組物件(分詞)
        self.assertEqual(len(組物件.內底詞), 6)
        self.assertEqual(len(組物件.內底詞[0].內底字), 1)

    def test_分詞組小寫專有符號袂使拆開(self):
        分詞 = 'g0v 是｜si7 咱｜lan2 的｜e5 好｜ho2 厝邊｜tshu3-pinn1'
        組物件 = 拆文分析器.分詞組物件(分詞)
        self.assertEqual(len(組物件.內底詞), 6)
        self.assertEqual(len(組物件.內底詞[0].內底字), 1)

    def test_分詞組大寫音標袂使拆開(self):
        分詞 = 'Sui2sui2 是｜si7 咱｜lan2 的｜e5 好｜ho2 厝邊｜tshu3-pinn1'
        組物件 = 拆文分析器.分詞組物件(分詞)
        self.assertEqual(len(組物件.內底詞), 6)
        self.assertEqual(len(組物件.內底詞[0].內底字), 1)

    def test_分詞組小寫音標袂使拆開(self):
        分詞 = 'sui2sui2 是｜si7 咱｜lan2 的｜e5 好｜ho2 厝邊｜tshu3-pinn1'
        組物件 = 拆文分析器.分詞組物件(分詞)
        self.assertEqual(len(組物件.內底詞), 6)
        self.assertEqual(len(組物件.內底詞[0].內底字), 1)

    def test_分詞組標點符號(self):
        分詞 = ' 「｜" 丈-姆｜tiunn7-m2 」｜" 就｜to7 是｜si7 阮｜guan2 某｜boo2 的｜e5 老-母｜lau7-bu2 。｜.'
        組物件 = 拆文分析器.分詞組物件(分詞)
        self.assertEqual(len(組物件.內底詞), 10)
        self.assertEqual(len(組物件.內底詞[0].內底字), 1)

    def test_分詞組無型音符號(self):
        換逝 = '丈-姆'
        組物件 = 拆文分析器.分詞組物件(換逝)
        self.assertEqual(len(組物件.內底詞), 1)
        self.assertEqual(組物件.內底詞[0].內底字, [字('丈', 無音), 字('姆', 無音)])

    def test_分詞組換逝(self):
        換逝 = '\n'
        組物件 = 拆文分析器.分詞組物件(換逝)
        self.assertEqual(len(組物件.內底詞), 1)
        self.assertEqual(組物件.內底詞[0].內底字, [字(換逝, 無音)])

    def test_分詞組集句章無半字(self):
        分詞 = ''
        組物件 = 拆文分析器.分詞組物件(分詞)
        self.assertEqual(len(組物件.內底詞), 0)
        集物件 = 拆文分析器.分詞集物件(分詞)
        self.assertEqual(len(集物件.內底組), 0)
        句物件 = 拆文分析器.分詞句物件(分詞)
        self.assertEqual(len(句物件.內底集), 0)
        章物件 = 拆文分析器.分詞章物件(分詞)
        self.assertEqual(len(章物件.內底句), 0)

    def test_分詞章濟句(self):
        分詞一 = '𪜶｜in1 兩｜nng7 个｜e5 兄-弟-仔｜hiann1-ti7-a2 '\
            '為-著｜ui7-tioh8 拚｜piann3 生-理｜sing1-li2 ，｜, '
        分詞二 = '就｜to7 按-呢｜an2-ne1 一-刀-兩-斷｜it4-to1-liong2-tuan7 '\
            '無｜bo5 來-去｜lai5-khi3 。｜.'
        分詞 = 分詞一 + 分詞二
        章物件 = 拆文分析器.分詞章物件(分詞)
        self.assertEqual(len(章物件.內底句), 2)
        self.assertEqual(章物件.內底句[0], 拆文分析器.分詞句物件(分詞一))
        self.assertEqual(章物件.內底句[1], 拆文分析器.分詞句物件(分詞二))

    def test_分詞章濟標點句(self):
        分詞零 = '。｜. 。｜. '
        分詞一 = '𪜶｜in1 兩｜nng7 个｜e5 兄-弟-仔｜hiann1-ti7-a2 '\
            '為-著｜ui7-tioh8 拚｜piann3 生-理｜sing1-li2 ，｜, 。｜. '
        分詞二 = '就｜to7 。｜. 。｜. '
        分詞三 = '就｜to7 按｜an2 。｜. '
        分詞四 = '就｜to7 按-呢｜an2-ne1 。｜. '
        分詞五 = '就｜to7 按-呢｜an2-ne1 一-刀-兩-斷｜it4-to1-liong2-tuan7 '\
            '無｜bo5 來-去｜lai5-khi3 。｜. 。｜. ！｜! '
        分詞陣列 = [分詞零, 分詞一, 分詞二, 分詞三, 分詞四, 分詞五]
        分詞 = ''.join(分詞陣列)
        章物件 = 拆文分析器.分詞章物件(分詞)
        句陣列 = []
        for 分 in 分詞陣列:
            句陣列.append(拆文分析器.分詞句物件(分))
        self.assertEqual(len(章物件.內底句), 6)
        self.assertEqual(章物件.內底句, 句陣列)

    def test_分詞章華語濟句(self):
        章分詞 = '如-果 你 5 歲 的 孩-子 罹-癌 ， 你 會 怎-樣 ？ 如-果 你 知-道 核-電 輻-射 正-在 慢-性 屠-殺 我-們 大-家 ， 你 要 怎-麼-辦 ？'
        句分詞 = ['如-果 你 5 歲 的 孩-子 罹-癌 ，',
               '你 會 怎-樣 ？',
               '如-果 你 知-道 核-電 輻-射 正-在 慢-性 屠-殺 我-們 大-家 ，',
               '你 要 怎-麼-辦 ？']
        章物件 = 拆文分析器.分詞章物件(章分詞)
        句陣列 = []
        for 分 in 句分詞:
            句陣列.append(拆文分析器.分詞句物件(分))
        self.assertEqual(章物件.內底句, 句陣列)

    def test_分詞章濟句用換逝符號隔開(self):
        語句 = '民視新聞報導\n桃園 工業區 的 連續 兩場 大火 ，'
        章物件 = 拆文分析器.分詞章物件(語句)
        self.assertEqual(len(章物件.內底句), 2)

    def test_分詞章濟句連紲換逝符號隔開(self):
        語句 = '民視新聞報導\n\n桃園 工業區 的 連續 兩場 大火 ，'
        章物件 = 拆文分析器.分詞章物件(語句)
        self.assertEqual(len(章物件.內底句), 3)

    def test_分詞章濟句連紲換逝符號隔開詞數(self):
        語句 = '民視新聞報導\n\n桃園 工業區 的 連續 兩場 大火 ，'
        章物件 = 拆文分析器.分詞章物件(語句)
        self.assertEqual(len(章物件.內底句[0].網出詞物件()), 2)
        self.assertEqual(len(章物件.內底句[1].網出詞物件()), 1)
        self.assertEqual(len(章物件.內底句[2].網出詞物件()), 7)

    def test_分詞章分詞濟句用斷句符號隔開(self):
        語句 = '𪜶｜in1 兩｜nng7 个｜e5 兄-弟-仔｜hiann1-ti7-a2 ，｜, '\
            '為-著｜ui7-tioh8 拚｜piann3 生-理｜sing1-li2 。｜. '
        章物件 = 拆文分析器.分詞章物件(語句)
        self.assertEqual(len(章物件.內底句), 2)

    def test_分詞章分詞濟句用換逝符號隔開(self):
        語句 = '𪜶｜in1 兩｜nng7 个｜e5 兄-弟-仔｜hiann1-ti7-a2\n'\
            '為-著｜ui7-tioh8 拚｜piann3 生-理｜sing1-li2 ，｜, 。｜. '
        章物件 = 拆文分析器.分詞章物件(語句)
        self.assertEqual(len(章物件.內底句), 2)

    def test_分詞章分詞濟句用換逝符號隔開詞數(self):
        語句 = '𪜶｜in1 兩｜nng7 个｜e5 兄-弟-仔｜hiann1-ti7-a2\n'\
            '為-著｜ui7-tioh8 拚｜piann3 生-理｜sing1-li2 ，｜, 。｜. '
        章物件 = 拆文分析器.分詞章物件(語句)
        self.assertEqual(len(章物件.內底句[0].網出詞物件()), 5)
        self.assertEqual(len(章物件.內底句[1].網出詞物件()), 5)

    def test_分詞章分詞濟句用換逝分詞隔開(self):
        語句 = '𪜶｜in1 兩｜nng7 个｜e5 兄-弟-仔｜hiann1-ti7-a2 \n｜\n '\
            '為-著｜ui7-tioh8 拚｜piann3 生-理｜sing1-li2 ，｜, 。｜. '
        章物件 = 拆文分析器.分詞章物件(語句)
        self.assertEqual(len(章物件.內底句), 2)

    def test_分詞章有加的空白佮換逝符號(self):
        分詞 = '  𪜶｜in1    兩｜nng7     个｜e5 \n'\
            '  生-做｜senn1-tso3 一-模-一-樣｜it4-boo5-it4-iunn7 。｜.    '
        章物件 = 拆文分析器.分詞章物件(分詞)
        self.assertEqual(len(章物件.內底句), 2)

    def test_分詞章有加的空白佮換逝符號詞數(self):
        分詞 = '  𪜶｜in1    兩｜nng7     个｜e5 \n'\
            '  生-做｜senn1-tso3 一-模-一-樣｜it4-boo5-it4-iunn7 。｜.    '
        章物件 = 拆文分析器.分詞章物件(分詞)
        self.assertEqual(len(章物件.內底句[0].網出詞物件()), 4)
        self.assertEqual(len(章物件.內底句[1].網出詞物件()), 3)

    def test_分詞章換逝後壁閣有符號(self):
        分詞 = '  𪜶｜in1    兩｜nng7     个｜e5 \n  。｜.    '
        章物件 = 拆文分析器.分詞章物件(分詞)
        self.assertEqual(len(章物件.內底句), 2)

    def test_分詞章干焦有換逝(self):
        分詞 = '\n\n'
        章物件 = 拆文分析器.分詞章物件(分詞)
        self.assertEqual(len(章物件.內底句), 2)

    def test_客話聲調(self):
        分詞 = '你｜hnˇ 好｜hauˋ 無｜vuˇ ？ 𠊎｜ngaiˇ 當-好｜dong+-ho^ ！'
        章物件 = 拆文分析器.分詞章物件(分詞)
        self.assertEqual(len(章物件.內底句), 2)

    def test_烏白傳參數(self):
        self.assertRaises(型態錯誤, 拆文分析器.分詞字物件, None)
        self.assertRaises(型態錯誤, 拆文分析器.分詞詞物件, 333)
        self.assertRaises(型態錯誤, 拆文分析器.分詞組物件, [])
        self.assertRaises(型態錯誤, 拆文分析器.分詞集物件, None)
        self.assertRaises(型態錯誤, 拆文分析器.分詞句物件, 14325)
        self.assertRaises(型態錯誤, 拆文分析器.分詞章物件, ('None',))

    def test_空白(self):
        分詞 = '去｜khi3 飛-翔｜pue1-siong5  ｜  走｜tsau2 遍｜pian3 世-界｜se3-kai3'
        組物件 = 拆文分析器.分詞組物件(分詞)
        self.assertEqual(len(組物件.內底詞), 6)
        self.assertEqual(len(組物件.內底詞[2].內底字), 1)
        字物件 = 拆文分析器.建立字物件('｜')
        self.assertEqual(組物件.內底詞[2].內底字[0], 字物件)

    def test_空白邊仔有空白(self):
        分詞 = '去｜khi3 飛-翔｜pue1-siong5    ｜    走｜tsau2 遍｜pian3 世-界｜se3-kai3'
        組物件 = 拆文分析器.分詞組物件(分詞)
        self.assertEqual(len(組物件.內底詞), 6)
        self.assertEqual(len(組物件.內底詞[2].內底字), 1)
        字物件 = 拆文分析器.建立字物件('｜')
        self.assertEqual(組物件.內底詞[2].內底字[0], 字物件)

    def test_全形空白(self):
        分詞 = '去｜khi3 飛-翔｜pue1-siong5 　｜　 走｜tsau2 遍｜pian3 世-界｜se3-kai3'
        組物件 = 拆文分析器.分詞組物件(分詞)
        self.assertEqual(len(組物件.內底詞), 6)
        self.assertEqual(len(組物件.內底詞[2].內底字), 1)
        字物件 = 拆文分析器.建立字物件('｜')
        self.assertEqual(組物件.內底詞[2].內底字[0], 字物件)

    def test_連續符號(self):
        分詞 = '去｜khi3 飛翔 ｜ ｜ ｜ 走｜tsau2 遍｜pian3 世-界｜se3-kai3'
        組物件 = 拆文分析器.分詞組物件(分詞)
        self.assertEqual(len(組物件.內底詞), 8)

    def test_袂當用全形空白隔開(self):
        分詞 = '去｜khi3\u3000飛-翔｜pue1-siong5'
        with self.assertRaises(解析錯誤):
            拆文分析器.分詞組物件(分詞)

    def test_接受無音的詞(self):
        分詞 = '梅山 猴-災 鄉-公所｜hiong1-kong1-soo2 tshiann2-lang5 趕-走｜kuann2-tsau2 猴山｜kau5-san1'
        組物件 = 拆文分析器.分詞組物件(分詞)
        答案詞陣列 = [
            拆文分析器.建立詞物件('梅山'),
            拆文分析器.建立詞物件('猴-災'),
            拆文分析器.對齊詞物件('鄉-公所', 'hiong1-kong1-soo2'),
            拆文分析器.建立詞物件('tshiann2-lang5'),
            拆文分析器.對齊詞物件('趕-走', 'kuann2-tsau2'),
            拆文分析器.對齊詞物件('猴山', 'kau5-san1'),
        ]
        self.assertEqual(組物件.內底詞, 答案詞陣列)

    def test_讀輕聲(self):
        分詞 = '--ê｜--ê'
        答案 = 拆文分析器.建立句物件('--ê', '--ê')
        self.assertEqual(拆文分析器.分詞句物件(分詞), 答案)

    def test_標準刪節號(self):
        組物件 = 拆文分析器.分詞組物件('枋寮｜Pang-liau5 漁港｜hi5-kang2 ……｜...')
        self.assertEqual(len(組物件.網出詞物件()), 3)
        self.assertEqual(組物件.篩出字物件()[-1], 拆文分析器.對齊字物件('……', '...'))
