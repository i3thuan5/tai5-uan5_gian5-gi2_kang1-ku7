# -*- coding: utf-8 -*-
from os import makedirs
from os.path import join, isdir


from 臺灣言語工具.系統整合.外部程式 import 外部程式
from 臺灣言語工具.系統整合.安裝程式腳本 import 安裝程式腳本


class 安裝KenLM訓練程式(安裝程式腳本):

    @classmethod
    def 安裝kenlm(cls, kenlm安裝路徑=外部程式.目錄(), 編譯CPU數=4):
        makedirs(kenlm安裝路徑, exist_ok=True)
        kenlm程式碼目錄 = cls.kenlm資料夾路徑(kenlm安裝路徑)
        if not isdir(kenlm程式碼目錄):
            with cls._換目錄(kenlm安裝路徑):
                cls._走指令([
                    'git', 'clone',
                    '--branch', 'master',
                    '--single-branch',
                    'https://github.com/sih4sing5hong5/kenlm.git',
                    'KenLM',
                ])
        else:
            with cls._換目錄(kenlm程式碼目錄):
                cls._更新專案()
        with cls._換目錄(kenlm程式碼目錄):
            cls._走指令(['./bjam', '-j{0}'.format(編譯CPU數)], 愛直接顯示輸出=True)

    @classmethod
    def kenlm資料夾路徑(cls, kenlm安裝路徑):
        return join(kenlm安裝路徑, 'KenLM')
