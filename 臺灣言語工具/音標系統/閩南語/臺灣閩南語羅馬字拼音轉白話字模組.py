import re
from 臺灣言語工具.音標系統.閩南語.教會系羅馬音標 import 教會系羅馬音標聲調符號表


def 取得白話字韻母調符對照表():
    結果 = {}
    for key, val in 教會系羅馬音標聲調符號表.items():
        結果.update({val: key})
    return 結果


class 臺羅轉白話字():
    白話字韻母調符對照表 = 取得白話字韻母調符對照表()

    @classmethod
    def 轉白話字(cls, 聲, 韻, 調):
        白話字聲 = cls.轉白話字聲(聲)
        白話字韻 = cls.轉白話字韻(韻)
        白話字傳統調韻 = cls.白話字韻標傳統調(白話字韻, 調)
        return (
            白話字聲 +
            白話字傳統調韻
        )

    @classmethod
    def 轉白話字聲(cls, 聲):
        白話字聲 = None
        if 聲 == 'ts':
            白話字聲 = 'ch'
        elif 聲 == 'tsh':
            白話字聲 = 'chh'
        else:
            白話字聲 = 聲
        return 白話字聲

    @classmethod
    def 轉白話字韻(cls, 韻):
        白話字韻 = None
        # 母音
        if 'ua' in 韻:
            白話字韻 = 韻.replace('ua', 'oa')
        elif 'ue' in 韻:
            白話字韻 = 韻.replace('ue', 'oe')
        else:
            # oo, au, ia, ai
            白話字韻 = 韻
        # 鼻化音
        if 'nnh' in 韻:
            白話字韻 = 白話字韻.replace('nnh', 'hⁿ')
        elif 'nn' in 韻:
            白話字韻 = 白話字韻.replace('nn', 'ⁿ')
        return 白話字韻

    @classmethod
    def 白話字韻標傳統調(cls, 白話字韻無調, 調):
        結果 = ''
        # 單元音
        if 'oo' in 白話字韻無調:
            結果 = cls.加上白話字調符(白話字韻無調, 'oo', 調)
        elif re.search('[aeiou]', 白話字韻無調):
            pass
        elif 'ng' in 白話字韻無調:
            結果 = cls.加上白話字調符(白話字韻無調, 'n', 調)
        elif 'm' in 白話字韻無調:
            結果 = cls.加上白話字調符(白話字韻無調, 'm', 調)
        return 結果

    @classmethod
    def 加上白話字調符(cls, 白話字韻無調, 標調字母, 調):
        return 白話字韻無調.replace(標調字母, cls.白話字韻母調符對照表[(標調字母, 調)])
