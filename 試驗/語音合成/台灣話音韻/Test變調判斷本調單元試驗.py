# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.語音合成.閩南語音韻.變調判斷 import 變調判斷
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 維持本調


class 變調判斷本調單元試驗(TestCase):
    愛檢查的 = [
        ('句尾變調', '我愛媠媠 #', 'gua2 ai3 sui2-sui2 #'),
    ]

    def test_檢查本調(self):
        for 名, 漢字, 臺羅 in self.愛檢查的:
            輸入物件 = self.產生套用前物件(漢字.replace('#', ''), 臺羅.replace('#', ''))
            結果 = 變調判斷.判斷(輸入物件)
            答案字陣列 = self.產生套用前物件(漢字, 臺羅).篩出字物件()

            這馬答案 = len(答案字陣列) - 1
            這馬結果 = len(結果) - 1
            while 這馬答案 >= 0:
                if 變調判斷.是井號無(答案字陣列[這馬答案]):
                    self.assertEqual(結果[這馬結果], 維持本調, 名)
                    這馬答案 -= 2
                else:
                    self.assertNotEqual(結果[這馬結果], 維持本調, 名)
                    這馬答案 -= 1
                這馬結果 -= 1
            self.assertLess(這馬結果, 0, 名)

    def 產生套用前物件(self, 漢字, 臺羅):
        return (
            拆文分析器.對齊章物件(漢字, 臺羅)
            .轉音(臺灣閩南語羅馬字拼音)
            .轉音(臺灣閩南語羅馬字拼音, 函式='音值')
        )
