
_聲母 = {
    'b': 'ㄅ', 'p': 'ㄆ', 'm': 'ㄇ', 'f': 'ㄈ',
    'd': 'ㄉ', 't': 'ㄊ', 'n': 'ㄋ', 'l': 'ㄌ',
    'g': 'ㄍ', 'k': 'ㄎ', 'h': 'ㄏ',
    'j': 'ㄐ', 'q': 'ㄑ', 'x': 'ㄒ',
    'zh': 'ㄓ', 'ch': 'ㄔ', 'sh': 'ㄕ', 'r': 'ㄖ',
    'z': 'ㄗ', 'c': 'ㄘ', 's': 'ㄙ',
}

_韻母 = {
    'a': 'ㄚ', 'o': 'ㄛ', 'e': 'ㄜ',
    'ai': 'ㄞ', 'ei': 'ㄟ', 'ao': 'ㄠ', 'ou': 'ㄡ',
    'an': 'ㄢ', 'en': 'ㄣ', 'ang': 'ㄤ', 'eng': 'ㄥ',
    'er': 'ㄦ',
}

_有聲母韻 = {
    'i': 'ㄧ', 'ia': 'ㄧㄚ', 'io': 'ㄧㄛ', 'ie': 'ㄧㄝ', 'iao': 'ㄧㄠ', 'iu': 'ㄧㄡ',
    'ian': 'ㄧㄢ', 'in': 'ㄧㄣ', 'iang': 'ㄧㄤ', 'ing': 'ㄧㄥ',
    'u': 'ㄨ', 'ua': 'ㄨㄚ', 'ui': 'ㄨㄛ', 'uai': 'ㄨㄞ', 'ui': 'ㄨㄟ',
    'uan': 'ㄨㄢ', 'un': 'ㄨㄣ', 'uang': 'ㄨㄤ', 'ong': 'ㄨㄥ',
    #'':'ㄩ','':'ㄩㄝ','':'ㄩㄢ','':'ㄩㄣ','':'ㄩㄥ',
}
_零聲母韻 = {
    'yi': 'ㄧ', 'ya': 'ㄧㄚ', 'yo': 'ㄧㄛ', 'ye': 'ㄧㄝ', 'yao': 'ㄧㄠ', 'you': 'ㄧㄡ',
    'yan': 'ㄧㄢ', 'yin': 'ㄧㄣ', 'yang': 'ㄧㄤ', 'ying': 'ㄧㄥ',
    'wu': 'ㄨ', 'wa': 'ㄨㄚ', 'wo': 'ㄨㄛ', 'wai': 'ㄨㄞ', 'wei': 'ㄨㄟ',
    'wan': 'ㄨㄢ', 'wen': 'ㄨㄣ', 'wang': 'ㄨㄤ', 'weng': 'ㄨㄥ',
    #'':'ㄩ','':'ㄩㄝ','':'ㄩㄢ','':'ㄩㄣ','':'ㄩㄥ',
}
_特例 = {
    'nv': 'ㄋㄩ', 'lv': 'ㄌㄩ',
}

_調 = {'1': '', '2': 'ˊ', '3': 'ˇ', '4': 'ˋ', '˙': '˙', }

_有聲母韻.update(_韻母)
_零聲母韻.update(_韻母)


class 漢語拼音:

    def __init__(self, 拼音):
        self.音標 = 拼音
        self.調 = 拼音[-1]
        self.聲韻 = 拼音[:-1]
        if self.聲韻 in _特例:
            self.聲 = self.聲韻[0]
            self.韻 = self.聲韻[1]
        elif self.聲韻 in _韻母:
            self.聲 = ''
            self.韻 = self.聲韻
        elif self.聲韻 in _零聲母韻:
            self.聲 = ''
            self.韻 = self.聲韻
        elif self.聲韻[:1] in _聲母 and self.聲韻[1:] in _有聲母韻:
            self.聲 = self.聲韻[:1]
            self.韻 = self.聲韻[1:]
        elif self.聲韻[:2] in _聲母 and self.聲韻[2:] in _有聲母韻:
            self.聲 = self.聲韻[:2]
            self.韻 = self.聲韻[2:]
        else:
            self.調 = None
            self.聲韻 = None
            self.音標 = None

    def 預設音標(self):
        return self.轉換到注音符號()

    def 轉換到注音符號(self):
        if self.音標 != None:
            if self.聲韻 in _特例:
                return  _特例[ self.聲韻] + _調[self.調]
            if self.聲 != '':
                return _聲母[self.聲] + _有聲母韻[self.韻] + _調[self.調]
            else:
                return _零聲母韻[self.韻] + _調[self.調]
