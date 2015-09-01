# -*- coding: utf-8 -*-
import re
import unicodedata
from itertools import chain

from 臺灣言語工具.基本元素.公用變數 import (分型音符號, 分字符號, 分詞符號, 斷句標點符號, 是拼音字元無, 是注音符號無, 標點符號,
                              無音, 組字式符號, 統一碼數字類, 統一碼注音聲調符號, 統一碼羅馬字類, 統一碼聲調符號)
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.基本元素.字 import 字
from 臺灣言語工具.基本元素.章 import 章
from 臺灣言語工具.基本元素.組 import 組
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.解析整理.程式掠漏 import 程式掠漏
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔


class 拆文分析器:
    符號邊仔加空白 = None
    減號有照規則無 = None
    _切組物件分詞 = re.compile('([^ ]*.｜.[^ ]*|\S+)')
    _切章分詞 = re.compile('(\n｜.|.｜\n|\n)', re.DOTALL)
    _掠漏 = 程式掠漏()

    def __init__(self):
        粗胚 = 文章粗胚()
        self.符號邊仔加空白 = 粗胚.符號邊仔加空白
        self.減號有照規則無 = 粗胚.減號有照規則無

    def 建立字物件(self, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == '':
            raise 解析錯誤('傳入來的語句是空的！')
        return 字(語句)

    def 建立詞物件(self, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == '':
            return 詞()
        拆好的字 = self.拆句做字(語句)
        字陣列 = []
        for 孤詞 in 拆好的字:
            字陣列.append(self.建立字物件(孤詞))
        詞物件 = 詞()
        詞物件.內底字 = 字陣列
        return 詞物件

    # 接受漢羅，但是注音會當作一字一字，除非用組字式。
    # 連字符的兩爿攏無使有空白，若減號愛留的，頭前上好有空白無就是佇句首。
    # 若無法度處理，閣愛保留連字符，用對齊來做。
    def 建立組物件(self, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == '':
            return 組()
        巢狀詞陣列 = self.拆句做巢狀詞(語句)
        詞陣列 = []
        for 孤詞 in 巢狀詞陣列:
            字陣列 = []
            for 孤字 in 孤詞:
                字陣列.append(self.建立字物件(孤字))
            詞物件 = 詞()
            詞物件.內底字 = 字陣列
            詞陣列.append(詞物件)
        組物件 = 組()
        組物件.內底詞 = 詞陣列
        return 組物件

    def 建立集物件(self, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == '':
            return 集()
        集物件 = 集()
        集物件.內底組 = [self.建立組物件(語句)]
        return 集物件

    def 建立句物件(self, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == '':
            return 句()
        句物件 = 句()
        句物件.內底集 = [self.建立集物件(語句)]
        return 句物件

    def 建立章物件(self, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == '':
            return 章()
        語句陣列 = self.拆章做句(語句)
        句陣列 = []
        for 一句 in 語句陣列:
            句陣列.append(self.建立句物件(一句))
        章物件 = 章()
        章物件.內底句 = 句陣列
        return 章物件

    def 產生對齊字(self, 型, 音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if not isinstance(音, str):
            raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '':
            raise 解析錯誤('傳入來的型是空的！')
        if 音 != 無音 and (型 in 標點符號) ^ (音 in 標點符號):
            raise 解析錯誤('型佮音干焦一个是標點符號！「{}」佮「{}」'.format(型, 音))
        return 字(型, 音)

    def 產生對齊詞(self, 型, 音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if not isinstance(音, str):
            raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '' and 音 == 無音:
            return 詞()
        型陣列 = self.拆句做字(型)
        音陣列 = self.詞音拆字(音)
        if len(型陣列) < len(音陣列):
            raise 解析錯誤('詞內底的型「{0}」比音「{1}」少！{2}：{3}'.format(
                str(型), str(音), len(型陣列), len(音陣列)))
        if len(型陣列) > len(音陣列):
            raise 解析錯誤('詞內底的型「{0}」比音「{1}」濟！{2}：{3}'.format(
                str(型), str(音), len(型陣列), len(音陣列)))
        return self.拆好陣列產生對齊詞(型陣列, 音陣列)

    def 拆好陣列產生對齊詞(self, 型陣列, 音陣列):
        if not isinstance(型陣列, list):
            raise 型態錯誤('傳入來的型毋是陣列：型陣列＝{}'.format(str(型陣列)))
        if not isinstance(音陣列, list):
            raise 型態錯誤('傳入來的音毋是陣列：音陣列＝{}'.format(str(音陣列)))
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
            if not isinstance(型陣列[位置], str):
                raise 型態錯誤('型陣列[{1}]毋是字串：型陣列＝{0}'.format(str(型陣列), 型陣列[位置]))
            if not isinstance(音陣列[位置], str):
                raise 型態錯誤('音陣列[{1}]毋是字串：音陣列＝{0}'.format(str(音陣列), 音陣列[位置]))
            字陣列.append(self.產生對齊字(型陣列[位置], 音陣列[位置]))
        return 詞物件

    # 斷詞會照音來斷，型的連字符攏無算
    def 產生對齊組(self, 型, 音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if not isinstance(音, str):
            raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '' and 音 == 無音:
            return 組()
        # #
# 		型陣列 = self.拆句做字(self.符號邊仔加空白(型))
        型陣列 = self.拆句做字(型)

        詞陣列 = []
        第幾字 = 0
        for 詞音 in self.符號邊仔加空白(音).strip(分詞符號).split(分詞符號):
            字音陣列 = self.詞音拆字(詞音)
            if 第幾字 + len(字音陣列) > len(型陣列):
                raise 解析錯誤('詞組內底的型「{0}」比音「{1}」少！配對結果：{2}'.format(
                    str(型), str(音), str(詞陣列)))
            詞陣列.append(
                self.拆好陣列產生對齊詞(型陣列[第幾字:第幾字 + len(字音陣列)], 字音陣列))
            第幾字 += len(字音陣列)
        if 第幾字 < len(型陣列):
            raise 解析錯誤('詞組內底的型「{0}」比音「{1}」濟！配對結果：{2}'.format(
                str(型), str(音), str(詞陣列)))
        組物件 = 組()
        組物件.內底詞 = 詞陣列
        return 組物件

    def 產生對齊集(self, 型, 音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if not isinstance(音, str):
            raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '' and 音 == 無音:
            return 集()
        集物件 = 集()
        集物件.內底組 = [self.產生對齊組(型, 音)]
        return 集物件

    def 產生對齊句(self, 型, 音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if not isinstance(音, str):
            raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '' and 音 == 無音:
            return 句()
        句物件 = 句()
        句物件.內底集 = [self.產生對齊集(型, 音)]
        return 句物件

    def 產生對齊章(self, 型, 音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if not isinstance(音, str):
            raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '' and 音 == 無音:
            return 章()
#  		raise 型態錯誤('QQ型＝{0}，音＝{1}'.format(str(型), str(音)))
        型陣列 = self.拆章做句(型)
        音陣列 = self.拆章做句(音)
        if len(型陣列) > len(音陣列):
            raise 解析錯誤('詞內底的型「{0}」比音「{1}」少！'.format(
                str(型), str(音)))
        if len(型陣列) < len(音陣列):
            raise 解析錯誤('詞內底的型「{0}」比音「{1}」濟！'.format(
                str(型), str(音)))
        句陣列 = []
        for 型物件, 音物件 in zip(型陣列, 音陣列):
            句陣列.append(self.產生對齊句(型物件, 音物件))
        章物件 = 章()
        章物件.內底句 = 句陣列
        return 章物件

    def 拆句做字(self, 語句):
        return self.句解析(語句)[0]

    def 拆句做巢狀詞(self, 語句):
        字陣列, 佮後一个字是佇仝一个詞 = self.句解析(語句)
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

    def 句解析(self, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
        if 語句 == 分詞符號:
            return ([分詞符號], [False])
        self.減號有照規則無(語句)
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
                if 長度 != 0:
                    raise RuntimeError('程式發生內部錯誤，語句＝{0}'.format(str(語句)))
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
                                    '一開始的減號是代表啥物？請用「文章粗胚.建立物件語句前處理減號」：語句{0}'.format(str(語句)))
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
            else:
                raise RuntimeError('程式發生內部錯誤，語句＝{0}'.format(str(語句)))
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
            else:
                raise RuntimeError('程式發生內部錯誤，語句＝{0}'.format(str(語句)))
        if len(字陣列) != len(佮後一个字是佇仝一个詞):
            raise RuntimeError('程式發生內部錯誤，語句＝{0}'.format(str(語句)))
        if [] in 字陣列:
            raise RuntimeError('程式發生內部錯誤，語句＝{0}'.format(str(語句)))
        return (字陣列, 佮後一个字是佇仝一个詞)

    def 拆章做句(self, 語句):
        # 敢有需要做
        # 枋寮漁港「大條巷」上闊兩公尺。=> 枋寮漁港  「  大條巷  」  上闊兩公尺  。
        # =>無，下佇仝詞組，予斷詞處理
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
# 		語句 = 語句.strip(分詞符號)
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

    def 詞音拆字(self, 詞音):
        if 詞音 == 分字符號:
            return[分字符號]
        return 詞音.split(分字符號)

    def 轉做字物件(self, 分詞):
        self._掠漏.毋是字串都毋著(分詞)
        切開結果 = 分詞.split(分型音符號)
        if len(切開結果) == 2:
            return self.產生對齊字(*切開結果)
        if len(切開結果) == 1:
            return self.建立字物件(*切開結果)
        raise 解析錯誤('毋是拄仔好有一个抑是兩个部份：{0}'.format(分詞))

    def 轉做詞物件(self, 分詞):
        self._掠漏.毋是字串都毋著(分詞)
        if 分詞 == '':
            return self.建立詞物件(分詞)
        切開結果 = 分詞.split(分型音符號)
        if len(切開結果) == 2:
            型, 音 = 切開結果
            if 型 == '':
                raise 解析錯誤('型是空的：{0}'.format(分詞))
            return self.產生對齊詞(型, 音)
        if len(切開結果) == 1:
            型 = 切開結果[0]
            if 型 == '':
                raise 解析錯誤('型是空的：{0}'.format(分詞))
            return self.建立詞物件(型)
        raise 解析錯誤('毋是拄仔好有一个抑是兩个部份：{0}'.format(分詞))

    def 轉做組物件(self, 分詞):
        self._掠漏.毋是字串都毋著(分詞)
        if 分詞 == '':
            return 組()
        組物件 = self.建立組物件('')
        切開 = self._切組物件分詞.split(分詞)
        if ''.join(切開[::2]).strip() != '':
            raise 解析錯誤('分詞無合法！！分詞加的：{0}。原來：{1}'
                       .format(切開[::2], 分詞))
        for 分 in 切開[1::2]:
            組物件.內底詞.append(self.轉做詞物件(分))
        return 組物件

    def 轉做集物件(self, 分詞):
        if 分詞 == '':
            return 集()
        集物件 = self.建立集物件('')
        集物件.內底組.append(self.轉做組物件(分詞))
        return 集物件

    def 轉做句物件(self, 分詞):
        if 分詞 == '':
            return 句()
        句物件 = self.建立句物件('')
        句物件.內底集.append(self.轉做集物件(分詞))
        return 句物件

    def 轉做章物件(self, 分詞):
        if 分詞 == '':
            return 章()
        全部斷句詞陣列 = []
        try:
            for 第幾个, 句分詞 in enumerate(self._切章分詞.split(分詞)):
                if 第幾个 % 2 == 0:
                    if 句分詞.strip() != '':
                        原來句物件 = self.轉做句物件(句分詞)
                        網仔 = 詞物件網仔()
                        原來詞陣列 = 網仔._網句(原來句物件)
                        斷句詞陣列 = self.詞陣列分一句一句(原來詞陣列)
                        全部斷句詞陣列.append(斷句詞陣列)
                else:
                    全部斷句詞陣列[-1][-1].append(self.轉做詞物件(句分詞))
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

    def 詞陣列分一句一句(self, 詞陣列):
        有一般字無 = False
        愛換的所在 = []
        for 詞物件 in 詞陣列[::-1]:
            是斷句 = self._詞物件干焦一个斷句符號無(詞物件)
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

    def _詞物件干焦一个斷句符號無(self, 詞物件):
        if len(詞物件.內底字) == 1:
            字物件 = 詞物件.內底字[0]
            if 字物件.型 in 斷句標點符號 and\
                    (字物件.音 == 無音 or 字物件.音 in 斷句標點符號):
                return True
        return False
