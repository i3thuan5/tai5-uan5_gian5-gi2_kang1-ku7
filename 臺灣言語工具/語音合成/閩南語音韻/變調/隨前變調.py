# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


class 隨前變調:
    對應表 = {
        '1': '1', '2': '3', '3': '3', '4': '3',
        '5': '7', '7': '7', '8': '3'
    }

    def __init__(self, 頂一个調):
        self._變調後輕聲音 = self.對應表[頂一个調]

    def __eq__(self, 別的):
        try:
            return self._變調後輕聲音 == 別的._變調後輕聲音
        except AttributeError:
            return False

    def 變調(self, 音):
        聲, 韻, 調 = 音
        if 韻.endswith('p') or 韻.endswith('t') or 韻.endswith('k'):
            raise 解析錯誤('入聲毋知愛按怎隨前變調！！{0}'.format((聲, 韻, 調)))
        return (聲, 韻.rstrip('hʔ'), self._變調後輕聲音)
