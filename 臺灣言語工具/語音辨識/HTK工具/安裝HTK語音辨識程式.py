# -*- coding: utf-8 -*-
from 臺灣言語工具.系統整合.安裝程式腳本 import 安裝程式腳本
from os import makedirs
from os.path import join, isdir


from 臺灣言語工具.系統整合.外部程式 import 外部程式


class 安裝HTK語音辨識程式(安裝程式腳本):

    @classmethod
    def 安裝htk(cls, htk安裝路徑=外部程式.目錄()):
        makedirs(htk安裝路徑, exist_ok=True)
        htk程式碼目錄 = join(htk安裝路徑, 'HTK')
        if not isdir(htk程式碼目錄):
            with cls._換目錄(htk安裝路徑):
                cls._走指令([
                    'git', 'clone',
                    '--branch', 'htk',
                    '--single-branch',
                    'https://github.com/a8568730/HTK_HTS.git',
                    'HTK',
                ])
        else:
            with cls._換目錄(htk程式碼目錄):
                cls._更新專案()
        with cls._換目錄(htk程式碼目錄):
            try:
                cls._走指令(['make', 'all', 'install'])
            except:
                cls._走指令(['chmod', 'u+x', 'configure'])
                cls._走指令([
                    './configure',
                    '--prefix={}'.format(htk程式碼目錄)
                ], 愛直接顯示輸出=True)
                cls._走指令(['make', 'all', 'install'], 愛直接顯示輸出=True)
