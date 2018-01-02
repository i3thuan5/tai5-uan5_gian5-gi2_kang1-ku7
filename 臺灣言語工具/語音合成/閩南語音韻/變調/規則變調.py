# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


class 規則變調:
    喉入聲變調規則 = {'4': '2', '8': '3'}
    入聲變調規則 = {'4': '8', '8': '10'}
    變調規則 = {'1': '7', '2': '1', '3': '2', '5': '7', '7': '3'}

    @classmethod
    def 變調(cls, 音):
        聲, 韻, 調 = 音
        if 韻.endswith('ʔ') or 韻.endswith('h'):
            try:
                調 = cls.喉入聲變調規則[調]
            except KeyError:
                raise 解析錯誤('喉塞尾調錯誤！！{0}'.format((聲, 韻, 調)))
            韻 = 韻[:-1]
        elif 韻.endswith('p') or 韻.endswith('t') or 韻.endswith('k'):
            try:
                調 = cls.入聲變調規則[調]
            except KeyError:
                raise 解析錯誤('入尾調錯誤！！{0}'.format((聲, 韻, 調)))
        else:
            if 調 in cls.變調規則:
                調 = cls.變調規則[調]
            else:
                raise 解析錯誤('非入調錯誤！！{0}'.format((聲, 韻, 調)))
        return (聲, 韻, 調)
