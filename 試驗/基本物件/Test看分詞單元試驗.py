from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 看分詞單元試驗(TestCase):

    def test_漢羅對照(self):
        書寫1 = '豬仔媠'
        書寫2 = 'ti-á suí'
        self.assertEqual(
            拆文分析器.建立句物件(書寫1, 書寫2).看分詞(),
            '豬-仔｜ti-á 媠｜suí'
        )

    def test_漢羅OK(self):
        書寫1 = '豬á媠'
        書寫2 = 'ti-á suí'
        self.assertEqual(
            拆文分析器.建立句物件(書寫1, 書寫2).看分詞(),
            '豬-á｜ti-á 媠｜suí'
        )

    def test_詞頭輕聲(self):
        書寫1 = '媠--啦'
        書寫2 = 'suí --lah'
        self.assertEqual(
            拆文分析器.建立句物件(書寫1, 書寫2).看分詞(),
            '媠｜suí --啦｜--lah'
        )

    def test_詞中輕聲(self):
        書寫1 = '媠--ê'
        書寫2 = 'suí--ê'
        self.assertEqual(
            拆文分析器.建立句物件(書寫1, 書寫2).看分詞(),
            '媠--ê｜suí--ê'
        )

    def test_一種書寫(self):
        書寫 = 'ti-á suí'
        self.assertEqual(
            拆文分析器.建立句物件(書寫).看分詞(),
            'ti-á suí'
        )

    def test_一種書寫ê輕聲(self):
        書寫 = 'ti-á suí --lah'
        self.assertEqual(
            拆文分析器.建立句物件(書寫).看分詞(),
            'ti-á suí --lah'
        )

    def test_字物件嘛輕聲(self):
        書寫 = '--lah'
        self.assertEqual(
            拆文分析器.建立字物件(書寫).看分詞(),
            '--lah'
        )
