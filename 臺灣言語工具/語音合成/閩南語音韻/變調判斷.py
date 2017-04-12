# -*- coding: utf-8 -*-
from 臺灣言語工具.基本物件.公用變數 import 本調符號
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.語音合成.閩南語音韻.變調.實詞變調 import 實詞變調
from 臺灣言語工具.語音合成.閩南語音韻.變調.維持本調 import 維持本調


class 變調判斷:

    @classmethod
    def 判斷(cls, 物件):
        if isinstance(物件, 章):
            return cls._章物件調(物件)
        return cls._句物件調(物件)

    @classmethod
    def _章物件調(cls, 章物件):
        結果 = []
        for 句物件 in 章物件.內底句:
            結果.extend(cls._句物件調(句物件))
        return 結果

    @classmethod
    def _句物件調(cls, 句物件):
        結果句物件 = 句(句物件.內底集)
        for 詞物件 in 結果句物件.網出詞物件():
            一詞的字陣列 = 詞物件.篩出字物件()
            try:
                if 一詞的字陣列[0].音[2] == '0':
                    for 字物件 in 一詞的字陣列[1:]:
                        字物件.音 = 字物件.音[:2] + ('0',)
            except:
                pass
        字陣列 = 結果句物件.篩出字物件()
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
        結果 = []
        for 字物件, 愛變調無 in zip(字陣列, 尾本調[::-1]):
            if 愛變調無:
                結果.append(實詞變調)
            else:
                結果.append(維持本調)
        return 結果
