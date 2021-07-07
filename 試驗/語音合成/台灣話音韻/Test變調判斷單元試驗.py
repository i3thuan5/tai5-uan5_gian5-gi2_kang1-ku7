# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.語音合成.閩南語音韻.變調判斷 import 變調判斷
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 規則變調
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 維持本調
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 輕聲
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 無調符號
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 三連音變調
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 隨前變調
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 仔前變調
from 臺灣言語工具.語音合成.閩南語音韻.變調 import 再變調


class 變調判斷單元試驗(TestCase):
    def tearDown(self):
        章物件 = self.產生套用前物件(self.漢字, self.臺羅)
        self.assertEqual(
            變調判斷.判斷(章物件), self.答案,
            (變調判斷.判斷(章物件), self.答案)
        )

    def test_句尾變調(self):
        self.漢字 = '我愛媠媠'
        self.臺羅 = 'gua2 ai3 sui2-sui2'
        self.答案 = [規則變調, 規則變調, 規則變調, 維持本調]

    def test_仝詞攏輕聲(self):
        self.漢字 = '伊是陳先生'
        self.臺羅 = 'i1 si7 tan5--sian1-sinn1'
        self.答案 = [規則變調, 規則變調, 維持本調, 輕聲, 輕聲]

    def test_的前無變調(self):
        self.漢字 = '我上愛媠媠的姑娘'
        self.臺羅 = 'gua2 siong7 ai3 sui2-sui2 e5 koo1-niu5'
        self.答案 = [規則變調, 規則變調, 規則變調, 規則變調, 維持本調, 規則變調, 規則變調, 維持本調]

    def test_的前代名詞變調(self):
        self.漢字 = '我的媠媠'
        self.臺羅 = 'gua2 e5 sui2-sui2'
        self.答案 = [規則變調, 規則變調, 規則變調, 維持本調]

    def test_井前無變調(self):
        self.漢字 = '你講我#愛媠媠'
        self.臺羅 = 'li2 kong2 gua2 # ai3 sui2-sui2'
        self.答案 = [規則變調, 規則變調, 維持本調, '愛提掉的', 規則變調, 規則變調, 維持本調]

    def test_標點符號句尾變調(self):
        self.漢字 = '我愛媠媠。'
        self.臺羅 = 'gua2 ai3 sui2-sui2 .'
        self.答案 = [規則變調, 規則變調, 規則變調, 維持本調, 無調符號]

    def test_三連音前大部份是名詞(self):
        self.漢字 = '這條路直直直'
        self.臺羅 = 'tsit4 tiau5 loo7 tit8-tit8-tit8'
        self.答案 = [規則變調, 規則變調, 維持本調, 三連音變調, 規則變調, 維持本調]

    def test_動詞有三个(self):
        self.漢字 = '來來來！你來！'
        self.臺羅 = 'lai5 lai5 lai5 ！ li2 lai5 !'
        self.答案 = [規則變調, 規則變調, 維持本調, 無調符號, 規則變調, 維持本調, 無調符號]

    def test_代名詞輕聲隨前變調(self):
        self.漢字 = '攏予你'
        self.臺羅 = 'long2 hoo7--li2'
        self.答案 = [規則變調, 維持本調, 隨前變調('7')]

    def test_代名詞句首一般輕聲(self):
        self.漢字 = '你攏予你'
        self.臺羅 = '--li2 long2 hoo7--li2'
        self.答案 = [輕聲, 規則變調, 維持本調, 隨前變調('7')]

    def test_代名詞輕聲佇外語詞後壁(self):
        self.漢字 = 'X你攏按呢'
        self.臺羅 = 'X --li2 long2 an2-ne1'
        self.答案 = [無調符號, 輕聲, 規則變調, 規則變調, 維持本調]

    def test_有仔的一般攏是名詞(self):
        self.漢字 = '豬仔有三隻'
        self.臺羅 = 'ti1-a2 u7 sann1-tsiah8'
        self.答案 = [仔前變調, 維持本調, 規則變調, 規則變調, 維持本調]

    def test_仔囥中央的變調(self):
        self.漢字 = '對今仔日起，咱就是翁仔某矣。'
        self.臺羅 = 'Tuì kin-á-ji̍t khí, lán tō-sī ang-á-bóo--ah.'
        self.答案 = [規則變調, 仔前變調, 規則變調, 維持本調, 維持本調, 無調符號,
                   規則變調, 規則變調, 規則變調, 仔前變調, 規則變調, 維持本調, 輕聲, 無調符號]

    def test_欲的變調(self):
        self.漢字 = '我想欲食飯'
        self.臺羅 = 'gua2 siunn7-beh4 tsiah8-png7 '
        self.答案 = [規則變調, 規則變調, 再變調, 規則變調, 維持本調]

    def 產生套用前物件(self, 漢字, 臺羅):
        return (
            拆文分析器.對齊章物件(漢字, 臺羅)
            .轉音(臺灣閩南語羅馬字拼音)
            .轉音(臺灣閩南語羅馬字拼音, 函式='音值')
        )
