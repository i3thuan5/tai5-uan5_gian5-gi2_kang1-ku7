# -*- coding: utf-8 -*-

# 仕上げ
# しあげ
# ㄒㄧ˫ ㄚ ㆣㆤㆷ
# 1si7_1a1_1geh4


class 羅馬音仕上げ:

    @classmethod
    def しあげ(cls, 原來語句):
        頭一字大寫 = 原來語句[0].upper() + 原來語句[1:]
        return cls.輕聲佮外來語(頭一字大寫)

    @classmethod
    def 輕聲佮外來語(cls, 原來語句):
        無輕聲 = 原來語句.replace('-0', '--')\
            .replace(' 0', '--')\
            .replace('0', '--')
        無外來語 = 無輕聲.replace('-1', '-*')\
            .replace(' 1', ' *')
        if 無外來語.startswith('1'):
            無外來語 = '*' + 無外來語[1:]
        return 無外來語
