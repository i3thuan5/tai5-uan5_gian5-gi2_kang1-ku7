from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 看語句單元試驗(TestCase):
    def test_接受無音的詞(self):
        組物件 = 拆文分析器.建立組物件('')
        組物件.內底詞 = [
            拆文分析器.建立詞物件('梅山'),
            拆文分析器.建立詞物件('猴災'),
            拆文分析器.建立詞物件('hiong-kong-sóo'),
            拆文分析器.建立詞物件('tshiann2-lang5'),
        ]
        分詞答案 = '梅山猴災hiong-kong-sóo tshiann2-lang5'
        self.assertEqual(組物件.看語句(), 分詞答案)

    def test_數字(self):
        詞物件 = 拆文分析器.分詞詞物件('0800｜0800')
        self.assertEqual(詞物件.看語句(), '0800')

    def test_漢字數字(self):
        詞物件 = 拆文分析器.分詞詞物件('二-十-六｜lī-tsa̍p-la̍k')
        self.assertEqual(詞物件.看語句(), '二十六')

    def test_空ê(self):
        詞物件 = 拆文分析器.建立詞物件('')
        self.assertEqual(詞物件.看語句(), '')
