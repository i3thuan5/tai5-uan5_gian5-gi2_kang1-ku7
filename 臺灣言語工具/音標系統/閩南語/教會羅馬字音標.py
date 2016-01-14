# -*- coding: utf-8 -*-
from 臺灣言語工具.音標系統.閩南語.教會系羅馬音標 import 教會系羅馬音標
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音次方言韻母表

教會羅馬字音標聲母表 = {
    'p', 'ph', 'm', 'b', 't', 'th', 'n', 'l',
    'k', 'kh', 'ng', 'g', 'h', 'ts', 'ch', 'chh', 's', 'j', ''
}
教會羅馬字音標韻母表 = {
    'a', 'ah', 'ap', 'at', 'ak', 'ann', 'annh',
    'am', 'an', 'ang',
    'e', 'eh', 'enn', 'ennh',
    'i', 'ih', 'ip', 'it', 'ek', 'inn', 'innh',
    'im', 'in', 'eng',
    'o', 'oh',
    'oo', 'ooh', 'op', 'ok', 'om', 'ong', 'onn', 'onnh',
    'ou', 'ouh',
    'oi', 'oih',  # 硩⿰落去
    'u', 'uh', 'ut', 'un',
    'ai', 'aih', 'ainn', 'ainnh',
    'au', 'auh', 'aunn', 'aunnh',
    'ia', 'iah', 'iap', 'iat', 'iak', 'iam', 'ian', 'iang', 'iann', 'iannh',
    'io', 'ioh',
    'iok', 'iong', 'ionn',
    'iu', 'iuh', 'iut', 'iunn', 'iunnh',
    'oa', 'oah', 'oat', 'oak', 'oan', 'oann', 'oannh',
    'oe', 'oeh', 'oenn', 'oennh',
    'ui', 'uih', 'uinn', 'uinnh',
    'iau', 'iauh', 'iaunn', 'iaunnh',
    'oai', 'oaih', 'oainn', 'oainnh',
    'm', 'mh', 'ng', 'ngh',
    'ioo', 'iooh',
    'iou', 'iouh',
}


class 教會羅馬字音標(教會系羅馬音標):
    聲母表 = 教會羅馬字音標聲母表
    韻母表 = 教會羅馬字音標韻母表 | 臺灣閩南語羅馬字拼音次方言韻母表

    def __init__(self, 音標):
        super(教會羅馬字音標, self).__init__()
        self.分析聲韻調(
            音標.replace('hN', 'Nh')
            .replace('ou', 'oo')
            .replace('ooN', 'onn').replace('oonn', 'onn')
        )
        if self.聲 == 'm' or self.聲 == 'n' or self.聲 == 'ng':
            if self.韻 == 'o':
                self.音標 = None

    def 轉換到臺灣閩南語羅馬字拼音(self):
        if self.音標 is None:
            return None
        聲母 = None
        if self.聲 == 'ch':
            聲母 = 'ts'
        elif self.聲 == 'chh':
            聲母 = 'tsh'
        else:
            聲母 = self.聲
        韻母 = None
        if self.韻[:2] == 'oa':
            韻母 = 'ua' + self.韻[2:]
        elif self.韻[:2] == 'oe':
            韻母 = 'ue' + self.韻[2:]
        elif self.韻[:2] == 'ou':
            韻母 = 'oo' + self.韻[2:]
        elif self.韻 == 'ek':
            韻母 = 'ik'
        elif self.韻 == 'eng':
            韻母 = 'ing'
        else:
            韻母 = self.韻
        return 聲母 + 韻母 + str(self.調)
    # 聲 介 韻 調，韻含元音跟韻尾
