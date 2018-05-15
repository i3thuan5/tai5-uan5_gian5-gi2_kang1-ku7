# -*- coding: utf-8 -*-
from unittest.case import TestCase
from unittest.mock import patch, call


from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器


class 摩西用戶端單元試驗(TestCase):

    def setUp(self):
        self.xmlrpcPatcher = patch('xmlrpc.client.ServerProxy')
        self.xmlrpcMock = self.xmlrpcPatcher.start()

        self.用戶端 = 摩西用戶端()  # 'localhost', '8080'
        華語語句 = "我 們 要 去 吃 飯 。"
        self.華語句物件 = 拆文分析器.建立句物件(華語語句)
        self.華語句物件二 = 拆文分析器.建立句物件('好喲！')
        self.華語章物件 = 章([self.華語句物件, self.華語句物件二])

        翻譯對應關係 = [
            {'tgt-start': 0, 'src-start': 0, 'src-end': 1},
            {'tgt-start': 1, 'src-start': 2, 'src-end': 2},
            {'tgt-start': 2, 'src-start': 3, 'src-end': 3},
            {'tgt-start': 3, 'src-start': 4, 'src-end': 5},
            {'tgt-start': 5, 'src-start': 6, 'src-end': 6},
        ]
        self.全漢翻譯結果 = {'nbest': [{
            'hyp': '阮  欲  去  食  飯  。  ',
            'align': 翻譯對應關係,
            'totalScore': -21.66,
            'word-align': [],
        }]}
        self.全漢全羅分詞翻譯結果 = {'nbest': [{
            'hyp': '阮｜gun2  欲｜beh4  去｜khi3  食｜tsiah8  飯｜png7  。｜.  ',
            'align': 翻譯對應關係,
            'totalScore': -21.66,
            'word-align': [],
        }]}
        self.全漢全羅分詞含詞翻譯結果 = {'nbest': [{
            'hyp': '阮｜gun2  欲｜beh4  去｜khi3  食｜tsiah8  炒-飯｜tsha2-png7  。｜.  ',
            'align': 翻譯對應關係,
            'totalScore': -21.66,
            'word-align': [],
        }]}
        self.翻譯結果有未知詞出來 = {'nbest': [{
            'hyp': '阮  要|UNK|UNK|UNK  去  食  飯  。  ',
            'align': 翻譯對應關係,
            'totalScore': -21.66,
            'word-align': [],
        }]}
        self.翻譯結果先後有變化 = {'nbest': [{
            'hyp': '阮  食  飯  愛  去  。  ',
            'align': [
                {'tgt-start': 0, 'src-start': 0, 'src-end': 1},
                {'tgt-start': 1, 'src-start': 4, 'src-end': 5},
                {'tgt-start': 3, 'src-start': 2, 'src-end': 2},
                {'tgt-start': 4, 'src-start': 3, 'src-end': 3},
                {'tgt-start': 5, 'src-start': 6, 'src-end': 6},
            ],
            'totalScore': -21.66,
            'word-align': [],
        }]}

    def tearDown(self):
        self.xmlrpcPatcher.stop()

    @patch('臺灣言語工具.解析整理.物件譀鏡.物件譀鏡.看分詞')
    def test_用看分詞(self, 分詞mock):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢翻譯結果
        self.用戶端.翻譯分析(self.華語句物件)
        分詞mock.assert_called_once_with(self.華語句物件)

    @patch('臺灣言語工具.翻譯.摩西工具.無編碼器.無編碼器.編碼')
    def test_有編碼(self, 編碼mock):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢翻譯結果
        self.用戶端.翻譯分析(self.華語句物件)
        編碼mock.assert_called_once_with("我 們 要 去 吃 飯 。")

    @patch('臺灣言語工具.翻譯.摩西工具.無編碼器.無編碼器.解碼')
    def test_有解碼(self, 解碼mock):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢翻譯結果
        解碼mock.return_value = '阮  欲  去  食  飯  。  '
        self.用戶端.翻譯分析(self.華語句物件)
        解碼mock.assert_called_once_with(self.全漢翻譯結果['nbest'][0]['hyp'])

    def test_翻譯結果是句物件(self):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢翻譯結果
        結果句物件, _, _ = self.用戶端.翻譯分析(self.華語句物件)
        self.assertIsInstance(結果句物件, 句)

    def test_翻譯結果結構(self):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢翻譯結果
        結果句物件, _, _ = self.用戶端.翻譯分析(self.華語句物件)
        閩南語組陣列 = [
            拆文分析器.分詞組物件('阮'),
            拆文分析器.分詞組物件('欲'),
            拆文分析器.分詞組物件('去'),
            拆文分析器.分詞組物件('食 飯'),
            拆文分析器.分詞組物件('。'),
        ]
        閩南語句物件 = self._組陣列分開包做句物件(閩南語組陣列)
        self.assertEqual(結果句物件, 閩南語句物件)

    def test_來源新結構檢查(self):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢翻譯結果
        _, 華語新結構句物件, _ = self.用戶端.翻譯分析(self.華語句物件)
        華語組陣列 = [
            拆文分析器.分詞組物件('我 們'),
            拆文分析器.分詞組物件('要'),
            拆文分析器.分詞組物件('去'),
            拆文分析器.分詞組物件('吃 飯'),
            拆文分析器.分詞組物件('。'),
        ]
        華語句物件 = self._組陣列分開包做句物件(華語組陣列)
        self.assertEqual(華語新結構句物件, 華語句物件)

    def test_翻譯結果佮來源長度相仝(self):
        結果句物件, 華語新結構句物件, _ = self.用戶端.翻譯分析(self.華語句物件)
        self.assertEqual(len(結果句物件.內底集),
                         len(華語新結構句物件.內底集))

    def test_翻譯結果對齊檢查(self):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢翻譯結果
        結果句物件, _, _ = self.用戶端.翻譯分析(self.華語句物件)
        for 集物件 in 結果句物件.內底集:
            self.assertEqual(集物件.內底組[0], 集物件.內底組[0].翻譯來源組物件.翻譯目標組物件)

    def test_來源新結構對齊檢查(self):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢翻譯結果
        _, 華語新結構句物件, _ = self.用戶端.翻譯分析(self.華語句物件)
        for 集物件 in 華語新結構句物件.內底集:
            self.assertEqual(集物件.內底組[0], 集物件.內底組[0].翻譯目標組物件.翻譯來源組物件)

    def test_翻譯分數(self):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢翻譯結果
        _, _, 分數 = self.用戶端.翻譯分析(self.華語句物件)
        self.assertEqual(分數, -21.66)

    def test_全漢全羅分詞結果(self):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢全羅分詞翻譯結果
        結果句物件, _, _ = self.用戶端.翻譯分析(self.華語句物件)
        閩南語組陣列 = [
            拆文分析器.分詞組物件('阮｜gun2'),
            拆文分析器.分詞組物件('欲｜beh4'),
            拆文分析器.分詞組物件('去｜khi3'),
            拆文分析器.分詞組物件('食｜tsiah8  飯｜png7'),
            拆文分析器.分詞組物件('。｜.'),
        ]
        閩南語句物件 = self._組陣列分開包做句物件(閩南語組陣列)
        self.assertEqual(結果句物件, 閩南語句物件)

    def test_全漢全羅分詞含詞結果(self):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢全羅分詞含詞翻譯結果
        結果句物件, _, _ = self.用戶端.翻譯分析(self.華語句物件)
        閩南語組陣列 = [
            拆文分析器.分詞組物件('阮｜gun2'),
            拆文分析器.分詞組物件('欲｜beh4'),
            拆文分析器.分詞組物件('去｜khi3'),
            拆文分析器.分詞組物件('食｜tsiah8 炒-飯｜tsha2-png7'),
            拆文分析器.分詞組物件('。｜.'),
        ]
        閩南語句物件 = self._組陣列分開包做句物件(閩南語組陣列)
        self.assertEqual(結果句物件, 閩南語句物件)

    def test_未知詞結果(self):
        self.xmlrpcMock.return_value.translate.return_value = self.翻譯結果有未知詞出來
        結果句物件, _, _ = self.用戶端.翻譯分析(self.華語句物件)
        閩南語組陣列 = [
            拆文分析器.分詞組物件('阮'),
            拆文分析器.分詞組物件('要'),
            拆文分析器.分詞組物件('去'),
            拆文分析器.分詞組物件('食 飯'),
            拆文分析器.分詞組物件('。'),
        ]
        閩南語句物件 = self._組陣列分開包做句物件(閩南語組陣列)
        self.assertEqual(結果句物件, 閩南語句物件)

    def test_未知詞的詞愛記錄(self):
        self.xmlrpcMock.return_value.translate.return_value = self.翻譯結果有未知詞出來
        結果句物件, _, _ = self.用戶端.翻譯分析(self.華語句物件)
        self.assertEqual(物件譀鏡.看型(結果句物件.內底集[1].內底組[0]), '要')
        self.assertTrue(結果句物件.內底集[1].內底組[0].屬性['未知詞'])

    def test_毋是未知詞的詞袂使記錄(self):
        self.xmlrpcMock.return_value.translate.return_value = self.翻譯結果有未知詞出來
        結果句物件, _, _ = self.用戶端.翻譯分析(self.華語句物件)
        self.assertEqual(物件譀鏡.看型(結果句物件.內底集[0].內底組[0]), '阮')
        self.assertFalse(結果句物件.內底集[0].內底組[0].屬性['未知詞'])

    def test_翻譯結果先後有變化(self):
        self.xmlrpcMock.return_value.translate.return_value = self.翻譯結果先後有變化
        結果句物件, _, _ = self.用戶端.翻譯分析(self.華語句物件)
        self.assertEqual(物件譀鏡.看型(結果句物件.內底集[1].內底組[0]), '食飯')
        self.assertEqual(物件譀鏡.看型(結果句物件.內底集[1].內底組[0].翻譯來源組物件), '吃飯')

    @patch('臺灣言語工具.翻譯.摩西工具.摩西用戶端.摩西用戶端._翻譯句物件')
    def test_章物件的結果是章物件(self, 翻譯句物件mock):
        翻譯句物件mock.return_value = None, None, -21.66
        結果章物件, _, _ = self.用戶端.翻譯分析(self.華語章物件)
        self.assertIsInstance(結果章物件, 章)

    @patch('臺灣言語工具.翻譯.摩西工具.摩西用戶端.摩西用戶端._翻譯句物件')
    def test_章物件的來源新結構章物件(self, 翻譯句物件mock):
        翻譯句物件mock.return_value = None, None, -21.66
        _, 華語新結構章物件, _ = self.用戶端.翻譯分析(self.華語章物件)
        self.assertIsInstance(華語新結構章物件, 章)

    @patch('臺灣言語工具.翻譯.摩西工具.摩西用戶端.摩西用戶端._翻譯句物件')
    def test_結果章物件長度佮原本一樣(self, 翻譯句物件mock):
        翻譯句物件mock.return_value = None, None, -21.66
        結果章物件, _, _ = self.用戶端.翻譯分析(self.華語章物件)
        self.assertEqual(len(結果章物件.內底句), len(self.華語章物件.內底句))

    @patch('臺灣言語工具.翻譯.摩西工具.摩西用戶端.摩西用戶端._翻譯句物件')
    def test_新結構章物件長度佮原本一樣(self, 翻譯句物件mock):
        翻譯句物件mock.return_value = None, None, -21.66
        _, 華語新結構章物件, _ = self.用戶端.翻譯分析(self.華語章物件)
        self.assertEqual(len(華語新結構章物件.內底句), len(self.華語章物件.內底句))

    @patch('臺灣言語工具.翻譯.摩西工具.摩西用戶端.摩西用戶端._翻譯句物件')
    def test_翻譯章物件的分數(self, 翻譯句物件mock):
        翻譯句物件mock.return_value = None, None, -21.66
        _, _, 分數 = self.用戶端.翻譯分析(self.華語章物件)
        self.assertEqual(分數, -21.66 - 21.66)

    @patch('臺灣言語工具.翻譯.摩西工具.摩西用戶端.摩西用戶端._翻譯句物件')
    def test_章物件是一句一句翻譯(self, 翻譯句物件mock):
        翻譯句物件mock.return_value = None, None, -21.66
        self.用戶端.翻譯分析(self.華語章物件)
        翻譯句物件mock.assert_has_calls(
            [call(self.華語句物件), call(self.華語句物件二)],
            any_order=True
        )

    def test_翻譯實際例(self):
        華語章 = '大-約 六-千 兩-百 九-十-六-萬-票 的 普-選-票 ；'
        self.xmlrpcMock.return_value.translate.return_value = {'nbest': [{
            'align': [
                {'src-end': 0, 'src-start': 0, 'tgt-start': 0},
                {'src-end': 1, 'src-start': 1, 'tgt-start': 1},
                {'src-end': 2, 'src-start': 2, 'tgt-start': 2},
                {'src-end': 3, 'src-start': 3, 'tgt-start': 3},
                {'src-end': 4, 'src-start': 4, 'tgt-start': 4},
                {'src-end': 5, 'src-start': 5, 'tgt-start': 5},
                {'src-end': 6, 'src-start': 6, 'tgt-start': 6},
            ],
            'hyp': ' \\uff0c  '
            '\\u516d-\\u5343-\\u5169-\\u767e-\\u4e5d-\\u5341-\\u516d-\\u842c|UNK|UNK|UNK  '
            '\\u7968|UNK|UNK|UNK  e5  \\u666e|UNK|UNK|UNK  \\uff0c  e5  ',
            'totalScore': -458.9802856445312,
            'word-align': [
                {'source-word': 0, 'target-word': 0},
                {'source-word': 1, 'target-word': 1},
                {'source-word': 2, 'target-word': 2},
                {'source-word': 3, 'target-word': 3},
                {'source-word': 4, 'target-word': 4},
                {'source-word': 5, 'target-word': 5},
                {'source-word': 6, 'target-word': 6},
            ]
        }]}
        用戶端 = 摩西用戶端(編碼器=語句編碼器())
        用戶端.翻譯分析(拆文分析器.分詞章物件(華語章))

    def test_翻譯語句換逝應該先提掉(self):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢翻譯結果
        章物件 = 拆文分析器.分詞章物件('我 們 要 去 吃 飯 。 \n')
        self.用戶端.翻譯分析(章物件)
        self.xmlrpcMock.return_value.translate.assert_called_once_with({
            'text': '我 們 要 去 吃 飯 。',
            'align': 'true',
            'nbest': 1,
            'report-all-factors': 'true',
        }
        )

    def test_翻譯語句換逝分詞應該先提掉(self):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢翻譯結果
        章物件 = 拆文分析器.分詞章物件('我 們 要 去 吃 飯 。\n｜\n')
        self.用戶端.翻譯分析(章物件)
        self.xmlrpcMock.return_value.translate.assert_called_once_with({
            'text': '我 們 要 去 吃 飯 。',
            'align': 'true',
            'nbest': 1,
            'report-all-factors': 'true',
        }
        )

    def test_翻譯語句上尾換逝結果物件應該閣愛有(self):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢翻譯結果
        章物件 = 拆文分析器.分詞章物件('我 們 要 去 吃 飯 。\n')
        結果章物件, _, _ = self.用戶端.翻譯分析(章物件)
        閩南語組陣列 = [
            拆文分析器.分詞組物件('阮'),
            拆文分析器.分詞組物件('欲'),
            拆文分析器.分詞組物件('去'),
            拆文分析器.分詞組物件('食 飯'),
            拆文分析器.分詞組物件('。'),
            拆文分析器.分詞組物件('\n'),
        ]
        閩南語句物件 = self._組陣列分開包做句物件(閩南語組陣列)
        self.assertEqual(結果章物件.內底句, [閩南語句物件])

    def test_翻譯語句上尾換逝新結構應該閣愛有(self):
        self.xmlrpcMock.return_value.translate.return_value = self.全漢翻譯結果
        章物件 = 拆文分析器.分詞章物件('我 們 要 去 吃 飯 。 \n')
        _, 華語新結構章物件, _ = self.用戶端.翻譯分析(章物件)
        華語組陣列 = [
            拆文分析器.分詞組物件('我 們'),
            拆文分析器.分詞組物件('要'),
            拆文分析器.分詞組物件('去'),
            拆文分析器.分詞組物件('吃 飯'),
            拆文分析器.分詞組物件('。'),
            拆文分析器.分詞組物件('\n'),
        ]
        華語句物件 = self._組陣列分開包做句物件(華語組陣列)
        self.assertEqual(華語新結構章物件.內底句, [華語句物件])

    def _組陣列分開包做句物件(self, 組陣列):
        句物件 = 句()
        for 組物件 in 組陣列:
            集物件 = 集()
            集物件.內底組 = [組物件]
            句物件.內底集.append(集物件)
        return 句物件

    @patch('臺灣言語工具.翻譯.摩西工具.摩西用戶端.摩西用戶端.翻譯分析')
    def test_翻譯物件(self, 翻譯分析mock):
        章物件 = 拆文分析器.分詞章物件('我 們 要 去 吃 飯 。 \n')
        翻譯章物件 = self.用戶端.翻譯(章物件)
        self.assertEqual(翻譯章物件, 翻譯分析mock.return_value[0])
