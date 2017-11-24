# -*- coding: utf-8 -*-
import re


# 仕上げ
# しあげ
# ㄒㄧ˫ ㄚ ㆣㆤㆷ
# 1si7_1a1_1geh4
class 羅馬字仕上げ:
    輕聲標記 = re.compile('([- ]|\A)0([^\b0-9\W\s])')
    外來語標記 = re.compile('(\W|\A)1([^\b0-9\W\s])')
    輕聲開頭 = re.compile('--[^\b0-9\W\s]')

    @classmethod
    def しあげ(cls, 原來語句):
        斷詞句 = cls.輕聲佮外來語(原來語句).replace(' --', '--')
        if cls.輕聲開頭.match(斷詞句):
            return cls.頭一字大寫(斷詞句[2:])
        return cls.頭一字大寫(斷詞句)

    @classmethod
    def 輕聲佮外來語(cls, 原來語句):
        無輕聲 = cls.輕聲標記.sub(cls.換輕聲, 原來語句)
        無外來語 = cls.外來語標記.sub(cls.換外來語, 無輕聲)
        return 無外來語

    @classmethod
    def 頭一字大寫(cls, 原來語句):
        return 原來語句[0].upper() + 原來語句[1:]

    @classmethod
    def 換輕聲(cls, 配對):
        if 配對.group(1) == ' ':
            return ' --' + 配對.group(2)
        return '--' + 配對.group(2)

    @classmethod
    def 換外來語(cls, 配對):
        return 配對.group(1) + '*' + 配對.group(2)
