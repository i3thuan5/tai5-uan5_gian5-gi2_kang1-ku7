from os.path import join, dirname, abspath, isfile
from shutil import rmtree
from tempfile import mkdtemp
from unittest.case import TestCase
from 臺灣言語工具.語音辨識.HTK工具.HTK語料處理 import HTK語料處理
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本


class HTK語料處理整合試驗(TestCase):

    def setUp(self):
        語料目錄 = join(dirname(abspath(__file__)), '語音語料')
        self.音檔目錄 = join(語料目錄, 'wav')
        self.標仔目錄 = join(語料目錄, 'labels')
        self.音節聲韻對照檔 = join(語料目錄, '聲韻對照.dict')
        self.音檔檔案目錄 = join(self.音檔目錄, '00001.wav')

        self.資料目錄 = mkdtemp()

    def tearDown(self):
        rmtree(self.資料目錄)

    def test_資料夾產生特徵檔(self):
        全部特徵檔 = HTK語料處理.產生特徵檔(self.音檔目錄, self.資料目錄)
        self.特徵檔數量著而且攏存在(全部特徵檔)

    def test_檔案產生特徵檔(self):
        全部特徵檔 = HTK語料處理.產生特徵檔(self.音檔檔案目錄, self.資料目錄)
        self.特徵檔數量著而且攏存在(全部特徵檔, 1)

    def test_產生特徵佮音節檔(self):
        全部特徵檔, 音節檔 = HTK語料處理.產生特徵佮音節檔(self.音檔目錄, self.標仔目錄, self.資料目錄)
        self.特徵檔數量著而且攏存在(全部特徵檔)
        self.音節抑是聲韻檔數量著(音節檔)

    def test_產生特徵佮聲韻檔(self):
        全部特徵檔, 聲韻檔 = HTK語料處理.產生特徵佮聲韻檔(
            self.音檔目錄, self.標仔目錄, self.音節聲韻對照檔, self.資料目錄)
        self.特徵檔數量著而且攏存在(全部特徵檔)
        self.音節抑是聲韻檔數量著(聲韻檔)

    def test_產生特徵佮音節佮聲韻檔(self):
        全部特徵檔, 音節檔, 聲韻檔 = HTK語料處理.產生特徵佮音節佮聲韻檔(
            self.音檔目錄, self.標仔目錄, self.音節聲韻對照檔, self.資料目錄
        )
        self.特徵檔數量著而且攏存在(全部特徵檔)
        self.音節抑是聲韻檔數量著(音節檔)
        self.音節抑是聲韻檔數量著(聲韻檔)

    def 特徵檔數量著而且攏存在(self, 全部特徵檔, 檔案數量=93):
        特徵檔檔名陣列 = 程式腳本._讀檔案(全部特徵檔)
        self.assertEqual(len(特徵檔檔名陣列), 檔案數量)
        for 檔名 in 特徵檔檔名陣列:
            self.assertTrue(isfile(檔名))

    def 音節抑是聲韻檔數量著(self, 資料檔):
        檔案數 = 0
        for 資料 in 程式腳本._讀檔案(資料檔):
            if 資料 == '.':
                檔案數 += 1
        self.assertEqual(檔案數, 93)
