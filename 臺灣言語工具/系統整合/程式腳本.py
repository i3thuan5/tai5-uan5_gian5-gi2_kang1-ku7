# -*- coding: utf-8 -*-
import gzip
import io
import os
from subprocess import Popen, PIPE
from contextlib import contextmanager


class 程式腳本:

    @classmethod
    def _走指令(cls, 指令, 愛直接顯示輸出=False,
             stdin=None, stdout=PIPE, stderr=PIPE, env=None):
        try:
            if 愛直接顯示輸出:
                程序 = Popen(指令, stdin=stdin)
                回傳值 = 程序.wait()
                if 回傳值 != 0:
                    cls._走指令錯誤(指令)
            else:
                程序 = Popen(指令, stdin=stdin, stdout=stdout, stderr=stderr)
                輸出資訊, 錯誤輸出資訊 = 程序.communicate()
                回傳值 = 程序.wait()
                if 回傳值 != 0:
                    cls._走指令錯誤(指令, 輸出資訊, 錯誤輸出資訊)
        except FileNotFoundError:
            raise RuntimeError(
                '檔案無存在，抑是指令參數愛用陣列的形式！！指令：{0}'
                .format(指令)
            )

    @classmethod
    def _走指令錯誤(cls, 指令, 輸出資訊=None, 錯誤輸出資訊=None):
        if 輸出資訊:
            輸出 = '輸出：{0}\n'.format(輸出資訊.decode('utf-8'))
        else:
            輸出 = ''
        if 錯誤輸出資訊:
            錯誤輸出 = '錯誤資訊：{0}\n'.format(錯誤輸出資訊.decode('utf-8'))
        else:
            錯誤輸出 = ''
        raise RuntimeError(
            '指令走到一半發生問題！！指令：{0}\n{1}{2}'
            .format(指令, 輸出, 錯誤輸出)
        )

    @classmethod
    def _細項目錄(cls, 資料目錄, 細項名):
        細項目錄 = os.path.join(資料目錄, 細項名)
        os.makedirs(細項目錄, exist_ok=True)
        return 細項目錄

    @classmethod
    def _陣列寫入檔案(cls, 檔名, 陣列):
        cls._字串寫入檔案(檔名, '\n'.join(陣列))

    @classmethod
    def _字串寫入檔案(cls, 檔名, 字串):
        開檔 = cls._開檔函式(檔名)
        檔案 = 開檔(檔名, mode='wt', encoding='utf-8')
        print(字串, file=檔案)
        檔案.close()

    @classmethod
    def _讀檔案(cls, 檔名):
        開檔 = cls._開檔函式(檔名)
        檔案 = 開檔(檔名, mode='rt', encoding='utf-8')
        資料 = []
        for 一逝 in 檔案:
            一逝 = 一逝.rstrip()
            if 一逝 != '':
                資料.append(一逝)
        檔案.close()
        return 資料

    @classmethod
    def _檔案合做一个(cls, 上尾平行語料檔名, 全部平行語料檔名陣列, 編碼器):
        with open(上尾平行語料檔名, 'w') as 寫檔:
            for 平行語料檔名 in 全部平行語料檔名陣列:
                for 一逝 in cls._讀檔案(平行語料檔名):
                    print(編碼器.編碼(一逝.strip()), file=寫檔)

    @classmethod
    def _開檔函式(cls, 檔名):
        if 檔名.endswith('gz'):
            return gzip.open
        else:
            return io.open

    @classmethod
    @contextmanager
    def _換目錄(cls, newdir):
        'http://stackoverflow.com/questions/431684/how-do-i-cd-in-python/24176022#24176022'
        prevdir = os.getcwd()
        os.chdir(os.path.expanduser(newdir))
        try:
            yield
        finally:
            os.chdir(prevdir)
