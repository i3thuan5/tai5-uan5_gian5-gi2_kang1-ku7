# -*- coding: utf-8 -*-


class 輕聲:
    輕聲調 = '3'
    入聲輕聲調 = '10'
    喉入聲變調規則 = {'4': '3', '8': '3'}
    入聲變調規則 = {'4': '10', '8': '10'}
    變調規則 = {'1': '3', '2': '3', '3': '3', '5': '3', '7': '3', '0': '3'}

    @classmethod
    def 變調(cls, 音):
        聲, 韻, 調 = 音
        if 韻.endswith('ʔ') or 韻.endswith('h'):
            調 = cls.輕聲調
            韻 = 韻[:-1]
        elif 韻.endswith('p') or 韻.endswith('t') or 韻.endswith('k'):
            調 = cls.入聲輕聲調
        else:
            調 = cls.輕聲調
        return (聲, 韻, 調)
