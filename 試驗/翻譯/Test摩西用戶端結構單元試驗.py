# -*- coding: utf-8 -*-
from unittest.case import TestCase
from unittest.mock import patch


from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器


class 摩西用戶端結構單元試驗(TestCase):

    def setUp(self):
        self.xmlrpcPatcher = patch('xmlrpc.client.ServerProxy')
        self.xmlrpcMock = self.xmlrpcPatcher.start()

        self.xmlrpcMock.return_value.translate.return_value = {'nbest': [{
            'align': [
                {'src-end': 0, 'src-start': 0, 'tgt-start': 0},
                {'src-end': 1, 'src-start': 1, 'tgt-start': 1},
                {'src-end': 2, 'src-start': 2, 'tgt-start': 2},
                {'src-end': 3, 'src-start': 3, 'tgt-start': 3},
                {'src-end': 4, 'src-start': 4, 'tgt-start': 4},
                {'src-end': 5, 'src-start': 5, 'tgt-start': 5},
                {'src-end': 6, 'src-start': 6, 'tgt-start': 6},
                {'src-end': 10, 'src-start': 7, 'tgt-start': 7},
                {'src-end': 11, 'src-start': 11, 'tgt-start': 14},
                {'src-end': 12, 'src-start': 12, 'tgt-start': 15},
                {'src-end': 13, 'src-start': 13, 'tgt-start': 16}
            ],
            'hyp': ' \\uff0c  '
            '\\u516d-\\u5343-\\u5169-\\u767e-\\u4e5d-\\u5341-\\u516d-\\u842c|UNK|UNK|UNK  '
            '\\u7968|UNK|UNK|UNK  e5  \\u666e|UNK|UNK|UNK  \\uff0c  e5  '
            'iann5-ke3 Kiong7-ho5-tong2 hau7-soan2-jin5 McCain e5 pah-hun-chi '
            'si3-chap8-lak8  e5  '
            '\\u767e-\\u5206-\\u4e4b-\\u56db-\\u5341-\\u516d|UNK|UNK|UNK  '
            '\\uff0c  ',
            'totalScore': -458.9802856445312,
            'word-align': [
                {'source-word': 0, 'target-word': 0},
                {'source-word': 1, 'target-word': 1},
                {'source-word': 2, 'target-word': 2},
                {'source-word': 3, 'target-word': 3},
                {'source-word': 4, 'target-word': 4},
                {'source-word': 5, 'target-word': 5},
                {'source-word': 6, 'target-word': 6},
                {'source-word': 7, 'target-word': 7},
                {'source-word': 8, 'target-word': 7},
                {'source-word': 8, 'target-word': 8},
                {'source-word': 8, 'target-word': 9},
                {'source-word': 8, 'target-word': 10},
                {'source-word': 8, 'target-word': 12},
                {'source-word': 8, 'target-word': 13},
                {'source-word': 9, 'target-word': 11},
                {'source-word': 11, 'target-word': 14},
                {'source-word': 12, 'target-word': 15},
                {'source-word': 13, 'target-word': 16}
            ]
        }]}
        華語句物件 = 拆文分析器.分詞句物件(
            '大-約 六-千 兩-百-九-十-六-萬-票 的 普-選-票 ； '
            '贏-過 共-和-黨 候-選-人 麥-肯 的 百-分-之 四-十-六 ，'
        )
        self.結果句物件, self.華語新結構句物件, _分數 = (
            摩西用戶端(編碼器=語句編碼器).翻譯分析(華語句物件)
        )

    def tearDown(self):
        self.xmlrpcPatcher.stop()

    def test_翻譯結果對著孤詞(self):
        結果詞陣列 = self.結果句物件.網出詞物件()
        華語詞陣列 = self.華語新結構句物件.網出詞物件()
        self.assertEqual(len(華語詞陣列[0].翻譯目標詞陣列), 1)
        self.assertIs(華語詞陣列[0].翻譯目標詞陣列[0], 結果詞陣列[0])

    def test_翻譯結果對著濟詞(self):
        結果詞陣列 = self.結果句物件.網出詞物件()
        華語詞陣列 = self.華語新結構句物件.網出詞物件()
        self.assertEqual(len(華語詞陣列[8].翻譯目標詞陣列), 6)
        self.assertIs(華語詞陣列[8].翻譯目標詞陣列[3], 結果詞陣列[10])

    def test_翻譯結果無對著詞(self):
        華語詞陣列 = self.華語新結構句物件.網出詞物件()
        self.assertEqual(len(華語詞陣列[10].翻譯目標詞陣列), 0)

    def test_來源新結構檢查(self):
        結果詞陣列 = self.結果句物件.網出詞物件()
        華語詞陣列 = self.華語新結構句物件.網出詞物件()
        self.assertEqual(len(結果詞陣列[16].翻譯來源詞陣列), 1)
        self.assertIs(結果詞陣列[16].翻譯來源詞陣列[0], 華語詞陣列[13])
