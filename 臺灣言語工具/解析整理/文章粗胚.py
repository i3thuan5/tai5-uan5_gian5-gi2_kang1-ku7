# -*- coding: utf-8 -*-
import unicodedata
from 臺灣言語工具.基本物件.公用變數 import 標點符號
from 臺灣言語工具.基本物件.公用變數 import 分字符號
from 臺灣言語工具.基本物件.公用變數 import 分詞符號
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.基本物件.公用變數 import 組字式符號
from 臺灣言語工具.基本物件.公用變數 import 統一碼漢字佮組字式類
from 臺灣言語工具.基本物件.公用變數 import 統一碼羅馬字類
from 臺灣言語工具.基本物件.公用變數 import 統一碼數字類
from 臺灣言語工具.基本物件.公用變數 import 聲調符號
import re


class 文章粗胚:
    分字符號代表字 = '{0}{1}{0}'.format(分詞符號, 分字符號)
    兩分字符號代表字 = '{0}{1}{0}{1}{0}'.format(分詞符號, 分字符號)
    雙分字符號 = 分字符號 * 2
    三分字符號 = 分字符號 * 3
    _一般 = '_一般'
    _組字 = '_組字'

    @classmethod
    def 建立物件語句前減號變標點符號(cls, 語句):
        return 語句.replace(分字符號, cls.分字符號代表字)

    # 輕聲連字符會擲掉，但是會留一个連字符做斷詞
    # 若減號兩邊毋是漢字、組字號，就是合法的音標，伊就當作連字符來斷詞
    @classmethod
    def 建立物件語句前處理減號(cls, 音標工具, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == 分字符號:
            return cls.分字符號代表字
        if 語句.startswith(分字符號 + 分字符號):
            if cls._後壁有音標無(音標工具, 語句[2:]):
                語句 = '0' + 語句[2:]
            elif(2 < len(語句) and unicodedata.category(語句[2]) in 統一碼漢字佮組字式類):
                語句 = 語句[2:]
        位置 = 0
        狀態 = cls._一般
        這回一開始狀態 = 狀態
        前回一開始狀態 = 狀態
        組字式長度 = 0
        字元陣列 = []
        while 位置 < len(語句):
            前回一開始狀態 = 這回一開始狀態
            這回一開始狀態 = 狀態
# 			print(狀態)
            if 語句[位置] in 組字式符號:
                組字式長度 -= 1
                狀態 = cls._組字
            else:
                組字式長度 += 1
            if 狀態 == cls._一般 and 組字式長度 == 1:
                if 語句[位置:].startswith(cls.三分字符號):
                    字元陣列.append(分詞符號)
                    while 位置 < len(語句) and 語句[位置] == 分字符號:
                        字元陣列.append(分字符號)
                        字元陣列.append(分詞符號)
                        位置 += 1
                    位置 -= 1
                elif 語句[位置:].startswith(cls.雙分字符號):
                    if cls._頭前有音標無(音標工具, 語句[位置 + 2:]):
                        if 前回一開始狀態 == cls._組字 or \
                                len(字元陣列) > 0 and unicodedata.category(字元陣列[-1][-1]) in 統一碼漢字佮組字式類 or\
                                cls._後壁有音標無(音標工具, 語句[:位置]):
                            字元陣列.append('-0')
                        else:
                            字元陣列.append('0')
                    elif (位置 + 2 < len(語句) and unicodedata.category(語句[位置 + 2]) in 統一碼漢字佮組字式類):
                        if 前回一開始狀態 == cls._組字 or \
                                len(字元陣列) > 0 and unicodedata.category(字元陣列[-1][-1]) in 統一碼漢字佮組字式類 or\
                                cls._後壁有音標無(音標工具, 語句[:位置]):
                            字元陣列.append(分字符號)
                    else:
                        字元陣列.append(cls.兩分字符號代表字)
                    位置 += 1
    # 				print('後來', 語句)
                elif 語句[位置] == 分字符號:
                    頭節 = cls._後壁有音標無(音標工具, 語句[:位置])
                    後節 = cls._頭前有音標無(音標工具, 語句[位置 + 1:])
                    頭前漢字抑是組字式 = (
                        位置 - 1 >= 0 and unicodedata.category(語句[位置 - 1]) in 統一碼漢字佮組字式類)
                    後壁漢字抑是組字式 = (
                        位置 + 1 < len(語句) and unicodedata.category(語句[位置 + 1]) in 統一碼漢字佮組字式類)
                    頭前閣是組字式 = (前回一開始狀態 == cls._組字)
# 					print(頭節 , 頭前漢字抑是組字式 , 頭前閣是組字式,後節 , 後壁漢字抑是組字式)
                    if (頭節 or 頭前漢字抑是組字式 or 頭前閣是組字式) and (後節 or 後壁漢字抑是組字式):
                        字元陣列.append(語句[位置])
                    else:
                        字元陣列.append(cls.分字符號代表字)
                else:
                    字元陣列.append(語句[位置])
                組字式長度 = 0
            elif 狀態 == cls._組字 and 組字式長度 == 1:
                狀態 = cls._一般
                組字式長度 = 0
                字元陣列.append(語句[位置])
            else:
                字元陣列.append(語句[位置])
            位置 += 1
        if 前回一開始狀態 == cls._一般 and 語句.endswith(分字符號):
            字元陣列.append(分詞符號)
        return cls._除掉重覆的空白(''.join(字元陣列))

    @classmethod
    def 符號邊仔加空白(cls, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        cls._減號有照規則無(語句)
# 		for 符號 in 標點符號:
# 			if 符號 != 分字符號 and 符號 != 分詞符號:
# 				語句 = 語句.replace(符號, '{0}{1}{0}'.format(分詞符號, 符號))
        位置 = 0
        狀態 = cls._一般
        組字式長度 = 0
        while 位置 < len(語句):
            if 語句[位置] in 組字式符號:
                組字式長度 -= 1
                狀態 = cls._組字
            else:
                組字式長度 += 1
            if 狀態 == cls._一般 and 組字式長度 == 1:
                if 語句[位置] in 聲調符號 \
                        and 位置 - 1 >= 0 and unicodedata.category(語句[位置 - 1]) in 統一碼羅馬字類:
                    pass
                elif 語句[位置] == '•' and cls._o結尾(語句[:位置]):
                    pass
                elif 語句[位置] != 分字符號 and 語句[位置] != 分詞符號 and 語句[位置] in 標點符號:
                    語句 = 語句[:位置] + \
                        '{0}{1}{0}'.format(分詞符號, 語句[位置]) + 語句[位置 + 1:]
                    位置 += 2
                組字式長度 = 0
            elif 狀態 == cls._組字 and 組字式長度 == 1:
                狀態 = cls._一般
                組字式長度 = 0
            位置 += 1
        return cls._除掉重覆的空白(語句)

    @classmethod
    def _減號有照規則無(cls, 語句):
        分字符號合法 = True
        狀態 = cls._一般
        組字式長度 = 0
        for 位置 in range(len(語句)):
            if 語句[位置] in 組字式符號:
                組字式長度 -= 1
                狀態 = cls._組字
            else:
                組字式長度 += 1
            if 狀態 == cls._一般 and 組字式長度 == 1:
                if 語句[位置] == 分字符號:
                    if 位置 + 1 < len(語句) and 語句[位置 + 1] == 分字符號:
                        raise 解析錯誤(
                            '語句內底袂使有連紲兩个減號，愛用空白隔開：{0}。請先用「{1}」抑是「{2}」'.format(
                                str(語句),
                                '文章粗胚.建立物件語句前處理減號()',
                                '文章粗胚.建立物件語句前減號變標點符號()',
                            )
                        )
                    if 分字符號合法:
                        上尾會使位置 = 位置
                    if 位置 == 0:
                        if len(語句) > 1:
                            分字符號合法 = False
                    elif 位置 == len(語句) - 1:
                        if len(語句) > 1:
                            分字符號合法 = False
                    elif 語句[位置 - 1] != 分詞符號 and 語句[位置 + 1] == 分詞符號:
                        分字符號合法 = False
                    elif 語句[位置 - 1] == 分詞符號 and 語句[位置 + 1] != 分詞符號:
                        分字符號合法 = False
                組字式長度 = 0
            elif 狀態 == cls._組字 and 組字式長度 == 1:
                狀態 = cls._一般
                組字式長度 = 0
        if not 分字符號合法:
            raise 解析錯誤(
                '語句內底減號，兩邊袂使干焦一邊是空白：位置＝{1}，語句＝{0}'.format(str(語句), 上尾會使位置))

    @classmethod
    def _頭前有音標無(cls, 音標工具, 語句):
        for 長度 in range(1, min(len(語句), 音標工具.音標上長長度) + 1):
            if 音標工具(語句[:長度]).音標 is not None:
                return True
        return False

    @classmethod
    def _後壁有音標無(cls, 音標工具, 語句):
        for 長度 in range(1, min(len(語句), 音標工具.音標上長長度) + 1):
            if 音標工具(語句[-長度:]).音標 is not None:
                return True
        return False

    @classmethod
    def _除掉重覆的空白(cls, 語句):
        新語句 = []
        for 字 in 語句:
            if len(新語句) == 0 or 新語句[-1] != 分詞符號 or 字 != 分詞符號:
                新語句.append(字)
        return ''.join(新語句)

    @classmethod
    def 數字英文中央全加分字符號(cls, 語句):
        新語句 = []
        舊字 = '字'
        for 字 in 語句:
            if unicodedata.category(舊字) in 統一碼數字類 and \
                    unicodedata.category(字) in 統一碼羅馬字類:
                新語句.append(分字符號)
            新語句.append(字)
            舊字 = 字
        return cls._除掉重覆的空白(''.join(新語句))

    @classmethod
    def 數字英文中央看情形加分字符號(cls, 語句, 專有名詞):
        愛切的物件 = '(' + '|'.join(專有名詞) + ')'
        切好的語句 = re.split(愛切的物件, 語句)
        結果 = []
        for 第幾个, 部份語句 in enumerate(切好的語句):
            if 第幾个 % 2 == 0:
                結果.append(cls.數字英文中央全加分字符號(部份語句))
            else:
                結果.append(部份語句)
        return ''.join(結果)

    @classmethod
    def _o結尾(cls, 語句):
        for o in ['o', 'ó', 'ò', 'ô', 'ǒ', 'ō', 'o̍', 'ő']:
            if 語句.endswith(o):
                return True
        return False
