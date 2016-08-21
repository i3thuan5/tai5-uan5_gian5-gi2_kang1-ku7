# -*- coding: utf-8 -*-
from os import makedirs
from os.path import join, isfile
from shutil import copy
from 臺灣言語工具.語音合成.語音標仔轉換 import 語音標仔轉換
from 臺灣言語工具.系統整合.外部程式 import 外部程式
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本


class HTK辨識模型(程式腳本):
    _轉合成標仔 = 語音標仔轉換()
    恬音 = _轉合成標仔.提出標仔主要音值(_轉合成標仔.恬音)
    短恬 = _轉合成標仔.提出標仔主要音值(_轉合成標仔.短恬)

    def __init__(self, 資料目錄=None,
                 音節聲韻對照檔=None, 聲韻類檔=None, 模型參數檔=None):
        if 音節聲韻對照檔:
            self._音節聲韻對照檔 = 音節聲韻對照檔
        else:
            self._音節聲韻對照檔 = join(資料目錄, '音節聲韻對照檔.dict')
        if 聲韻類檔:
            self._聲韻類檔 = 聲韻類檔
        else:
            self._聲韻類檔 = join(資料目錄, '聲韻類檔.list')
        if 模型參數檔:
            self._模型參數檔 = 模型參數檔
        else:
            self._模型參數檔 = join(資料目錄, '模型參數檔.macro')
        for 檔名 in [self._音節聲韻對照檔, self._聲韻類檔, self._模型參數檔]:
            if not isfile(檔名):
                raise OSError('"{0}"無存在！！'.format(檔名))
        self._聲韻類檔資料 = self._讀檔案(self.聲韻類檔所在())

    def 音節聲韻對照檔所在(self):
        return self._音節聲韻對照檔

    def 聲韻類檔所在(self):
        return self._聲韻類檔

    def 模型參數檔所在(self):
        return self._模型參數檔

    def 存資料佇(self, 目標目錄):
        makedirs(目標目錄, exist_ok=True)
        copy(self.音節聲韻對照檔所在(), join(目標目錄, '音節聲韻對照檔.dict'))
        copy(self.聲韻類檔所在(), join(目標目錄, '聲韻類檔.list'))
        copy(self.模型參數檔所在(), join(目標目錄, '模型參數檔.macro'))

    def _對齊(self, 參數檔, 對照檔,
            標仔檔, 特徵檔, 結果夾, 執行檔路徑=外部程式.htk預設目錄()):
        makedirs(結果夾, exist_ok=True)
        對齊指令 = [
            join(執行檔路徑, 'HVite'), '-A',
            '-C', 參數檔, '-p', '-20', '-t', '10000.0', '15000.0', '100000.1',
            '-H', self.模型參數檔所在(), '-I', 標仔檔,
            '-S', 特徵檔, '-o', 'S', '-y', 'lab', '-l', 結果夾, 對照檔, self.聲韻類檔所在()
        ]
        self._走指令(對齊指令)
        return

    def 對齊聲韻(self, 聲韻檔, 特徵檔, 資料目錄, 執行檔路徑=外部程式.htk預設目錄()):
        makedirs(資料目錄, exist_ok=True)
        參數檔 = join(資料目錄, '參數檔.cfg')
        self._設定指定參數檔(參數檔)
        聲韻對照檔 = join(資料目錄, '聲韻對照檔.dict')
        self._設定聲韻對照聲韻檔(聲韻對照檔)
        對齊結果檔 = join(資料目錄, '對齊聲韻結果')
        self._對齊(參數檔, 聲韻對照檔, 聲韻檔, 特徵檔, 對齊結果檔, 執行檔路徑)
        return 對齊結果檔

    def 對齊音節(self, 音節檔, 特徵檔, 資料目錄, 執行檔路徑=外部程式.htk預設目錄()):
        makedirs(資料目錄, exist_ok=True)
        參數檔 = join(資料目錄, '參數檔.cfg')
        self._設定指定參數檔(參數檔)
        對齊結果檔 = join(資料目錄, '對齊音節結果')
        self._對齊(參數檔, self.音節聲韻對照檔所在(), 音節檔, 特徵檔, 對齊結果檔, 執行檔路徑)
        return 對齊結果檔

    def _辨識(self, 設定檔, 對照檔, 網路檔, 幾條網路, 特徵檔, 結果檔, 結果網路資料夾, 執行檔路徑=外部程式.htk預設目錄()):
        if int(幾條網路) > 0:
            makedirs(結果網路資料夾, exist_ok=True)
            幾條網路設定 = ['-n', str(幾條網路)]
        else:
            結果網路資料夾 = '*'
            幾條網路設定 = []
        辨識指令 = [
            join(執行檔路徑, 'HVite'), '-A',
            '-C', 設定檔, '-p', '-20', '-t', '10000.0', '15000.0', '100000.1',
            '-H', self.模型參數檔所在(), '-w', 網路檔,
            '-S', 特徵檔, '-o', 'N', '-y', 'rec', '-z', 'lattices',
            '-i', 結果檔, '-l', 結果網路資料夾
        ] + 幾條網路設定 + [
            對照檔, self.聲韻類檔所在()
        ]
        self._走指令(辨識指令)
        return

    def 辨識聲韻(self, 特徵檔, 資料目錄, 幾條網路, 執行檔路徑=外部程式.htk預設目錄()):
        makedirs(資料目錄, exist_ok=True)
        參數檔 = join(資料目錄, '參數檔.cfg')
        self._設定指定參數檔(參數檔)
        網路檔 = join(資料目錄, '聲韻網路檔.slf')  # HTK Standard Lattice Format
        self._生辨識網路(執行檔路徑, 資料目錄, self._聲韻類檔資料, 網路檔)
        結果檔 = join(資料目錄, '辨識聲韻結果檔.mlf')
        聲韻對照檔 = join(資料目錄, '聲韻對照檔.dict')
        self._設定聲韻對照聲韻檔(聲韻對照檔)
        結果網路資料夾 = join(資料目錄, '辨識聲韻網路')
        self._辨識(參數檔, 聲韻對照檔, 網路檔, 幾條網路,
                 特徵檔, 結果檔, 結果網路資料夾, 執行檔路徑)
        return 結果檔, 結果網路資料夾

    def 辨識音節(self, 特徵檔, 資料目錄, 幾條網路, 執行檔路徑=外部程式.htk預設目錄()):
        makedirs(資料目錄, exist_ok=True)
        參數檔 = join(資料目錄, '參數檔.cfg')
        self._設定指定參數檔(參數檔)
        網路檔 = join(資料目錄, '音節網路檔.slf')
        self._生辨識網路(執行檔路徑, 資料目錄, self._看聲韻類檔設定辨識音節的音節類檔資料(), 網路檔)
        結果檔 = join(資料目錄, '辨識音節結果檔.mlf')
        結果網路資料夾 = join(資料目錄, '辨識音節網路')
        self._辨識(參數檔, self.音節聲韻對照檔所在(), 網路檔, 幾條網路,
                 特徵檔, 結果檔, 結果網路資料夾, 執行檔路徑)
        return 結果檔, 結果網路資料夾

    def _生辨識網路(self, 執行檔路徑, 資料目錄, 辨識類檔資料, 網路檔):
        辨識的可能 = set()
        短恬語法 = ''
        for 聲韻 in 辨識類檔資料:
            主要音值 = self._轉合成標仔.提出標仔主要音值(聲韻)
            if 主要音值 == self.短恬:
                短恬語法 = '[{0}]'.format(self.短恬)
            elif 主要音值 == self.恬音:
                pass
            else:
                辨識的可能.add(主要音值)
        語法 = '{2}={3};\n({0} < {2} {1} > {0})'.format(
            self.恬音, 短恬語法,
            '$SYL', '|'.join(辨識的可能))
        語法檔 = join(資料目錄, '語法檔.ebnf')  # extended Backus-Naur Form
        self._字串寫入檔案(語法檔, 語法)
        產生網路指令 = [
            join(執行檔路徑, 'HParse'),
            '-A', 語法檔, 網路檔
        ]
        self._走指令(產生網路指令)

    def _看聲韻類檔設定辨識音節的音節類檔資料(self):
        聲韻類 = set()
        for 聲韻 in self._聲韻類檔資料:
            聲韻類.add(self._轉合成標仔.提出標仔主要音值(聲韻))
        類表 = []
        for 類 in self._讀檔案(self.音節聲韻對照檔所在()):
            音節, *拆聲韻 = 類.split()
            for 聲韻 in 拆聲韻:
                if 聲韻 not in 聲韻類:
                    break
            else:
                類表.append('{0}'.format(音節))
        return 類表

    def _設定聲韻對照聲韻檔(self, 對照檔):
        對照表 = []
        for 類 in self._聲韻類檔資料:
            對照表.append('{0}\t{0}'.format(
                self._轉合成標仔.提出標仔主要音值(類))
            )
        self._陣列寫入檔案(對照檔, set(對照表))

    def _設定指定參數檔(self, 上尾參數檔):
        參數 = ['noNumEscapes = TRUE']
        if '-' in ''.join(self._聲韻類檔資料):
            參數.append('ALLOWXWRDEXP = TRUE')
            參數.append('FORCECXTEXP = TRUE')
        self._陣列寫入檔案(上尾參數檔, 參數)
