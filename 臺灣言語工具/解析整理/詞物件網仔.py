# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.程式掠漏 import 程式掠漏


class 詞物件網仔:

    @classmethod
    def 網出詞物件(cls, 物件):
        try:
            return 物件.網出詞物件()
        except AttributeError:
            程式掠漏.毋是字詞組集句章的毋著(物件)
