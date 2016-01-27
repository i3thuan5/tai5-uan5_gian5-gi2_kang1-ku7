from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 字單元試驗(TestCase):

    def test_看字(self):
        型 = '我'
        音 = 'gua2'
        字物件 = 拆文分析器.產生對齊字(型, 音)
        self.assertEqual(字物件.看型(), 型)
        self.assertEqual(字物件.看音(), 音)
        分詞 = 型 + '｜' + 音
        self.assertEqual(字物件.看分詞(), 分詞)

    def test_無音字(self):
        字物件 = 拆文分析器.建立字物件('媠')
        self.assertEqual(字物件.看型(), '媠')
        self.assertEqual(字物件.看音(), '')
        self.assertEqual(字物件.看分詞(), '媠')