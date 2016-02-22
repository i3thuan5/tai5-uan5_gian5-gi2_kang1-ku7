# -*- coding: utf-8 -*-
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本


class 安裝程式腳本(程式腳本):
    pull深度 = '100'

    @classmethod
    def _下載專案(cls, 專案git路徑):
        try:
            cls._走指令([
                'git', 'clone',
                '--depth', cls.pull深度,
                專案git路徑
            ])
        except:
            cls._走指令([
                'git', 'clone',
                專案git路徑
            ])

    @classmethod
    def _更新專案(cls):
        try:
            cls._走指令(
                ['git', 'pull', '--depth', cls.pull深度],
                愛直接顯示輸出=True
            )
        except:
            cls._走指令(
                ['git', 'pull'],
                愛直接顯示輸出=True
            )
