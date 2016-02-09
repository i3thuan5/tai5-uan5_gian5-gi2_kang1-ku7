# -*- coding: utf-8 -*-
from 臺灣言語工具.解析整理.程式掠漏 import 程式掠漏
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.基本物件.字 import 字


class 詞物件網仔:

    @classmethod
    def 網出詞物件(cls, 物件):
        try:
            return 物件.網出詞物件()
        except 解析錯誤:
            if isinstance(物件, 字):
                詞物件 = 詞()
                詞物件.內底字 = [物件]
                return [詞物件]
            raise
        except AttributeError:
            程式掠漏.毋是字詞組集句章的毋著(物件)
