# -*- coding: utf-8 -*-
from 臺灣言語工具.基本物件.公用變數 import 分字符號
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.基本物件.組 import 組
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from itertools import chain
import re
from kesi import Ku, TuiBeTse
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.基本物件.公用變數 import 斷句標點符號
from 臺灣言語工具.基本物件.公用變數 import 分型音符號
from 臺灣言語工具.解析整理.程式掠漏 import 程式掠漏


class 拆文分析器:
    _切組物件分詞 = re.compile('(([^ ｜]*[^ ]｜[^ ][^ ｜]*) ?|[^ ]+)')
    _切章分詞 = re.compile('(\n｜.|.｜\n|\n)', re.DOTALL)
    _是空白 = re.compile(r'[^\S\n]+')
    _是分字符號 = re.compile('{}+'.format(分字符號))
    _是數字 = set('0123456789')

    @classmethod
    def 建立字物件(cls, 語句, 別種書寫=None):
        if 別種書寫 is None:
            return cls._物件的音攏提掉(cls.對齊字物件(語句, 語句))
        return cls.對齊字物件(語句, 別種書寫)

    @classmethod
    def 建立詞物件(cls, 語句, 別種書寫=None):
        if 別種書寫 is None:
            return cls._物件的音攏提掉(cls.對齊詞物件(語句, 語句))
        return cls.對齊詞物件(語句, 別種書寫)

    @classmethod
    def 建立組物件(cls, 語句, 別種書寫=None):
        if 別種書寫 is None:
            return cls._物件的音攏提掉(cls.對齊組物件(語句, 語句))
        return cls.對齊組物件(語句, 別種書寫)

    @classmethod
    def 建立集物件(cls, 語句, 別種書寫=None):
        if 別種書寫 is None:
            return cls._物件的音攏提掉(cls.對齊集物件(語句, 語句))
        return cls.對齊集物件(語句, 別種書寫)

    @classmethod
    def 建立句物件(cls, 語句, 別種書寫=None):
        if 別種書寫 is None:
            return cls._物件的音攏提掉(cls.對齊句物件(語句, 語句))
        return cls.對齊句物件(語句, 別種書寫)

    @classmethod
    def 建立章物件(cls, 語句, 別種書寫=None):
        if 別種書寫 is None:
            return cls._物件的音攏提掉(cls.對齊章物件(語句, 語句))
        return cls.對齊章物件(語句, 別種書寫)

    @classmethod
    def 對齊字物件(cls, 型, 音):
        if 型 in ['<s>', '</s>'] and 型 == 音:
            return 字(型)
        組物件 = cls.對齊組物件(型, 音)
        tsuan = 組物件.篩出字物件()
        if len(tsuan) == 1:
            return tsuan[0]
        if len(tsuan) == 0:
            raise 解析錯誤('「{0}」、「{1}」bô字'.format(型, 音))
        raise 解析錯誤('「{0}」、「{1}」超過一e字'.format(型, 音))

    @classmethod
    def 對齊詞物件(cls, 型, 音):
        組物件 = cls.對齊組物件(型, 音)
        if len(組物件.內底詞) == 0:
            return 詞()
        if len(組物件.內底詞) > 1:
            raise 解析錯誤('「{0}」、「{1}」超過一e5詞'.format(型, 音))
        return 組物件.內底詞[0]

    # 斷詞會照音來斷，型的連字符攏無算
    # 毋過若是型kah音其中一个有輕聲符--，就當作輕聲字
    @classmethod
    def 對齊組物件(cls, 型, 音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if not isinstance(音, str):
            raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '' and 音 == 無音:
            return 組()

        try:
            組物件 = 組()
            for su in Ku(型, 音):
                詞物件 = 詞()
                for ji in su:
                    jie = 字.tuìKeSi(ji)
                    詞物件.內底字.append(jie)
                組物件.內底詞.append(詞物件)
        except TuiBeTse:
            raise 解析錯誤('詞內底的型、音bô平長')

        return 組物件

    @classmethod
    def 對齊集物件(cls, 型, 音):
        if 型 == '' and 音 == 無音:
            return 集()
        集物件 = 集()
        集物件.內底組 = [cls.對齊組物件(型, 音)]
        return 集物件

    @classmethod
    def 對齊句物件(cls, 型, 音):
        if 型 == '' and 音 == 無音:
            return 句()
        句物件 = 句()
        句物件.內底集 = [cls.對齊集物件(型, 音)]
        return 句物件

    @classmethod
    def 對齊章物件(cls, 型, 音):
        if 型 == '' and 音 == 無音:
            return 章()

        斷句詞陣列 = cls._詞陣列分一句一句(cls.對齊句物件(型, 音).網出詞物件())
        return cls._斷句詞陣列轉章物件(斷句詞陣列)

    @classmethod
    def 分詞字物件(cls, 分詞):
        程式掠漏.毋是字串都毋著(分詞)
        切開結果 = 分詞.split(分型音符號)
        if len(切開結果) == 2:
            return cls.對齊字物件(*切開結果)
        return cls._分詞字詞處理(分詞, 切開結果, cls.建立字物件)

    @classmethod
    def 分詞詞物件(cls, 分詞):
        程式掠漏.毋是字串都毋著(分詞)
        分詞 = 分詞.strip(' 　')
        if 分詞 == '' or 分詞 == 分型音符號:
            return cls.建立詞物件(分詞)
        切開結果 = 分詞.split(分型音符號)
        if len(切開結果) == 2:
            型, 音 = 切開結果
            return cls.對齊詞物件(型, 音)
        return cls._分詞字詞處理(分詞, 切開結果, cls.建立詞物件)

    @classmethod
    def 分詞組物件(cls, 分詞):
        程式掠漏.毋是字串都毋著(分詞)
        if 分詞 == '':
            return 組()
        組物件 = cls.建立組物件('')
        切開 = cls._切組物件分詞.split(分詞)
        for 分, 細 in zip(切開[1::3], 切開[2::3]):
            if 細 is not None:
                組物件.內底詞.append(cls.分詞詞物件(細))
            else:
                組物件.內底詞.append(cls.分詞詞物件(分))
        return 組物件

    @classmethod
    def 分詞集物件(cls, 分詞):
        if 分詞 == '':
            return 集()
        集物件 = cls.建立集物件('')
        集物件.內底組.append(cls.分詞組物件(分詞))
        return 集物件

    @classmethod
    def 分詞句物件(cls, 分詞):
        if 分詞 == '':
            return 句()
        句物件 = cls.建立句物件('')
        句物件.內底集.append(cls.分詞集物件(分詞))
        return 句物件

    @classmethod
    def 分詞章物件(cls, 分詞):
        if 分詞 == '':
            return 章()
        斷出來的詞陣列 = []
        try:
            for 第幾个, 句分詞 in enumerate(cls._切章分詞.split(分詞)):
                if 第幾个 % 2 == 0:
                    斷出來的詞陣列.append(
                        cls.分詞句物件(句分詞).網出詞物件()
                    )
                else:
                    斷出來的詞陣列.append(
                        cls.分詞詞物件(句分詞).網出詞物件()
                    )
        except TypeError:
            raise 型態錯誤('分詞型態有問題，分詞：{}'.format(分詞))
        斷句詞陣列 = cls._詞陣列分一句一句(list(chain(*斷出來的詞陣列)))
        return cls._斷句詞陣列轉章物件(斷句詞陣列)

    @classmethod
    def _詞陣列分一句一句(cls, 詞陣列):
        有一般字無 = False
        愛換的所在 = []
        for 詞物件 in 詞陣列[::-1]:
            是斷句, 是換逝 = cls._詞物件敢是斷句符號抑是換逝(詞物件)
            if (有一般字無 and 是斷句) or 是換逝:
                愛換的所在.append(True)
                有一般字無 = False
            else:
                愛換的所在.append(False)
                if not 是斷句:
                    有一般字無 = True
        愛換的所在 = 愛換的所在[::-1]
        斷句詞陣列 = []
        頭前 = 0
        for 第幾字 in range(len(詞陣列)):
            if 愛換的所在[第幾字]:
                斷句詞陣列.append(詞陣列[頭前:第幾字 + 1])
                頭前 = 第幾字 + 1
        if 頭前 < len(詞陣列):
            斷句詞陣列.append(詞陣列[頭前:])
        return 斷句詞陣列

    @classmethod
    def _斷句詞陣列轉章物件(cls, 斷句詞陣列):
        章物件 = 章()
        for 詞陣列 in 斷句詞陣列:
            組物件 = 組()
            組物件.內底詞 = 詞陣列
            集物件 = 集()
            集物件.內底組 = [組物件]
            句物件 = 句()
            句物件.內底集 = [集物件]
            章物件.內底句.append(句物件)
        return 章物件

    @classmethod
    def _詞物件敢是斷句符號抑是換逝(cls, 詞物件):
        if len(詞物件.內底字) == 1:
            字物件 = 詞物件.內底字[0]
            if 字物件.型 == '\n' or 字物件.音 == '\n':
                return False, True
            if 字物件.型 in 斷句標點符號 and\
                    (字物件.音 == 無音 or 字物件.音 in 斷句標點符號):
                return True, False
        return False, False

    @classmethod
    def _拆好陣列對齊詞物件(cls, 型陣列, 音陣列, 輕聲陣列):
        if len(型陣列) < len(音陣列):
            raise 解析錯誤('詞內底的型「{0}」比音「{1}」少！{2}：{3}'.format(
                str(型陣列), str(音陣列), len(型陣列), len(音陣列)))
        if len(型陣列) > len(音陣列):
            raise 解析錯誤('詞內底的型「{0}」比音「{1}」濟！{2}：{3}'.format(
                str(型陣列), str(音陣列), len(型陣列), len(音陣列)))
        if 型陣列 == [] and 音陣列 == []:
            return 詞()
        長度 = len(型陣列)
        詞物件 = 詞()
        字陣列 = 詞物件.內底字
        for 位置 in range(長度):
            字陣列.append(字(型陣列[位置], 音陣列[位置], 輕聲陣列[位置]))
        return 詞物件

    @classmethod
    def _物件的音攏提掉(cls, 對齊物件):
        for 字物件 in 對齊物件.篩出字物件():
            字物件.音 = 無音
        return 對齊物件

    @classmethod
    def _分詞字詞處理(cls, 分詞, 切開結果, 建立物件的函式):
        if len(切開結果) == 1:
            return 建立物件的函式(分詞)
        if 切開結果 == [''] * 4:
            return 建立物件的函式(分型音符號, 分型音符號)
        if len(切開結果) == 3:
            if 切開結果[:2] == [''] * 2:
                return 建立物件的函式(分型音符號, 切開結果[2])
            if 切開結果[-2:] == [''] * 2:
                return 建立物件的函式(切開結果[0], 分型音符號)
        raise 解析錯誤('毋是拄仔好有一个抑是兩个部份：{0}'.format(分詞))
