from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


class 變調規則表:
    def __init__(self, 名, 喉入聲變調規則, 入聲變調規則, 變調規則):
        self.名 = 名
        self.喉入聲變調規則 = 喉入聲變調規則
        self.入聲變調規則 = 入聲變調規則
        self.變調規則 = 變調規則

    def __str__(self):
        return self.名

    def 變調(self, 音):
        聲, 韻, 調 = 音
        if 韻.endswith('ʔ') or 韻.endswith('h'):
            try:
                調 = self.喉入聲變調規則[調]
            except KeyError:
                raise 解析錯誤('喉塞尾調錯誤！！{0}'.format((聲, 韻, 調)))
            韻 = 韻[:-1]
        elif 韻.endswith('p') or 韻.endswith('t') or 韻.endswith('k'):
            try:
                調 = self.入聲變調規則[調]
            except KeyError:
                raise 解析錯誤('入尾調錯誤！！{0}'.format((聲, 韻, 調)))
        else:
            if 調 in self.變調規則:
                調 = self.變調規則[調]
            else:
                raise 解析錯誤('非入調錯誤！！{0}'.format((聲, 韻, 調)))
        return (聲, 韻, 調)


class 免變:

    def __init__(self, 名):
        self.名 = 名

    def __str__(self):
        return self.名

    @classmethod
    def 變調(cls, 音):
        return 音
