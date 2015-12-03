# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
import itertools


class 生決策樹仔問題:
    題型 = 'QS "{0}是{1}" {{ {2} }}'
    任意字 = '*'
    符號所在 = ['頭前', '中央', '後壁']

    @classmethod
    def 檢查(cls, 問題集):
        名集 = {}
        for 問題 in 問題集:
            類型, 名, 內容 = 問題.split(' ', 2)
            if 類型 != 'QS':
                raise 解析錯誤('頭前愛是QS，問題：{}'.format(問題))
            if not 內容.startswith('{') or not 內容.endswith('}'):
                raise 解析錯誤('內容愛有大括號，問題：{}'.format(問題))
            if 名 in 名集:
                raise 解析錯誤('有兩个問題名仝款，問題：{}、{}'.format(問題, 名集[名]))
            名集[名] = 問題

    @classmethod
    def 問題集(cls, 分類, 分開符號, 問題種類):
        問題 = set()
        for 所在, 頭前分開, 後壁分開 in \
                zip(cls.符號所在, 分開符號[:-1], 分開符號[1:]):
            if 問題種類 == '孤條':
                for 名, 選 in 分類:
                    一逝 = cls._一逝題目(所在, 頭前分開, 後壁分開, [名], [選])
                    問題.add(一逝)
            elif 問題種類 == '連紲':
                for 頭 in range(len(分類)):
                    for 尾 in range(頭 + 1, len(分類) + 1):
                        一逝 = cls._一堆組合產生問題(
                            所在, 頭前分開, 後壁分開, 分類[頭:尾])
                        問題.add(一逝)
            elif 問題種類 == '組合':
                for 長度 in range(1, len(分類) + 1):
                    for 子分類 in itertools.combinations(分類, 長度):
                        一逝 = cls._一堆組合產生問題(
                            所在, 頭前分開, 後壁分開, 子分類)
                        問題.add(一逝)
            else:
                raise 解析錯誤('種類愛是孤條、連紲、組合其中一个，傳入來的是：{}'
                           .format(問題種類))
        return 問題

    @classmethod
    def _一逝題目(cls, 所在, 頭前分開, 後壁分開, 名, 選):
        題名 = '、'.join(名)
        符合 = cls._選符合的(頭前分開, 後壁分開, 選)
        return cls.題型.format(所在, 題名, 符合)

    @classmethod
    def _選符合的(cls, 頭前分開, 後壁分開, 選):
        符合 = []
        for 條 in itertools.chain.from_iterable(選):
            型 = '"'
            if 頭前分開 != '':
                型 += cls.任意字 + 頭前分開
            型 += 條
            if 後壁分開 != '':
                型 += 後壁分開 + cls.任意字
            型 += '"'
            符合.append(型)
        return ','.join(符合)

    @classmethod
    def _一堆組合產生問題(cls, 所在, 頭前分開, 後壁分開, 分類):
        名集 = []
        選集 = []
        for 名, 選 in 分類:
            名集.append(名)
            選集.append(選)
        return cls._一逝題目(所在, 頭前分開, 後壁分開, 名集, 選集)
