# -*- coding: utf-8 -*-
from 臺灣言語工具.音標系統.閩南語.教會系羅馬音標 import 教會系羅馬音標
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音聲母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音韻母表

教會羅馬字音標聲母表 = {'p', 'ph', 'm', 'b', 't', 'th', 'n', 'l',
              'k', 'kh', 'ng', 'g', 'h', 'ch', 'chh', 's', 'j', ''
              } | 臺灣閩南語羅馬字拼音聲母表
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
} | 臺灣閩南語羅馬字拼音韻母表
教會羅馬字音標聲調符號表 = dict(
    á=('a', 2), à=('a', 3), â=('a', 5), ǎ=('a', 6), ā=('a', 7), a̍=('a', 8), a̋=('a', 9),
    é=('e', 2), è=('e', 3), ê=('e', 5), ě=('e', 6), ē=('e', 7), e̍=('e', 8), e̋=('e', 9),
    í=('i', 2), ì=('i', 3), î=('i', 5), ǐ=('i', 6), ī=('i', 7), i̍=('i', 8), i̋=('i', 9),
    ó=('o', 2), ò=('o', 3), ô=('o', 5), ǒ=('o', 6), ō=('o', 7), o̍=('o', 8), ő=('o', 9),
    ú=('u', 2), ù=('u', 3), û=('u', 5), ǔ=('u', 6), ū=('u', 7), u̍=('u', 8), ű=('u', 9),
    ḿ=('m', 2), m̀=('m', 3), m̂=('m', 5), m̌=('m', 6), m̄=('m', 7), m̍=('m', 8), m̋=('m', 9),
    ń=('n', 2), ǹ=('n', 3), n̂=('n', 5), ň=('n', 6), n̄=('n', 7), n̍=('n', 8), n̋=('n', 9),)


class 教會羅馬字音標(教會系羅馬音標):
    聲母表 = 教會羅馬字音標聲母表
    韻母表 = 教會羅馬字音標韻母表

    def __init__(self, 音標):
        super(教會羅馬字音標, self).__init__()
        self.分析聲韻調(音標.replace('hN', 'Nh').replace('ou', 'oo')
                   .replace('ooN', 'onn').replace('oonn', 'onn'))
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
