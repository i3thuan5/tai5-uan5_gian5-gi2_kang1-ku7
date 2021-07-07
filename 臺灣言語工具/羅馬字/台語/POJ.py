# -*- coding: utf-8 -*-
from kesi.susia.TL import tsuanTL
from 臺灣言語工具.音標系統.閩南語.教會系羅馬音標 import 教會系羅馬音標
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音次方言韻母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音

白話字聲母表 = {
    'p', 'ph', 'm', 'b', 't', 'th', 'n', 'l',
    'k', 'kh', 'ng', 'g', 'h', 'ts', 'ch', 'chh', 's', 'j', ''
}
白話字韻母表 = {
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


class 白話字(教會系羅馬音標):
    聲母表 = 白話字聲母表
    韻母表 = 白話字韻母表 | 臺灣閩南語羅馬字拼音次方言韻母表

    def __init__(self, 音標):
        super().__init__()
        self.音標 = 音標
        self.分析聲韻調(
            音標.replace('hN', 'Nh')
            .replace('ou', 'oo')
            .replace('ooN', 'onn').replace('oonn', 'onn')
        )

    def 轉換到臺灣閩南語羅馬字拼音(self):
        if self.音標 is None:
            return self.音標
        return 臺灣閩南語羅馬字拼音(tsuanTL(self.音標)).音標

    def 音值(self):
        if self.音標 is None:
            return None
        return 臺灣閩南語羅馬字拼音(self.轉換到臺灣閩南語羅馬字拼音()).音值()
