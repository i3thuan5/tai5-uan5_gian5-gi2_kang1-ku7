# -*- coding: utf-8 -*-
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.基本物件.組 import 組
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.正規.阿拉伯數字 import 阿拉伯數字
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 辭典語言模型斷詞:

    @classmethod
    def 斷詞(cls, 辭典, 語言模型, 物件):
        # 字詞組集句=>句
        # 章=>章
        return cls.斷詞分析(辭典, 語言模型, 物件)[0]

    @classmethod
    def 斷詞分析(cls, 辭典, 語言模型, 物件):
        if isinstance(物件, 章):
            return cls._章斷詞(辭典, 語言模型, 物件)
        if isinstance(物件, 字):
            詞物件 = 拆文分析器.建立詞物件('')
            詞物件.內底字.append(物件)
            物件 = 詞物件
        if isinstance(物件, 詞):
            組物件 = 拆文分析器.建立組物件('')
            組物件.內底詞.append(物件)
            物件 = 組物件
        if isinstance(物件, 組):
            集物件 = 拆文分析器.建立集物件('')
            集物件.內底組.append(物件)
            物件 = 集物件
        if isinstance(物件, 集):
            句物件 = 拆文分析器.建立句物件('')
            句物件.內底集.append(物件)
            物件 = 句物件
        if isinstance(物件, 句):
            return cls._句斷詞(辭典, 語言模型, 物件)
        cls._掠漏.毋是字詞組集句章的毋著(物件)

    @classmethod
    def _字陣列斷詞(cls, 辭典, 語言模型, 頂一个狀態, 頂一个分析, 這馬字陣列):
        if hasattr(辭典, '空'):
            這馬字陣列 = cls._字陣列改數字(辭典, 這馬字陣列)
        頂一个上尾的詞, 頂一个上尾賰的字 = 頂一个狀態
        字陣列 = 頂一个上尾賰的字 + 這馬字陣列
        斷詞結果 = []
        for 所在 in range(len(字陣列)):
            斷詞結果.append(辭典.查詞(詞(字陣列[所在:所在 + 辭典.上濟字數()])))

        結果表 = [{頂一个上尾的詞: 頂一个分析}]
        for 所在 in range(len(字陣列)):
            結果表.append({})
        for 所在 in range(len(字陣列) + 1):
            if len(結果表[所在]) == 0:
                cls._對前一个結果加一字產生這馬的結果(語言模型, 字陣列, 結果表, 所在)
            if 所在 < len(字陣列):
                cls._共詞提入來揣上好結果(語言模型, 斷詞結果, 結果表, 所在)
        結果 = {}
        for 所在 in range(min(辭典.上濟字數(), len(結果表))):
            if 所在 == 0:
                賰的字 = tuple()
            else:
                賰的字 = tuple(字陣列[-所在:])
            for 上尾的詞, 分析 in 結果表[-所在 - 1].items():
                結果[(上尾的詞, 賰的字)] = 分析
        return 結果

    @classmethod
    def _對前一个結果加一字產生這馬的結果(cls, 語言模型, 字陣列, 結果表, 所在):
        詞物件 = 詞([字陣列[所在 - 1]])
        詞物件.屬性 = {'無佇辭典': True}
        for 上尾的詞, 分析 in 結果表[所在 - 1].items():
            分數, _頂一个狀態, _頂一个詞 = 分析
            合做伙上尾詞 = (上尾的詞 + (詞物件,))

            if len(合做伙上尾詞) >= 語言模型.上濟詞數():
                這馬上尾詞 = 合做伙上尾詞[-語言模型.上濟詞數():][1:]
            else:
                這馬上尾詞 = 合做伙上尾詞

            結果表[所在][這馬上尾詞] = (
                分數 + sum(
                    語言模型.評詞陣列分(合做伙上尾詞, 開始的所在=len(上尾的詞))
                ),
                分析,
                詞物件
            )

    @classmethod
    def _共詞提入來揣上好結果(cls, 語言模型, 斷詞結果, 結果表, 所在):
        for 斷詞集 in 斷詞結果[所在]:
            for 斷詞的候選詞 in 斷詞集:
                斷詞長度 = len(斷詞的候選詞.內底字)
                for 上尾的詞, 分析 in 結果表[所在].items():
                    分數, _頂一个狀態, _頂一个詞 = 分析
                    合做伙上尾詞 = (上尾的詞 + (斷詞的候選詞,))
                    這馬分數 = 分數 + sum(
                        語言模型.評詞陣列分(合做伙上尾詞, 開始的所在=len(上尾的詞))
                    )

                    if len(合做伙上尾詞) >= 語言模型.上濟詞數():
                        這馬上尾詞 = 合做伙上尾詞[-語言模型.上濟詞數():][1:]
                    else:
                        這馬上尾詞 = 合做伙上尾詞

                    if (這馬上尾詞 not in 結果表[所在 + 斷詞長度] or
                            這馬分數 > 結果表[所在 + 斷詞長度][這馬上尾詞][0]):
                        結果表[所在 + 斷詞長度][這馬上尾詞] = (
                            這馬分數, 分析, 斷詞的候選詞
                        )

    @classmethod
    def _集斷詞(cls, 辭典, 語言模型, 集物件, 頂一層結果):
        集物件結果 = {}
        for 狀態, 分析 in 頂一層結果.items():
            if len(集物件.內底組) == 0:
                raise RuntimeError('無應該有空的集！！可能是辭典設計有問題！！請回報！！')
            for 組物件 in 集物件.內底組:
                字陣列 = 組物件.篩出字物件()
                結果 = cls._字陣列斷詞(辭典, 語言模型, 狀態, 分析, tuple(字陣列))
                for 這个狀態, 這个分析 in 結果.items():
                    這个分數, _這个頂一个狀態, _這个詞 = 這个分析
                    if (這个狀態 not in 集物件結果 or
                            這个分數 > 集物件結果[這个狀態][0]):
                        集物件結果[這个狀態] = 這个分析
        return 集物件結果

    @classmethod
    def _句斷詞(cls, 辭典, 語言模型, 句物件):
        # 結果={狀態:分析}
        #  狀態 = 頂一層上尾的詞, 頂一層上尾賰的字
        #  分析 = 分數, 頂一个狀態, 這个詞物件
        頂一層結果 = {
            ((None,) * (語言模型.上濟詞數() - 1), tuple()):
            (0, None, None)
        }
        for 集物件 in 句物件.內底集:
            頂一層結果 = cls._集斷詞(辭典, 語言模型, 集物件, 頂一層結果)
        return cls._結果揣上好(語言模型, 頂一層結果)

    @classmethod
    def _章斷詞(cls, 辭典, 語言模型, 章物件):
        if not isinstance(章物件, 章):
            raise 型態錯誤('傳入來的毋是章物件：{0}'.format(str(章物件)))
        標好章 = 章()
        用好句 = 標好章.內底句
        總分 = 0
        總詞數 = 0
        for 一句 in 章物件.內底句:
            斷好句物件, 分數, 詞數 = cls._句斷詞(辭典, 語言模型, 一句)
            用好句.append(斷好句物件)
            總分 += 分數
            總詞數 += 詞數
        return 標好章, 總分, 總詞數

    @classmethod
    def _結果揣上好(cls, 語言模型, 頂一層結果):
        上好分數 = None
        上好結果 = None
        for 上尾狀態, 上尾分析 in 頂一層結果.items():
            上尾的詞, 上尾賰的字 = 上尾狀態
            上尾分數, _頂一个狀態, _頂一个詞 = 上尾分析
            if len(上尾賰的字) == 0:
                分數 = 上尾分數 + sum(
                    語言模型.評詞陣列分(
                        上尾的詞 + (None,),
                        開始的所在=len(上尾的詞)
                    )
                )
                if 上好分數 is None or 上好分數 < 分數:
                    上好分數 = 分數
                    上好結果 = 上尾分析
        這馬結果 = 上好結果
        答案詞陣列 = []
        while 這馬結果 is not None:
            分數, 頂一个結果, 這个詞 = 這馬結果
            答案詞陣列.append(這个詞)
            這馬結果 = 頂一个結果
        組物件 = 拆文分析器.建立組物件('')
        組物件.內底詞 = 答案詞陣列[-2::-1]
        集物件 = 拆文分析器.建立集物件('')
        集物件.內底組.append(組物件)
        句物件 = 拆文分析器.建立句物件('')
        句物件.內底集.append(集物件)
        return 句物件, 上好分數, len(答案詞陣列) - 1

    @classmethod
    def _字陣列改數字(cls, 辭典, 字陣列):
        改字了字陣列 = []
        for 字物件 in 字陣列:
            if 阿拉伯數字.是數量無(字物件.型):
                數量 = 阿拉伯數字.轉數量(辭典.空, 字物件.型)
                組物件 = 拆文分析器.建立組物件(數量)
                改字了字陣列 += 組物件.篩出字物件()
            elif 阿拉伯數字.是號碼無(字物件.型):
                號碼 = 阿拉伯數字.轉號碼(辭典.空, 字物件.型)
                組物件 = 拆文分析器.建立組物件(號碼)
                改字了字陣列 += 組物件.篩出字物件()
            else:
                改字了字陣列.append(字物件)
        return 改字了字陣列
