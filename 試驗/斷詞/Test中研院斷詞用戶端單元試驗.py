# -*- coding: utf-8 -*-
from itertools import zip_longest
import unittest
from unittest.mock import patch, call


from 臺灣言語工具.斷詞.中研院.斷詞用戶端 import 斷詞用戶端
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.組 import 組
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔
from 臺灣言語工具.基本物件.詞 import 詞


@patch('臺灣言語工具.斷詞.中研院.斷詞用戶端.斷詞用戶端.語句斷詞做語句')
class 中研院斷詞用戶端單元試驗(unittest.TestCase):
    def setUp(self):
        self.用戶端 = 斷詞用戶端()

    def tearDown(self):
        pass

    def test_物件斷一句話句物件內容(self, 語句斷詞做語句mock):
        輸入句物件 = 拆文分析器.建立句物件('我想吃飯。')
        語句斷詞做語句mock.return_value = [[
            '\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)'
        ]]
        斷詞後句物件 = self.用戶端.斷詞(輸入句物件)
        答案組物件 = 組()
        答案組物件.內底詞 = [
            拆文分析器.建立詞物件('我'),
            拆文分析器.建立詞物件('想'),
            拆文分析器.建立詞物件('吃飯'),
            拆文分析器.建立詞物件('。'),
        ]
        答案集物件 = 集()
        答案集物件.內底組 = [答案組物件]
        答案句物件 = 句()
        答案句物件.內底集 = [答案集物件]
        self.assertEqual(斷詞後句物件, 答案句物件)

    def test_物件斷一句話句物件詞性(self, 語句斷詞做語句mock):
        輸入句物件 = 拆文分析器.建立句物件('我想吃飯。')
        語句斷詞做語句mock.return_value = [[
            '\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)'
        ]]
        斷詞後章物件 = self.用戶端.斷詞(輸入句物件)
        for 詞物件, 詞性 in zip_longest(
                詞物件網仔.網出詞物件(斷詞後章物件),
                ['N', 'Vt', 'Vi', 'PERIODCATEGORY']
        ):
            self.assertEqual(詞物件.屬性['詞性'], 詞性)

    def test_物件斷一句話章物件內容(self, 語句斷詞做語句mock):
        輸入章物件 = 拆文分析器.建立章物件('我想吃飯。')
        語句斷詞做語句mock.return_value = [[
            '\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)'
        ]]
        斷詞後章物件 = self.用戶端.斷詞(輸入章物件)
        答案組物件 = 組()
        答案組物件.內底詞 = [
            拆文分析器.建立詞物件('我'),
            拆文分析器.建立詞物件('想'),
            拆文分析器.建立詞物件('吃飯'),
            拆文分析器.建立詞物件('。'),
        ]
        答案集物件 = 集()
        答案集物件.內底組 = [答案組物件]
        答案句物件 = 句()
        答案句物件.內底集 = [答案集物件]
        答案章物件 = 章()
        答案章物件.內底句 = [答案句物件]
        self.assertEqual(斷詞後章物件, 答案章物件)

    def test_物件斷一句話章物件詞性(self, 語句斷詞做語句mock):
        輸入章物件 = 拆文分析器.建立章物件('我想吃飯。')
        語句斷詞做語句mock.return_value = [[
            '\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)'
        ]]
        斷詞後章物件 = self.用戶端.斷詞(輸入章物件)
        for 詞物件, 詞性 in zip_longest(
                詞物件網仔.網出詞物件(斷詞後章物件),
                ['N', 'Vt', 'Vi', 'PERIODCATEGORY']
        ):
            self.assertEqual(詞物件.屬性['詞性'], 詞性)

    @patch('臺灣言語工具.斷詞.中研院.斷詞用戶端.斷詞用戶端._斷句物件詞')
    def test_物件斷一逝字(self, 斷句物件詞mock, 語句斷詞做語句mock):
        輸入章物件 = 拆文分析器.建立章物件('我想吃飯。我想吃很多飯。')
        語句斷詞做語句mock.return_value = [[
            '\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
            '\u3000我(N)\u3000想(Vt)\u3000吃(Vt)\u3000很多(DET)\u3000飯(N)\u3000。(PERIODCATEGORY)',
        ]]
        self.用戶端.斷詞(輸入章物件)
        斷句物件詞mock.assert_has_calls([
            call(拆文分析器.建立句物件('我想吃飯。'), 10, False),
            call(拆文分析器.建立句物件('我想吃很多飯。'), 10, False)
        ])

    def test_物件上尾有換逝符號詞數檢查(self, 語句斷詞做語句mock):
        輸入章物件 = 拆文分析器.建立章物件('我想吃飯。\n')
        語句斷詞做語句mock.return_value = [[
            '\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
        ]]
        斷詞後章物件 = self.用戶端.斷詞(輸入章物件)
        self.assertEqual(
            len(詞物件網仔.網出詞物件(斷詞後章物件)),
            5,
        )

    def test_物件上尾有換逝符號結構檢查(self, 語句斷詞做語句mock):
        輸入章物件 = 拆文分析器.建立章物件('我想吃飯。\n')
        語句斷詞做語句mock.return_value = [[
            '\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
        ]]
        斷詞後章物件 = self.用戶端.斷詞(輸入章物件)
        答案組物件 = 組()
        答案組物件.內底詞 = [
            拆文分析器.建立詞物件('我'),
            拆文分析器.建立詞物件('想'),
            拆文分析器.建立詞物件('吃飯'),
            拆文分析器.建立詞物件('。'),
            拆文分析器.建立詞物件('\n'),
        ]
        答案集物件 = 集()
        答案集物件.內底組 = [答案組物件]
        答案句物件 = 句()
        答案句物件.內底集 = [答案集物件]
        答案章物件 = 章()
        答案章物件.內底句 = [答案句物件]
        self.assertEqual(斷詞後章物件, 答案章物件)

    def test_物件上尾有換逝符號詞性檢查(self, 語句斷詞做語句mock):
        輸入章物件 = 拆文分析器.建立章物件('我想吃飯。\n')
        語句斷詞做語句mock.return_value = [[
            '\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
        ]]
        斷詞後章物件 = self.用戶端.斷詞(輸入章物件)
        for 詞物件, 詞性 in zip_longest(
                詞物件網仔.網出詞物件(斷詞後章物件),
                ['N', 'Vt', 'Vi', 'PERIODCATEGORY', '']
        ):
            self.assertEqual(詞物件.屬性['詞性'], 詞性)

    def test_物件空白逝句物件詞數檢查(self, 語句斷詞做語句mock):
        輸入章物件 = 拆文分析器.建立章物件('\n \n')
        語句斷詞做語句mock.return_value = []
        斷詞後章物件 = self.用戶端.斷詞(輸入章物件)
        self.assertEqual(
            len(詞物件網仔.網出詞物件(斷詞後章物件)),
            2,
        )

    def test_物件空白逝句物件結構檢查(self, 語句斷詞做語句mock):
        輸入章物件 = 拆文分析器.建立章物件('\n \n')
        語句斷詞做語句mock.return_value = []
        斷詞後章物件 = self.用戶端.斷詞(輸入章物件)
        答案組物件 = 組()
        答案組物件.內底詞 = [
            詞([拆文分析器.建立字物件('\n')]),
            詞([拆文分析器.建立字物件('\n')]),
        ]
        答案集物件 = 集()
        答案集物件.內底組 = [答案組物件]
        答案句物件 = 句()
        答案句物件.內底集 = [答案集物件]
        答案章物件 = 章()
        答案章物件.內底句 = [答案句物件]
        self.assertEqual(斷詞後章物件, 答案章物件)

    def test_物件空白逝句物件詞性檢查(self, 語句斷詞做語句mock):
        輸入章物件 = 拆文分析器.建立章物件('\n \n')
        語句斷詞做語句mock.return_value = []
        斷詞後章物件 = self.用戶端.斷詞(輸入章物件)
        for 詞物件, 詞性 in zip_longest(
                詞物件網仔.網出詞物件(斷詞後章物件),
                ['', '']
        ):
            self.assertEqual(詞物件.屬性['詞性'], 詞性)

    def test_物件斷小於符號的空白結果(self, 語句斷詞做語句mock):
        輸入章物件 = 拆文分析器.建立章物件('我想) :<')
        語句斷詞做語句mock.return_value = []
        斷詞後章物件 = self.用戶端.斷詞(輸入章物件)
        for 詞物件, 詞性 in zip_longest(
                詞物件網仔.網出詞物件(斷詞後章物件),
                ['', '', '', '', '', ]
        ):
            self.assertEqual(詞物件.屬性['詞性'], 詞性)

    def test_物件英文字(self, 語句斷詞做語句mock):
        輸入章物件 = 拆文分析器.建立章物件('sui2')
        語句斷詞做語句mock.return_value = [['\u3000sui2(FW)']]
        斷詞後章物件 = self.用戶端.斷詞(輸入章物件)
        for 詞物件, 詞性 in zip_longest(
                詞物件網仔.網出詞物件(斷詞後章物件),
                ['FW']
        ):
            self.assertEqual(詞物件.屬性['詞性'], 詞性)

    def test_結構斷一句話(self, 語句斷詞做語句mock):
        語句斷詞做語句mock.return_value = [[
            '\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
        ]]
        self.assertEqual(self.用戶端.語句斷詞後結構化('我想吃飯。'), [[
            [('我', 'N'), ('想', 'Vt'), ('吃飯', 'Vi'), ('。', 'PERIODCATEGORY')],
        ]])

    def test_結構斷一逝字(self, 語句斷詞做語句mock):
        語句斷詞做語句mock.return_value = [[
            '\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
            '\u3000我(N)\u3000想(Vt)\u3000吃(Vt)\u3000很多(DET)\u3000飯(N)\u3000。(PERIODCATEGORY)',
        ]]
        self.assertEqual(self.用戶端.語句斷詞後結構化('我想吃飯。我想吃很多飯。'), [[
            [('我', 'N'), ('想', 'Vt'), ('吃飯', 'Vi'), ('。', 'PERIODCATEGORY')],
            [('我', 'N'), ('想', 'Vt'), ('吃', 'Vt'),
             ('很多', 'DET'), ('飯', 'N'), ('。', 'PERIODCATEGORY')]
        ]])

    def test_結構斷兩逝字(self, 語句斷詞做語句mock):
        語句斷詞做語句mock.return_value = [
            [
                '\u3000我(N)\u3000想(Vt)\u3000吃飯(Vi)\u3000。(PERIODCATEGORY)',
                '\u3000我(N)\u3000想(Vt)\u3000吃(Vt)\u3000很多(DET)\u3000飯(N)\u3000。(PERIODCATEGORY)',
            ], [
                '\u3000我(N)\u3000吃飽(Vi)\u3000了(T)\u3000。(PERIODCATEGORY)',
            ]
        ]
        self.assertEqual(self.用戶端.語句斷詞後結構化('我想吃飯。我想吃很多飯。\n我吃飽了。'), [
            [
                [('我', 'N'), ('想', 'Vt'), ('吃飯', 'Vi'),
                 ('。', 'PERIODCATEGORY')],
                [('我', 'N'), ('想', 'Vt'), ('吃', 'Vt'),
                 ('很多', 'DET'), ('飯', 'N'), ('。', 'PERIODCATEGORY')]
            ],
            [
                [('我', 'N'), ('吃飽', 'Vi'), ('了', 'T'),
                 ('。', 'PERIODCATEGORY')],
            ],
        ])

    def test_結構斷大於符號(self, 語句斷詞做語句mock):
        語句斷詞做語句mock.return_value = [[
            '\u3000我(N)\u3000想(Vt)\u3000)(PARENTHESISCATEGORY)\u3000:(COLONCATEGORY)\u3000&gt;(PARENTHESISCATEGORY)'
        ]]
        self.assertEqual(self.用戶端.語句斷詞後結構化('我想) :>'), [[
            [('我', 'N'), ('想', 'Vt'), (')', 'PARENTHESISCATEGORY'),
             (':', 'COLONCATEGORY'), ('&gt;', 'PARENTHESISCATEGORY')],
        ]])

    def test_結構斷小於符號的空白結果(self, 語句斷詞做語句mock):
        語句斷詞做語句mock.return_value = []
        self.assertEqual(self.用戶端.語句斷詞後結構化('我想) :<'), [
        ])
