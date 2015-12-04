# -*- coding: utf-8 -*-
from 臺灣言語工具.語音辨識.生文本音值對照表 import 生文本音值對照表
from 臺灣言語工具.音標系統.官話.官話注音符號 import 官話注音符號
from 臺灣言語工具.音標系統.官話.官話注音符號 import 官話注音符號聲
from 臺灣言語工具.音標系統.官話.官話注音符號 import 官話注音符號韻
from 臺灣言語工具.音標系統.官話.官話注音符號轉音值模組 import 官話注音符號對照音值聲母表
from 臺灣言語工具.音標系統.官話.官話注音符號轉音值模組 import 官話韻母實際音值表


class 官話文本音值表:
    _文本音值對照表 = 生文本音值對照表()

    @classmethod
    def 音節佮聲韻對照(cls):
        return cls._文本音值對照表.生音節佮聲韻對照(官話注音符號, 官話注音符號聲, 官話注音符號韻)

    @classmethod
    def 聲韻表(cls):
        return cls._文本音值對照表.生聲韻表(官話注音符號對照音值聲母表, 官話韻母實際音值表)

if __name__ == '__main__':
    文本音值表 = 官話文本音值表()
    print('\n'.join(文本音值表.音節佮聲韻對照()), file=open('官話聲韻對照.dict', 'w'))
    print('\n'.join(文本音值表.聲韻表()), file=open('官話聲韻表.dict', 'w'))
