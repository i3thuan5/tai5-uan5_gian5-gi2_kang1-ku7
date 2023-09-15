import os
from unittest.case import TestCase
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
from 臺灣言語工具.斷詞.語言模型揀集內組 import 語言模型揀集內組
from 臺灣言語工具.語言模型.KenLM語言模型 import KenLM語言模型
from 臺灣言語工具.辭典.型音辭典 import 型音辭典


class 標全漢全羅整合試驗(TestCase):

    def test_字串辭典斷詞得著音(self):
        閩南語辭典 = 型音辭典(2)
        閩南語辭典.加詞(拆文分析器.對齊詞物件('阿媠', 'a1-sui2'))
        閩南語辭典.加詞(拆文分析器.對齊詞物件('愛 ', 'ai3'))
        閩南語辭典.加詞(拆文分析器.對齊詞物件('我', 'gua2'))
        閩南語辭典.加詞(拆文分析器.對齊詞物件('我', 'ngoo2'))
        閩南語語言模型 = KenLM語言模型(os.path.join(  # '我｜gua2 愛｜ai3 阿-媠｜a1-sui2'
            os.path.dirname(os.path.abspath(__file__)), '語言模型', '我愛阿媠.arpa')
        )

        閩南語語句 = '我愛阿媠'

        句物件 = (
            拆文分析器.建立句物件(閩南語語句)
            .轉音(臺灣閩南語羅馬字拼音)
            .揣詞(拄好長度辭典揣詞, 閩南語辭典)
            .揀(語言模型揀集內組, 閩南語語言模型)
        )
        self.assertEqual(句物件.看音(), 'gua2 ai3 a1-sui2')
        結果 = 句物件.看語句()
        self.assertEqual(拆文分析器.建立句物件(結果).看語句(), '我愛阿媠')
