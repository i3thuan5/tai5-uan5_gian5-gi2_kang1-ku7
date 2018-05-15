# -*- coding: utf-8 -*-
from http.client import HTTPConnection
import json


from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.組 import 組
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 國教院斷詞用戶端:

    @classmethod
    def 斷詞(cls, 物件):
        if isinstance(物件, 章):
            return cls._斷章物件詞(物件)
        return cls._斷句物件詞(物件)

    @classmethod
    def _斷章物件詞(cls, 章物件):
        結果章物件 = 章()
        for 句物件 in 章物件.內底句:
            結果章物件.內底句.append(cls._斷句物件詞(句物件))
        return 結果章物件

    @classmethod
    def _斷句物件詞(cls, 句物件):
        語句 = 句物件.看型(' ', ' ')
        結果詞陣列 = []
        for 詞條, _詞性 in cls.語句斷詞做陣列(語句):
            結果詞陣列.append(拆文分析器.建立詞物件(詞條))
        結果組物件 = 組()
        結果組物件.內底詞 = 結果詞陣列
        結果集物件 = 集()
        結果集物件.內底組 = [結果組物件]
        結果句物件 = 句()
        結果句物件.內底集 = [結果集物件]
        return 結果句物件

    @classmethod
    def 語句斷詞做陣列(cls, 語句):
        連線 = HTTPConnection('coct.naer.edu.tw')
        資料 = json.dumps({'RawText': 語句})
        連線.request(
            "POST", "/Segmentor/Func/getSegResult/",
            資料,
            {'Content-Type': 'application/json'}
        )
        回應字串 = 連線.getresponse().read().decode('utf-8')
        連線.close()
        return json.loads(回應字串)['result']
