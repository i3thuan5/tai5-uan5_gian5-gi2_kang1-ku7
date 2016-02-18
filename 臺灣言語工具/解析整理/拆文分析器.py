# -*- coding: utf-8 -*-
from 臺灣言語工具.基本物件.公用變數 import 分字符號
from 臺灣言語工具.基本物件.公用變數 import 分詞符號
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.基本物件.組 import 組
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.基本物件.公用變數 import 組字式符號
from 臺灣言語工具.基本物件.公用變數 import 斷句標點符號
from 臺灣言語工具.基本物件.公用變數 import 標點符號
from itertools import chain
import re
import unicodedata


from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.基本物件.公用變數 import 分型音符號
from 臺灣言語工具.解析整理.程式掠漏 import 程式掠漏
from 臺灣言語工具.基本物件.公用變數 import 統一碼羅馬字類
from 臺灣言語工具.基本物件.公用變數 import 統一碼聲調符號
from 臺灣言語工具.基本物件.公用變數 import 統一碼注音聲調符號
from 臺灣言語工具.基本物件.公用變數 import 是拼音字元無
from 臺灣言語工具.基本物件.公用變數 import 是注音符號無
from 臺灣言語工具.基本物件.公用變數 import 統一碼數字類


class 拆文分析器:
    _切組物件分詞 = re.compile('([^ ]*.｜.[^ ]*|\S+)')
    _切章分詞 = re.compile('(\n｜.|.｜\n|\n)', re.DOTALL)

    @classmethod
    def 建立字物件(cls, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == '':
            raise 解析錯誤('傳入來的語句是空的！')
        return 字(語句)

    @classmethod
    def 建立詞物件(cls, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == '':
            return 詞()
        拆好的字 = cls._拆句做字(語句)
        字陣列 = []
        for 孤詞 in 拆好的字:
            字陣列.append(cls.建立字物件(孤詞))
        詞物件 = 詞()
        詞物件.內底字 = 字陣列
        return 詞物件

    # 接受漢羅，但是注音會當作一字一字，除非用組字式。
    # 連字符的兩爿攏無使有空白，若減號愛留的，頭前上好有空白無就是佇句首。
    # 若無法度處理，閣愛保留連字符，用對齊來做。
    @classmethod
    def 建立組物件(cls, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == '':
            return 組()
        巢狀詞陣列 = cls._拆句做巢狀詞(語句)
        詞陣列 = []
        for 孤詞 in 巢狀詞陣列:
            字陣列 = []
            for 孤字 in 孤詞:
                字陣列.append(cls.建立字物件(孤字))
            詞物件 = 詞()
            詞物件.內底字 = 字陣列
            詞陣列.append(詞物件)
        組物件 = 組()
        組物件.內底詞 = 詞陣列
        return 組物件

    @classmethod
    def 建立集物件(cls, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == '':
            return 集()
        集物件 = 集()
        集物件.內底組 = [cls.建立組物件(語句)]
        return 集物件

    @classmethod
    def 建立句物件(cls, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == '':
            return 句()
        句物件 = 句()
        句物件.內底集 = [cls.建立集物件(語句)]
        return 句物件

    @classmethod
    def 建立章物件(cls, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == '':
            return 章()
        語句陣列 = cls._拆章做句(語句)
        句陣列 = []
        for 一句 in 語句陣列:
            句陣列.append(cls.建立句物件(一句))
        章物件 = 章()
        章物件.內底句 = 句陣列
        return 章物件

    @classmethod
    def 對齊字物件(cls, 型, 音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if not isinstance(音, str):
            raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '':
            raise 解析錯誤('傳入來的型是空的！')
        if 音 != 無音 and (型 in 標點符號) ^ (音 in 標點符號):
            raise 解析錯誤('型佮音干焦一个是標點符號！「{}」佮「{}」'.format(型, 音))
        return 字(型, 音)

    @classmethod
    def 對齊詞物件(cls, 型, 音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if not isinstance(音, str):
            raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '' and 音 == 無音:
            return 詞()
        型陣列 = cls._拆句做字(型)
        音陣列 = cls._詞音拆字(音)
        if len(型陣列) < len(音陣列):
            raise 解析錯誤('詞內底的型「{0}」比音「{1}」少！{2}：{3}'.format(
                str(型), str(音), len(型陣列), len(音陣列)))
        if len(型陣列) > len(音陣列):
            raise 解析錯誤('詞內底的型「{0}」比音「{1}」濟！{2}：{3}'.format(
                str(型), str(音), len(型陣列), len(音陣列)))
        return cls._拆好陣列對齊詞物件(型陣列, 音陣列)

    @classmethod
    def _拆好陣列對齊詞物件(cls, 型陣列, 音陣列):
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
            字陣列.append(cls.對齊字物件(型陣列[位置], 音陣列[位置]))
        return 詞物件

    # 斷詞會照音來斷，型的連字符攏無算
    @classmethod
    def 對齊組物件(cls, 型, 音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if not isinstance(音, str):
            raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '' and 音 == 無音:
            return 組()
        # #
# 		型陣列 = cls._拆句做字(文章粗胚.符號邊仔加空白(型))
        型陣列 = cls._拆句做字(型)

        詞陣列 = []
        第幾字 = 0
        for 詞音 in 文章粗胚.符號邊仔加空白(音).strip(分詞符號).split(分詞符號):
            字音陣列 = cls._詞音拆字(詞音)
            if 第幾字 + len(字音陣列) > len(型陣列):
                raise 解析錯誤('詞組內底的型「{0}」比音「{1}」少！配對結果：{2}'.format(
                    str(型), str(音), str(詞陣列)))
            詞陣列.append(
                cls._拆好陣列對齊詞物件(型陣列[第幾字:第幾字 + len(字音陣列)], 字音陣列))
            第幾字 += len(字音陣列)
        if 第幾字 < len(型陣列):
            raise 解析錯誤('詞組內底的型「{0}」比音「{1}」濟！配對結果：{2}'.format(
                str(型), str(音), str(詞陣列)))
        組物件 = 組()
        組物件.內底詞 = 詞陣列
        return 組物件

    @classmethod
    def 對齊集物件(cls, 型, 音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if not isinstance(音, str):
            raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '' and 音 == 無音:
            return 集()
        集物件 = 集()
        集物件.內底組 = [cls.對齊組物件(型, 音)]
        return 集物件

    @classmethod
    def 對齊句物件(cls, 型, 音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if not isinstance(音, str):
            raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '' and 音 == 無音:
            return 句()
        句物件 = 句()
        句物件.內底集 = [cls.對齊集物件(型, 音)]
        return 句物件

    @classmethod
    def 對齊章物件(cls, 型, 音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if not isinstance(音, str):
            raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '' and 音 == 無音:
            return 章()
#  		raise 型態錯誤('QQ型＝{0}，音＝{1}'.format(str(型), str(音)))
        型陣列 = cls._拆章做句(型)
        音陣列 = cls._拆章做句(音)
        if len(型陣列) > len(音陣列):
            raise 解析錯誤('詞內底的型「{0}」比音「{1}」少！'.format(
                str(型), str(音)))
        if len(型陣列) < len(音陣列):
            raise 解析錯誤('詞內底的型「{0}」比音「{1}」濟！'.format(
                str(型), str(音)))
        句陣列 = []
        for 型物件, 音物件 in zip(型陣列, 音陣列):
            句陣列.append(cls.對齊句物件(型物件, 音物件))
        章物件 = 章()
        章物件.內底句 = 句陣列
        return 章物件

    @classmethod
    def _拆句做字(cls, 語句):
        return cls._句解析(語句)[0]

    @classmethod
    def _拆句做巢狀詞(cls, 語句):
        字陣列, 佮後一个字是佇仝一个詞 = cls._句解析(語句)
        巢狀詞陣列 = []
        位置 = 0
        while 位置 < len(字陣列):
            範圍 = 位置
            while 範圍 < len(佮後一个字是佇仝一个詞) and 佮後一个字是佇仝一个詞[範圍]:
                範圍 += 1
            範圍 += 1
            巢狀詞陣列.append(字陣列[位置:範圍])
            位置 = 範圍
        return 巢狀詞陣列

    @classmethod
    def _句解析(cls, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == 分詞符號:
            return ([分詞符號], [False])
        字陣列 = []
        佮後一个字是佇仝一个詞 = []
        # 一般　組字
        狀態 = '一般'
        頂一个字 = None
        頂一个字種類 = None
        頂一个是注音符號 = False
        # 下組字式抑是數羅
        一个字 = ''
        長度 = 0
        位置 = 0
        while 位置 < len(語句):
            字 = 語句[位置]
            字種類 = unicodedata.category(字)
            是注音符號 = 是注音符號無(字)
# 			print(字種類, 字陣列, 是注音符號, unicodedata.name(字, 'QQ'))
            if 狀態 == '組字':
                一个字 += 字
                if 字 in 組字式符號:
                    長度 -= 1
                else:
                    長度 += 1
                if 長度 == 1:
                    字陣列.append(一个字)
                    佮後一个字是佇仝一个詞.append(False)
                    狀態 = '一般'
                    一个字 = ''
                    長度 = 0
            elif 狀態 == '一般':
                if 字 in 分字符號:
                    if 一个字 != '':
                        字陣列.append(一个字)
                        佮後一个字是佇仝一个詞.append(False)
                        一个字 = ''
                    if 語句[:位置].endswith(分詞符號) or 語句[位置 + 1:].startswith(分詞符號):
                        字陣列.append(分字符號)
                        佮後一个字是佇仝一个詞.append(False)
                    else:
                        if len(佮後一个字是佇仝一个詞) == 0:
                            if len(語句) > 1:
                                raise 解析錯誤(
                                    '一開始的減號是代表啥物？請用「文章粗胚.建立物件語句前處理減號」。語句：「{0}」'.format(
                                        str(語句)
                                    )
                                )
                            else:
                                字陣列.append(字)
                                佮後一个字是佇仝一个詞.append(False)
                        else:
                            佮後一个字是佇仝一个詞[-1] = True
                elif 字 in 分詞符號:
                    if 一个字 != '':
                        字陣列.append(一个字)
                        佮後一个字是佇仝一个詞.append(False)
                        一个字 = ''
                # 羅馬字接做伙
                elif 是拼音字元無(字, 字種類):
                    # 頭前是羅馬字抑是輕聲、外來語的數字
                    # 「N1N1」、「g0v」濫做伙名詞，「sui2sui2」愛變做兩个字，予粗胚處理。
                    if not 是拼音字元無(頂一个字, 頂一个字種類)\
                            and 頂一个字種類 not in 統一碼數字類:
                        # 頭前愛清掉
                        if 一个字 != '':
                            字陣列.append(一个字)
                            佮後一个字是佇仝一个詞.append(False)
                            一个字 = ''
                    一个字 += 字
                # 數字
                elif 字種類 in 統一碼數字類:
                    if not 是拼音字元無(頂一个字, 頂一个字種類)\
                            and 頂一个字種類 not in 統一碼數字類\
                            and not 頂一个是注音符號:
                        # 頭前愛清掉
                        if 一个字 != '':
                            字陣列.append(一个字)
                            佮後一个字是佇仝一个詞.append(False)
                            一个字 = ''
                    一个字 += 字
                # 音標後壁可能有聲調符號
                elif 字種類 in 統一碼聲調符號 and 頂一个字種類 in 統一碼羅馬字類:
                    一个字 += 字
                # 處理注音，輕聲、注音、空三个後壁會當接注音
                elif 是注音符號:
                    if 頂一个字種類 not in 統一碼注音聲調符號\
                            and not 頂一个是注音符號:
                        # 頭前愛清掉
                        if 一个字 != '':
                            字陣列.append(一个字)
                            佮後一个字是佇仝一个詞.append(False)
                            一个字 = ''
                    一个字 += 字
                # 注音後壁會當接聲調
                elif 字種類 in 統一碼注音聲調符號 and 頂一个是注音符號:
                    一个字 += 字

                elif 字 in 標點符號:
                    if 字 == '•' and 文章粗胚._o結尾(一个字):
                        一个字 += 字
                    else:
                        if 一个字 != '':
                            字陣列.append(一个字)
                            佮後一个字是佇仝一个詞.append(False)
                            一个字 = ''
                        字陣列.append(字)
                        佮後一个字是佇仝一个詞.append(False)
                else:
                    if 一个字 != '':
                        字陣列.append(一个字)
                        佮後一个字是佇仝一个詞.append(False)
                        一个字 = ''
                    一个字 += 字
                    if 字 in 組字式符號:
                        長度 -= 1
                        狀態 = '組字'
                    else:
                        長度 += 1
                    if 長度 == 1:
                        字陣列.append(一个字)
                        佮後一个字是佇仝一个詞.append(False)
                        一个字 = ''
                        長度 = 0
            位置 += 1
            頂一个字 = 字
            頂一个字種類 = 字種類
            頂一个是注音符號 = 是注音符號
        if 一个字 != '':
            if 狀態 == '一般':
                字陣列.append(一个字)
                佮後一个字是佇仝一个詞.append(False)
            elif 狀態 == '組字':
                raise 解析錯誤('語句組字式無完整，語句＝{0}'.format(str(語句)))
        return (字陣列, 佮後一个字是佇仝一个詞)

    @classmethod
    def _拆章做句(cls, 語句):
        # 敢有需要做
        # 枋寮漁港「大條巷」上闊兩公尺。=> 枋寮漁港  「  大條巷  」  上闊兩公尺  。
        # =>無，下佇仝詞組，予斷詞處理
        有一般字無 = False
        愛換的所在 = []
        for 第幾字 in range(len(語句))[::-1]:
            if 語句[第幾字] in 斷句標點符號 and 有一般字無:
                愛換的所在.append(True)
                有一般字無 = False
            else:
                愛換的所在.append(False)
                if 語句[第幾字] not in 斷句標點符號 and 語句[第幾字] != 分詞符號:
                    有一般字無 = True
        愛換的所在 = 愛換的所在[::-1]
        句陣列 = []
        頭前 = 0
        for 第幾字 in range(len(語句)):
            if 愛換的所在[第幾字]:
                if 語句[第幾字] in 斷句標點符號 and 語句[第幾字 + 1] == 分詞符號:
                    句陣列.append(語句[頭前:第幾字 + 2])
                else:
                    句陣列.append(語句[頭前:第幾字 + 1])
                頭前 = 第幾字 + 1
        句陣列.append(語句[頭前:])
        處理了頭前的句陣列 = []
        for 一句 in 句陣列:
            if 一句.startswith(分詞符號) and 一句[1] not in 標點符號:
                處理了頭前的句陣列.append(一句[1:])
            else:
                處理了頭前的句陣列.append(一句)
        return 處理了頭前的句陣列

    @classmethod
    def _詞音拆字(cls, 詞音):
        if 詞音 == 分字符號:
            return [分字符號]
        return 詞音.split(分字符號)

    @classmethod
    def 分詞字物件(cls, 分詞):
        程式掠漏.毋是字串都毋著(分詞)
        切開結果 = 分詞.split(分型音符號)
        if len(切開結果) == 2:
            return cls.對齊字物件(*切開結果)
        if len(切開結果) == 1:
            return cls.建立字物件(*切開結果)
        raise 解析錯誤('毋是拄仔好有一个抑是兩个部份：{0}'.format(分詞))

    @classmethod
    def 分詞詞物件(cls, 分詞):
        程式掠漏.毋是字串都毋著(分詞)
        if 分詞 == '':
            return cls.建立詞物件(分詞)
        切開結果 = 分詞.split(分型音符號)
        if len(切開結果) == 2:
            型, 音 = 切開結果
            if 型 == '':
                raise 解析錯誤('型是空的：{0}'.format(分詞))
            return cls.對齊詞物件(型, 音)
        if len(切開結果) == 1:
            return cls.建立詞物件(分詞)
        raise 解析錯誤('毋是拄仔好有一个抑是兩个部份：{0}'.format(分詞))

    @classmethod
    def 分詞組物件(cls, 分詞):
        程式掠漏.毋是字串都毋著(分詞)
        if 分詞 == '':
            return 組()
        組物件 = cls.建立組物件('')
        切開 = cls._切組物件分詞.split(分詞)
        for 分 in 切開[1::2]:
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
        全部斷句詞陣列 = []
        try:
            for 第幾个, 句分詞 in enumerate(cls._切章分詞.split(分詞)):
                if 第幾个 % 2 == 0:
                    if 句分詞.strip() != '':
                        原來句物件 = cls.分詞句物件(句分詞)
                        原來詞陣列 = 原來句物件.網出詞物件()
                        斷句詞陣列 = cls._詞陣列分一句一句(原來詞陣列)
                        全部斷句詞陣列.append(斷句詞陣列)
                else:
                    全部斷句詞陣列[-1][-1].append(cls.分詞詞物件(句分詞))
        except TypeError:
            raise 型態錯誤('分詞型態有問題，分詞：{}' .format(分詞))
        章物件 = 章()
        for 詞陣列 in chain.from_iterable(全部斷句詞陣列):
            組物件 = 組()
            組物件.內底詞 = 詞陣列
            集物件 = 集()
            集物件.內底組 = [組物件]
            句物件 = 句()
            句物件.內底集 = [集物件]
            章物件.內底句.append(句物件)
        return 章物件

    @classmethod
    def _詞陣列分一句一句(cls, 詞陣列):
        有一般字無 = False
        愛換的所在 = []
        for 詞物件 in 詞陣列[::-1]:
            是斷句 = cls._詞物件干焦一个斷句符號無(詞物件)
            if 有一般字無 and 是斷句:
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
        斷句詞陣列.append(詞陣列[頭前:第幾字 + 1])
        return 斷句詞陣列

    @classmethod
    def _詞物件干焦一个斷句符號無(cls, 詞物件):
        if len(詞物件.內底字) == 1:
            字物件 = 詞物件.內底字[0]
            if 字物件.型 in 斷句標點符號 and\
                    (字物件.音 == 無音 or 字物件.音 in 斷句標點符號):
                return True
        return False
