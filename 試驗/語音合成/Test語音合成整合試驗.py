from os import remove
from os.path import join, dirname, abspath
from unittest.case import TestCase
from urllib.request import urlopen


from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.語音合成.漢語語音標仔轉換 import 漢語語音標仔轉換
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
from 臺灣言語工具.斷詞.語言模型揀集內組 import 語言模型揀集內組
from 臺灣言語工具.語言模型.KenLM語言模型 import KenLM語言模型
from 臺灣言語工具.辭典.型音辭典 import 型音辭典
from 臺灣言語工具.語音合成.HTS工具.HTS合成模型 import HTS合成模型
from 臺灣言語工具.語音合成.閩南語音韻規則 import 閩南語音韻規則


class 語音合成整合試驗(TestCase):
    模型網址 = 'https://i3thuan5.github.io/hts_engine_python/example/Taiwanese.htsvoice'
    閩南語模型 = 'Taiwanese.htsvoice'

    @classmethod
    def setUpClass(cls):
        with urlopen(cls.模型網址) as 模型資料:
            with open(cls.閩南語模型, 'wb') as 模型檔案:
                模型檔案.write(模型資料.read())

    @classmethod
    def tearDownClass(cls):
        remove(cls.閩南語模型)

    def test_閩南語字串轉聲音檔(self):
        合成模型 = HTS合成模型(self.閩南語模型)
        閩南語語句 = 'gua2 ai3 a1-sui2'

        章物件 = 拆文分析器.建立章物件(閩南語語句)
        標準章物件 = 章物件.轉音(臺灣閩南語羅馬字拼音)
        音值物件 = 標準章物件.轉音(臺灣閩南語羅馬字拼音, 函式='音值')
        變調物件 = 閩南語音韻規則.套用(音值物件)
        標仔陣列 = 漢語語音標仔轉換.物件轉完整合成標仔(變調物件)
        愛合成標仔 = 漢語語音標仔轉換.跳脫標仔陣列(標仔陣列)
        音檔 = 合成模型.合成(愛合成標仔)
        self.assertIsInstance(音檔.wav格式資料(), bytes)

    def test_閩南語字串斷詞後轉聲音檔(self):
        閩南語辭典 = 型音辭典(2)
        閩南語辭典.加詞(拆文分析器.對齊詞物件('阿媠', 'a1-sui2'))
        閩南語辭典.加詞(拆文分析器.對齊詞物件('愛 ', 'ai3'))
        閩南語辭典.加詞(拆文分析器.對齊詞物件('我', 'gua2'))
        閩南語辭典.加詞(拆文分析器.對齊詞物件('我', 'ngoo2'))
        閩南語語言模型 = KenLM語言模型(join(  # '我｜gua2 愛｜ai3 阿-媠｜a1-sui2'
            dirname(abspath(__file__)), '語言模型', '我愛阿媠.arpa')
        )
        合成模型 = HTS合成模型(self.閩南語模型)

        閩南語語句 = '我愛阿媠'

        章物件 = (
            拆文分析器.建立章物件(閩南語語句)
            .轉音(臺灣閩南語羅馬字拼音)
            .揣詞(拄好長度辭典揣詞, 閩南語辭典)
            .揀(語言模型揀集內組, 閩南語語言模型)
            .轉音(臺灣閩南語羅馬字拼音, 函式='音值')
            .做(閩南語音韻規則, '套用')
        )
        標仔陣列 = 漢語語音標仔轉換.物件轉完整合成標仔(章物件)
        愛合成標仔 = 漢語語音標仔轉換.跳脫標仔陣列(標仔陣列)
        音檔 = 合成模型.合成(愛合成標仔)
        self.assertIsInstance(音檔.wav格式資料(), bytes)
