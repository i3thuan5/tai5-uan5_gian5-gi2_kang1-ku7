from unittest.case import TestCase
from unittest.mock import patch
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.音標系統.閩南語綜合標音 import 閩南語綜合標音


class 句單元試驗(TestCase):

    def test_句烏白傳(self):
        self.assertRaises(型態錯誤, 句, None)
        self.assertRaises(型態錯誤, 句, [None])
        self.assertRaises(型態錯誤, 句, ['sui2'])

    def test_看句(self):
        型 = '恁老母ti3佗位'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7'
        句物件 = 拆文分析器.對齊句物件(型, 音)
        self.assertEqual(句物件.看型(), 型)
        self.assertEqual(句物件.看音(), 音)
        分詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7'
        self.assertEqual(句物件.看分詞(), 分詞)

    def test_一句無連字綜合標音(self):
        句物件 = 拆文分析器.對齊句物件('點仔膠，黏著跤，', 'tiam2 a2 ka1, liam5 tioh8 kha1,')
        頭一句,  = 句物件.綜合標音(閩南語綜合標音)
        self.assertIn('漢字', 頭一句)
        self.assertIn('臺羅數字調', 頭一句)
        self.assertIn('臺羅閏號調', 頭一句)
        self.assertIn('通用數字調', 頭一句)
        self.assertIn('吳守禮方音', 頭一句)
        self.assertIn('分詞', 頭一句)

    def test_一句連字綜合標音(self):
        句物件 = 拆文分析器.對齊句物件('點仔膠，黏著跤，', 'tiam2-a2-ka1, liam5-tioh8-kha1,')
        頭一句,  = 句物件.綜合標音(閩南語綜合標音)
        self.assertIn('漢字', 頭一句)
        self.assertIn('臺羅數字調', 頭一句)
        self.assertIn('臺羅閏號調', 頭一句)
        self.assertIn('通用數字調', 頭一句)
        self.assertIn('吳守禮方音', 頭一句)
        self.assertIn('分詞', 頭一句)

    def test_混合連詞綜合標音(self):
        句物件 = 拆文分析器.對齊句物件('點仔膠，黏著跤，', 'tiam2-a2-ka1, liam5-tioh8 kha1,')
        頭一句,  = 句物件.綜合標音(閩南語綜合標音)
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
