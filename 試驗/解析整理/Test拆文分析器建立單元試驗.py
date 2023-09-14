# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.基本物件.字 import 字


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
        語句 = '椅仔'
        self.assertEqual(
            拆文分析器.建立詞物件(語句).內底字,
            [拆文分析器.建立字物件('椅'), 拆文分析器.建立字物件('仔')]
        )

    def test_建立詞濟字音標(self):
        語句 = 'tsit8-tiunn1'
        self.assertEqual(
            拆文分析器.建立詞物件(語句).內底字,
            [拆文分析器.建立字物件('tsit8'), 拆文分析器.建立字物件('tiunn1')]
        )

    def test_建立詞濟字漢羅(self):
        語句 = 'tsit8-張'
        self.assertEqual(
            拆文分析器.建立詞物件(語句).內底字,
            [拆文分析器.建立字物件('tsit8'), 拆文分析器.建立字物件('張')]
        )

    def test_建立詞底線嘛算是詞的一部份V_2(self):
        語句 = 'V_2'
        self.assertEqual(
            拆文分析器.建立詞物件(語句).內底字,
            [拆文分析器.建立字物件(語句)]
        )

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
        切好語句 = ['我有一張椅仔', '！']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_建立組濟字有詞配空白(self):
        原來語句 = '我 有 一-張 椅仔！'
        切好語句 = ['我', '有', '一張', '椅仔', '！']
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

    def test_雙數字音標(self):
        原來語句 = 'gua51 ai51 li51'
        切好語句 = ['gua51', 'ai51', 'li51']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(詞陣列, 組物件.內底詞)

    def test_無空白分開的閩南語音標(self):
        有空白 = 'sui2 sui2 e5 koo1 niu5'
        無空白 = 有空白.replace(' ', '')
        self.assertNotEqual(拆文分析器.建立組物件(有空白), 拆文分析器.建立組物件(無空白))

    def test_無空白分開的音調音標(self):
        有空白 = 'sui55 sui51 e13 koo33 niu13'
        無空白 = 有空白.replace(' ', '')
        self.assertNotEqual(拆文分析器.建立組物件(有空白), 拆文分析器.建立組物件(無空白))

    def test_大寫專有符號袂使拆開(self):
        無空白 = 'H1N1 新型 流感 包含 四種 病毒'
        有空白 = 'H1 N1 新型 流感 包含 四種 病毒'
        self.assertEqual(len(拆文分析器.建立組物件(無空白).內底詞), 6)
        self.assertNotEqual(拆文分析器.建立組物件(有空白), 拆文分析器.建立組物件(無空白))

    def test_小寫專有符號袂使拆開(self):
        無空白 = 'g0v 是 咱 的 好 厝邊'
        有空白 = 'g0 v 是 咱 的 好 厝邊'
        self.assertEqual(
            len(拆文分析器.建立組物件(無空白).內底詞), 6
        )
        self.assertNotEqual(
            拆文分析器.建立組物件(有空白), 拆文分析器.建立組物件(無空白)
        )

    def test_大寫音標袂使拆開(self):
        # 愛予粗胚處理
        無空白 = 'Sui2sui2 是 咱 的 好 厝邊'
        有空白 = 'Sui2 sui2 是 咱 的 好 厝邊'
        self.assertEqual(len(拆文分析器.建立組物件(無空白).內底詞), 6)
        self.assertNotEqual(拆文分析器.建立組物件(有空白), 拆文分析器.建立組物件(無空白))

    def test_小寫音標袂使拆開(self):
        # 愛予粗胚處理
        無空白 = 'sui2sui2 是 咱 的 好 厝邊'
        有空白 = 'sui2 sui2 是 咱 的 好 厝邊'
        self.assertEqual(len(拆文分析器.建立組物件(無空白).內底詞), 6)
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

    def test_建立組換逝(self):
        換逝 = '\n'
        組物件 = 拆文分析器.建立組物件(換逝)
        self.assertEqual(組物件.內底詞, [拆文分析器.建立詞物件(換逝)])
        self.assertEqual(組物件.內底詞[0].內底字, [字(換逝, 無音)])

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
            [句物件.看語句() for 句物件 in 拆文分析器.建立章物件(語句).內底句],
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

    def test_臺羅刪節號(self):
        組物件 = 拆文分析器.建立組物件('Pang-liau5 hi5-kang2...')
        self.assertEqual(len(組物件.網出詞物件()), 3)
        self.assertEqual(組物件.篩出字物件()[-1], 拆文分析器.建立字物件('...'))

    def test_漢字刪節號(self):
        組物件 = 拆文分析器.建立組物件('枋寮漁港……')
        self.assertEqual(len(組物件.網出詞物件()), 2)
        self.assertEqual(組物件.篩出字物件()[-1], 拆文分析器.建立字物件('……'))

    def test_臺羅刪節詞(self):
        詞物件 = 拆文分析器.建立詞物件('...')
        self.assertEqual(詞物件.篩出字物件(), [拆文分析器.建立字物件('...')])

    def test_漢字刪節詞(self):
        詞物件 = 拆文分析器.建立詞物件('……')
        self.assertEqual(詞物件.篩出字物件(), [拆文分析器.建立字物件('……')])

    def test_綜合刪節詞(self):
        組物件 = 拆文分析器.建立組物件('………....…')
        self.assertEqual(組物件.篩出字物件(), [
            拆文分析器.建立字物件('……'),
            拆文分析器.建立字物件('…'),
            拆文分析器.建立字物件('...'),
            拆文分析器.建立字物件('.'),
            拆文分析器.建立字物件('…'),
        ])

    def test_破折號(self):
        詞物件 = 拆文分析器.建立詞物件('──')
        self.assertEqual(詞物件.篩出字物件(), [拆文分析器.建立字物件('──')])

    def test_tab當做空白(self):
        組物件 = 拆文分析器.建立組物件('\t千金小姐\ttshian1-kim1-sio2-tsia2\t')
        self.assertEqual(
            組物件.篩出字物件(),
            [
                拆文分析器.建立字物件('千'),
                拆文分析器.建立字物件('金'),
                拆文分析器.建立字物件('小'),
                拆文分析器.建立字物件('姐'),
                拆文分析器.建立字物件('tshian1'),
                拆文分析器.建立字物件('kim1'),
                拆文分析器.建立字物件('sio2'),
                拆文分析器.建立字物件('tsia2'),
            ]
        )

    def test_干焦tab(self):
        組物件 = 拆文分析器.建立組物件('\t\t')
        self.assertEqual(len(組物件.網出詞物件()), 0)
        self.assertEqual(len(組物件.篩出字物件()), 0)

    def test_兩參數就當做是對齊字(self):
        字物件 = 拆文分析器.建立字物件('媠', 'Suí')
        self.assertEqual(字物件.型, '媠')
        self.assertEqual(字物件.音, 'Suí')

    @patch('臺灣言語工具.解析整理.拆文分析器.拆文分析器.對齊詞物件')
    def test_兩參數就當做是對齊詞(self, 對齊mock):
        拆文分析器.建立詞物件('媠', 'Suí')
        對齊mock.assert_called_once_with('媠', 'Suí')

    @patch('臺灣言語工具.解析整理.拆文分析器.拆文分析器.對齊詞物件')
    def test_兩參數的結果佮對齊詞仝款(self, 對齊mock):
        self.assertEqual(拆文分析器.建立詞物件('媠', 'Suí'), 對齊mock.return_value)

    @patch('臺灣言語工具.解析整理.拆文分析器.拆文分析器.對齊組物件')
    def test_兩參數就當做是對齊組(self, 對齊mock):
        拆文分析器.建立組物件('媠', 'Suí')
        對齊mock.assert_called_once_with('媠', 'Suí')

    @patch('臺灣言語工具.解析整理.拆文分析器.拆文分析器.對齊組物件')
    def test_兩參數的結果佮對齊組仝款(self, 對齊mock):
        self.assertEqual(拆文分析器.建立組物件('媠', 'Suí'), 對齊mock.return_value)

    @patch('臺灣言語工具.解析整理.拆文分析器.拆文分析器.對齊集物件')
    def test_兩參數就當做是對齊集(self, 對齊mock):
        拆文分析器.建立集物件('媠', 'Suí')
        對齊mock.assert_called_once_with('媠', 'Suí')

    @patch('臺灣言語工具.解析整理.拆文分析器.拆文分析器.對齊集物件')
    def test_兩參數的結果佮對齊集仝款(self, 對齊mock):
        self.assertEqual(拆文分析器.建立集物件('媠', 'Suí'), 對齊mock.return_value)

    @patch('臺灣言語工具.解析整理.拆文分析器.拆文分析器.對齊句物件')
    def test_兩參數就當做是對齊句(self, 對齊mock):
        拆文分析器.建立句物件('媠', 'Suí')
        對齊mock.assert_called_once_with('媠', 'Suí')

    @patch('臺灣言語工具.解析整理.拆文分析器.拆文分析器.對齊句物件')
    def test_兩參數的結果佮對齊句仝款(self, 對齊mock):
        self.assertEqual(拆文分析器.建立句物件('媠', 'Suí'), 對齊mock.return_value)

    @patch('臺灣言語工具.解析整理.拆文分析器.拆文分析器.對齊章物件')
    def test_兩參數就當做是對齊章(self, 對齊mock):
        拆文分析器.建立章物件('媠', 'Suí')
        對齊mock.assert_called_once_with('媠', 'Suí')

    @patch('臺灣言語工具.解析整理.拆文分析器.拆文分析器.對齊章物件')
    def test_兩參數的結果佮對齊章仝款(self, 對齊mock):
        self.assertEqual(拆文分析器.建立章物件('媠', 'Suí'), 對齊mock.return_value)
