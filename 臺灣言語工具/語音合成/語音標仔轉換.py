# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔
from 臺灣言語工具.基本物件.公用變數 import 標點符號
import curses.ascii
import itertools


from 臺灣言語工具.基本物件.章 import 章
"""
變調
處理無音的字物件
轉聲韻
算佇詞句中的所在
產生標仔
"""
# 前音-此音+後音/調：調類/詞：第幾字!上尾第幾字@攏總字/句：第幾字^上尾第幾字_攏總字/驗:md5


class 語音標仔轉換:
    恬音 = 'sil'
    短恬 = 'sp'
    免知 = 'x'
    音標格式 = '{0}-{1}+{2}/調:{3}<{4}>{5}/詞:{6}!{7}@{8}/句:{9}^{10}_{11}'
    音值格式 = '{0}'

    @classmethod
    def 恬標仔(cls):
        return cls._用全部資訊產生合成標仔(cls.免知, cls.恬音, cls.免知,
                                cls.免知, cls.免知, cls.免知,
                                cls.免知, cls.免知, cls.免知,
                                cls.免知, cls.免知, cls.免知,
                                )

    @classmethod
    def 短恬標仔(cls):
        return cls._用全部資訊產生合成標仔(cls.免知, cls.短恬, cls.免知,
                                cls.免知, cls.免知, cls.免知,
                                cls.免知, cls.免知, cls.免知,
                                cls.免知, cls.免知, cls.免知,
                                )

    @classmethod
    def 物件轉完整合成標仔(cls, 物件, 加短恬=False):
        if isinstance(物件, 章):
            return cls._章物件轉完整合成標仔(物件, 加短恬)
        return cls._句物件轉完整合成標仔(物件, 加短恬)

    @classmethod
    def 提出標仔陣列主要音值(cls, 完整標仔陣列):
        '''予HTK切音，而且HTS粗胚用的'''
        音值標仔陣列 = []
        for 標仔 in 完整標仔陣列:
            音值標仔陣列.append(cls.提出標仔主要音值(標仔))
        return 音值標仔陣列

    @classmethod
    def 提出標仔主要音值(cls, 完整標仔):
        'split(None, 1)[0]是為著縛做伙三連音做對照表時會當用的'
        音 = 完整標仔.split(None, 1)[0].split('+', 1)[0].split('-', 1)[-1]
        return 音

    @classmethod
    def 跳脫標仔陣列(cls, 標仔陣列):
        新標仔 = []
        for 語句 in 標仔陣列:
            新標仔.append(cls.跳脫標仔(語句))
        return 新標仔

    @classmethod
    def 跳脫標仔(cls, 標仔):
        """
        佇HTK內底的HShell.c
        ReWriteString((char*)s.c_str(), NULL, ESCAPE_CHAR)
        ....
        else if (isprint(*p) || noNumEscapes) fputc(*p,f);
        else {
         n=*p;
         fputc(ESCAPE_CHAR,f);
         fputc(((n/64)%8)+'0',f);fputc(((n/8)%8)+'0',f);fputc((n%8)+'0',f);
         """
        處理了 = []
        for 字元編碼 in 標仔.encode(encoding='utf_8', errors='strict'):
            字元 = chr(字元編碼)
            if curses.ascii.isprint(字元):
                處理了.append(字元)
            else:
                處理了.append('\\')
                數值 = 字元編碼
                for 編碼 in [(數值 // 64) % 8, (數值 // 8) % 8, 數值 % 8]:
                    處理了.append(chr(ord('0') + 編碼))
        return ''.join(處理了)

    @classmethod
    def _章物件轉完整合成標仔(cls, 章物件, 加短恬):
        全部標仔 = []
        for 句物件 in 章物件.內底句:
            全部標仔.append(cls._句物件轉完整合成標仔(句物件, 加短恬))
        return itertools.chain.from_iterable(全部標仔)

    @classmethod
    def _句物件轉完整合成標仔(cls, 句物件, 加短恬):
        for 集物件 in 句物件.內底集:
            新組陣列 = []
            for 詞物件 in 集物件.內底組[0].內底詞:
                if len(詞物件.內底字) > 1 or\
                        詞物件.內底字[0].型 not in 標點符號:
                    新組陣列.append(詞物件)
            集物件.內底組[0].內底詞 = 新組陣列
        詞陣列 = 詞物件網仔.網出詞物件(句物件)
        攏總詞數量 = len(詞陣列)
        if 攏總詞數量 == 0:
            return [cls.恬標仔()]
        句中第幾詞 = 0
        全部詞資料 = []
        全部字資料 = []
        全部聲韻資料 = []
        for 詞物件 in 詞陣列:
            字陣列 = 字物件篩仔.篩出字物件(詞物件)
            攏總字數量 = len(字陣列)
            詞中第幾字 = 0
            for 字物件 in 字陣列:
                try:
                    聲, 韻, 調 = 字物件.音
                    if 加短恬 and len(全部聲韻資料) > 0:
                        頂一个聲韻 = 全部聲韻資料[-1][0]
                        if 頂一个聲韻 != cls.恬音 and 頂一个聲韻 != cls.短恬:
                            全部聲韻資料.append((cls.短恬, len(全部字資料)))
                    全部聲韻資料.append((聲, len(全部字資料)))
                    全部聲韻資料.append((韻, len(全部字資料)))
                except:
                    調 = cls.免知
                    全部聲韻資料.append((cls.恬音, len(全部字資料)))
                全部字資料.append((調, 詞中第幾字, 攏總字數量, len(全部詞資料)))
                詞中第幾字 += 1
            全部詞資料.append((句中第幾詞, 攏總詞數量))
            句中第幾詞 += 1
        合成標仔 = [cls.恬標仔()]
        for 聲韻資料所在 in range(len(全部聲韻資料)):
            這馬聲韻, 這馬字所在 = 全部聲韻資料[聲韻資料所在]
            if 這馬聲韻 == cls.恬音:
                合成標仔.append(cls.恬標仔())
                continue
            elif 這馬聲韻 == cls.短恬:
                合成標仔.append(cls.短恬標仔())
                continue
            if 聲韻資料所在 - 1 >= 0 and 全部聲韻資料[聲韻資料所在 - 1][0] != cls.短恬:
                頭前聲韻 = 全部聲韻資料[聲韻資料所在 - 1][0]
            elif 聲韻資料所在 - 2 >= 0 and 全部聲韻資料[聲韻資料所在 - 2][0] != cls.短恬:
                頭前聲韻 = 全部聲韻資料[聲韻資料所在 - 2][0]
            else:
                頭前聲韻 = cls.恬音
            if 聲韻資料所在 + 1 < len(全部聲韻資料) and 全部聲韻資料[聲韻資料所在 + 1][0] != cls.短恬:
                後壁聲韻 = 全部聲韻資料[聲韻資料所在 + 1][0]
            elif 聲韻資料所在 + 2 < len(全部聲韻資料) and 全部聲韻資料[聲韻資料所在 + 2][0] != cls.短恬:
                後壁聲韻 = 全部聲韻資料[聲韻資料所在 + 2][0]
            else:
                後壁聲韻 = cls.恬音

            這馬字調, 詞中第幾字, 攏總字數量, 這馬詞所在 = \
                全部字資料[這馬字所在]
            if 這馬字所在 - 1 >= 0:
                頭前字調 = 全部字資料[這馬字所在 - 1][0]
            else:
                頭前字調 = cls.免知
            if 這馬字所在 + 1 < len(全部字資料):
                後壁字調 = 全部字資料[這馬字所在 + 1][0]
            else:
                後壁字調 = cls.免知
            句中第幾詞, 攏總詞數量 = 全部詞資料[這馬詞所在]

            聲韻標仔 = cls._用音節佮部份順序資訊產生合成標仔(
                頭前聲韻, 這馬聲韻, 後壁聲韻,
                頭前字調, 這馬字調, 後壁字調,
                詞中第幾字, 攏總字數量,
                句中第幾詞, 攏總詞數量)
            合成標仔.append(聲韻標仔)
        合成標仔.append(cls.恬標仔())
        return 合成標仔

    @classmethod
    def _用全部資訊產生合成標仔(cls, 前音, 此音, 後音, 前字調, 此字調, 後字調,
                     詞中第幾字, 詞中上尾幾字, 詞攏總字數,
                     句中第幾詞, 句中上尾幾詞, 句攏總詞數):
        原本音標 = cls.音標格式.format(
            前音, 此音, 後音, 前字調, 此字調, 後字調,
            詞中第幾字, 詞中上尾幾字, 詞攏總字數,
            句中第幾詞, 句中上尾幾詞, 句攏總詞數)
        return 原本音標

    @classmethod
    def _用音節佮部份順序資訊產生合成標仔(cls, 前音, 此音, 後音, 前字調, 此字調, 後字調,
                          詞中第幾字, 詞攏總字數, 句中第幾詞, 句攏總詞數):
        return cls._用全部資訊產生合成標仔(
            前音, 此音, 後音, 前字調, 此字調, 後字調,
            詞中第幾字, 詞攏總字數 - 詞中第幾字, 詞攏總字數,
            句中第幾詞, 句攏總詞數 - 句中第幾詞, 句攏總詞數)
