# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 物件轉字串整合試驗(TestCase):
    # 原本字串生按怎就照伊原本--的顯示

    def tearDown(self):
        物件 = 拆文分析器.建立句物件(self.語句)
        結果 = getattr(self, '結果', self.語句)
        self.assertEqual(物件.看語句(), 結果)

    def test_全羅(self):
        self.語句 = 'Lia̍h suí-ti'

    def test_全羅句頭輕聲詞(self):
        self.語句 = 'Ah'

    def test_全羅句頭輕聲(self):
        self.語句 = '--Ah'

    def test_全羅句頭無大寫輕聲(self):
        self.語句 = '--ah'

    def test_全羅濟字輕聲(self):
        self.語句 = 'Kín--tshut-lâi'

    def test_全羅輕聲後壁接詞(self):
        self.語句 = 'Kín--tshut-lâi lia̍h'

    def test_全羅輕聲前有空白(self):
        self.語句 = 'Kín --tshut-lâi'

    def test_全羅連續輕聲(self):
        self.語句 = 'Kín --tshut-lâi --lah'

    def test_全羅粗坯的輕聲(self):
        self.語句 = 'Kin2-0tshut-lai5-0ah'

    def test_全漢làng格(self):
        self.語句 = '欲 掠豬'
        self.結果 = '欲掠豬'

    def test_全漢無空白(self):
        self.語句 = '欲掠豬'

    def test_全漢輕聲(self):
        self.語句 = '--啊'

    def test_全漢濟字輕聲(self):
        self.語句 = '緊--出-來'

    def test_全漢連續輕聲(self):
        self.語句 = '緊--出-來--啦'

    def test_漢字濟字輕聲混合201802p13(self):
        self.語句 = '想--起-來就ē驚'

    def test_漢字濟字輕聲混合201802p13無空白(self):
        self.語句 = '想--起-來就 ē 驚'
        self.結果 = '想--起-來就ē驚'

    def test_bongpo_201804p25(self):
        self.語句 = '調--來ê兵仔'

    def test_bongpo_201804p25無空白(self):
        self.語句 = '調--來 ê 兵仔'
        self.結果 = '調--來ê兵仔'

    def test_漢羅(self):
        self.語句 = '欲 lia̍h-ti'
        self.結果 = '欲lia̍h-ti'

    def test_漢羅無空白(self):
        self.語句 = '欲lia̍h-ti'

    def test_漢羅連字符(self):
        self.語句 = '欲-lia̍h-ti'
        self.結果 = '欲lia̍h-ti'

    def test_漢羅無空白無連字符(self):
        self.語句 = '欲lia̍h豬'

    def test_半形標點符號(self):
        self.語句 = 'ti!'

    def test_全形標點符號(self):
        self.語句 = 'ti！'

    def test_漢字接標點符號(self):
        self.語句 = '好！'

    def test_空ê(self):
        self.語句 = ''

    def test_電話(self):
        self.語句 = 'Khà 1-pái 0912-345-678'

    def test_數字(self):
        self.語句 = 'Ké-siáu 10,000.0'

    def test_減號(self):
        self.語句 = 'Kín - 好~'
