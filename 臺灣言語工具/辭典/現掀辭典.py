# -*- coding: utf-8 -*-
from 臺灣言語工具.辭典.文字辭典 import 文字辭典
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.參數錯誤 import 參數錯誤


class 現掀辭典(文字辭典):
    def __init__(self, 上濟字數):
        if 上濟字數 <= 0:
            raise 參數錯誤('字數愛是正整數，傳入來的是{0}'.format(上濟字數))
        self._上濟字數 = 上濟字數
        self.條目 = []

    def 加詞(self, 詞物件):
        if not isinstance(詞物件, 詞):
            raise 型態錯誤('傳入來的毋是詞物件：{0}'.format(str(詞物件)))
        if len(詞物件.內底字) == 0:
            raise 解析錯誤('傳入來的詞物件是空的：{0}'.format(str(詞物件)))
        if len(詞物件.內底字) <= self.上濟字數():
            self.條目.append(詞物件)
        return

    def 查詞(self, 詞物件):
        if not isinstance(詞物件, 詞):
            raise 型態錯誤('傳入來的毋是詞物件：{0}'.format(str(詞物件)))
        結果 = []
        for _ in range(len(詞物件.內底字)):
            結果.append(set())
        for 辭典條 in self.條目:
            if self.查詞有仝無(詞物件, 辭典條):
                結果[len(辭典條.內底字) - 1].add(辭典條)
        return 結果

    def 查詞有仝無(self, 詞物件, 辭典條):
        if len(詞物件.內底字) < len(辭典條.內底字):
            return False
        for 第幾字 in range(len(辭典條.內底字)):
            字物件 = 詞物件.內底字[第幾字]
            辭典條字物件 = 辭典條.內底字[第幾字]
            有著 = False
            if 字物件.音 != 無音:
                if 字物件 == 辭典條字物件:
                    有著 = True
            elif 字物件.型 == 辭典條字物件.型 or 字物件.型 == 辭典條字物件.音:
                有著 = True
            if not 有著:
                return False
        return True
