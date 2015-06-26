# -*- coding: utf-8 -*-

臺灣客家話拼音對照音值聲母表 = {
    'b': 'p', 'p': 'pʰ', 'bb': 'b', 'm': 'm', 'f': 'f', 'v': 'v',
    'd': 't', 't': 'tʰ', 'l': 'l', 'n': 'n', 'r': 'j',
    'z': 'ts', 'c': 'tsʰ', 's': 's',
    'j': 'tɕ', 'q': 'tɕʰ', 'x': 'ɕ',
    'zh': 'tʃ', 'ch': 'tʃʰ', 'sh': 'ʃ', 'rh': 'ʒ',
    'g': 'k', 'k': 'kʰ', 'ng': 'ŋ',
    'h': 'h', '': 'ʔ',
}

臺灣客家話拼音對照音值韻母表 = {
    'ii': 'ï', 'i': 'i', 'e': 'e', 'a': 'a', 'o': 'o', 'u': 'u',
    'ie': 'ie', 'eu': 'eu', 'ieu': 'ieu', 'ia': 'ia', 'ua': 'ua', 'ai': 'ai',
    'iai': 'iai', 'uai': 'uai', 'au': 'au', 'iau': 'iau', 'io': 'io', 'oi': 'oi',
    'ioi': 'ioi', 'iu': 'iu', 'ui': 'ui', 'iui': 'iui',
    'ue': 'ue',
    'iim': 'ïm', 'im': 'im', 'em': 'em', 'iem': 'iem', 'am': 'am', 'iam': 'iam',
    'iin': 'ïn', 'in': 'in', 'en': 'en', 'ien': 'ien', 'uen': 'uen', 'an': 'an',
    'ian': 'ian', 'uan': 'uan', 'on': 'on', 'ion': 'ion', 'un': 'un', 'iun': 'iun',
    'ang': 'aŋ', 'iang': 'iaŋ', 'uang': 'uaŋ',
    'ong': 'oŋ', 'iong': 'ioŋ', 'ung': 'uŋ', 'iung': 'iuŋ',
    'iib': 'ïp', 'ib': 'ip', 'eb': 'ep', 'ieb': 'iep', 'ab': 'ap', 'iab': 'iap',
    'iid': 'ït', 'id': 'it', 'ed': 'et', 'ied': 'iet', 'ued': 'uet',
    'ad': 'at', 'iad': 'iat', 'uad': 'uat', 'od': 'ot', 'iod': 'iot', 'ud': 'ut', 'iud': 'iut',
    'ag': 'ak', 'iag': 'iak', 'uag': 'uak', 'og': 'ok', 'iog': 'iok', 'ug': 'uk', 'iug': 'iuk',
    'er': 'ə',
    'm': 'm̩', 'n': 'n̩', 'ng': 'ŋ̩',
    'oo': 'ɔ',
    'ee': 'ɛ', 'eeb': 'ɛp', 'eed': 'ɛt', 'eem': 'ɛm', 'een': 'ɛn', 'eeu': 'ɛu',
    'ainn': 'aⁿiⁿ', 'ann': 'aⁿ', 'iann': 'iⁿaⁿ', 'inn': 'iⁿ', 'onn': 'oⁿ', 'uainn': 'uⁿaⁿiⁿ',
}

臺灣客家話拼音聲母實際音值表 = {'ngi': 'ȵ'}
臺灣客家話拼音聲母實際音值表.update(臺灣客家話拼音對照音值聲母表)


class 臺灣客家話拼音轉音值模組():
    聲母表 = 臺灣客家話拼音對照音值聲母表
    韻母表 = 臺灣客家話拼音對照音值韻母表

    def 轉(self, 聲, 韻, 調):
        if 聲 is None or 韻 is None or 調 is None:
            return (None,)
        音值聲 = self.聲母表[聲]
        音值韻 = self.韻母表[韻]
        if 音值聲 == 'ŋ' and 音值韻.startswith('i'):
            音值聲 = 'ȵ'
        音值調 = 調
        return (音值聲, 音值韻, 音值調)
