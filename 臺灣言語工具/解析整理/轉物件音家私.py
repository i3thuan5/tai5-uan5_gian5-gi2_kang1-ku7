# -*- coding: utf-8 -*-
from 臺灣言語工具.基本元素.字 import 字
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.基本元素.組 import 組
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.基本元素.章 import 章
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本元素.公用變數 import 無音
from 臺灣言語工具.基本元素.公用變數 import 標點符號


class 轉物件音家私():
    # 逐个函式攏愛產生新的物件
    @classmethod
    def _轉字音(cls, 音標工具, 字物件, 函式):
        if not isinstance(字物件, 字):
            raise 型態錯誤('傳入來的毋是字物件：{0}'.format(str(字物件)))
        if 字物件.型 in 標點符號 and 字物件.音 in 標點符號:
            新音 = 字物件.音
        elif 字物件.音 != 無音:
            新音物件 = 音標工具(字物件.音)
            if 新音物件 is None:
                raise 解析錯誤('音標無合法：{0}'.format(str(字物件)))
            新音 = getattr(新音物件, 函式)()
            if 新音 is None:
                raise 解析錯誤('音標無法度轉：{0}'.format(str(字物件)))
        else:
            新音 = 無音
        新型物件 = 音標工具(字物件.型)
        新型預設音標 = getattr(新型物件, 函式)()
        if 字物件.音.startswith(字物件.型) and isinstance(新音, str):
            新型 = 新音
        elif 新型物件 is not None\
                and 新型預設音標 is not None and isinstance(新型預設音標, str):
            新型 = 新型預設音標
        else:
            新型 = 字物件.型
        return 字(新型, 新音)

    @classmethod
    def _轉詞音(cls, 音標工具, 詞物件, 函式):
        if not isinstance(詞物件, 詞):
            raise 型態錯誤('傳入來的毋是詞物件：{0}'.format(str(詞物件)))
        新詞物件 = 詞()
        for 字物件 in 詞物件.內底字:
            新詞物件.內底字.append(cls._轉字音(音標工具, 字物件, 函式))
        return 新詞物件

    @classmethod
    def _轉組音(cls, 音標工具, 組物件, 函式):
        if not isinstance(組物件, 組):
            raise 型態錯誤('傳入來的毋是組物件：{0}'.format(str(組物件)))
        新組物件 = 組()
        for 詞物件 in 組物件.內底詞:
            新組物件.內底詞.append(cls._轉詞音(音標工具, 詞物件, 函式))
        return 新組物件

    @classmethod
    def _轉集音(cls, 音標工具, 集物件, 函式):
        if not isinstance(集物件, 集):
            raise 型態錯誤('傳入來的毋是集物件：{0}'.format(str(集物件)))
        新集物件 = 集()
        for 組物件 in 集物件.內底組:
            新集物件.內底組.append(cls._轉組音(音標工具, 組物件, 函式))
        return 新集物件

    @classmethod
    def _轉句音(cls, 音標工具, 句物件, 函式):
        if not isinstance(句物件, 句):
            raise 型態錯誤('傳入來的毋是句物件：{0}'.format(str(句物件)))
        新句物件 = 句()
        for 集物件 in 句物件.內底集:
            新句物件.內底集.append(cls._轉集音(音標工具, 集物件, 函式))
        return 新句物件

    @classmethod
    def _轉章音(cls, 音標工具, 章物件, 函式):
        if not isinstance(章物件, 章):
            raise 型態錯誤('傳入來的毋是章物件：{0}'.format(str(章物件)))
        新章物件 = 章()
        for 句物件 in 章物件.內底句:
            新章物件.內底句.append(cls._轉句音(音標工具, 句物件, 函式))
        return 新章物件

    @classmethod
    def 轉音(cls, 音標工具, 物件, 函式='預設音標'):
        if isinstance(物件, 字):
            return cls._轉字音(音標工具, 物件, 函式)
        if isinstance(物件, 詞):
            return cls._轉詞音(音標工具, 物件, 函式)
        if isinstance(物件, 組):
            return cls._轉組音(音標工具, 物件, 函式)
        if isinstance(物件, 集):
            return cls._轉集音(音標工具, 物件, 函式)
        if isinstance(物件, 句):
            return cls._轉句音(音標工具, 物件, 函式)
        if isinstance(物件, 章):
            return cls._轉章音(音標工具, 物件, 函式)
        raise 型態錯誤('傳入來的毋是字詞組集句章其中一種物件：{0}，{1}'
                   .format(type(物件), str(物件)))
