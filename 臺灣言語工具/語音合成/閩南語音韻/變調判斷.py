# -*- coding: utf-8 -*-
from 臺灣言語工具.基本物件.公用變數 import 本調符號
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.語音合成.閩南語音韻.變調.規則變調 import 規則變調
from 臺灣言語工具.語音合成.閩南語音韻.變調.維持本調 import 維持本調
from 臺灣言語工具.語音合成.閩南語音韻.變調.無調符號 import 無調符號
from 臺灣言語工具.語音合成.閩南語音韻.變調.輕聲 import 輕聲
from 臺灣言語工具.語音合成.閩南語音韻.變調.三連音變調 import 三連音變調
from 臺灣言語工具.語音合成.閩南語音韻.變調.仔前變調 import 仔前變調
from 臺灣言語工具.語音合成.閩南語音韻.變調.隨前變調 import 隨前變調
from 臺灣言語工具.語音合成.閩南語音韻.變調.再變調 import 再變調


class 變調判斷:
    愛提掉的 = '愛提掉的'

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
            except IndexError:
                pass
            if len(一詞的字陣列) == 3 and len(set(一詞的字陣列)) == 1:
                一詞的字陣列[0].是三連音 = True
            有仔 = False
            for 字物件 in 一詞的字陣列:
                有仔 = 有仔 or cls.是仔無(字物件)
            if 有仔:
                一詞的字陣列[-1].有仔 = True
        字陣列 = 結果句物件.篩出字物件()
        尾結果 = []
        紲落來是本調 = True
        頂一个是斷詞點 = False
        頂一个是仔 = False
        for 字物件 in 字陣列[::-1]:
            這个是斷詞點 = False
            if hasattr(字物件, '是三連音'):
                delattr(字物件, '是三連音')
                尾結果.append(三連音變調)
                紲落來是本調 = False
                這个是斷詞點 = True
            elif hasattr(字物件, '有仔'):
                delattr(字物件, '有仔')
                尾結果.append(維持本調)
                紲落來是本調 = False
            elif cls.是井號無(字物件):
                尾結果.append(cls.愛提掉的)
                紲落來是本調 = True
            elif len(字物件.音) != 3:
                尾結果.append(無調符號)
            else:
                _聲, _韻, 調 = 字物件.音
                if len(尾結果) > 0 and 尾結果[-1] == 隨前變調:
                    尾結果[-1] = 隨前變調(調)
                if 調 == '0':
                    if cls.輕聲是隨前變調無(字物件):
                        尾結果.append(隨前變調)
                    else:
                        尾結果.append(輕聲)
                    紲落來是本調 = True
                elif 頂一个是仔:
                    尾結果.append(仔前變調)
                    紲落來是本調 = False
                elif (
                    紲落來是本調 or
                    (頂一个是斷詞點 and not cls.是代名詞無(字物件))
                ):
                    尾結果.append(維持本調)
                    紲落來是本調 = False
                elif cls.是再變調(字物件):
                    尾結果.append(再變調)
                    紲落來是本調 = False
                else:
                    尾結果.append(規則變調)
                    紲落來是本調 = False
            if cls.會有斷詞點無(字物件):
                這个是斷詞點 = True
            頂一个是仔 = cls.是仔無(字物件)
            頂一个是斷詞點 = 這个是斷詞點
        上尾結果 = []
        for 結果 in 尾結果[::-1]:
            if 結果 == 隨前變調:
                上尾結果.append(輕聲)
            else:
                上尾結果.append(結果)
        return 上尾結果

    @classmethod
    def 是井號無(cls, 字物件):
        if 字物件.型 == 本調符號:  # and 字物件.音==cls.本調記號:
            return True
        return False

    @classmethod
    def 是仔無(cls, 字物件):
        if 字物件.型 == '仔':  # and 字物件.音==cls.本調記號:
            return True
        return False

    @classmethod
    def 是代名詞無(cls, 字物件):
        if 字物件.型 in ['我', '你', '伊', '咱', '阮', '恁', '𪜶', ]:
            return True
        return False

    @classmethod
    def 輕聲是隨前變調無(cls, 字物件):
        if cls.是代名詞無(字物件):
            return True
        if 字物件.型 in ['的', '仔', '裡', ]:
            return True
        return False

    @classmethod
    def 是再變調(cls, 字物件):
        if 字物件.型 in ['欲', '去']:
            return True
        return False

    @classmethod
    def 會有斷詞點無(cls, 字物件):
        if 字物件.型 in ['的']:
            return True
        return False
