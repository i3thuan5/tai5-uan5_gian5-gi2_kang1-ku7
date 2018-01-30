# -*- coding: utf-8 -*-
import re
from 臺灣言語工具.基本物件.公用變數 import 斷句標點符號


# 仕上げ
# しあげ
# ㄒㄧ˫ ㄚ ㆣㆤㆷ
# 1si7_1a1_1geh4
class 羅馬字仕上げ:
    _斷句標點 = (
        r'|'.join(sorted(斷句標點符號, key=lambda tiam2: len(tiam2)))
        .replace('.', '\\.')
        .replace('?', '\\?')
    )
    輕聲標記 = re.compile('([- ]|\A)0([^\b0-9\W\s])')
    外來語標記 = re.compile('(\W|\A)1([^\b0-9\W\s])')
    句中輕聲 = re.compile('\w --')
    標點前有空白 = re.compile(r' ({})'.format(_斷句標點))
    標點後有輕聲 = re.compile(r'({}) (--)?(\w)'.format(_斷句標點))
    輕聲開頭 = re.compile('--[^\b0-9\W\s]')

    @classmethod
    def しあげ(cls, 原來語句):
        斷詞句 = cls.輕聲佮外來語(原來語句)
        句中輕聲莫閬格 = cls.句中輕聲.sub(
            lambda khing: khing.group(0).replace(' ', ''), 斷詞句
        )
        標點前空白提掉 = cls.標點前有空白.sub(
            lambda tiam2: tiam2.group(1), 句中輕聲莫閬格
        )
        標點後輕聲提掉 = cls.標點後有輕聲.sub(
            lambda tiam2: '{} {}'.format(
                tiam2.group(1), tiam2.group(3).upper()
            ),
            標點前空白提掉
        )
        if cls.輕聲開頭.match(標點後輕聲提掉):
            return cls.頭一字大寫(標點後輕聲提掉[2:])
        return cls.頭一字大寫(標點後輕聲提掉)

    @classmethod
    def 輕聲佮外來語(cls, 原來語句):
        無輕聲 = cls.輕聲標記.sub(cls.換輕聲, 原來語句)
        無外來語 = cls.外來語標記.sub(cls.換外來語, 無輕聲)
        return 無外來語

    @classmethod
    def 頭一字大寫(cls, 原來語句):
        try:
            return 原來語句[0].upper() + 原來語句[1:]
        except IndexError:
            return ''

    @classmethod
    def 換輕聲(cls, 配對):
        if 配對.group(1) == ' ':
            return ' --' + 配對.group(2)
        return '--' + 配對.group(2)

    @classmethod
    def 換外來語(cls, 配對):
        return 配對.group(1) + '*' + 配對.group(2)
