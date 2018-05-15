import re
from 臺灣言語工具.音標系統.閩南語.教會系羅馬音標 import 教會系羅馬音標聲調符號表


def 取得白話字韻母調符對照表():
    結果 = {}
    for 白話字傳統調, 臺羅組 in 教會系羅馬音標聲調符號表.items():
        if 白話字傳統調 == 'ı̍':
            # i8有兩種unicode，踢掉跟教典不同的。
            continue

        臺羅, 數字調 = 臺羅組
        新鍵值 = 臺羅組
        if 臺羅 == 'oo':
            新鍵值 = ('o͘', 數字調)
        結果.update({新鍵值: 白話字傳統調})
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
        if 'oo' in 韻:
            白話字韻 = 韻.replace('oo', 'o͘')
        elif 'ua' in 韻:
            白話字韻 = 韻.replace('ua', 'oa')
        elif 'ue' in 韻:
            白話字韻 = 韻.replace('ue', 'oe')
        else:
            # oo, au, ia, ai
            白話字韻 = 韻
        # 鼻化音
        if 'nnh' in 韻:
            白話字韻 = 白話字韻.replace('nnh', 'ⁿh')
        elif 'nn' in 韻:
            白話字韻 = 白話字韻.replace('nn', 'ⁿ')
        return 白話字韻

    @classmethod
    def 白話字韻標傳統調(cls, 白話字韻無調, 調):
        該標調的字 = ''
        if 'o͘' in 白話字韻無調:
            該標調的字 = 'o͘'
        elif re.search('(iau)|(oai)', 白話字韻無調):
            # 三元音 攏標佇a面頂
            該標調的字 = 'a'
        elif re.search('[aeiou]{2}', 白話字韻無調):
            # 雙元音
            if 白話字韻無調[0] == 'i':
                該標調的字 = 白話字韻無調[1]
            elif 白話字韻無調[1] == 'i':
                該標調的字 = 白話字韻無調[0]
            elif len(白話字韻無調) == 2:
                # xx
                該標調的字 = 白話字韻無調[0]
            elif 白話字韻無調[-1] == 'ⁿ' and 白話字韻無調[-2:] != 'hⁿ':
                # xxⁿ
                該標調的字 = 白話字韻無調[0]
            else:
                # xxn, xxng, xxhⁿ
                該標調的字 = 白話字韻無調[1]
        elif re.search('[aeiou]', 白話字韻無調):
            # 單元音
            該標調的字 = 白話字韻無調[0]
        elif 'ng' in 白話字韻無調:
            # ng, mng
            該標調的字 = 'n'
        elif 'm' in 白話字韻無調:
            該標調的字 = 'm'
        結果 = cls.加上白話字調符(白話字韻無調, 該標調的字, 調)
        return 結果

    @classmethod
    def 加上白話字調符(cls, 白話字韻無調, 標調字母, 調):
        if 調 == '1' or 調 == '4':
            return 白話字韻無調
        return 白話字韻無調.replace(標調字母, cls.白話字韻母調符對照表[(標調字母, 調)])
