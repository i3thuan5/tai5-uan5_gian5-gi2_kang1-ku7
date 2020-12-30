# -*- coding: utf-8 -*-
from unittest.case import TestCase
from unittest.mock import patch
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.羅馬字.台語.多元書寫 import 台語多元書寫
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


class 多元書寫單元試驗(TestCase):

    def test_檢查分詞(self):
        多元書寫 = self.物件拍無去矣()
        self.assertEqual(
            多元書寫['分詞'],
            '--啊｜--ah ！｜! kue-á-鬚｜kue-á-tshiu 拍-無--去｜phah-bô--khì --矣｜--ah 。｜.'
        )

    def test_檢查漢字(self):
        多元書寫 = self.物件拍無去矣()
        self.assertEqual(多元書寫['漢字'], '啊！Kue-á鬚拍無--去--矣。')

    def test_檢查漢字斷詞(self):
        多元書寫 = self.物件拍無去矣()
        self.assertEqual(多元書寫['漢字斷詞'], '--啊 ！ kue-á鬚 拍無--去 --矣 。')

    def test_檢查臺羅(self):
        多元書寫 = self.物件拍無去矣()
        self.assertEqual(多元書寫['臺羅'], 'Ah! Kue-á-tshiu phah-bô--khì--ah.')

    def test_檢查白話字(self):
        多元書寫 = self.物件拍無去矣()
        self.assertEqual(
            多元書寫['白話字'],  'Ah! Koe-á-chhiu phah-bô--khì--ah.'
        )

    def test_臺羅照詞分開(self):
        多元書寫 = self.物件拍無去矣()
        self.assertEqual(
            多元書寫['臺羅斷詞'], '--ah ! kue-á-tshiu phah-bô--khì --ah .')

    def test_臺羅保持原本大寫(self):
        多元書寫 = 台語多元書寫.書寫句(拆文分析器.對齊句物件('豬',  'Ti'))
        self.assertEqual(多元書寫['臺羅斷詞'],  'Ti')

    def test_臺羅閏號調愛提掉(self):
        多元書寫 = self.物件拍無去矣()
        self.assertNotIn('臺羅閏號調', 多元書寫)

    def test_檢查臺羅數字調(self):
        多元書寫 = self.物件拍無去矣()
        self.assertEqual(
            多元書寫['臺羅數字調'], '--ah4 ! kue1-a2-tshiu1 phah4-bo5--khi3 --ah4 .'
        )

    def test_檢查吳守禮方音(self):
        多元書寫 = self.物件拍無去矣()
        self.assertEqual(
            多元書寫['吳守禮方音'], '˙ㄚㆷ ! ㄍㄨㆤ ㄚˋ ㄑㄧㄨ ㄆㄚㆷ ㆠㄜˊ ˙ㄎㄧ ˙ㄚㆷ .'
        )

    def test_干焦漢字多元書寫(self):
        多元書寫 = 台語多元書寫.書寫句(拆文分析器.建立句物件('我'))
        self.assertEqual(多元書寫['臺羅'], '我')

    def test_干焦臺羅多元書寫(self):
        多元書寫 = 台語多元書寫.書寫句(拆文分析器.建立句物件('gua2'))
        self.assertEqual(多元書寫['漢字'], 'Guá')

    def test_無合法音就照伊彼音(self):
        多元書寫 = 台語多元書寫.書寫句(拆文分析器.對齊句物件('豬',  'Pigu'))
        self.assertEqual(多元書寫['臺羅'],  'Pigu')

    def test_多元書寫集內底組濟个就例外_因為程式有問題(self):
        我 = 拆文分析器.對齊集物件('我', 'gua2')
        愛 = 拆文分析器.對齊集物件('愛', 'ai3')
        媠某 = 拆文分析器.對齊組物件('美女', 'sui2-boo2')
        美女 = 拆文分析器.對齊組物件('美女', 'mi2-lu2')
        莉 = 集([媠某, 美女])
        句物件 = 句([我, 愛, 莉])
        with self.assertRaises(解析錯誤):
            台語多元書寫.書寫句(句物件)

    def test_空句多元書寫袂例外(self):
        # 因為攏用佇輸出，愛檢查就佇程式別位檢查
        多元書寫 = 台語多元書寫.書寫句(句())
        self.assertIn('漢字', 多元書寫)
        self.assertIn('臺羅數字調', 多元書寫)
        self.assertIn('吳守禮方音', 多元書寫)
        self.assertIn('白話字', 多元書寫)
        self.assertIn('分詞', 多元書寫)

    @patch('臺灣言語工具.音標系統.台語.多元書寫.台語多元書寫.書寫句')
    def test_多元書寫用句的來鬥(self, 句多元書寫mock):
        章物件 = 拆文分析器.對齊章物件('點仔膠，黏著跤，', 'tiam2-a2-ka1, liam5-tioh8 kha1,')
        self.assertEqual(台語多元書寫.書寫章(章物件), [
            句多元書寫mock.return_value,
            句多元書寫mock.return_value,
        ])

    def test_白話字方言就莫轉換(self):
        多元書寫 = self.方言音()
        self.assertEqual(
            多元書寫['白話字'],  'Khòaⁿ chir'
        )

    def test_白話字外來詞就莫振動(self):
        多元書寫 = self.外來詞()
        self.assertEqual(
            多元書寫['白話字'],  'Pigu!'
        )

    def test_空章多元書寫袂例外(self):
        # 因為攏用佇輸出，愛檢查就佇程式別位檢查
        self.assertEqual(台語多元書寫.書寫章(拆文分析器.建立章物件('')), [])

    def 物件拍無去矣(self):
        句物件 = 拆文分析器.對齊句物件(
            '啊！kue1-a2鬚拍無去矣。', '--ah4 ! kue-a2-tshiu phah4-bo5--khi3 --ah.'
        )
        return 台語多元書寫.書寫句(句物件)

    def 方言音(self):
        句物件 = 拆文分析器.對齊句物件('讀書', 'Khuann3 tsir1')
        return 台語多元書寫.書寫句(句物件)

    def 外來詞(self):
        句物件 = 拆文分析器.建立句物件('Pigu!')
        return 台語多元書寫.書寫句(句物件)
