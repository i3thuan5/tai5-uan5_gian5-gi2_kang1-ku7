# -*- coding: utf-8 -*-
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.基本物件.公用變數 import 分詞符號


def 斷詞轉斷字編碼器():
    class 斷詞轉斷字編碼器型態(語句編碼器):

        @classmethod
        def 編碼(cls, 斷詞語句):
            句物件 = 拆文分析器.分詞句物件(斷詞語句)
            字陣列 = 字物件篩仔.篩出字物件(句物件)
            孤字 = []
            for 字物件 in 字陣列:
                孤字.append(物件譀鏡.看分詞(字物件))
            斷字語句 = 分詞符號.join(孤字)
            return super(cls, cls).編碼(斷字語句)
    return 斷詞轉斷字編碼器型態
