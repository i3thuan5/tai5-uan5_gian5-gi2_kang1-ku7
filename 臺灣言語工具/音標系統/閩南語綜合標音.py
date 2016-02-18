# -*- coding: utf-8 -*-
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤


class 閩南語綜合標音:
    #     型體 = None
    #     臺羅數字調 = None
    #     臺羅閏號調 = None
    #     通用數字調 = None
    #     吳守禮方音 = None

    def __init__(self, 字物件, 音標一定愛著=False):
        if not isinstance(字物件, 字):
            raise 型態錯誤('傳入來的毋是字物件！{0}，{1}'.format(type(字物件), str(字物件)))
        self.漢字 = 字物件.型
        if 字物件.音 == 無音:
            源頭 = 字物件.型
        else:
            源頭 = 字物件.音
        臺羅 = 臺灣閩南語羅馬字拼音(源頭)
        if 臺羅.音標 is None:
            self.臺羅數字調 = 源頭
            self.臺羅閏號調 = 源頭
            self.通用數字調 = 源頭
            self.吳守禮方音 = 源頭
        else:
            self.臺羅數字調 = 臺羅.音標
            self.吳守禮方音 = 臺羅.產生吳守禮方音物件().音標
            self.臺羅閏號調 = 臺羅.轉閏號調()
            self.通用數字調 = 臺羅.轉通用拼音()

    def 轉json格式(self):
        return [{
            "漢字": self.漢字,
            "臺羅數字調": self.臺羅數字調,
            "臺羅閏號調": self.臺羅閏號調,
            "通用數字調": self.通用數字調,
            "吳守禮方音": self.吳守禮方音,
        }]

    def __repr__(self):
        return self.轉json格式()

    def __str__(self):
        return self.轉json格式()
