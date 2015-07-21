# -*- coding: utf-8 -*-
from 臺灣言語工具.音標系統.閩南語.教會系羅馬音標 import 教會系羅馬音標
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音韻母表

臺灣語言音標聲母表 = {'p', 'ph', 'm', 'b', 't', 'th', 'n', 'l',
             'k', 'kh', 'ng', 'g', 'h', 'c', 'ch', 's', 'j', ''}
臺灣語言音標韻母表 = 臺灣閩南語羅馬字拼音韻母表


class 臺灣語言音標(教會系羅馬音標):
    聲母表 = 臺灣語言音標聲母表
    韻母表 = 臺灣語言音標韻母表

    def __init__(self, 音標):
        super(臺灣語言音標, self).__init__()
        self.分析聲韻調(音標)
        # ##
        if self.聲 == 'm' or self.聲 == 'n' or self.聲 == 'ng':
            if self.韻 == 'o':
                self.韻 = 'oo'
                self.做音標()

    def 轉換到臺灣閩南語羅馬字拼音(self):
        if self.音標 is None:
            return None
        聲母 = None
        if self.聲 == 'c':
            聲母 = 'ts'
        elif self.聲 == 'ch':
            聲母 = 'tsh'
        else:
            聲母 = self.聲
        return 聲母 + self.韻 + self.調
