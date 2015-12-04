# -*- coding: utf-8 -*-
import sys


class 剖析結構化工具:

    @classmethod
    def 結構化剖析結果(cls, 剖析結果字串):
        空白, 語句資訊, 結束符號 = 剖析結果字串.split('#')
        if 空白 != '':
            raise RuntimeError('剖析工具的格式有改變！！')
        逝資料, 語句 = 語句資訊.split(' ', 1)
        return 逝資料.split(':')[0], cls._結構化語句(語句), 結束符號

    @classmethod
    def _結構化語句(cls, 剖析語句):
        括號位置 = 剖析語句.find('(')
        冒號位置 = 剖析語句.find(':')
# 		elif 冒號位置 >= 0 and (括號位置 < 0 or 括號位置 > 冒號位置):
        if 冒號位置 >= 0 and 括號位置 < 0:
            return tuple(剖析語句.split(':')[::-1])
# 		if 括號位置 >= 0 and (冒號位置 < 0 or 冒號位置 > 括號位置):
        elif 括號位置 >= 0:  # and (冒號位置 < 0 or 冒號位置 > 括號位置):
            正括號位置 = 剖析語句.rfind(')')
            片語內容 = list(map(cls._結構化語句, cls._切片語(剖析語句[括號位置 + 1:正括號位置])))
            # #會切著中央的
            if 剖析語句[正括號位置 + 1:] != '':
                raise RuntimeError('剖析時，「' + 剖析語句 + '」後壁有加物件！！！')
            return [剖析語句[:括號位置]] + 片語內容
# 		print('「' + 剖析語句 + '」毋知按怎切！！！')
        return (剖析語句)

    @classmethod
    def _切片語(cls, 片語):
        切開結果 = []
        有問題 = False
        深度 = 0
        詞 = ''
        for 字 in 片語:
            if 字 == '|' and 深度 == 0:
                切開結果.append(詞)
                詞 = ''
            elif 字 == '(':
                深度 += 1
                詞 += 字
            elif 字 == ')':
                深度 -= 1
                詞 += 字
            else:
                詞 += 字
            if 深度 < 0:
                有問題 = True
        if 深度 != 0:
            有問題 = True
        切開結果.append(詞)
        if 有問題:
            raise RuntimeError('剖析時，「' + 片語 + '」括號有問題！！！')
        return 切開結果

    @classmethod
    def 處理結構化結果(cls, 剖析結果, 處理函式):
        處理結果 = []
        for 一段剖析 in 剖析結果:
            if isinstance(一段剖析, list):
                處理結果.append(cls.處理結構化結果(一段剖析, 處理函式))
            elif isinstance(一段剖析, tuple):
                處理結果.append(處理函式(一段剖析))
            else:
                處理結果.append(一段剖析)
        return 處理結果

    @classmethod
    def 印出(cls, 型體佮詞性語意, 目的=sys.stdout):
        print(型體佮詞性語意[0], end=' ', file=目的)
