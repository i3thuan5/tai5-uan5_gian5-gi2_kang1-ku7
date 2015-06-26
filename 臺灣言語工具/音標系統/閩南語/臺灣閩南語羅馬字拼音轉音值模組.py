# -*- coding: utf-8 -*-

臺灣閩南語羅馬字拼音對照音值聲母表 = {
    'p': 'p', 'ph': 'pʰ', 'm': 'm', 'b': 'b',
    't': 't', 'th': 'tʰ', 'n': 'n', 'l': 'l',
    'k': 'k', 'kh': 'kʰ', 'ng': 'ŋ', 'g': 'g',
    'ts': 'ts', 'tsh': 'tsʰ', 's': 's', 'j': 'dz',
    'h': 'h', '': 'ʔ',
}

臺灣閩南語羅馬字拼音對照音值韻母表 = {
    'a': 'a', 'ah': 'aʔ', 'ap': 'ap', 'at': 'at', 'ak': 'ak',
    'am': 'am', 'an': 'an', 'ang': 'aŋ',
    'ann': 'aⁿ', 'annh': 'aⁿʔ',
    'e': 'e', 'eh': 'eʔ', 'enn': 'eⁿ', 'ennh': 'eⁿʔ',
    'i': 'i', 'ih': 'iʔ', 'ip': 'ip', 'it': 'it', 'ik': 'ik',
    'inn': 'iⁿ', 'innh': 'iⁿʔ',
    'im': 'im', 'in': 'in', 'ing': 'iŋ',
    'o': 'ə', 'oh': 'əʔ',
    'oo': 'o', 'ooh': 'oʔ', 'op': 'op', 'ok': 'ok',
    'om': 'om', 'ong': 'oŋ',
    'onn': 'oⁿ', 'onnh': 'oⁿʔ',
    'oi': 'əi', 'oih': 'əiʔ',  # ##
    'u': 'u', 'uh': 'uʔ', 'ut': 'ut', 'un': 'un',
    'ai': 'ai', 'aih': 'aiʔ', 'ainn': 'aⁿiⁿ', 'ainnh': 'aⁿiⁿʔ',
    'au': 'au', 'auh': 'auʔ', 'aunn': 'aⁿuⁿ', 'aunnh': 'aⁿuⁿʔ',
    'ia': 'ia', 'iah': 'iaʔ', 'iap': 'iap', 'iat': 'iet', 'iak': 'iak',
    'iam': 'iam', 'ian': 'ien', 'iang': 'iaŋ',
    'iann': 'iⁿaⁿ', 'iannh': 'iⁿaⁿʔ',
    'io': 'iə', 'ioh': 'iəʔ', 'iok': 'iok',
    'iong': 'ioŋ', 'ionn': 'iⁿoⁿ',
    'iu': 'iu', 'iuh': 'iuʔ', 'iut': 'iut',
    'iunn': 'iⁿuⁿ', 'iunnh': 'iⁿuⁿʔ',
    'ua': 'ua', 'uah': 'uaʔ', 'uat': 'uat', 'uak': 'uak',
    'uan': 'uan', 'uann': 'uⁿaⁿ', 'uannh': 'uⁿaⁿʔ',
    'ue': 'ue', 'ueh': 'ueʔ',
    'uenn': 'uⁿeⁿ', 'uennh': 'uⁿeⁿʔ',
    'ui': 'ui', 'uih': 'uiʔ',
    'uinn': 'uⁿiⁿ', 'uinnh': 'uⁿiⁿʔ',
    'iau': 'iau', 'iauh': 'iauʔ',
    'iaunn': 'iⁿaⁿuⁿ', 'iaunnh': 'iⁿaⁿuⁿʔ',
    'uai': 'uai', 'uaih': 'uaiʔ',
    'uainn': 'uⁿaⁿiⁿ', 'uainnh': 'uⁿaⁿiⁿʔ',
    'm': 'm̩', 'mh': 'm̩ʔ',
    'ng': 'ŋ̩', 'ngh': 'ŋ̩ʔ',
    'ioo': 'io', 'iooh': 'ioʔ',
    'er': 'ə', 'erh': 'əʔ',
    'erm': 'əm', 'ere': 'əe', 'ereh': 'əeʔ',
    'ee': 'ɛ', 'eeh': 'ɛʔ', 'eng': 'eŋ', 'uee': 'uee',
    'ir': 'ɨ', 'irh': 'ɨʔ', 'irp': 'ɨp', 'irt': 'ɨt', 'irk': 'ɨk',
    'irm': 'ɨm', 'irn': 'ɨn', 'irng': 'ɨŋ',
    'irinn': 'ɨⁿiⁿ',
    'ie': 'ie',
    'or': 'ə', 'orh': 'əʔ', 'ior': 'iə', 'iorh': 'iəʔ',
    'uang': 'uaŋ',
}


class 臺灣閩南語羅馬字拼音轉音值模組():
    聲母表 = 臺灣閩南語羅馬字拼音對照音值聲母表
    韻母表 = 臺灣閩南語羅馬字拼音對照音值韻母表

    def 轉(self, 聲, 韻, 調, 輕):
        if 聲 is None or 韻 is None or 調 is None or 輕 is None:
            return (None,)
        音值聲 = self.聲母表[聲]
        音值韻 = self.韻母表[韻]
        音值調 = 調
        if 音值調 == '0' or 輕 == '0':
            音值調 = '0'
            if 音值韻.endswith('ʔ') or 音值韻.endswith('p')\
                    or 音值韻.endswith('t') or 音值韻.endswith('k'):
                音值韻 = 音值韻[:-1]
        return (音值聲, 音值韻, 音值調)
