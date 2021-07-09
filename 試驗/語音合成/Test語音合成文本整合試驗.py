from unittest.case import TestCase


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.Pangcah.原住民族語言書寫系統秀姑巒阿美語 import 原住民族語言書寫系統秀姑巒阿美語
from 臺灣言語工具.語音合成.南島語語音標仔轉換 import 南島語語音標仔轉換


class 語音合成文本整合試驗(TestCase):

    def test_阿美文字處理(self):
        語句 = "Nga'ay ho?"

        章物件 = 拆文分析器.建立章物件(語句)
        for 字物件 in 章物件.篩出字物件():
            字物件.音 = 字物件.型
        音值物件 = 章物件.轉音(原住民族語言書寫系統秀姑巒阿美語, 函式='音值')
        標仔陣列 = 南島語語音標仔轉換.物件轉完整合成標仔(音值物件)
        愛合成標仔 = 南島語語音標仔轉換.跳脫標仔陣列(標仔陣列)
        self.assertGreaterEqual(len(愛合成標仔), 10)
