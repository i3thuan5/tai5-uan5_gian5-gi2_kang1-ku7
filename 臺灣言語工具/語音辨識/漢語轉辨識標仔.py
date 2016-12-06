# -*- coding: utf-8 -*-
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.基本物件.公用變數 import 聲調符號


class 漢語轉辨識標仔:
    恬音 = 'sil'
    全部聲調符號 = '0123456789' + ''.join(聲調符號)

    @classmethod
    def 物件轉音節標仔(cls, 物件, 音標系統):
        if isinstance(物件, 章):
            return cls._章物件轉音節標仔(物件, 音標系統)
        return cls._句物件轉音節標仔(物件, 音標系統)

    @classmethod
    def _章物件轉音節標仔(cls, 章物件, 音標系統):
        全部標仔 = []
        for 句物件 in 章物件.內底句:
            全部標仔 = 全部標仔[:-1]
            全部標仔.extend(cls._句物件轉音節標仔(句物件, 音標系統))
        return 全部標仔

    @classmethod
    def _句物件轉音節標仔(cls, 句物件, 音標系統):
        全部標仔 = [cls.恬音]
        for 字物件 in 句物件.篩出字物件():
            if 音標系統(字物件.音).音標 is not None:
                音節 = 字物件.音.strip(cls.全部聲調符號)
                全部標仔.append(音節)
            else:
                if 全部標仔[-1] != cls.恬音:
                    全部標仔.append(cls.恬音)
        if 全部標仔[-1] != cls.恬音:
            全部標仔.append(cls.恬音)
        return 全部標仔
