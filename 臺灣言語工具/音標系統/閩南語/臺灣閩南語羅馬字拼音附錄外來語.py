# -*- coding: utf-8 -*-
import re
from 臺灣言語工具.音標系統.閩南語.教會系羅馬音標 import 教會系羅馬音標
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音聲母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音韻母表


實際調值對應調號 = {
    '11': '3',
    '33': '7',
    '55': '1',
    '51': '2',
    '13': '5',
    '35': '9',
}
入聲調實際調值對應調號 = {
    '1': '10',
    '3': '4',
    '5': '8',
}


class 臺灣閩南語羅馬字拼音附錄外來語(教會系羅馬音標):
    聲母表 = 臺灣閩南語羅馬字拼音聲母表
    韻母表 = 臺灣閩南語羅馬字拼音韻母表
    調值分開 = re.compile(r'([a-z]+)([1-5]{1,2})\Z')

    def __init__(self, 音標):
        super().__init__()
        self.分析聲韻調(音標)
        self.原本音標 = 音標

    def 轉換到臺灣閩南語羅馬字拼音(self):
        return self.音標

    def 分析聲韻調(self, 音標):
        if self.分析聲韻調傳結果(音標):
            self.音標 = ''.join(['1', self.聲, self.韻, self.調])
        else:
            self.音標 = None
        return self.音標

    def 分析聲韻調傳結果(self, 音標):
        try:
            聲韻, 調值 = self.調值分開.match(音標).group(1, 2)
        except AttributeError:
            return False
        聲韻符合, self.聲, self.韻 = self._揣聲韻(聲韻)
        if not 聲韻符合:
            return False
        elif self.韻[-1] in ['p', 't', 'k', 'h']:
            if 調值 in 入聲調實際調值對應調號:
                self.調 = 入聲調實際調值對應調號[調值]
            else:
                return False
        else:
            if 調值 in 實際調值對應調號:
                self.調 = 實際調值對應調號[調值]
            else:
                return False
        if self.聲 in ['m', 'n', 'ng']:
            if self.韻 not in ['ng', 'ngh'] and ('n' in self.韻 or 'm' in self.韻):
                return False
            elif self.韻[-1] in ['p', 't', 'k']:
                return False
            elif self.韻 == 'o':
                return False
        if self.聲 in ['b', 'l', 'g']:
            if 'nn' in self.韻:
                return False
        return True
