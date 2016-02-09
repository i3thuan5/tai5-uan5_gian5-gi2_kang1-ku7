# -*- coding: utf-8 -*-
from math import log10
from math import pow
from abc import ABCMeta
from abc import abstractmethod
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔


class 語言模型(metaclass=ABCMeta):
    # 無看過的詞的出現機率，佮srilm仝款當做負的無限
    無看過 = -99
    _開始 = 詞([拆文分析器.建立字物件('<s>')])
    _結束 = 詞([拆文分析器.建立字物件('</s>')])

    def 開始(self):
        return self._開始

    def 結束(self):
        return self._結束

    def 對數(self, 數字):
        return log10(數字)

    def 指數(self, 數字):
        return pow(10.0, 數字)

    @abstractmethod
    def 上濟詞數(self):
        pass

    def 評分(self, 物件):
        詞陣列 = [self.開始()] + 詞物件網仔.網出詞物件(物件) + [self.結束()]
        return self.評詞陣列分(詞陣列, 開始的所在=1)

    @abstractmethod
    def 評詞陣列分(self, 詞陣列, 開始的所在=0):
        pass
