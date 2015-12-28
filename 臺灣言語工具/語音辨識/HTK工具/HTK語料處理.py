# -*- coding: utf-8 -*-
import os
from os.path import join, isfile, basename
from 臺灣言語工具.語音合成.語音標仔轉換 import 語音標仔轉換
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
from 臺灣言語工具.系統整合.外部程式 import 外部程式


class HTK語料處理(程式腳本):
    wav副檔名 = '.wav'
    音檔副檔名 = wav副檔名
    標仔副檔名 = '.lab'
    特徵 = 'mfcc'
    特徵副檔名 = '.' + 特徵
    _轉合成標仔 = 語音標仔轉換()
    恬音 = _轉合成標仔.提出標仔主要音值(_轉合成標仔.恬音)
    短恬 = _轉合成標仔.提出標仔主要音值(_轉合成標仔.短恬)

    @classmethod
    def 產生特徵檔(cls, 音檔所在, 資料目錄, 執行檔路徑=外部程式.htk預設目錄()):
        if isfile(音檔所在):
            全部語料 = [(basename(音檔所在), 音檔所在)]
        else:
            全部語料 = cls._揣全部語料(音檔所在, None)
        全部特徵檔 = os.path.join(資料目錄, '資料特徵檔.scp')
        os.makedirs(資料目錄, exist_ok=True)
        cls._揣特徵而且算(執行檔路徑, 資料目錄, 全部語料, 全部特徵檔)
        return 全部特徵檔

    @classmethod
    def 產生特徵佮音節檔(cls, 音檔目錄, 標仔目錄, 資料目錄, 執行檔路徑=外部程式.htk預設目錄()):
        全部語料 = cls._揣全部語料(音檔目錄, 標仔目錄)
        全部特徵檔 = os.path.join(資料目錄, '資料特徵檔.scp')
        os.makedirs(資料目錄, exist_ok=True)
        cls._揣特徵而且算(執行檔路徑, 資料目錄, 全部語料, 全部特徵檔)

        全部標仔檔 = os.path.join(資料目錄, '試驗語料標仔檔.scp')
        音節檔 = os.path.join(資料目錄, '試驗語料音節檔.mlf')
        全部標仔 = []
        for 語料 in 全部語料:
            標仔所在 = 語料[2]
            全部標仔.append(標仔所在)
        cls._陣列寫入檔案(全部標仔檔, 全部標仔)
        用袂著的檔案 = os.path.join(資料目錄, '用袂著的檔案.garbage')
        cls._標仔收集起來(執行檔路徑, 全部標仔檔, 資料目錄, 用袂著的檔案, 音節檔)
        return 全部特徵檔, 音節檔

    @classmethod
    def 產生特徵佮聲韻檔(cls, 音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑=外部程式.htk預設目錄()):
        全部特徵檔, _音節檔, 聲韻檔 = cls.產生特徵佮音節佮聲韻檔(音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑)
        return 全部特徵檔, 聲韻檔

    @classmethod
    def 產生特徵佮音節佮聲韻檔(cls, 音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑=外部程式.htk預設目錄()):
        全部特徵檔, 音節檔 = cls.產生特徵佮音節檔(音檔目錄, 標仔目錄, 資料目錄, 執行檔路徑)
        聲韻類檔 = os.path.join(資料目錄, '試驗語料聲韻類檔.list')
        聲韻檔 = os.path.join(資料目錄, '試驗語料聲韻檔.mlf')
        cls._標仔切做聲韻(執行檔路徑, 音節檔, 音節聲韻對照檔, 資料目錄, 聲韻類檔, 聲韻檔)
        return 全部特徵檔, 音節檔, 聲韻檔

    @classmethod
    def _揣全部語料(cls, 音檔目錄, 標仔目錄):
        全部語料 = []
        for 音檔檔名 in sorted(os.listdir(音檔目錄)):
            if 音檔檔名.endswith(cls.音檔副檔名):
                語料名 = 音檔檔名[:-len(cls.音檔副檔名)]
                音檔所在 = os.path.join(音檔目錄, 音檔檔名)
                if 標仔目錄 is None:
                    全部語料.append((語料名, 音檔所在))
                else:
                    標仔所在 = os.path.join(標仔目錄,
                                        語料名 + cls.標仔副檔名)
                    if os.path.isfile(標仔所在):
                        全部語料.append((語料名, 音檔所在, 標仔所在))
        return 全部語料

    @classmethod
    def _揣特徵而且算(cls, 執行檔路徑, 資料目錄, 全部語料, 全部特徵檔):
        _算特徵參數檔 = os.path.join(資料目錄, '_算特徵參數.cfg')
        cls._字串寫入檔案(_算特徵參數檔,
                    cls.特徵參數.format('WAVEFORM', 'WAV'))
        特徵目錄 = os.path.join(資料目錄, cls.特徵)
        os.makedirs(特徵目錄, exist_ok=True)
        全部特徵 = []
        for 語料 in 全部語料:
            語料名, 音檔所在 = 語料[0:2]
            特徵所在 = os.path.join(特徵目錄,
                                語料名 + cls.特徵副檔名)
            cls._算特徵(執行檔路徑, _算特徵參數檔, 音檔所在, 特徵所在)
            全部特徵.append(特徵所在)
        cls._陣列寫入檔案(全部特徵檔, 全部特徵)

    @classmethod
    def _算特徵(cls, 執行檔路徑, 參數檔, 音檔所在, 特徵所在):
        特徵指令 = [
            join(執行檔路徑, 'HCopy'),
            '-A', '-C', 參數檔, 音檔所在, 特徵所在
        ]
        cls._走指令(特徵指令)

    @classmethod
    def _標仔收集起來(cls, 執行檔路徑, 全部標仔檔, 資料目錄, 原來音類檔, 原來音節檔):
        莫跳脫聲韻 = os.path.join(資料目錄, '莫跳脫聲韻.cfg')
        cls._字串寫入檔案(莫跳脫聲韻, 'noNumEscapes = T')
        整理音節指令 = [
            join(執行檔路徑, 'HLEd'), '-A', '-C', 莫跳脫聲韻, '-l', '*', '-n',
            原來音類檔, '-i', 原來音節檔, '-S', 全部標仔檔, '/dev/null'
        ]
        cls._走指令(整理音節指令)

    @classmethod
    def _標仔切做聲韻(cls, 執行檔路徑, 音節檔, 音節聲韻對照檔, 資料目錄, 聲韻類檔, 聲韻檔):
        莫跳脫聲韻 = os.path.join(資料目錄, '莫跳脫聲韻.cfg')
        cls._字串寫入檔案(莫跳脫聲韻, 'noNumEscapes = T')
        切聲韻參數檔 = os.path.join(資料目錄, '拆聲韻參數檔.led')
        cls._字串寫入檔案(切聲韻參數檔, 'EX')
        切聲韻指令 = [
            join(執行檔路徑, 'HLEd'), '-A',
            '-C', 莫跳脫聲韻, '-l', '*',
            '-i', 聲韻檔, '-n', 聲韻類檔, '-d', 音節聲韻對照檔, 切聲韻參數檔, 音節檔
        ]
        cls._走指令(切聲韻指令)

    特徵參數 = \
        '''
SOURCEKIND = {0}
SOURCEFORMAT = {1}
TARGETKIND = MFCC_E_D_A_Z
TARGETRATE = 100000.0
WINDOWSIZE = 200000.0
PREEMCOEF = 0.975
NUMCHANS = 26
CEPLIFTER = 22
NUMCEPS = 12
USEHAMMING = T
DELTAWINDOW = 2
ACCWINDOW = 2
'''
