from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.語音辨識.漢語轉辨識標仔 import 漢語轉辨識標仔
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 漢語轉辨識標仔單元試驗(TestCase):

    def test_一句(self):
        分詞 = '予｜hoo7 人｜lang5 真-感-心｜tsin1-kam2-sim1'
        句物件 = 拆文分析器.分詞句物件(分詞)
        標仔 = 漢語轉辨識標仔.物件轉音節標仔(句物件, 臺灣閩南語羅馬字拼音)
        self.assertEqual(
            標仔,
            [
                'sil',
                'hoo',
                'lang',
                'tsin',
                'kam',
                'sim',
                'sil',
            ]
        )

    def test_濟句(self):
        分詞 = '有｜u7 你｜li2 ，｜, 予｜hoo7 人｜lang5 真-感-心｜tsin1-kam2-sim1'
        章物件 = 拆文分析器.分詞章物件(分詞)
        標仔 = 漢語轉辨識標仔.物件轉音節標仔(章物件, 臺灣閩南語羅馬字拼音)
        self.assertEqual(
            標仔,
            [
                'sil',
                'u',
                'li',
                'sil',
                'hoo',
                'lang',
                'tsin',
                'kam',
                'sim',
                'sil',
            ]
        )

    def test_句中央有無合法的拼音(self):
        分詞 = '予｜hoo7 人｜X 真-感-心｜tsin1-kam2-sim1'
        句物件 = 拆文分析器.分詞句物件(分詞)
        標仔 = 漢語轉辨識標仔.物件轉音節標仔(句物件, 臺灣閩南語羅馬字拼音)
        self.assertEqual(
            標仔,
            [
                'sil',
                'hoo',
                'sil',
                'tsin',
                'kam',
                'sim',
                'sil',
            ]
        )

    def test_袂有連續的恬音(self):
        分詞 = '予｜X 人｜X 真-感-心｜tsin1-kam2-X'
        句物件 = 拆文分析器.分詞句物件(分詞)
        標仔 = 漢語轉辨識標仔.物件轉音節標仔(句物件, 臺灣閩南語羅馬字拼音)
        self.assertEqual(
            標仔,
            [
                'sil',
                'tsin',
                'kam',
                'sil',
            ]
        )
    def test_輕聲佮外來語(self):
        分詞 = '騎｜khia5 1oo7-1too1-1bai2｜1oo7-1too1-1bai2 出-去｜tshut8-khi3 矣｜ah0'
        句物件 = 拆文分析器.分詞句物件(分詞)
        標仔 = 漢語轉辨識標仔.物件轉音節標仔(句物件, 臺灣閩南語羅馬字拼音)
        self.assertEqual(
            標仔,
            [
                'sil',
                'khia',
                'oo',
                'too',
                'bai',
                'tshut',
                'khi',
                'ah',
                'sil',
            ]
        )
