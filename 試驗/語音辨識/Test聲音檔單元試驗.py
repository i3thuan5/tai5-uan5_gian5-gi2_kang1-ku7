from os.path import dirname, abspath, join
from unittest.case import TestCase
from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔


class 聲音檔單元試驗(TestCase):

    def setUp(self):
        這馬所在 = dirname(abspath(__file__))
        音檔目錄 = join(這馬所在, '音檔')
        self.音檔 = join(音檔目錄, '我.wav')
        self.原始檔 = join(音檔目錄, '我.raw')

    def test_讀檔(self):
        聲音檔.從檔案讀(self.音檔)

    def test_提掉頭前表(self):
        with open(self.音檔, 'rb') as 音:
            音檔 = 聲音檔.從資料轉(音.read())
        with open(self.原始檔, 'rb') as 原始:
            self.assertEqual(音檔.wav音值資料(), 原始.read())

    def test_加起哩頭前表(self):
        with open(self.原始檔, 'rb') as 原始:
            音檔 = 聲音檔.從參數轉(2, 16000, 1, 原始.read())
        with open(self.音檔, 'rb') as 音:
            self.assertEqual(音檔.wav格式資料(), 音.read())

    def test_音框(self):
        # 1.615秒
        音檔 = 聲音檔.從檔案讀(self.音檔)
        self.assertEqual(len(list(音檔.全部音框(音框秒數=0.02))), 81)
