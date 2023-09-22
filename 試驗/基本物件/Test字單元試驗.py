from unittest.case import TestCase
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.基本物件.公用變數 import 無音


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

    def test_合成的tuple(self):
        型 = '媠'
        音 = ('s', 'ui', '2')
        字物件 = 字(型, 音)
        self.assertEqual(字物件.型, 型)
        self.assertEqual(字物件.音, 音)

    def test_看字(self):
        型 = '我'
        音 = 'gua2'
        字物件 = 字(型, 音)
        self.assertEqual(字物件.看語句(), 型)
        self.assertEqual(字物件.看音(), 音)
        self.assertEqual(字物件.看分詞(), 型 + '｜' + 音)

    def test_看字無音(self):
        字物件 = 字('媠')
        self.assertEqual(字物件.看語句(), '媠')
        self.assertEqual(字物件.看音(), '')
        self.assertEqual(字物件.看分詞(), '媠')

    def test_漢語語音合成字(self):
        字('媠', ('s', 'ui', '2'))

    def test_南島語語音合成字(self):
        字("Nga'ay", [['ŋ', 'a'], ['ʡ', 'a', 'j']])

    def test_語音合成無音(self):
        字('，', (None,))

    def test_本調口語調辭典_用tuple分開(self):
        字(('？', '?'), '?')
