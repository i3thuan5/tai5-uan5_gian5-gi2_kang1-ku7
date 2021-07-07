# -*- coding: utf-8 -*-
from unittest.case import TestCase
from unittest.mock import patch
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.音標系統.閩南語綜合標音 import 閩南語綜合標音
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.基本物件.組 import 組


class 閩南語綜合標音單元試驗(TestCase):

    def setUp(self):
        self.我型, self.我音 = '我', 'gua2'

    def test_一般綜合標音(self):
        self.assertEqual(字('我', 'gua2').綜合標音(閩南語綜合標音), [{
            "漢字": "我",
            "臺羅數字調": "gua2",
            "臺羅閏號調": "guá",
            "通用數字調": "ghua4",
            "吳守禮方音": "ㆣㄨㄚˋ"
        }])

    def test_干焦漢字綜合標音(self):
        self.assertEqual(字('我', 無音).綜合標音(閩南語綜合標音), [{
            "漢字": "我",
            "臺羅數字調": "我",
            "臺羅閏號調": "我",
            "通用數字調": "我",
            "吳守禮方音": "我"
        }])

    def test_干焦臺羅綜合標音(self):
        self.assertEqual(字('gua2', 無音).綜合標音(閩南語綜合標音), [{
            "漢字": "gua2",
            "臺羅數字調": "gua2",
            "臺羅閏號調": "guá",
            "通用數字調": "ghua4",
            "吳守禮方音": "ㆣㄨㄚˋ"
        }])

    def test_標點綜合標音(self):
        self.assertEqual(字('，', 無音).綜合標音(閩南語綜合標音), [{
            "漢字": "，",
            "臺羅數字調": "，",
            "臺羅閏號調": "，",
            "通用數字調": "，",
            "吳守禮方音": "，"
        }])

    def test_對齊標點綜合標音(self):
        self.assertEqual(字('，', ',').綜合標音(閩南語綜合標音), [{
            "漢字": "，",
            "臺羅數字調": ",",
            "臺羅閏號調": ",",
            "通用數字調": ",",
            "吳守禮方音": ","
        }])

    def test_無合法音綜合標音(self):
        self.assertEqual(字('我', 'uo3').綜合標音(閩南語綜合標音), [{
            "漢字": "我",
            "臺羅數字調": "uo3",
            "臺羅閏號調": "uo3",
            "通用數字調": "uo3",
            "吳守禮方音": "uo3"
        }])

    def test_有分詞(self):
        綜合標音 = 拆文分析器.對齊句物件('我', 'uo3').綜合標音(閩南語綜合標音)
        self.assertIn('分詞', 綜合標音[0])

    def test_烏白傳(self):
        self.assertRaises(型態錯誤, 閩南語綜合標音, '我')
        self.assertRaises(型態錯誤, 閩南語綜合標音, '我', False)
        self.assertRaises(型態錯誤, 閩南語綜合標音, '我', True)

    def test_一句無連字綜合標音(self):
        句物件 = 拆文分析器.對齊句物件('點仔膠，黏著跤，', 'tiam2 a2 ka1, liam5 tioh8 kha1,')
        頭一句, = 句物件.綜合標音(閩南語綜合標音)
        self.assertIn('漢字', 頭一句)
        self.assertIn('臺羅數字調', 頭一句)
        self.assertIn('臺羅閏號調', 頭一句)
        self.assertIn('通用數字調', 頭一句)
        self.assertIn('吳守禮方音', 頭一句)
        self.assertIn('分詞', 頭一句)

    def test_一句連字綜合標音(self):
        句物件 = 拆文分析器.對齊句物件('點仔膠，黏著跤，', 'tiam2-a2-ka1, liam5-tioh8-kha1,')
        頭一句, = 句物件.綜合標音(閩南語綜合標音)
        self.assertIn('漢字', 頭一句)
        self.assertIn('臺羅數字調', 頭一句)
        self.assertIn('臺羅閏號調', 頭一句)
        self.assertIn('通用數字調', 頭一句)
        self.assertIn('吳守禮方音', 頭一句)
        self.assertIn('分詞', 頭一句)

    def test_混合連詞綜合標音(self):
        句物件 = 拆文分析器.對齊句物件('點仔膠，黏著跤，', 'tiam2-a2-ka1, liam5-tioh8 kha1,')
        頭一句, = 句物件.綜合標音(閩南語綜合標音)
        self.assertIn('漢字', 頭一句)
        self.assertIn('臺羅數字調', 頭一句)
        self.assertIn('臺羅閏號調', 頭一句)
        self.assertIn('通用數字調', 頭一句)
        self.assertIn('吳守禮方音', 頭一句)
        self.assertIn('分詞', 頭一句)

    @patch('臺灣言語工具.基本物件.集.集.綜合標音')
    def test_綜合標音用集的來鬥(self, 集綜合標音mock):
        句物件 = 句([
            拆文分析器.對齊集物件('點仔膠', 'tiam2-a2-ka1'),
            拆文分析器.對齊集物件('，', ','),
            拆文分析器.對齊集物件('黏著', 'liam5-tioh8'),
            拆文分析器.對齊集物件('跤', 'kha1'),
            拆文分析器.對齊集物件('，', ','),
        ])
        句物件.綜合標音(閩南語綜合標音)
        self.assertEqual(集綜合標音mock.call_count, 5)

    def test_綜合標音集內底組濟個嘛袂例外(self):
        # 因為攏用佇輸出，愛檢查就佇程式別位檢查
        我 = 拆文分析器.對齊集物件('我', 'gua2')
        愛 = 拆文分析器.對齊集物件('愛', 'ai3')
        媠某 = 拆文分析器.對齊組物件('美女', 'sui2-boo2')
        美女 = 拆文分析器.對齊組物件('美女', 'mi2-lu2')
        莉 = 集([媠某, 美女])
        句物件 = 句([我, 愛, 莉])

        句物件.綜合標音(閩南語綜合標音)

    def test_空句綜合標音袂例外(self):
        # 因為攏用佇輸出，愛檢查就佇程式別位檢查
        self.assertEqual(句().綜合標音(閩南語綜合標音), [
            {}
        ])

    def test_綜合標音章物件(self):
        章物件 = 拆文分析器.對齊章物件('點仔膠，黏著跤，', 'tiam2-a2-ka1, liam5-tioh8 kha1,')
        頭一句, 上尾句 = 章物件.綜合標音(閩南語綜合標音)
        self.assertIn('漢字', 頭一句)
        self.assertIn('臺羅數字調', 頭一句)
        self.assertIn('臺羅閏號調', 頭一句)
        self.assertIn('通用數字調', 頭一句)
        self.assertIn('吳守禮方音', 頭一句)
        self.assertIn('分詞', 頭一句)
        self.assertIn('漢字', 上尾句)
        self.assertIn('臺羅數字調', 上尾句)
        self.assertIn('臺羅閏號調', 上尾句)
        self.assertIn('通用數字調', 上尾句)
        self.assertIn('吳守禮方音', 上尾句)
        self.assertIn('分詞', 上尾句)

    @patch('臺灣言語工具.基本物件.句.句.綜合標音')
    def test_綜合標音用句的來鬥(self, 句綜合標音mock):
        章物件 = 拆文分析器.對齊章物件('點仔膠，黏著跤，', 'tiam2-a2-ka1, liam5-tioh8 kha1,')
        self.assertEqual(章物件.綜合標音(閩南語綜合標音), [
            句綜合標音mock.return_value[0],
            句綜合標音mock.return_value[0],
        ])

    def test_一組綜合標音json格式(self):
        組物件 = 拆文分析器.對齊組物件('椅仔', 'i2-a2')
        頭一个詞, = 組物件.綜合標音(閩南語綜合標音)
        self.assertIn('漢字', 頭一个詞)
        self.assertIn('臺羅數字調', 頭一个詞)
        self.assertIn('臺羅閏號調', 頭一个詞)
        self.assertIn('通用數字調', 頭一个詞)
        self.assertIn('吳守禮方音', 頭一个詞)
        self.assertIn('分詞', 頭一个詞)

    def test_一組兩詞綜合標音json格式(self):
        組物件 = 拆文分析器.對齊組物件('椅仔', 'i2 a2')
        頭一个詞, = 組物件.綜合標音(閩南語綜合標音)
        self.assertIn('漢字', 頭一个詞)
        self.assertIn('臺羅數字調', 頭一个詞)
        self.assertIn('臺羅閏號調', 頭一个詞)
        self.assertIn('通用數字調', 頭一个詞)
        self.assertIn('吳守禮方音', 頭一个詞)
        self.assertIn('分詞', 頭一个詞)

    def test_空組綜合標音莫例外(self):
        # 因為攏用佇輸出，愛檢查空愛佇程式別位檢查
        組物件 = 組()
        self.assertEqual(組物件.綜合標音(閩南語綜合標音), [
            {}
        ])

    def test_綜合標音(self):
        字物件 = 拆文分析器.對齊字物件('意', 'i2')
        self.assertEqual(字物件.綜合標音(閩南語綜合標音), [{
            "漢字": "意", "臺羅數字調": "i2", "臺羅閏號調": "í",
            "通用數字調": "i4", "吳守禮方音": "ㄧˋ"
        }])

    def test_綜合標音json格式(self):
        詞物件 = 拆文分析器.對齊詞物件('椅仔', 'i2-a2')
        頭一个詞, = 詞物件.綜合標音(閩南語綜合標音)
        self.assertIn('漢字', 頭一个詞)
        self.assertIn('臺羅數字調', 頭一个詞)
        self.assertIn('臺羅閏號調', 頭一个詞)
        self.assertIn('通用數字調', 頭一个詞)
        self.assertIn('吳守禮方音', 頭一个詞)
        self.assertIn('分詞', 頭一个詞)

    def test_綜合標音空詞莫例外(self):
        # 因為攏用佇輸出，愛檢查空愛佇程式別位檢查
        詞物件 = 拆文分析器.建立詞物件('')
        self.assertEqual(詞物件.綜合標音(閩南語綜合標音), [
            {}
        ])

    @patch('臺灣言語工具.基本物件.組.組.綜合標音')
    def test_綜合標音用組的結果(self, 組綜合標音mock):
        集物件 = 拆文分析器.對齊集物件('美女', 'mi2-lu2')
        self.assertEqual(集物件.綜合標音(閩南語綜合標音), 組綜合標音mock.return_value)

    def test_綜合標音愛用頭一組(self):
        # 因為攏用佇輸出，愛檢查就佇程式別位檢查
        媠某 = 拆文分析器.對齊組物件('美女', 'sui2-boo2')
        美女 = 拆文分析器.對齊組物件('美女', 'mi2-lu2')
        self.assertEqual(
            集([媠某, 美女]).綜合標音(閩南語綜合標音),
            集([媠某]).綜合標音(閩南語綜合標音)
        )

    def test_空集綜合標音莫例外(self):
        # 因為攏用佇輸出，愛檢查空愛佇程式別位檢查
        集物件 = 集()
        self.assertEqual(集物件.綜合標音(閩南語綜合標音), [
            {}
        ])
