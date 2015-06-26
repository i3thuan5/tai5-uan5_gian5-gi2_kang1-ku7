# -*- coding: utf-8 -*-
from 臺灣言語工具.音標系統.閩南語.閩南語音標介面 import 閩南語音標介面
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音

通用拼音佮臺灣羅馬聲母對照表 = {
    'b': 'p',
    'p': 'ph',
    'bh': 'b',
    'v': 'b',
    'm': 'm',
    'd': 't',
    't': 'th',
    'n': 'n',
    'l': 'l',
    'g': 'k',
    'k': 'kh',
    'gh': 'g',
    'q': 'g',
    'ng': 'ng',
    'z': 'ts',
    'c': 'tsh',
    's': 's',
    'r': 'j',
    'h': 'h',
    '': '',
}
通用拼音佮臺灣羅馬韻母對照表 = {
    'a': 'a', 'ah': 'ah', 'ap': 'ap', 'at': 'at', 'ak': 'ak',
    'am': 'am', 'an': 'an', 'ang': 'ang',
    'ann': 'ann', 'annh': 'annh',
    'ai': 'ai', 'aih': 'aih', 'ainn': 'ainn', 'ainnh': 'ainnh',
    'au': 'au', 'auh': 'auh', 'aunn': 'aunn', 'aunnh': 'aunnh',
    'e': 'e', 'eh': 'eh', 'en': 'ian', 'et': 'iat', 'enn': 'enn', 'ennh': 'ennh',
    'er': 'o', 'erh': 'oh', 'ernn': 'onn',
    'ia': 'ia', 'iah': 'iah', 'iap': 'iap', 'iak': 'iak',
    'iam': 'iam', 'iang': 'iang',
    'iann': 'iann', 'iannh': 'iannh',
    'iau': 'iau', 'iauh': 'iauh', 'iaunn': 'iaunn', 'iaunnh': 'iaunnh',
    'ier': 'io', 'ierh': 'ioh',
    'i': 'i', 'ih': 'ih', 'ip': 'ip', 'it': 'it', 'ik': 'ik',
    'im': 'im', 'in': 'in', 'ing': 'ing',
    'inn': 'inn', 'innh': 'innh',
    'io': 'ioo', 'ioh': 'iooh', 'iok': 'iok', 'iong': 'iong', 'ionn': 'ionn',
    'ior': 'io', 'iorh': 'ioh',
    'iu': 'iu', 'iuh': 'iuh', 'iut': 'iut', 'iunn': 'iunn', 'iunnh': 'iunnh',
    'm': 'm', 'mh': 'mh', 'ng': 'ng', 'ngh': 'ngh',
    'o': 'oo', 'oh': 'ooh', 'op': 'op', 'ok': 'ok',
    'om': 'om', 'ong': 'ong',
    'onn': 'onn', 'onnh': 'onnh',
    'or': 'o', 'orh': 'oh', 'orm': 'om', 'ornn': 'onn',
    'oi': 'oi', 'oih': 'oih',
    'ua': 'ua', 'uah': 'uah', 'uat': 'uat', 'uak': 'uak', 'uainn': 'uainn', 'uainnh': 'uainnh',
    'uan': 'uan', 'uann': 'uann', 'uannh': 'uannh',
    'uai': 'uai', 'uaih': 'uaih',
    'ue': 'ue', 'ueh': 'ueh', 'uenn': 'uenn', 'uennh': 'uennh',
    'ui': 'ui',
    'uih': 'uih', 'uinn': 'uinn', 'uinnh': 'uinnh',
    'u': 'u', 'un': 'un', 'uh': 'uh', 'ut': 'ut',
    'ie': 'ie', 'uang': 'uang',
}
通用拼音佮臺灣羅馬調類對照表 = {
    '1': '1', '2': '7', '3': '3', '4': '2', '5': '5',
    '6': '8', '7': '4', '8': '10', '9': '9'}


class 通用拼音音標(閩南語音標介面):
    # 0 bh iaunnh 9 保險
    音標上長長度 = 1 + 2 + 6 + 1 + 1
    聲 = None
    韻 = None
    聲韻 = None
    調 = None
    音標 = None

    def __init__(self, 音標):
        self.聲母對照表 = 通用拼音佮臺灣羅馬聲母對照表
        self.韻母對照表 = 通用拼音佮臺灣羅馬韻母對照表
        self.調類對照表 = 通用拼音佮臺灣羅馬調類對照表
        self.音標 = None
        self.音標 = None
        if 音標[-1:] in self.調類對照表:
            for 所在 in range(len(音標) - 1):
                if 音標[:所在] in self.聲母對照表 and 音標[所在:-1] in self.韻母對照表:
                    self.聲 = 音標[:所在]
                    self.韻 = 音標[所在:-1]
                    self.調 = 音標[-1:]
                    if self.韻.endswith('h') or self.韻.endswith('p') or \
                            self.韻.endswith('t') or self.韻.endswith('k'):
                        if self.調 == '1':
                            self.調 = '6'
                        elif self.調 == '2':
                            self.調 = '7'
                        elif self.調 == '3':
                            self.調 = '8'
                    self.聲韻 = self.聲 + self.韻
                    self.音標 = self.聲韻 + self.調
        if self.轉換到臺灣閩南語羅馬字拼音() is None:
            self.聲韻 = None
            self.音標 = None

    def 轉換到臺灣閩南語羅馬字拼音(self):
        if self.音標 is None:
            return None
        聲 = self.聲母對照表[self.聲]
        韻 = self.韻母對照表[self.韻]
        調 = self.調類對照表[self.調]
        臺羅 = 臺灣閩南語羅馬字拼音(聲 + 韻 + 調)
        return 臺羅.音標
