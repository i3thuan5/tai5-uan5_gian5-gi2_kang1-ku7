# -*- coding: utf-8 -*-
from os import makedirs
from os.path import isdir, join
from shutil import copyfile, move

from 臺灣言語工具.系統整合.外部程式 import 外部程式
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本

_外部程式目錄 = 外部程式().目錄()


class 安裝摩西翻譯佮相關程式(程式腳本):
    pull深度 = '100'

    def 安裝moses(self, moses安裝路徑=_外部程式目錄, 編譯CPU數=4):
        makedirs(moses安裝路徑, exist_ok=True)
        moses程式碼目錄 = join(moses安裝路徑, 'mosesdecoder')
        if not isdir(moses程式碼目錄):
            with self._換目錄(moses安裝路徑):
                self._走指令([
                    'git', 'clone',
                    '--depth', self.pull深度,
                    'https://github.com/sih4sing5hong5/mosesdecoder.git'
                ])
        else:
            with self._換目錄(moses程式碼目錄):
                self._走指令(['git', 'pull', '--depth', self.pull深度], 愛直接顯示輸出=True)
        with self._換目錄(moses程式碼目錄):
            self._走指令(['./bjam', '-j{0}'.format(編譯CPU數)], 愛直接顯示輸出=True)

    def 安裝gizapp(self, gizapp安裝路徑=_外部程式目錄):
        makedirs(gizapp安裝路徑, exist_ok=True)
        gizapp程式碼目錄 = join(gizapp安裝路徑, 'giza-pp')
        if not isdir(gizapp程式碼目錄):
            with self._換目錄(gizapp安裝路徑):
                self._走指令([
                    'git', 'clone',
                    '--depth', self.pull深度,
                    'https://github.com/sih4sing5hong5/giza-pp.git'
                ])
        else:
            with self._換目錄(gizapp程式碼目錄):
                self._走指令(['git', 'pull', '--depth', self.pull深度], 愛直接顯示輸出=True)
        with self._換目錄(gizapp程式碼目錄):
            self._走指令('make', 愛直接顯示輸出=True)
        執行檔目錄 = self._細項目錄(gizapp程式碼目錄, 'bin')
        for 資料夾, 檔名 in [
            ('GIZA++-v2', 'GIZA++'),
            ('GIZA++-v2', 'snt2cooc.out'),
            ('mkcls-v2', 'mkcls'),
        ]:
            move(join(gizapp程式碼目錄, 資料夾, 檔名), join(執行檔目錄, 檔名))

    def 安裝mgiza(self, mgiza安裝路徑=_外部程式目錄):
        makedirs(mgiza安裝路徑, exist_ok=True)
        mgiza程式碼目錄 = join(mgiza安裝路徑, 'mgiza', 'mgizapp')
        if not isdir(mgiza程式碼目錄):
            with self._換目錄(mgiza安裝路徑):
                self._走指令([
                    'git', 'clone',
                    '--depth', self.pull深度,
                    'https://github.com/moses-smt/mgiza.git'
                ])
        else:
            with self._換目錄(mgiza程式碼目錄):
                self._走指令(['git', 'pull', '--depth', self.pull深度], 愛直接顯示輸出=True)
        with self._換目錄(mgiza程式碼目錄):
            self._走指令(['cmake', '.'])
            self._走指令('make', 愛直接顯示輸出=True)
            self._走指令(['make', 'install'], 愛直接顯示輸出=True)
            copyfile(
                join('scripts', 'merge_alignment.py'),
                join('bin', 'merge_alignment.py')
            )
