from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.公用變數 import 分字符號
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤


class 詞單元試驗(TestCase):

    def test_詞(self):
        型 = '媠'
        音 = 'ㄙㄨㄧˋ'
        字物件 = 字(型, 音)
        字陣列 = [字物件, 字物件]
        詞物件 = 詞(字陣列)
        另外字陣列 = [字(型, 音), 字(型, 音)]
        self.assertEqual(詞物件.內底字, 另外字陣列)

    def test_看詞(self):
        型 = '姑-娘'
        音 = 'koo1-niu5'
        詞物件 = 拆文分析器.對齊詞物件(型, 音)
        無分字型 = 型.replace(分字符號, '')
        self.assertEqual(詞物件.看語句(), 無分字型)
        self.assertEqual(詞物件.看音(), 音)
        分詞 = 型 + '｜' + 音
        self.assertEqual(詞物件.看分詞(), 分詞)

    def test_詞烏白傳(self):
        self.assertRaises(型態錯誤, 詞, None)
        self.assertRaises(型態錯誤, 詞, [None])
        self.assertRaises(型態錯誤, 詞, ['sui2'])

    def test_兩字詞有字無音(self):
        梅詞物件 = 拆文分析器.建立詞物件('')
        梅詞物件.內底字 = [
            拆文分析器.對齊字物件('梅', 'mui5'),
            拆文分析器.建立字物件('山'),
        ]
        梅分詞答案 = '梅-山｜mui5-'
        self.assertEqual(梅詞物件.看分詞(), 梅分詞答案)
        山詞物件 = 拆文分析器.建立詞物件('')
        山詞物件.內底字 = [
            拆文分析器.建立字物件('梅'),
            拆文分析器.對齊字物件('山', 'san1'),
        ]
        山分詞答案 = '梅-山｜-san1'
        self.assertEqual(山詞物件.看分詞(), 山分詞答案)

    def test_三字詞有字無音(self):
        公詞物件 = 拆文分析器.建立詞物件('')
        公詞物件.內底字 = [
            拆文分析器.建立字物件('鄉'),
            拆文分析器.對齊字物件('公', 'kong1'),
            拆文分析器.建立字物件('所'),
        ]
        公分詞答案 = '鄉-公-所｜-kong1-'
        self.assertEqual(公詞物件.看分詞(), 公分詞答案)

        鄉所詞物件 = 拆文分析器.建立詞物件('')
        鄉所詞物件.內底字 = [
            拆文分析器.對齊字物件('鄉', 'hiang1'),
            拆文分析器.建立字物件('公'),
            拆文分析器.對齊字物件('所', 'soo2'),
        ]
        鄉所分詞答案 = '鄉-公-所｜hiang1--soo2'
        self.assertEqual(鄉所詞物件.看分詞(), 鄉所分詞答案)

    def test_輕聲詞(self):
        詞物件 = 詞([
            字('喔', 'ooh', 輕聲標記=True),
        ])
        self.assertTrue(
            詞物件.篩出字物件()[0].敢有輕聲標記()
        )
