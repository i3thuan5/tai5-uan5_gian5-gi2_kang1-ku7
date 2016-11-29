# -*- coding: utf-8 -*-
import re


# 仕上げ
# しあげ
# ㄒㄧ˫ ㄚ ㆣㆤㆷ
# 1si7_1a1_1geh4
class 羅馬音仕上げ:
    輕聲標記 = re.compile('([- ]|\A)0([^\b0-9])')
    外來語標記 = re.compile('(\W|\A)1([^\b0-9])')

    @classmethod
    def しあげ(cls, 原來語句):
        頭一字大寫 = 原來語句[0].upper() + 原來語句[1:]
        return cls.輕聲佮外來語(頭一字大寫)

    @classmethod
    def 輕聲佮外來語(cls, 原來語句):
        無輕聲 = cls.輕聲標記.sub(cls.換輕聲, 原來語句)
        無外來語 = cls.外來語標記.sub(cls.換外來語, 無輕聲)
        return 無外來語

    @classmethod
    def 換輕聲(cls, 配對):
        return '--' + 配對.group(2)

    @classmethod
    def 換外來語(cls, 配對):
        return 配對.group(1) + '*' + 配對.group(2)
