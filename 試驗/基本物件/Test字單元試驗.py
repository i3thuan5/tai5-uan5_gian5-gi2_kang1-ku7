from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤


class 字單元試驗(TestCase):

    def test_字(self):
        型 = '媠'
        音 = 'ㄙㄨㄧˋ'
        字物件 = 字(型, 音)
        self.assertEqual(字物件.型, 型)
        self.assertEqual(字物件.音, 音)

    def test_字無音(self):
        型 = '媠'
        字物件 = 字(型)
        self.assertEqual(字物件.型, 型)
        self.assertEqual(字物件.音, 無音)

    def test_字烏白傳(self):
        型 = '媠'
        音 = 'ㄙㄨㄧˋ'
        self.assertRaises(型態錯誤, 字, 4)
        self.assertRaises(型態錯誤, 字, (音,))
        self.assertRaises(型態錯誤, 字, 型, None)
        self.assertRaises(型態錯誤, 字, 型, 20)

    def test_看字(self):
        型 = '我'
        音 = 'gua2'
        字物件 = 拆文分析器.對齊字物件(型, 音)
        self.assertEqual(字物件.看型(), 型)
        self.assertEqual(字物件.看音(), 音)
        分詞 = 型 + '｜' + 音
        self.assertEqual(字物件.看分詞(), 分詞)

    def test_無音字(self):
        字物件 = 拆文分析器.建立字物件('媠')
        self.assertEqual(字物件.看型(), '媠')
        self.assertEqual(字物件.看音(), '')
        self.assertEqual(字物件.看分詞(), '媠')
