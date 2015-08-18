# -*- coding: utf-8 -*-
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔


class 文字辭典:
    _上濟字數 = None

    def 上濟字數(self):
        return self._上濟字數

    def 加檔案的詞(self, 檔名):
        腳本 = 程式腳本()
        分析器 = 拆文分析器()
        網仔 = 詞物件網仔()
        for 一逝 in 腳本._讀檔案(檔名):
            for 詞物件 in 網仔.網出詞物件(分析器.轉做句物件(一逝)):
                self.加詞(詞物件)
