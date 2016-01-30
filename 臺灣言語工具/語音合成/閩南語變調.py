# -*- coding: utf-8 -*-
from 臺灣言語工具.基本物件.公用變數 import 本調符號
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.基本物件.句 import 句


class 閩南語變調:
    實詞變調規則 = {'1': '7', '2': '1', '3': '2', '5': '7',
              '7': '3', '0': '0', '6': '3'}  # 6聲愛查

    @classmethod
    def 變調(cls, 物件):
        if isinstance(物件, 章):
            return cls._變章物件調(物件)
        return cls._變句物件調(物件)

    @classmethod
    def _變章物件調(cls, 章物件):
        結果章物件 = 章()
        for 句物件 in 章物件.內底句:
            結果章物件.內底句.append(cls._變句物件調(句物件))
        return 結果章物件

    @classmethod
    def _變句物件調(cls, 句物件):
        結果句物件 = 句(句物件.內底集)
        字陣列 = 字物件篩仔.篩出字物件(結果句物件)
        尾本調 = []
        有出現上尾字無 = False
        頂一个是本調記號 = False
        頂一个是斷詞點 = False
        for 字物件 in 字陣列[::-1]:
            if len(字物件.音) == 3:
                if not 有出現上尾字無 or\
                        頂一个是本調記號 or\
                        (頂一个是斷詞點 and 字物件.型 not in ['我', '你', '伊', '咱', '阮', '恁', '𪜶', ]):
                    尾本調.append(False)
                    有出現上尾字無 = True
                else:
                    尾本調.append(True)
            else:
                尾本調.append(False)
            頂一个是本調記號 = False
            頂一个是斷詞點 = False
            if 字物件.型 == 本調符號:  # and 字物件.音==cls.本調記號:
                頂一个是本調記號 = True
            if 字物件.型 in ['的', '是']:  # and 字物件.音==cls.本調記號:
                頂一个是斷詞點 = True
        for 字物件, 愛變調無 in zip(字陣列, 尾本調[::-1]):
            if 愛變調無:
                字物件.音 = cls.實詞變調(*字物件.音)
        return 結果句物件

    @classmethod
    def 實詞變調(cls, 聲, 韻, 調):
        if 韻.endswith('ʔ') or 韻.endswith('h'):
            if 調 == '4':
                調 = '2'
            elif 調 == '8':
                調 = '3'
            else:
                raise 解析錯誤('喉塞尾調錯誤！！{0}'.format((聲, 韻, 調)))
            韻 = 韻[:-1]
        elif 韻.endswith('p') or 韻.endswith('t') or 韻.endswith('k'):
            if 調 == '4':
                調 = '8'
            elif 調 == '8':
                調 = '10'
            else:
                raise 解析錯誤('入尾調錯誤！！{0}'.format((聲, 韻, 調)))
        else:
            if 調 in cls.實詞變調規則:
                調 = cls.實詞變調規則[調]
            else:
                raise 解析錯誤('非入調錯誤！！{0}'.format((聲, 韻, 調)))
        return (聲, 韻, 調)
