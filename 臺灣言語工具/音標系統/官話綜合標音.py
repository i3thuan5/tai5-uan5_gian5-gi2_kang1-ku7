# -*- coding: utf-8 -*-
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.音標系統.官話.官話注音符號 import 官話注音符號


class 官話綜合標音:

    def __init__(self, 字物件, 音標一定愛著=False):
        if not isinstance(字物件, 字):
            raise 型態錯誤('傳入來的毋是字物件！{0}，{1}'.format(type(字物件), str(字物件)))
        self.漢字 = 字物件.型
        if 字物件.音 == 無音:
            源頭 = 字物件.型
        else:
            源頭 = 字物件.音
        注音 = 官話注音符號(字物件.音).音標
        if 注音 is not None:
            self.注音符號 = 注音
        else:
            self.注音符號 = 源頭

    def 轉json格式(self):
        return [{"漢字": self.漢字, "注音符號": self.注音符號}]

    def __repr__(self):
        return self.轉json格式()

    def __str__(self):
        return self.轉json格式()
